import sys
import time
import random
sys.path.append("gen-py")
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol
from OpenSourceProjects import Projects
from OpenSourceProjects import ttypes

def is_valid_host(h):
	return h != None

def is_valid_port(p):
	return p != None

def is_valid_action(a):
	if type(a) == str and a.isdigit():
		a = int(a)
		return (a == 1 or a == 2 or a == 3)
	return False

host = None
port = None
action = None

while (not is_valid_host(host)):
	print("Press enter to select localhost")
	host = raw_input("Host: ")
	if (host == ""):
		host = "localhost"
		break

while (not is_valid_port(port)):
	print("Press enter to select 9090")
	port = raw_input("Port: ")
	if (port == ""):
		port = 9090
		break

while (not is_valid_action(action)):
	print("Press enter to select 1")
	action = raw_input("Enter 1 for get(), 2 for create(), or 3 for create() followed by get(): ")
	if (action == ""):
		action = 1
		break

print("You have selected %s for host, %s for port, and %s for action" %(host, port, action))      

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
def get_test():
	trans = TSocket.TSocket(host, port)
	trans = TTransport.TBufferedTransport(trans)
	proto = TCompactProtocol.TCompactProtocol(trans)
	client = Projects.Client(proto)
	trans.open()
	
	p = make_project("Thrift", "AFS", 10, 1, 2007)
	client.create(p)

	start = time.time()
	
	for i in range(requests):
		client.get("Thrift")
	
	end = time.time()
	trans.close()
	
	return end - start


# --------------------------1 million create()---------------------------#
def create_test():
	trans = TSocket.TSocket(host, port)
	trans = TTransport.TBufferedTransport(trans)
	proto = TCompactProtocol.TCompactProtocol(trans)
	client = Projects.Client(proto)
	trans.open()

	start = time.time()
	
	for i in range(requests):
		p = make_project("Thrift", "AFS", 10, 1, 2007)
		client.create(p)
	
	end = time.time()
	onecc = end - start

	start = time.time()
	proj_get = client.get(name)
	end = time.time()

	trans.close()
	
	return end - start


# -------------------1 million get() then create()-----------------------#
def get_create_test():
	trans = TSocket.TSocket(host, port)
	trans = TTransport.TBufferedTransport(trans)
	proto = TCompactProtocol.TCompactProtocol(trans)
	client = Projects.Client(proto)
	trans.open()

	start = time.time()
	
	for i in range(requests):
		p = make_project("Thrift", "AFS", 10, 1, 2007)
		client.create(p)
		client.get("Thrift")
	
	end = time.time()
	onecc = end - start

	start = time.time()
	proj_get = client.get(name)
	end = time.time()

	trans.close()
	
	return end - start

#---------------Call the appropriate test based on user input------------#
if (action == 1):
	print("Time to get() %d times: %s" % (requests, get_test()))
elif (action == 2):
	print("Time to create() %d times: %s" % (requests, create_test()))
else:
	print("Time to create() then get() %d times: %s" % (requests, get_create_test()))
