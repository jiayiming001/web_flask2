import time


def log(*args, **kwargs):
    format = "%Y/%m/%d %H/%M/%S"
    value = int(time.time())
    dt = time.strftime(format, value)
    with open('log.gua.txt', 'a', encoding='utf-8') as f:
        print(dt, *args, file=f, **kwargs)

