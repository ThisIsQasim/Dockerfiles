FROM python:3.6

RUN pip install --no-cache-dir elasticsearch-curator

COPY ./config.yml /root/.curator/curator.yml

CMD ["sleep","inf"]