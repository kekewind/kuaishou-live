import logging


from kuaishou import KsLive


if __name__ == '__main__':
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)
    ks = KsLive.Tool()
    cookie = '你的cookie'
    url = 'https://live.kuaishou.com/u/haiwangqi'
    ks.init(url, cookie)
    # ks.getUserCardInfoById('a604500425')
    # ks.follow('haiwangqi', 2)
    # ks.sendMsg("666~", ks.getLiveRoomId())
    # ks.wssServerStart()