FROM python:3.14-slim

RUN apt-get update && \
    apt-get upgrade -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    pkg-config \
    libsystemd-dev \
    gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir paho-mqtt systemd-python mppsolar[systemd]

WORKDIR /etc/mpp-solar

CMD ["mpp-solar", "-C", "mpp-solar.conf", "--daemon"]
