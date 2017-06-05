IDL_DIR = idl
IDL = project.thrift

all: build

gen-py/__init__.py: $(IDL_DIR)/$(IDL)
	cp $(IDL_DIR)/$(IDL) .
	docker run --rm  -v ${CURDIR}/$*:/tmp/ thrift/thrift-compiler --gen py --o /tmp /tmp/$(IDL) 

%/gen-py/__init__.py: gen-py/__init__.py
	mkdir -p $*/gen-py
	cp -r gen-py/* $*/gen-py/.

build-svr: server/gen-py/__init__.py
	docker build -t nsuke/tpydemosvr:v1 server

build-cli: client/gen-py/__init__.py
	docker build -t nsuke/tpydemocli:v1 client

build-cli-loop: client_repeat/gen-py/__init__.py
	docker build -t nsuke/tpydemocli:loop client_repeat

build: build-svr build-cli build-cli-loop

push: build
	docker push nsuke/tpydemosvr:v1
	docker push nsuke/tpydemocli:v1
	docker push nsuke/tpydemocli:loop

clean:
	$(RM) -r gen-py */gen-py
