#!/bin/bash

pid=`jps | grep "QuorumPeerMain" | cut -f1 -d" "`
kill -9 $pid
