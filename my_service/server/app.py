import time
import os
from my_service.helpers.cache import RedisQueue
from flask import Flask

###################
# Global vars
###################

app = Flask(__name__)
redis_host = os.environ.get('REDIS_HOST') or "redis"
redis_port = os.environ.get('REDIS_PORT') or 6379
cache = RedisQueue(host=redis_host, port=redis_port)


def add_request(video_path):
    cache.lpush('video_cleaning', video_path)


@app.route('/<word>')
def show(word="word"):
    """
    GET endpoint where the additional URI is used as the task to process

    Example : http://localhost:5000/something will define video_url="something"

    The expected result in the toy example is "something_processed"
    """
    video_url = word
    
    # Send the task to the worker through Redis
    add_request(video_url)

    # Wait for the result on the right path
    new_version = cache.fetch_result(video_url)

    return new_version

@app.route('/')
def index():
    return show()
