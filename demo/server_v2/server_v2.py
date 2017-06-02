from thrift.protocol.TCompactProtocol import TCompactProtocolFactory
from thrift.server.TServer import TThreadedServer
from thrift.transport.TSocket import TServerSocket
from thrift.transport.TTransport import TBufferedTransportFactory

import OpenSourceProjects.Projects as Projects
import OpenSourceProjects.ttypes as ttypes


class ProjectHandler(Projects.Iface):
    def get(self, name):
        return ttypes.Project(
            name,
            host,
            ttypes.Date(2007, 1, 10),
            commits=5012
        )

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
