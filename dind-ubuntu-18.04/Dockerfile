FROM ubuntu:20.04

MAINTAINER Ajeet Khan <i.ajeetkhan@gmail.com>

# Fake dmsetup, as device-mapper isn't compatible for static builds
ADD ./dmsetup /usr/local/bin/dmsetup

# Let's start with some basic stuff.
RUN apt-get update -qq && apt-get install -qqy \
    apt-transport-https \
    ca-certificates \
    curl \
    lxc \
    iptables
    
# Install Docker from Docker Inc. repositories.
RUN curl -sSL https://get.docker.com/ | sh

# Install the magic wrapper.
ADD ./wrapdocker /usr/local/bin/wrapdocker
RUN chmod +x /usr/local/bin/wrapdocker

# Define additional metadata for our image.
VOLUME /var/lib/docker.sock
CMD ["/usr/local/bin/wrapdocker"]