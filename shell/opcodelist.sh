#!/bin/bash
bin=$1
if [ "$1" == "" ];then
	echo "provide binary"
	exit
fi

shellcode=$(objdump -D $bin |grep '[0-9a-f]:'|grep -v 'file'|cut -f2 -d:|cut -f1-6 -d' '|tr -s ' '|tr '\t' ' '|sed 's/ $//g'|sed 's/ /\\x/g'|paste -d '' -s |sed 's/^/"/'|sed 's/$/"/g')
echo "[*] shellcode"
echo $shellcode

echo "[*] Loader"

echo "char shellcode[] = ""$shellcode""

int main(){

    int *ret;
    ret = (int *)&ret +2;
    (*ret) = (int)shellcode;
}
"
