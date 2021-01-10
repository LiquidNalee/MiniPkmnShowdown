make build
make run
docker run -a stdin -a stdout -i -t minishowdown python -m pytest tests/

