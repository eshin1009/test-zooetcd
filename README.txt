--------------------------
Etcd testing client
CS654 Project
--------------------------

etcd verison 2.0.5

Client and Server environment:
   - Amazon EC2
   - AMI: Ubuntu Server 14.04 LTS (HVM), SSD Volume Type - ami-29ebb519
   - t2.micro  (Variable ECUs, 1 vCPUs, 2.5 GHz, Intel Xeon Family, 1 GiB memory, EBS only)
   - 3 to 13 number of servers, and about 200 simulated clients on few dozens of client nodes

Testing details
   - Mixed workload throughput test
   - The read to write ratio will vary from 0% to 100%
   - Test will be done with varying number of servers: 3, 7, and 13
   - Requests per second will be the benchmark
   - Throughput upon failures
     - Test will be done with varying number of servers: 5, 7, and 13
     - The write to read ratios to be tested are: 5%, 20%, 50%
