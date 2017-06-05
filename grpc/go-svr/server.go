package main

import (
	"fmt"
	"log"
	"net"
	"os"
	"strconv"

	"OpenSourceProjects"
	"golang.org/x/net/context"
	"google.golang.org/grpc"
)

type projectServer struct {
}

func (s *projectServer) Get(ctx context.Context, in *OpenSourceProjects.GetArg) (*OpenSourceProjects.Project, error) {
	p := &OpenSourceProjects.Project{
		Name: in.Name,
		Host: "ASF",
		Inception: &OpenSourceProjects.Project_Date{
			Year:  2007,
			Month: 1,
			Day:   10,
		},
	}
	return p, nil
}

func (s *projectServer) Create(ctx context.Context, in *OpenSourceProjects.Project) (*OpenSourceProjects.CreateResult, error) {
	cr := &OpenSourceProjects.CreateResult{
		Code:    200,
		Message: "ok",
	}
	return cr, nil
}

func main() {
	port := 9090
	if len(os.Args) == 2 {
		port0, err := strconv.Atoi(os.Args[1])
		if err != nil {
			log.Fatalf("invalid port")
		}
		port = port0
	}

	lis, err := net.Listen("tcp", fmt.Sprintf(":%d", port))
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	server := grpc.NewServer()
	OpenSourceProjects.RegisterProjectsServer(server, &projectServer{})
	fmt.Println("Listening on", port)
	server.Serve(lis)
}
