package main

import (
	"flag"
	"fmt"
	"log"
	"strconv"
	"time"

	"OpenSourceProjects"
	"golang.org/x/net/context"
	"google.golang.org/grpc"
)

func main() {
	//Parse command line
	hostPtr := flag.String("host", "localhost", "hostname to connect to")
	portPtr := flag.Int("port", 9090, "port to connect to")
	actionPtr := flag.Int("action", 1, "tests to run")
	repeatPtr  := flag.Int("repeat", 1000000, "number of repeat")
	flag.Parse()
	addr := *hostPtr + ":" + strconv.Itoa(*portPtr)

	conn, err := grpc.Dial(addr, grpc.WithInsecure())
	if err != nil {
		log.Fatal(err)
		return
	}
	defer conn.Close()
	cli := OpenSourceProjects.NewProjectsClient(conn)
	p := &OpenSourceProjects.Project{
		Name: "",
		Host: "",
		Inception: &OpenSourceProjects.Project_Date{
			Year:  2007,
			Month: 1,
			Day:   10,
		},
	}
	start := time.Now()
	switch *actionPtr {
	case 1:
		for i := 0; i < *repeatPtr  ; i++ {
			cli.Get(context.Background(), &OpenSourceProjects.GetArg{Name: "Thrift"})
		}
	case 2:
		for i := 0; i < *repeatPtr  ; i++ {
			cli.Create(context.Background(), p)
		}
	case 3:
		for i := 0; i < *repeatPtr  ; i++ {
			cli.Create(context.Background(), p)
			cli.Get(context.Background(), &OpenSourceProjects.GetArg{Name: "Thrift"})
		}
	default:
		fmt.Println("Invalid action, must be 1-3")
	}
	elap := time.Since(start)
	fmt.Printf("Time for %d times: %v\n", *repeatPtr, elap)
}
