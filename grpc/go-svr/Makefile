all:
	cd .. && docker build -t ggosvr -f go-svr/Dockerfile .

run:
	docker run --net=host --rm ggosvr
