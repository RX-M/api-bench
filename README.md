# api-bench
API systems benchmarks

To compile thrift APIs use:

```
$ docker run -v ~/linuxcon/loadtest/project.thrift:/project.thrift -v ~/linuxcon/loadtest/:/out thrift thrift -o /out -gen py project.thrift

$ chown -R user *
```

## Client

All client programs must be named `client` and accept a server ip and port on the command line.

```
$ client 10.4.6.2 9090
```

If no command line arguments are provided, the client should use localhost and port 9090. All client project files for a given language must be in a directory named ./[lang]-cli. For example: `python-cli`.


## Server

All server programs must be named `server` and all servers must listen on port 9090 on all interfaces. All server project files for a given language must be in a directory named ./[lang]-svr. For example: `python-svr`.

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
