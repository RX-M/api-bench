import argparse

from thrift.transport.TSocket import TSocket
from thrift.transport.TTransport import TBufferedTransport
from thrift.protocol.TCompactProtocol import TCompactProtocol

import OpenSourceProjects.Projects as gen

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--host', '-H', default='localhost')
    p.add_argument('--port', '-p', type=int, default=9090)
    args = p.parse_args()

    sock = TSocket(args.host, args.port)
    trans = TBufferedTransport(sock)
    proto = TCompactProtocol(trans)
    client = gen.Client(proto)
    trans.open()
    try:
        proj = client.get("Thrift")
        print(proj)
    finally:
        trans.close()
