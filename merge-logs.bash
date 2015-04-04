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
  cat ${base}/log/log-dur-${ratio}-${cluster}-write* > log/dur-${ratio}-${cluster}-write-${base}.txt
  cat ${base}/log/log-dur-${ratio}-${cluster}-read* > log/dur-${ratio}-${cluster}-read-${base}.txt
  cat ${base}/log/log-ts-${ratio}-${cluster}-write* > log/ts-${ratio}-${cluster}-write-${base}.txt
  cat ${base}/log/log-ts-${ratio}-${cluster}-read* > log/ts-${ratio}-${cluster}-read-${base}.txt
done
