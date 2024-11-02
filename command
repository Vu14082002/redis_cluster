redis-cli --cluster create 192.168.10.2:6379 192.168.10.3:6379 192.168.10.4:6379 --cluster-replicas 0
redis-cli --cluster create 203.171.29.4:6379 203.171.29.4:6380 203.171.29.4:6381 --cluster-replicas 0

redis-cli -h 127.0.0.1 -p 6379 cluster info