import os

import redis

from video_clean.worker.worker import VideoCleaningWorker


class TestVideoCleaner:

    def test_video_cleaner(self):
        os.environ['REDIS_HOST'] = "localhost"
        cache = redis.Redis("localhost", 6379)

        cache.lpush("video_cleaning", "test")
        vc = VideoCleaningWorker()

        vc.single_loop()

        rez = cache.hget("result", "test")

        assert(rez == b"test_transformed")
