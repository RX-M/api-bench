import sys
sys.path.append("./gen-py")
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol
from OpenSourceProjects import Projects

trans = TSocket.TSocket("ab843e00c401e11e7a157069614ef926-296924515.us-west-1.elb.amazonaws.com", 9090)
trans = TTransport.TBufferedTransport(trans)
proto = TCompactProtocol.TCompactProtocol(trans)
client = Projects.Client(proto)

trans.open()
proj = client.get("thrift")
print("[Client] received: %s" % proj.name)
print(proj)
trans.close()
