import redis

class MyRedis():

    def in_queue(self, file_name, file_size):
        with redis.Redis(decode_responses=True, port=6379) as conn:
            conn.rpush(file_name, file_size)

    def out_queue(self, file_name):
        with redis.Redis(decode_responses=True, port=6379) as conn:
            return conn.lpop(file_name)
