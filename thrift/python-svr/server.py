import sys
sys.path.append("gen-py") 

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol
from thrift.server import TServer
from OpenSourceProjects import Projects
from OpenSourceProjects import ttypes

class ProjectHandler(Projects.Iface):

    #def __init__(self):
        #self.projects = {}

    def get(self, name):
        p = ttypes.Project()
        p.name = name
        p.host = "ASF"
        p.inception = ttypes.Date()
        p.inception.year = 2007
        p.inception.month = 1
        p.inception.day = 10
        return p
	#return ttypes.Project()
        #try:
            #return self.projects[name]
	#except KeyError:
	    #print("No project called %s was found" %name)
            #return ttypes.Project()

    def create(self, p):
        #self.projects[p.name] = p
        return ttypes.CreateResult(42, "sucess")

p = raw_input("Enter a port number (press enter for 9090) ")
if (p == ""): p = 9090
else: p = int(p)
print("You have selected port %d" %p) 
handler = ProjectHandler()
proc = Projects.Processor(handler)
trans_svr = TSocket.TServerSocket(port=p)
trans_fac = TTransport.TBufferedTransportFactory()
proto_fac = TCompactProtocol.TCompactProtocolFactory()
server = TServer.TThreadedServer(proc, trans_svr, trans_fac, proto_fac)

print("[Server] Started")
server.serve()

