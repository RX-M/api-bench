IDL = project.thrift
IMAGE = tpydemosvr:loop

gen-py: ../$(IDL)
	cp ../$(IDL) ./
	docker run --rm  -v ${CURDIR}:/tmp/ thrift/thrift-compiler --gen py --o /tmp /tmp/$(IDL) 

build: gen-py
	docker build -t nsuke/$(IMAGE) .

push: build
	docker push nsuke/$(IMAGE)

clean:
	$(RM) -r gen-py
	$(RM) $(IDL)

all: build
