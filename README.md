# api-bench

API systems benchmarks

This project aims to compare popular API styles. The API styles/systems compared are:

- Apache Thrift
- CNCF gRPC/ProtoBuf
- JSON/HTTP (not yet)
- REST/ROA

Repo layout:
- root - contains no files with the exception of this README
    - thrift - contains all of the Apache thrift test files
    - grpc - contains all of the gRPC test files
    - rest - contains all of the RESTful service test files

The API tested in all cases is something like this (in pseudo-code):

```
struct date {
    i16 year
    i16 month
    i16 day
}

struct project {
    date inception
    string name
    string host
}

struct create_result {
    1: i16 code
    2: string message
}

interface Projects {
    project get(string name)
    create_result create(project p)
}
```

The RESTfult version uses the resource route `/projects/`. To get a project in REST we use `GET /projects/[name]` and
to create a project we use `PUT /projects/[name]`.


## Client

All client programs must be named `client` and accept a server ip, port and action on the command line. Action 1 calls the get() function, Action 2 calls the create() function and Action 3 calls create() then get(). This allows us to seperate performance for read and write operations (important when looking at REST).

```
$ client --host 10.4.6.2 --port 9090 --action 1
```

If no command line arguments are provided, the client should use **localhost**, port **9090** and action **1**. All client project
files for a given language must be in a directory named ./[apisys]/[lang]-cli. For example: `./thrift/python-cli`.


## Server

All server programs must be named `server` and all servers must listen on port **9090** on **all interfaces**. Servers should accept an alternative port on the command line. All server project files for a given language must be in a directory named ./[apisys]/[lang]-svr. For example:
`./thrift/python-svr`.

In response to get() all servers should return data identical to the following:

```python
    def get(self, name):
        p = ttypes.Project()
        p.name = name
        p.host = "ASF"
        p.inception = ttypes.Date()
        p.inception.year = 2007
        p.inception.month = 1
        p.inception.day = 10
        return p
```

In response to create() servers should return data identical to the following:

```python
    def create(self, p):
        #self.projects[p.name] = p
        return CreateResult(200, "ok")

```

The benchmark goal is not to test how quickly languages execute complex logic, rather it is to compare the performance of the API mechanics.


## Apache Thrift

To compile thrift APIs use:

```
$ docker run -v ~/api-bench/thrift/project.thrift:/project.thrift -v ~/api-bench/thrift/[appdir]:/out thrift thrift -o /out -gen [lang] project.thrift

Output will be owned by root so you may then want to:

$ chown -R user ~/api-bench/*
```
