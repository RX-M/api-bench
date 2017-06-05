all:
	cd .. && docker build -t gcppcli -f cpp-cli/Dockerfile .

run:
	time docker run --net=host --rm gcppcli

run2:
	time docker run --net=host --rm gcppcli --action 2

run3:
	time docker run --net=host --rm gcppcli --action 3
