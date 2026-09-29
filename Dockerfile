# syntax=docker/dockerfile:1.6
# ============================================================
# NEMESIS-CRAB-V2 - Alpine Linux Container (Multi-Stage)
# ============================================================

# ---------- Stage 1: Builder ----------
FROM alpine:3.19 AS builder

LABEL stage="builder"

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Build-time dependencies (removed in final stage)
RUN apk add --no-cache --virtual .build-deps \
        python3 \
        python3-dev \
        py3-pip \
        gcc \
        g++ \
        musl-dev \
        make \
        cmake \
        cargo \
        rust \
        linux-headers \
        libffi-dev \
        openssl-dev \
        libpcap-dev \
        jpeg-dev \
        zlib-dev \
        freetype-dev \
        libx11-dev \
        libxtst-dev \
        libxext-dev \
        libgcrypt-dev \
        libgpg-error-dev \
        libxml2-dev \
        libxslt-dev \
        hdf5-dev \
        git

# Create virtualenv
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN pip install --upgrade pip setuptools wheel

# Install Python deps
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# ============================================================
# ---------- Stage 2: Runtime ----------
# ============================================================
FROM alpine:3.19 AS runtime

LABEL org.opencontainers.image.title="nemesis-crab-v2" \
      org.opencontainers.image.version="2.0.0" \
      org.opencontainers.image.description="Ultimate Cybersecurity Command & Control Platform" \
      org.opencontainers.image.authors="Ian Carter Kulani" \
      org.opencontainers.image.licenses="MIT"

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/opt/venv/bin:$PATH" \
    NEMESIS_HOME=/app \
    TZ=UTC

# Runtime packages only
RUN apk add --no-cache \
        python3 \
        py3-pip \
        bash \
        tini \
        curl \
        wget \
        git \
        ca-certificates \
        tzdata \
        iputils \
        bind-tools \
        traceroute \
        mtr \
        nmap \
        nmap-scripts \
        netcat-openbsd \
        socat \
        whois \
        openssh-client \
        openssl \
        libpcap \
        libffi \
        jpeg \
        zlib \
        freetype \
        libx11 \
        libxtst \
        libxext \
        chromium \
        chromium-chromedriver \
        docker-cli \
        docker-cli-compose \
        procps \
        htop \
        jq \
        yq \
        tcpdump \
        && rm -rf /var/cache/apk/*

# Copy virtualenv from builder
COPY --from=builder /opt/venv /opt/venv

# Create non-root user (but keep root for NET_RAW/NET_ADMIN compat)
RUN addgroup -g 1000 nemesis && \
    adduser -D -u 1000 -G nemesis -h /app -s /bin/bash nemesis

WORKDIR /app

# Copy application files
COPY --chown=nemesis:nemesis nemesis_crab_v2.py /app/
COPY --chown=nemesis:nemesis requirements.txt    /app/
COPY --chown=nemesis:nemesis health.py           /app/
COPY --chown=nemesis:nemesis requirements-check.py /app/
COPY --chown=nemesis:nemesis test-command.py     /app/

# Create runtime directories
RUN mkdir -p /app/.nemesis_crab_v2 \
             /app/.nemesis_crab_v2/payloads \
             /app/.nemesis_crab_v2/keylogs \
             /app/.nemesis_crab_v2/keylog_screenshots \
             /app/.nemesis_crab_v2/captured_credentials \
             /app/.nemesis_crab_v2/scans \
             /app/.nemesis_crab_v2/agents \
             /app/.nemesis_crab_v2/c2_logs \
             /app/.nemesis_crab_v2/dos_logs \
             /app/.nemesis_crab_v2/reverse_engineering \
             /app/.nemesis_crab_v2/cracking \
             /app/.nemesis_crab_v2/docker_scans \
             /app/nemesis_reports \
             /app/temp && \
    chown -R nemesis:nemesis /app

# Healthcheck (uses our health.py)
HEALTHCHECK --interval=30s --timeout=10s --start-period=20s --retries=3 \
    CMD python3 /app/health.py --json --exit-code || exit 1

# Ports
EXPOSE 5000 4444 5555 8080

# Volumes
VOLUME ["/app/.nemesis_crab_v2", "/app/nemesis_reports"]

# Use tini as PID 1
ENTRYPOINT ["/sbin/tini", "--"]

# Default: interactive shell
CMD ["python3", "/app/nemesis_crab_v2.py"]
