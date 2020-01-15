def make_readable(seconds):
    # Do something
    list = []
    while seconds != 0:
        list.append(seconds % 60)
        seconds = seconds // 60
    return ":".join(list)


def make_readable(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)