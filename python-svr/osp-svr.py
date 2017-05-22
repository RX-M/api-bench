import sys
sys.path.append("../out/gen-py")

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol
from thrift.server import TServer
from OpenSourceProjects import Projects
from OpenSourceProjects import ttypes

class ProjectHandler(Projects.Iface):
    def get(self, name):
        p = ttypes.Project()
        p.name = name
        p.host = "ASF"
        p.inception = ttypes.Date()
        p.inception.year = 2007
        p.inception.month = 1
        p.inception.day = 10
        return p

    def create(self, p):
        """
        Parameters:
         - p
        """
        pass


handler = ProjectHandler()
proc = Projects.Processor(handler)
trans_svr = TSocket.TServerSocket(port=9090)
trans_fac = TTransport.TBufferedTransportFactory()
proto_fac = TCompactProtocol.TCompactProtocolFactory()
server = TServer.TThreadedServer(proc, trans_svr, trans_fac, proto_fac)

print("[Server] Started")
server.serve()

