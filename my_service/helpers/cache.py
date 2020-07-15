import redis
import time


class RedisQueue(redis.Redis):
    """
    Extension of redis to handle the queue of tasks and the results retrieval
    """

    def post_result(self, key, value):
        self.hset("result", key, value)

    def fetch_result(self, key):
        """
        Infinite polling is handled by this function.

        For real world application a timeout would be needed
        """
        result = self.hget("result", key) 

        while result is None:
            result = self.hget("result", key) 
            time.sleep(1)

        # Redis stores its results in bin format by default
        if type(result) == bytes:
            result = result.decode("utf-8")

        return result