"""REST client that makes requests from server"""
from __future__ import print_function
import time
import argparse
import httplib

# Change number of requests here
REQUESTS = 1000000
JSON = '{"name":"Thrift", "host":"AFS", "day":"1", "month":"10","year":"2007"}'
HEADERS = {"Content-Type": "application/json", "Accept":"json"}

# ----------------------------1 million get()----------------------------#
def get_test(client):
    """Calls get() 1 million times"""
    client.request("POST", "/projects", JSON, HEADERS)
    client.getresponse()
    start = time.time()
    for _ in range(REQUESTS):
        client.request("GET", "/projects/Thrift")
        resp = client.getresponse()
        resp.read()
    end = time.time()
    return end - start

# --------------------------1 million create()---------------------------#
def create_test(client):
    """Calls create() 1 million times"""
    start = time.time()
    for _ in range(REQUESTS):
        client.request("POST", "/projects", JSON, HEADERS)
        resp = client.getresponse()
        resp.read()
    end = time.time()
    return end - start

# -------------------1 million get() then create()-----------------------#
def get_create_test(client):
    """Calls create(), then get() 1 million times"""
    start = time.time()
    for _ in range(REQUESTS):
        client.request("POST", "/projects", JSON, HEADERS)
        resp = client.getresponse()
        resp.read()
        client.request("GET", "/projects/Thrift")
        resp = client.getresponse()
        resp.read()
    end = time.time()
    return end - start

#---------------Call the appropriate test based on user inPOST------------#
if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('-H', '--host', default='localhost')
    PARSER.add_argument('-p', '--port', default='9090')
    PARSER.add_argument('-a', '--action', default='1')
    ARGS = vars(PARSER.parse_args())
    print("[Client] Host %s, Port %s, Action %s" %(ARGS['host'], ARGS['port'], ARGS['action']))
    CLIENT = httplib.HTTPConnection(ARGS['host'], int(ARGS['port']))
    CLIENT.connect()
    if ARGS['action'] == '1':
        print("Time to get() %d times: %s" % (REQUESTS, get_test(CLIENT)))
    elif ARGS['action'] == '2':
        print("Time to create() %d times: %s" % (REQUESTS, create_test(CLIENT)))
    else:
        print("Time to create() then get() %d times: %s" % (REQUESTS, get_create_test(CLIENT)))
    CLIENT.close()
