#!/bin/bash

if [ $# -lt 1 ]; then
  echo "usage: $0 <etcd|zookeeper> [write-ratio...]" 1>&2
fi

base=$1
shift

mkdir -p log

for ratio in $*; do
  cat ${base}/log/log-dur-${ratio}* > log/dur-${ratio}-${base}.txt
  cat ${base}/log/log-ts-${ratio}* > log/ts-${ratio}-${base}.txt
done
