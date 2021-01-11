from os.path import join, dirname, realpath
from pathlib import Path
from typing import List
from json import dump
from requests import request
from re import sub

database_dir = Path(dirname(realpath(__file__)))
__pokeApi_url = "https://pokeapi.co/api/v2/"


def updatePkmnDatabase(pkmn_list: List):
    for pkmn_name, pkmn_data in getPkmnDatabase(pkmn_list).items():
        print(f"Uploaded {pkmn_name}.json")
        with open(join(database_dir, "pkmn", f"{pkmn_name}.json"), mode='w') as pkmn_data_file:
            dump(pkmn_data, pkmn_data_file)


def getPkmnDatabase(pkmn_list: List[str]) -> {}:
    db = {}
    for pkmn in pkmn_list:
        res = request("GET", f"{__pokeApi_url}/pokemon/{pkmn}")

        if res.status_code == 200:
            pkmn_json = {
                "type": {str(pkmn_type["slot"] - 1): pkmn_type["type"]["name"].capitalize()
                         for pkmn_type in res.json()["types"]},
                "base_stats": {__convertApiStatNameToDbStatName(pkmn_stat["stat"]["name"]): pkmn_stat["base_stat"]
                               for pkmn_stat in res.json()["stats"]}
            }
            db[res.json()["name"]] = pkmn_json
    return db


def updateMoveDatabase(move_list: List):
    for move_name, move_data in getMoveDatabase(move_list).items():
        print(f"Uploaded {move_name.lower()}.json")
        with open(join(database_dir, "moves", f"{move_name.lower()}.json"), mode='w') as move_data_file:
            dump(move_data, move_data_file)


def getMoveDatabase(move_list: List[str]) -> {}:
    db = {}
    for move in move_list:
        move_url = sub('\\s', '-', move.lower())
        res = request("GET", f"{__pokeApi_url}/move/{move_url}")

        if res.status_code == 200:
            move_json = {
                "type": res.json()["type"]["name"].capitalize(),
                "category": res.json()["damage_class"]["name"].capitalize(),
                "pp": res.json()["pp"],
                "power": res.json()["power"],
                "accuracy": res.json()["accuracy"],
                "priority": res.json()["priority"],
                "effect_rate": res.json()["effect_chance"],
                "self_stat_mod": {__convertApiStatNameToDbStatName(pkmn_stat["stat"]["name"]): pkmn_stat["change"]
                                  for pkmn_stat in res.json()["stat_changes"]} if res.json()["target"]["name"] == "user"
                else {},
                "trgt_stat_mod": {__convertApiStatNameToDbStatName(pkmn_stat["stat"]["name"]): pkmn_stat["change"]
                                  for pkmn_stat in res.json()["stat_changes"]} if res.json()["target"]["name"] != "user"
                else {}
            }
            db[move] = move_json
    return db


def __convertApiStatNameToDbStatName(api_stat: str) -> str:
    return "atk" if api_stat == "attack" \
        else "phys_def" if api_stat == "defense" \
        else "spe_atk" if api_stat == "special-attack" \
        else "spe_def" if api_stat == "special-defense" \
        else "spd" if api_stat == "speed" \
        else "hp"
