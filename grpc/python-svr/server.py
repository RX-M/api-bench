from concurrent import futures
import argparse
import sys
import time

import grpc
import projects_pb2
import projects_pb2_grpc


class ProjectsServicer(projects_pb2_grpc.ProjectsServicer):
    def Get(self, request, context):
        return projects_pb2.Project(
            name=request.name,
            host='ASF',
            inception=projects_pb2.Project.Date(
                year=2007,
                month=10,
                day=1,
            ),
        )

    def Create(self, request, context):
        return projects_pb2.CreateResult(
            code=200,
            message='success',
        )


def main(argv):
    p = argparse.ArgumentParser()
    p.add_argument('-p', '--port', type=int, default=9090)
    args = p.parse_args()

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    projects_pb2.add_ProjectsServicer_to_server(ProjectsServicer(), server)
    server.add_insecure_port('0.0.0.0:%d' % args.port)
    server.start()
    while True:
        time.sleep(3600 * 24)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
