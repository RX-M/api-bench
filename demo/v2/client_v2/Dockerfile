FROM python:alpine
RUN pip install thrift
COPY client.py gen-py/ ./
CMD ["python", "client.py", "--host", "ossproj.default.svc.cluster.local", "--port", "9090"]

