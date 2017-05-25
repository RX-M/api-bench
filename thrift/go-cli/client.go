package main

import (
	"fmt"
	"flag"
	"time"
	"strconv"
	"git.apache.org/thrift.git/lib/go/thrift"
	"OpenSourceProjects"
)

func main() {
	hostPtr := flag.String("host", "localhost", "hostname to connect to")
	portPtr := flag.Int("port", 9090, "port to connect to")
	actionPtr := flag.Int("action", 1, "tests to run")
	flag.Parse()
	addr := *hostPtr + ":" + strconv.Itoa(*portPtr)
	transEP, err := thrift.NewTSocket(addr)
	if err != nil {
		fmt.Println("Error creating socket:", err)
		return
	}
	transFac := thrift.NewTBufferedTransportFactory(8192)
	trans := transFac.GetTransport(transEP)
	protoFac := thrift.NewTCompactProtocolFactory()
	cli := OpenSourceProjects.NewProjectsClientFactory(trans, protoFac)
        fmt.Printf("[Client] Host %s, Port %d, Action %d\n", *hostPtr, *portPtr, *actionPtr)

	if err := trans.Open(); err != nil {
		fmt.Println("Error opening socket:", err)
		return
	}
	defer trans.Close()

	start := time.Now()
	for i := 0; i < 1000000; i++ {
		_, _ = cli.Get("Thrift")
	}
	elap := time.Since(start)
	fmt.Printf("Time to get() 1000000 times: %v\n", elap)
}
