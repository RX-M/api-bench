IDL_DIR = ../idl
IDL = project.thrift
IMAGE = tpydemocli:loop

gen-py: $(IDL_DIR)/$(IDL)
	cp $(IDL_DIR)/$(IDL) ./
	docker run --rm  -v ${CURDIR}:/tmp/ thrift/thrift-compiler --gen py --o /tmp /tmp/$(IDL) 

build: gen-py
	docker build -t nsuke/$(IMAGE) .

push: build
	docker push nsuke/$(IMAGE)

clean:
	$(RM) -r gen-py
	$(RM) $(IDL)

all: build
