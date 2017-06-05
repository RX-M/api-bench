FROM grpc/go
COPY go-cli/client.go projects.proto ./
RUN mkdir src/OpenSourceProjects
RUN protoc -I. ./projects.proto --go_out=plugins=grpc:src/OpenSourceProjects
ENTRYPOINT ["go", "run", "client.go"]
