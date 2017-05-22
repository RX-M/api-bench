# api-bench
API systems benchmarks

To compile thrift APIs use:

```
$ docker run -v ~/linuxcon/loadtest/project.thrift:/project.thrift -v ~/linuxcon/loadtest/out:/out thrift thrift -o /out -gen py project.thrift
```
