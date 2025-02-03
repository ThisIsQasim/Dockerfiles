FROM python:3.13-slim

RUN DEBIAN_FRONTEND=noninteractive \
	apt-get update && \
	apt-get install -y --no-install-recommends \
        openjdk-17-jre-headless

RUN pip install tabula-py actualpy
