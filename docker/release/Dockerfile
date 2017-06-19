FROM bottledjinni/botbackend-base:latest
MAINTAINER Anwar HAssen <anwar.hassen@aalto.fi>

# Copy application artifacts
COPY target /wheelhouse

# Install application
RUN . /appenv/bin/activate && \
    pip install --no-index -f /wheelhouse botbackend && \
    rm -rf /wheelhouse
