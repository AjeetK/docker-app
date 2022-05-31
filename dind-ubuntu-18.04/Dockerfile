FROM ubuntu:latest
RUN apt-get update 
RUN apt install curl docker.io -y
RUN apt update && apt dist-upgrade -y
RUN apt-get install -y libapparmor-dev apparmor-utils  
COPY ./apparmor.d/docker-nginx /etc/apparmor.d/containers/docker-nginx
#RUN export BANE_SHA256="69df3447cc79b028d4a435e151428bd85a816b3e26199cd010c74b7a17807a05" && curl -fSL "https://github.com/genuinetools/bane/releases/download/v0.4.4/bane-linux-amd64" -o "/usr/local/bin/bane" \
#       && echo "${BANE_SHA256}  /usr/local/bin/bane" | sha256sum -c - \
#       && chmod a+x "/usr/local/bin/bane"
WORKDIR /etc/apparmor.d/containers
#RUN bane docker-nginx
#RUN /usr/sbin/apparmor_parser -r -W /etc/apparmor.d/containers/docker-nginx
RUN docker --version
RUN chmod 666 /dev/null
ENTRYPOINT nohup dockerd