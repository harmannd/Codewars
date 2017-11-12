def make_readable(seconds):
    time = ""

    if seconds >= 3600:
        time += add_zero(str(int(seconds / 3600))) + ":"
        seconds = seconds % 3600
    else:
        time += "00:"
    if seconds >= 60:
        time += add_zero(str(int(seconds / 60))) + ":"
        seconds = seconds % 60
    else:
        time += "00:"
    time += add_zero(str(seconds))

    return time

def add_zero(value):
    if int(value) < 10:
        value = "0" + value
    return value