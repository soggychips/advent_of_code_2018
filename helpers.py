def get_input(day):
    import os
    if str(day) in os.listdir("input"):
        print "Data for day {} found locally.".format(day)
        text = open("input/{}".format(day), 'r').read()
    else:
        print "Data for day {} not found locally. Downloading...".format(day)
        import requests
        from config import cookies
        url = "https://adventofcode.com/2018/day/{}/input".format(day)
        text = requests.get(url, cookies=cookies).text.strip()
        with open("input/{}".format(day), 'w') as f:
            f.write(text)
    return text.split('\n')


def timed(f):
    from time import time
    def fun(*a, **k):
        s = time()
        o = f(*a, **k)
        e = time()
        print ("Func: {} Time taken: {} ms".format(f.__name__, ((e - s) * 1000)))
        return o

    return fun
