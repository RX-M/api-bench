import argparse
# import time

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
    cnt = 0
    try:
        while True:
            proj = client.get("Thrift")
            cnt += 1
            if cnt == 10000:
                cnt = 0
                print(proj)
    finally:
        trans.close()
