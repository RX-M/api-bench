IDL_DIR = ../idl_v2
IDL = project_v2.thrift
IMAGE = tpydemosvr:v2

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
