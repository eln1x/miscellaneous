#!/bin/sh
if [ -z $1 ];then
    echo "usage: ./dns-zone-transfer.sh domain.com"
    exit
fi
for ns in $(host -t ns $1 |cut -d " " -f 4);do
    host -l $1 $ns |grep "has address"
done
