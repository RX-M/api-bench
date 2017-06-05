FROM python:alpine
RUN pip install thrift
COPY server_v2.py gen-py ./
CMD ["python", "server_v2.py"]
