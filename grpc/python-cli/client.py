import argparse
import sys
import time

import grpc
import projects_pb2
import projects_pb2_grpc

REQUESTS = 1000000


def main(argv):
    p = argparse.ArgumentParser()
    p.add_argument('-H', '--host', default='localhost')
    p.add_argument('-p', '--port', type=int, default='9090')
    p.add_argument('-a', '--action', type=int, choices=[1, 2, 3], default=1)
    args = p.parse_args(argv)
    print("[Client] Host %s, Port %s, Action %s" % (args.host, args.port, args.action))

    channel = grpc.insecure_channel('%s:%d' % (args.host, args.port))
    stub = projects_pb2_grpc.ProjectsStub(channel)

    start = time.time()
    if args.action == 1:
        print("Time to get() %d times: " % REQUESTS, end='')
        for _ in range(REQUESTS):
            stub.Get(projects_pb2.GetArg(name='Thrift'))
    elif args.action == 2:
        print("Time to create() %d times: " % REQUESTS, end='')
        for _ in range(REQUESTS):
            stub.Create(projects_pb2.Project(
                name='Thrift',
                host='ASF',
                inception=projects_pb2.Project.Date(
                    year=2007,
                    month=10,
                    day=1,
                ),
            ))
    else:
        print("Time to create() then get() %d times: " % REQUESTS, end='')
        for _ in range(REQUESTS):
            stub.Get(projects_pb2.GetArg(name='Thrift'))
            stub.Create(projects_pb2.Project(
                name='Thrift',
                host='ASF',
                inception=projects_pb2.Project.Date(
                    year=2007,
                    month=10,
                    day=1,
                ),
            ))
    elapsed = time.time() - start
    print(elapsed)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
