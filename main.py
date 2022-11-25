import logging


from kuaishou import KsLive


if __name__ == '__main__':
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)
    ks = KsLive.Tool()
    ks.wssServerStart('https://live.kuaishou.com/u/3xv4wcvybm8qzv9')