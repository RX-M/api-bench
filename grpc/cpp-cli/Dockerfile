FROM grpc/cxx
RUN apt-get update && apt-get install -y --no-install-recommends libboost-program-options-dev
RUN mkdir cpp-cli
COPY projects.proto ./
COPY cpp-cli/Makefile.docker cpp-cli/client.cpp ./
RUN make -f Makefile.docker
ENTRYPOINT ["./client"]
