package main

import (
	"fmt"
	"os"
	"git.apache.org/thrift.git/lib/go/thrift"
	"OpenSourceProjects"
)

type ProjectsHandler struct {
}

func (ph ProjectsHandler) Get(name string) (r *OpenSourceProjects.Project, err error) {
	d := OpenSourceProjects.Date{2007,1,10}
	p := OpenSourceProjects.Project{name, "ASF", &d}
	return &p, nil
}

func (ph ProjectsHandler) Create(p *OpenSourceProjects.Project) (r *OpenSourceProjects.CreateResult_, err error) {
	cr := OpenSourceProjects.CreateResult_{200, "ok"}
	return &cr, nil
}

func main() {
	addr := "0.0.0.0:9090"
	if len(os.Args) == 2 {
		addr = "0.0.0.0:" + os.Args[1]
	}
        handler := ProjectsHandler{}
        processor := OpenSourceProjects.NewProjectsProcessor(handler)
	protocolFactory := thrift.NewTCompactProtocolFactory()
	transportFactory := thrift.NewTBufferedTransportFactory(8192)
        transport, err := thrift.NewTServerSocket(addr)
        if err != nil {
		fmt.Println(err)
                return
        }
        server := thrift.NewTSimpleServer4(processor, transport, transportFactory, protocolFactory)
        fmt.Println("Starting the server... on ", addr)
        server.Serve()
}
