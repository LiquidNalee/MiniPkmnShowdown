from os.path import join, dirname, realpath
from pathlib import Path
from typing import List
from json import dump
from requests import request

database_dir = Path(dirname(realpath(__file__)))
__pokeApi_url = "https://pokeapi.co/api/v2/"


def updatePkmnDatabase(pkmn_list: List):
    for pkmn_name, pkmn_data in getPkmnDatabase(pkmn_list).items():
        with open(join(database_dir, "pkmn", f"{pkmn_name}.json"), mode='w') as pkmn_data_file:
            dump(pkmn_data, pkmn_data_file)


def getPkmnDatabase(pkmn_list: List[str]) -> {}:
    db = {}
    for pkmn in pkmn_list:
        res = request("GET", __pokeApi_url + "pokemon/" + pkmn)

        if res.status_code == 200:
            pkmn_json = {
                "type": {str(pkmn_type["slot"] - 1): pkmn_type["type"]["name"]
                         for pkmn_type in res.json()["types"]},
                "base_stats": {__convertApiStatNameToDbStatName(pkmn_stat["stat"]["name"]): pkmn_stat["base_stat"]
                               for pkmn_stat in res.json()["stats"]}
            }
            db[res.json()["name"]] = pkmn_json
    return db


def __convertApiStatNameToDbStatName(api_stat: str) -> str:
    return "atk" if api_stat == "attack" \
        else "phys_def" if api_stat == "defense" \
        else "spe_atk" if api_stat == "special-attack" \
        else "spe_def" if api_stat == "special-defense" \
        else "spd" if api_stat == "speed" \
        else "hp"
