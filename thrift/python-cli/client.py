import sys
import time
import random
sys.path.append("gen-py")
import argparse
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol
from OpenSourceProjects import Projects
from OpenSourceProjects import ttypes

# ----------------- Helper function for testing ------------------------
def make_project(name, host, day, month, year):
	p = ttypes.Project()
	p.name = name
	p.host = host
	p.inception = ttypes.Date()
	p.inception.year = year
	p.inception.month = month
	p.inception.day = day
	return p

# Change number of requests here
requests = 1000000

# ----------------------------1 million get()----------------------------#
def get_test(client):
	start = time.time()
	
	for i in range(requests):
		client.get("Thrift")
	
	end = time.time()

	return end - start


# --------------------------1 million create()---------------------------#
def create_test(client):
    p = make_project("Thrift", "AFS", 10, 1, 2007)
    start = time.time()	
    for i in range(requests):
        client.create(p)

    end = time.time()
    return end - start


# -------------------1 million get() then create()-----------------------#
def get_create_test(client):
	start = time.time()
	
	for i in range(requests):
		p = make_project("Thrift", "AFS", 10, 1, 2007)
		client.create(p)
		client.get("Thrift")
	
	end = time.time()

	return end - start

#---------------Call the appropriate test based on user input------------#
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-H', '--host', default='localhost')
    parser.add_argument('-p', '--port', default='9090')
    parser.add_argument('-a', '--action', default='1')
    args = vars(parser.parse_args())

    print("[Client] Host %s, Port %s, Action %s" %(args['host'], args['port'], args['action']))      

    trans = TSocket.TSocket(args['host'], args['port'])
    trans = TTransport.TBufferedTransport(trans)
    proto = TCompactProtocol.TCompactProtocol(trans)
    client = Projects.Client(proto)
    trans.open()

    if (args['action'] == '1'):
        print("Time to get() %d times: %s" % (requests, get_test(client)))
    elif (args['action'] == '2'):
        print("Time to create() %d times: %s" % (requests, create_test(client)))
    else:
        print("Time to create() then get() %d times: %s" % (requests, get_create_test(client)))

    trans.close()