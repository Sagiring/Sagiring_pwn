FROM ubuntu:20.04

RUN sed -i "s/http:\/\/archive.ubuntu.com/http:\/\/mirrors.tuna.tsinghua.edu.cn/g" /etc/apt/sources.list && \
    apt-get update && apt-get -y dist-upgrade && \
    apt-get install -y lib32z1 xinetd

RUN useradd -m ctf

WORKDIR /home/ctf/work

RUN cp -R /usr/lib* /home/ctf/work

RUN mkdir /home/ctf/dev && \
    mknod /home/ctf/dev/null c 1 3 && \
    mknod /home/ctf/dev/zero c 1 5 && \
    mknod /home/ctf/dev/random c 1 8 && \
    mknod /home/ctf/dev/urandom c 1 9 && \
    chmod 666 /home/ctf/dev/*

RUN mkdir /home/ctf/bin && \
    cp /bin/sh /home/ctf/bin && \
    cp /bin/ls /home/ctf/bin && \
    cp /bin/cat /home/ctf/bin

COPY ./ctf.xinetd /etc/xinetd.d/ctf
COPY ./start.sh /start.sh
RUN echo "Blocked by ctf_xinetd" > /etc/banner_fail

RUN chmod +x /start.sh

# 复制脚本文件到容器中
COPY ./start_damon.sh /start_damon.sh

# 设定脚本文件的执行权限
RUN chmod +x /start_damon.sh

# 在容器启动时执行脚本

COPY ./bin/flag /home/ctf/
COPY ./bin/mkudisk /home/ctf/work/
COPY ./bin/vold /home/ctf/work/
COPY ./libc-2.31.so /home/ctf/lib/x86_64-linux-gnu 
RUN chown -R root:ctf /home/ctf && \
    chmod -R 750 /home/ctf && \
    chmod 700 /home/ctf/flag

RUN mkdir /home/ctf/tmp && \
    chmod 777 /home/ctf/tmp && \
    mkdir /home/ctf/mybin && \
    mkdir /home/ctf/mnt && \
    chmod 777 /home/ctf/work
    
COPY ./log /home/ctf/mybin
CMD ["/start.sh"]
EXPOSE 9999
