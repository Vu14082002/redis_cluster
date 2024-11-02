from rediscluster import RedisCluster

startup_nodes = [
    {"host": "localhost", "port": 6379},
    {"host": "localhost", "port": 6380},
    {"host": "localhost", "port": 6381},
]

client = RedisCluster(
    startup_nodes=startup_nodes,
    decode_responses=True, 
    socket_timeout=5, 
    socket_connect_timeout=5, 
    retry_on_timeout=True, 
    skip_full_coverage_check=True
)
print(client.ping())
client.set("foo", "bar")
print(client.get("foo"))