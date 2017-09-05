#!/bin/sh
if [ -z $1 ];then
    echo "usage:./dns-reverse-ptr.sh domain.com " 
fi

for ip in $(host $1|grep "has address" |cut -d " " -f4|cut -d "." -f1,2,3|sort -u);do
    echo "Reversig ptr recored for:" $ip[0-255]
    for i in $(seq 0 255);do
        echo $ip.$i
        host $ip.$i|grep `echo $1|cut -d "." -f1`|cut -d " " -f1,5
    done
done
