FROM python:alpine
RUN pip install thrift
COPY server.py gen-py ./
CMD ["python", "server.py"]
