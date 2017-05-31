"""Thrift server that handles requests"""
from __future__ import print_function
import sys
sys.path.append("gen-py")
import argparse

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol
from thrift.server import TServer
from OpenSourceProjects import Projects
from OpenSourceProjects import ttypes

class ProjectHandler(Projects.Iface):
    """Implements the methods defined in project.thrift"""

    #def __init__(self):
        #self.projects = {}

    def get(self, name):
        """Returns a new project with the given name"""
        project = ttypes.Project()
        project.name = name
        project.host = "ASF"
        project.inception = ttypes.Date()
        project.inception.year = 2007
        project.inception.month = 1
        project.inception.day = 10
        return project
    #return ttypes.Project()
        #try:
            #return self.projects[name]
    #except KeyError:
        #print("No project called %s was found" %name)
            #return ttypes.Project()

    def create(self, project):
        """Creates a trivial result"""
        #pylint: disable=unused-argument
        #self.projects[p.name] = p
        return ttypes.CreateResult(42, "sucess")

PARSER = argparse.ArgumentParser()
PARSER.add_argument('-p', '--port', default='9090')
ARGS = vars(PARSER.parse_args())
HANDLER = ProjectHandler()
PROC = Projects.Processor(HANDLER)
TRANS_SVR = TSocket.TServerSocket(port=ARGS['port'])
TRANS_FAC = TTransport.TBufferedTransportFactory()
PROTO_FAC = TCompactProtocol.TCompactProtocolAcceleratedFactory(fallback=False)
SERVER = TServer.TThreadedServer(PROC, TRANS_SVR, TRANS_FAC, PROTO_FAC)

print("[Server] Listening on port " + ARGS['port'])
SERVER.serve()
