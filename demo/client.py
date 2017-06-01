import sys

from thrift.transport.TSocket import TSocket
from thrift.transport.TTransport import TBufferedTransport
from thrift.protocol.TCompactProtocol import TCompactProtocolAccelerated

import OpenSourceProjects as gen

if __name__ == '__main__':
    sock = TSocket()
    trans = TBufferedTransport(sock)
    proto = TCompactProtocol(trans)
    client = gen.Projects.Client(proto)
    trans.open()
    try:
        client.get("Thrift")
    finally:
        trans.close()
