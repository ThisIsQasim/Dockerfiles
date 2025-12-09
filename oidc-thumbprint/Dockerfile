FROM --platform=$BUILDPLATFORM golang:latest AS build

WORKDIR /app

COPY . .
ARG TARGETOS TARGETARCH
ENV GOOS=$TARGETOS GOARCH=$TARGETARCH CGO_ENABLED=0
RUN go mod tidy && go build -o oidc-thumbprint

FROM alpine:3.16
RUN apk add --no-cache ca-certificates
WORKDIR /app
COPY --from=build /app/oidc-thumbprint /app/oidc-thumbprint

ENTRYPOINT ["/app/oidc-thumbprint"]
