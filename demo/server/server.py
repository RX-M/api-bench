import sys

from thrift.server.TServer import TThreadedServer
from thrift.transport.TSocket import TServerSocket
from thrift.protocol.TCompactProtocol import TCompactProtocolFactory
from thrift.transport.TTransport import TBufferedTransportFactory

import OpenSourceProjects.Projects as Projects
import OpenSourceProjects.ttypes as ttypes


class ProjectHandler(Projects.Iface):
    def get(self, name):
        project = ttypes.Project()
        project.name = name
        project.host = "ASF"
        project.inception = ttypes.Date()
        project.inception.year = 2007
        project.inception.month = 1
        project.inception.day = 10
        return project

    def create(self, project):
        return ttypes.CreateResult(200, "sucess")

if __name__ == '__main__':
    server = TThreadedServer(
        Projects.Processor(ProjectHandler()),
        TServerSocket(),
        TBufferedTransportFactory(),
        TCompactProtocolFactory(),
    )
    server.serve()
