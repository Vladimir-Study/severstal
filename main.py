from photos import Photo
from redis_cls import MyRedis
from datebase import session, Images
from logger import logger
import pathlib
import threading
from time import sleep

redis = MyRedis()
photo = Photo()
lock = threading.Lock()


def put_redis() -> None:
    try:
        current_directory = pathlib.Path().absolute()
        photo_directory = current_directory.joinpath('src/images/')
        dir = photo_directory.iterdir()
        flag = True
        count = 1
        while flag:
            try:
                photo_size = photo.file_size(next(dir))
                logger.info(f"Put file size {photo_size}, count = {count}")
                lock.acquire()
                redis.in_queue('images', photo_size)
                lock.release()
                count += 1
            except StopIteration:
                flag = False
    except Exception as E:
        logger.error(E)


def get_redis() -> None:
    try:
        flag = True
        count = 1
        while flag:
            lock.acquire()
            image_size = redis.out_queue('images')
            lock.release()
            if image_size == None:
                flag = False
            else:
                images = Images(
                    size_images=image_size
                )
                session.add(images)
                session.commit()
                logger.info(f"Get image size, count = {count}")
                count += 1
        logger.info(f"Number of files send: {count-1}")
    except Exception as E:
        logger.error(E)

if __name__ == "__main__":
    print('asdfas')
    tread_put = threading.Thread(target=put_redis)
    tread_get = threading.Timer(1, get_redis)
    tread_put.start()
    tread_get.start()
    tread_put.join()
    tread_get.join()