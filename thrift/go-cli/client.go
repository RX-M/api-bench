package main

import (
	"fmt"
	"git.apache.org/thrift.git/lib/go/thrift"
	"OpenSourceProjects"
)

func main() {
	addr := "localhost:9090"
	transport, err := thrift.NewTSocket(addr)
	if err != nil {
		fmt.Println("Error creating socket:", err)
		return
	}
	transportFactory := thrift.NewTBufferedTransportFactory(8192)
	transport = transportFactory.GetTransport(transport)
	defer transport.Close()
	if err := transport.Open(); err != nil {
		fmt.Println("Error opening socket:", err)
		return
	}
	protocolFactory := thrift.NewTCompactProtocolFactory()
	client := OpenSourceProjects.NewProjectsClientFactory(transport, protocolFactory)

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
