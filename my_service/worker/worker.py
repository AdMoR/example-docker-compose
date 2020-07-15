import time
import os
from my_service.helpers.cache import RedisQueue


class ExampleWorker:
    """
    This worker expectes to read tasks from the redis queue, process it 
    and post the result on a specific location

    process function defines the business logic
    single_loop defines the 
    """

    def __init__(self):
        redis_host = os.environ.get('REDIS_HOST') or "redis"
        redis_port = os.environ.get('REDIS_PORT') or 6379
        self.cache = RedisQueue(host=redis_host, port=redis_port)
        self.queue = "video_cleaning"

    def process(self, video_url):
        """
        A simple logic is applied here to avoid making the code too complex
        """
        time.sleep(1)
        if type(video_url) == bytes:
            video_url = video_url.decode("utf-8")
        return video_url + "_transformed"

    def single_loop(self):
        """
        This function handles 
        - the retrieval from the redis queue of its next work
        - the processing
        - The write donw of the result

        Some sleep are done to avoid polling the redis too much
        """
        task = self.cache.lpop(self.queue) 

        if task is not None:
            result = self.process(task)
            self.cache.post_result(task, result)
        else:
            time.sleep(1)

    def run(self):
        """
        The main of the worker, an infinite loop of single_loop
        """
        while True:
            self.single_loop()

if __name__ == "__main__":
    worker = ExampleWorker()
    worker.run()