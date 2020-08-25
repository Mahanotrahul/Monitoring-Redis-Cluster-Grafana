#!/bin/bash

for i in `seq 9100 9105`; do  echo $i; docker run --rm -d -v $(pwd)/redis/redis_$i.conf:/usr/local/etc/redis/redis.conf --net host --name redis_$i redis:alpine redis-server /usr/local/etc/redis/redis.conf; done

# echo "Pinging the redis instances"
# for i in 910{0..5}; do  echo $i; docker run -it --net host redis:alpine redis-cli -p $i ping ; done

echo "Creating cluster. Type yes when prompted"
docker run --rm -it --net host redis:alpine redis-cli --cluster create 127.0.0.1:9100 127.0.0.1:9101 127.0.0.1:9102 127.0.0.1:9103 127.0.0.1:9104 127.0.0.1:9105 --cluster-replicas 1

echo "Performing Cluster Check"
docker run -it --net host redis:alpine redis-cli --cluster check 127.0.0.1:9100

echo "Starting Monitoring"
echo "If you face any issues related to install failure, you can manually import dashboard and datasources from grafana/datasources and grafana/dashboards folder"
docker-compose up
