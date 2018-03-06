from datetime import timedelta

def what_is_the_time(time_in_mirror):
    mirror = timedelta(hours=int(time_in_mirror.split(':')[0]), minutes=int(time_in_mirror.split(':')[1]))
    base = timedelta(hours=24, minutes=0)
    actual_time = str(base - mirror)[:-3]
    hour = int(actual_time[:2])
    if hour > 12:
        actual_time = str(hour - 12) + actual_time[2:]
    if len(actual_time) != 5:
        actual_time = '0' + actual_time
    return actual_time


