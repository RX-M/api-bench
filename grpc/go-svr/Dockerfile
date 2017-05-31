FROM grpc/go
COPY go-svr/server.go projects.proto ./
RUN mkdir src/OpenSourceProjects
RUN protoc -I. ./projects.proto --go_out=plugins=grpc:src/OpenSourceProjects
CMD go run server.go

