"""Client that makes requests from server"""
from __future__ import print_function
import sys
import time
sys.path.append("gen-py")
import argparse
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol
from OpenSourceProjects import Projects
from OpenSourceProjects import ttypes

# ----------------- Helper function for testing ------------------------
def make_project(name, host, day, month, year):
    """Creates a new project object"""
    project = ttypes.Project()
    project.name = name
    project.host = host
    project.inception = ttypes.Date()
    project.inception.year = year
    project.inception.month = month
    project.inception.day = day
    return project

# Change number of requests here
REQUESTS = 1000000

# ----------------------------1 million get()----------------------------#
def get_test(client):
    """Calls get() 1 million times"""
    start = time.time()
    for _ in range(REQUESTS):
        client.get("Thrift")
    end = time.time()
    return end - start

# --------------------------1 million create()---------------------------#
def create_test(client):
    """Calls create() 1 million times"""
    project = make_project("Thrift", "ASF", 10, 1, 2007)
    start = time.time()
    for _ in range(REQUESTS):
        client.create(project)
    end = time.time()
    return end - start

# -------------------1 million get() then create()-----------------------#
def get_create_test(client):
    """Calls create(), then get() 1 million times"""
    start = time.time()
    for _ in range(REQUESTS):
        project = make_project("Thrift", "ASF", 10, 1, 2007)
        client.create(project)
        client.get("Thrift")
    end = time.time()
    return end - start

#---------------Call the appropriate test based on user input------------#
if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('-H', '--host', default='localhost')
    PARSER.add_argument('-p', '--port', default='9090')
    PARSER.add_argument('-a', '--action', default='1')
    PARSER.add_argument('-N', '--no-accel', action='store_true')
    ARGS = vars(PARSER.parse_args())
    print("[Client] Host %s, Port %s, Action %s" %(ARGS['host'], ARGS['port'], ARGS['action']))
    TRANS = TTransport.TBufferedTransport(TSocket.TSocket(ARGS['host'], ARGS['port']))
    if ARGS['no_accel']:
        PROTO = TCompactProtocol.TCompactProtocol(TRANS)
    else:
        PROTO = TCompactProtocol.TCompactProtocolAccelerated(TRANS, fallback=False)
    CLIENT = Projects.Client(PROTO)
    TRANS.open()
    if ARGS['action'] == '1':
        print("Time to get() %d times: %s" % (REQUESTS, get_test(CLIENT)))
    elif ARGS['action'] == '2':
        print("Time to create() %d times: %s" % (REQUESTS, create_test(CLIENT)))
    else:
        print("Time to create() then get() %d times: %s" % (REQUESTS, get_create_test(CLIENT)))
    TRANS.close()
