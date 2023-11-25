#!/bin/bash

# 检测mkudisk进程是否存在
check_mkudisk() {
    pgrep mkudisk > /dev/null  # 检查mkudisk进程是否在运行
}

# 检测vold进程是否存在
check_vold() {
    pgrep vold > /dev/null  # 检查vold进程是否在运行
}

# 启动vold进程
start_vold() {
    nohup /home/ctf/work/vold &  # 启动vold，并将其放入后台运行
    echo "Started vold."
}

# 关闭vold进程
stop_vold() {
    pkill vold  # 杀死所有名为vold的进程
    echo "Stopped vold."
}

# 循环检测mkudisk进程是否存在，根据情况启动或关闭vold
while true; do
    if check_mkudisk; then
        if ! check_vold; then
            start_vold
        fi
    else
        if check_vold; then
            stop_vold
        fi
    fi
    sleep 1  # 休眠1秒钟再进行下一轮循环
done

