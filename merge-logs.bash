#!/bin/bash

if [ $# -lt 1 ]; then
  echo "usage: $0 <etcd|zookeeper> <cluster number> [write-ratio...] " 1>&2
fi

base=$1
cluster=$2
shift
shift

mkdir -p log

for ratio in $*; do
  cat ${base}/log/log-dur-${ratio}-${cluster}-* > log/dur-${ratio}-${cluster}-${base}.txt
  cat ${base}/log/log-ts-${ratio}-${cluster}-* > log/ts-${ratio}-${cluster}-${base}.txt
done
