FROM grpc/cxx
RUN apt-get update && apt-get install -y --no-install-recommends libboost-program-options-dev
RUN mkdir cpp-svr
COPY projects.proto ./
COPY cpp-svr/Makefile.docker cpp-svr/server.cpp cpp-svr/
RUN make -C cpp-svr -f Makefile.docker
CMD cpp-svr/server
