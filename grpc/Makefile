DOCKER_USER ?= nsuke

all: build

build: gpycli gpysvr gcppcli gcppsvr ggocli ggosvr

gpycli:
	docker build -t $(DOCKER_USER)/$@ -f python-cli/Dockerfile .

gpysvr:
	docker build -t $(DOCKER_USER)/$@ -f python-svr/Dockerfile .

gcppcli:
	docker build -t $(DOCKER_USER)/$@ -f cpp-cli/Dockerfile .

gcppsvr:
	docker build -t $(DOCKER_USER)/$@ -f cpp-svr/Dockerfile .

ggocli:
	docker build -t $(DOCKER_USER)/$@ -f go-cli/Dockerfile .

ggosvr:
	docker build -t $(DOCKER_USER)/$@ -f go-svr/Dockerfile .

push: build
	docker push $(DOCKER_USER)/gpycli
	docker push $(DOCKER_USER)/gpysvr
	docker push $(DOCKER_USER)/gcppcli
	docker push $(DOCKER_USER)/gcppsvr
	docker push $(DOCKER_USER)/ggocli
	docker push $(DOCKER_USER)/ggosvr

run-%:
	docker run --rm --net=host $(DOCKER_USER)/$*
