import sys
import time
import random
sys.path.append("../out/gen-py")
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol
from OpenSourceProjects import Projects
from OpenSourceProjects import ttypes

# ----------------- Helper functions for testing ------------------------
def make_project(name, host, day, month, year):
	p = ttypes.Project()
	p.name = name
	p.host = host
	p.inception = ttypes.Date()
	p.inception.year = year
	p.inception.month = month
	p.inception.day = day
	return p

def make_random_name():
	name = ""
	for i in range(5):
		name += chr(random.randint(65,90))
	return name

# ------------------------------1 client--------------------------------#
def one_client():
	trans = TSocket.TSocket("localhost", 9090)
	trans = TTransport.TBufferedTransport(trans)
	proto = TCompactProtocol.TCompactProtocol(trans)
	client = Projects.Client(proto)
	trans.open()

	start = time.time()
	name = make_random_name()
	p = make_project(name, "AFS", 10, 1, 2007)
	client.create(p)
	end = time.time()
	onecc = end - start

	start = time.time()
	proj_get = client.get(name)
	end = time.time()
	onecg = end - start

	trans.close()
	
	return (onecc, onecg)

def one(x):
	create = 0
	get = 0
	for i in range(x):
		create += one_client()[0]
		get += one_client()[1]
	return (create/x, get/x)

# -------------------------------10 clients-----------------------------#
def ten_clients():
	trans = TSocket.TSocket("localhost", 9090)
	trans = TTransport.TBufferedTransport(trans)
	proto = TCompactProtocol.TCompactProtocol(trans)
	client = Projects.Client(proto)
	trans.open()

	start = time.time()
	names = []
	for i in range(10):
		name = make_random_name()
		names.append(name)
		p = make_project(name, "AFS", 10, 1, 2007)
		client.create(p)
	end = time.time()
	tencc = end - start

	start = time.time()
	for name in names:
		client.get(name)
	end = time.time()
	tencg = end - start
	
	trans.close()
	
	return (tencc, tencg)

def ten(x):
	create = 0
	get = 0
	for i in range(x):
		create += ten_clients()[0]
		get += ten_clients()[1]
	return (create/x, get/x)

# -------------------------------100 clients-----------------------------#
def hundred_clients():
	trans = TSocket.TSocket("localhost", 9090)
	trans = TTransport.TBufferedTransport(trans)
	proto = TCompactProtocol.TCompactProtocol(trans)
	client = Projects.Client(proto)
	trans.open()

	start = time.time()
	names = []
	for i in range(100):
		name = make_random_name()
		names.append(name)
		p = make_project(name, "AFS", 10, 1, 2007)
		client.create(p)
	end = time.time()
	huncc = end - start

	start = time.time()
	for name in names:
		client.get(name)
	end = time.time()
	huncg = end - start

	trans.close()

	return (huncc, huncg)

def hundred(x):
	create = 0
	get = 0
	for i in range(x):
		create += hundred_clients()[0]
		get += hundred_clients()[1]
	return (create/x, get/x)

# ------------------------------1000 clients-----------------------------#
def thousand_clients():
	trans = TSocket.TSocket("localhost", 9090)
	trans = TTransport.TBufferedTransport(trans)
	proto = TCompactProtocol.TCompactProtocol(trans)
	client = Projects.Client(proto)
	trans.open()

	start = time.time()
	names = []
	for i in range(1000):
		name = make_random_name()
		names.append(name)
		p = make_project(name, "AFS", 10, 1, 2007)
		client.create(p)
	end = time.time()
	thouscc = end - start

	start = time.time()
	for name in names:
		client.get(name)
	end = time.time()
	thouscg = end - start

	trans.close()
	
	return (thouscc, thouscg)

def thousand(x):
	create = 0
	get = 0
	for i in range(x):
		create += thousand_clients()[0]
		get += thousand_clients()[1]
	return (create/x, get/x)

#----------------------------- Results -----------------------------------

x = 100 # number of trials to run
print("Results")
print("-----------------------------------------------------")
print("1 client create():     %s seconds" %one(x)[0])
print("1 client get():        %s seconds" %one(x)[1])
print("10 clients create():   %s seconds" %ten(x)[0])
print("10 clients get():      %s seconds" %ten(x)[1])
print("100 clients create():  %s seconds" %hundred(x)[0])
print("100 clients get():     %s seconds" %hundred(x)[1])
print("1000 clients create(): %s seconds" %thousand(x)[0])
print("1000 clients get():    %s seconds" %thousand(x)[1])
