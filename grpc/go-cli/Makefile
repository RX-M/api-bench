all:
	cd .. && docker build -t ggocli -f go-cli/Dockerfile .

run:
	docker run --net=host --rm ggocli

run2:
	docker run --net=host --rm ggocli go run client.go --action 2

run3:
	docker run --net=host --rm ggocli go run client.go --action 3
