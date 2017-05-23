import sys
sys.path.append("../out/gen-py")

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol
from thrift.server import TServer
from OpenSourceProjects import Projects
from OpenSourceProjects import ttypes

class ProjectHandler(Projects.Iface):

    def __init__(self):
        self.projects = {}

    def get(self, name):
        try:
            return self.projects[name]
	except KeyError:
	    print("No project called %s was found" %name)
            return ttypes.Project()

    def create(self, p):
        self.projects[p.name] = p
        return p


handler = ProjectHandler()
proc = Projects.Processor(handler)
trans_svr = TSocket.TServerSocket(port=9090)
trans_fac = TTransport.TBufferedTransportFactory()
proto_fac = TCompactProtocol.TCompactProtocolFactory()
server = TServer.TThreadedServer(proc, trans_svr, trans_fac, proto_fac)

print("[Server] Started")
server.serve()

