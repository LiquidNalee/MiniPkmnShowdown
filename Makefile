build:
	docker build -t minishowdown:latest .

run:
	docker run -d --name minishowdown minishowdown

clean:
	docker stop minishowdown
	docker rm minishowdown
	docker image rm minishowdown