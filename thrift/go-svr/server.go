package main

import (
	"fmt"
	"git.apache.org/thrift.git/lib/go/thrift"
	"OpenSourceProjects"
)

type ProjectsHandler struct {
}

func (ph ProjectsHandler) Get(name string) (r *OpenSourceProjects.Project, err error) {
	return
}

func (ph ProjectsHandler) Create(p *OpenSourceProjects.Project) (r *OpenSourceProjects.CreateResult_, err error) {
	return
}

func main() {
	addr := "localhost:9090"
        handler := ProjectsHandler{}
        processor := OpenSourceProjects.NewProjectsProcessor(handler)
	protocolFactory := thrift.NewTCompactProtocolFactory()
	transportFactory := thrift.NewTBufferedTransportFactory(8192)
        transport, err := thrift.NewTServerSocket(addr)
        if err != nil {
		fmt.Println(err)
                return
        }
        fmt.Printf("%T\n", transport)
        server := thrift.NewTSimpleServer4(processor, transport, transportFactory, protocolFactory)
        fmt.Println("Starting the server... on ", addr)
        server.Serve()
}
