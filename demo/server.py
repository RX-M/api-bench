import sys

from thrift.server.TServer import TThreadedServer
from thrift.transport.TSocket import TServerSocket
from thrift.protocol.TCompactProtocol import TCompactProtocolFactory
from thrift.transport.TThreadedServer import TBufferedTransportFactory

import OpenSourceProjects as gen


class ProjectHandler(gen.Projects.Iface):
    def get(self, name):
        project = gen.ttypes.Project()
        project.name = name
        project.host = "ASF"
        project.inception = gen.ttypes.Date()
        project.inception.year = 2007
        project.inception.month = 1
        project.inception.day = 10
        return project

    def create(self, project):
        return gen.ttypes.CreateResult(200, "sucess")

if __name__ == '__main__':
    server = TServer.TThreadedServer(
        gen.Projects.Processor(ProjectHandler()),
        TServerSocket(),
        TBufferedTransportFactory(),
        TCompactProtocolFactory(),
    )
    server.serve()
