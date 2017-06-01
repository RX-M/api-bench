DOCKER_USER ?= nsuke

all: build

build: gpycli gpysvr gcppcli gcppsvr ggocli ggosvr gpycli2 gpysvr2

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

gpycli2:
	docker build  --build-arg PYTHON_VERSION= -t $(DOCKER_USER)/gpycli:2 -f python-cli/Dockerfile .

gpysvr2:
	docker build --build-arg PYTHON_VERSION= -t $(DOCKER_USER)/gpysvr:2 -f python-svr/Dockerfile .

push: build
	docker push $(DOCKER_USER)/gpycli
	docker push $(DOCKER_USER)/gpysvr
	docker push $(DOCKER_USER)/gpycli:2
	docker push $(DOCKER_USER)/gpysvr:2
	docker push $(DOCKER_USER)/gcppcli
	docker push $(DOCKER_USER)/gcppsvr
	docker push $(DOCKER_USER)/ggocli
	docker push $(DOCKER_USER)/ggosvr

run-%:
	docker run --rm --net=host $(DOCKER_USER)/$*
