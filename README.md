# api-bench

API systems benchmarks

This project aims to compare popular API styles. The API styles/systems compared are:

- Apache Thrift
- CNCF gRPC/ProtoBuf
- JSON/HTTP
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

All client programs must be named `client` and accept a server ip and port on the command line.

```
$ client 10.4.6.2 9090
```

If no command line arguments are provided, the client should use **localhost** and port **9090**. All client project
files for a given language must be in a directory named ./[apisys]/[lang]-cli. For example: `./thrift/python-cli`.


## Server

All server programs must be named `server` and all servers must listen on port **9090** on **all interfaces**. All
server project files for a given language must be in a directory named ./[apisys]/[lang]-svr. For example:
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
        return CreateResult(42, "sucess")

```


## Apache Thrift

To compile thrift APIs use:

```
$ docker run -v ~/api-bench/project.thrift:/project.thrift -v ~/api-bench/:/out thrift thrift -o /out -gen py project.thrift

$ chown -R user ~/api-bench/*
```
