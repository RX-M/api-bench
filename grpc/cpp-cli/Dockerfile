FROM grpc/cxx
RUN apt-get update && apt-get install -y --no-install-recommends libboost-program-options-dev
RUN mkdir cpp-cli
COPY projects.proto ./
COPY cpp-cli/Makefile.docker cpp-cli/client.cpp cpp-cli/
RUN make -C cpp-cli -f Makefile.docker
CMD cpp-cli/client

