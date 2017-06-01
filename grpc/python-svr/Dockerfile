FROM buildpack-deps:xenial
# Either "3" or empty
ARG PYTHON_VERSION=3
RUN apt-get update && apt-get install -y --no-install-recommends python3-dev python3-pip python3-setuptools python3-wheel
RUN pip3 install -U grpcio-tools grpcio
COPY python-svr/server.py projects.proto ./
RUN python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. projects.proto
ENTRYPOINT ["python3", "/server.py"]
