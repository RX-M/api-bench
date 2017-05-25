package main

import (
	"OpenSourceProjects"
	"flag"
	"fmt"
	"git.apache.org/thrift.git/lib/go/thrift"
	"strconv"
	"time"
)

func main() {
	//Parse command line
	hostPtr := flag.String("host", "localhost", "hostname to connect to")
	portPtr := flag.Int("port", 9090, "port to connect to")
	actionPtr := flag.Int("action", 1, "tests to run")
	flag.Parse()
	addr := *hostPtr + ":" + strconv.Itoa(*portPtr)
	//Setup Thrift I/O stack
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
	//Connect to the server
	if err := trans.Open(); err != nil {
		fmt.Println("Error opening socket:", err)
		return
	}
	defer trans.Close()
	//Setup a mock project
	d := OpenSourceProjects.Date{2007, 1, 10}
	p := OpenSourceProjects.Project{"Thrift", "ASF", &d}
	//Run the test
	start := time.Now()
	switch *actionPtr {
	case 1:
		for i := 0; i < 1000000; i++ {
			_, _ = cli.Get("Thrift")
		}
	case 2:
		for i := 0; i < 1000000; i++ {
			_, _ = cli.Create(&p)
		}
	case 3:
		for i := 0; i < 1000000; i++ {
			_, _ = cli.Create(&p)
			_, _ = cli.Get("Thrift")
		}
	default:
		fmt.Println("Invalid action, must be 1-3")
	}
	elap := time.Since(start)
	fmt.Printf("Time to get() 1000000 times: %v\n", elap)
}
