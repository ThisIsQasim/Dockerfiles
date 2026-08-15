# Builds vminsert/vmselect/vmstorage from a plain shallow clone of
# VictoriaMetrics/VictoriaMetrics at a given version tag (the workflow
# clones this fresh per build - see
# ../.github/workflows/victoriametrics.yaml - rather than a committed
# submodule, since there's no single commit that would work for all the
# versions being built).
#
# Custom-written because upstream has no Dockerfile at all for these
# three components past each LTS line's initial .0 release - checked
# directly against the repo: neither the plain version tag nor any
# "-cluster" suffixed tag exists for a patch release (e.g. v1.122.27
# has no v1.122.27-cluster tag, unlike v1.122.0-cluster which does).
# Only the .0 release ever got the full "buildable release" treatment;
# every later LTS patch is Enterprise-pipeline-only and its public tag
# is just a source snapshot - main.go/go.mod/vendor are there, no
# Dockerfile. Building the Go binary inside this multi-stage image
# works from that same source snapshot regardless.
#
# One Dockerfile for all three cluster components - which one gets built
# is picked by the APP_NAME build-arg (vminsert, vmselect, or vmstorage).
# Flags below mirror upstream's own deployment/docker/Makefile
# app-via-docker target as closely as practical.

ARG GO_VERSION=1.26.5

FROM golang:${GO_VERSION} AS builder
ARG APP_NAME
ARG VERSION
WORKDIR /src
COPY . .
RUN CGO_ENABLED=1 go build -trimpath -buildvcs=false \
    -ldflags "-extldflags '-static' -X 'github.com/VictoriaMetrics/VictoriaMetrics/lib/buildinfo.Version=${APP_NAME}-${VERSION}'" \
    -tags 'netgo osusergo' \
    -o /out/app-prod \
    "./app/${APP_NAME}"

FROM alpine:3.24.1
RUN apk add --no-cache ca-certificates
COPY --from=builder /out/app-prod /vm-app
# vminsert:8480, vmselect:8481, vmstorage:8482 (HTTP) + 8400/8401 (internal
# insert/select-to-storage traffic) - harmless to expose all regardless of
# which component this particular image is.
EXPOSE 8480 8481 8482 8400 8401
ENTRYPOINT ["/vm-app"]
