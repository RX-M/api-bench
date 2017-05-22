import sys
sys.path.append("../out/gen-py")
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol
from OpenSourceProjects import Projects

trans = TSocket.TSocket("localhost", 9090)
trans = TTransport.TBufferedTransport(trans)
proto = TCompactProtocol.TCompactProtocol(trans)
client = Projects.Client(proto)

trans.open()
proj = client.get("Thrift")
print("[Client] received: %s" % proj.name)
print(proj)
trans.close()
