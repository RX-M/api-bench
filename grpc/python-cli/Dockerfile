FROM buildpack-deps:xenial
# Either "3" or empty
ARG PYTHON_VERSION=3
RUN apt-get update && apt-get install -y --no-install-recommends python${PYTHON_VERSION}-dev python${PYTHON_VERSION}-pip python${PYTHON_VERSION}-setuptools python${PYTHON_VERSION}-wheel
RUN pip${PYTHON_VERSION} install -U grpcio-tools grpcio
COPY python-cli/client.py projects.proto ./
RUN python${PYTHON_VERSION} -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. projects.proto
ENV PYTHON python${PYTHON_VERSION}
ENTRYPOINT ${PYTHON} /client.py
