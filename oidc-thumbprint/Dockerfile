FROM golang:latest

WORKDIR /app

COPY . .
RUN go get hacking.jvt.me/oidc-thumbprint && go build

ENTRYPOINT ["/app/oidc-thumbprint"]
