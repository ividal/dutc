# TASK: given the below timings, print out a performance
#       report listing how long each step took
#       e.g., start    -          pre-boot: 23 μs
#             pre-boot -              boot: 73 μs
#             boot     - filesystems ready: 86 μs
#             ...

from datetime import datetime, timedelta
from random import randrange

times = {
    'start':             (start := datetime.today()),
    'pre-boot':          start + timedelta(microseconds=  0 + randrange(10, 100)),
    'boot':              start + timedelta(microseconds=100 + randrange(10, 100)),
    'filesystems ready': start + timedelta(microseconds=200 + randrange(10, 100)),
    'os ready':          start + timedelta(microseconds=300 + randrange(10, 100)),
    'networking ready':  start + timedelta(microseconds=400 + randrange(10, 100)),
    'ready for use':     start + timedelta(microseconds=500 + randrange(10, 100)),
}


delta_titles = list(times.keys())

[print(f'{delta_titles[i]} - {delta_titles[i+1]} = {(times[delta_titles[i+1]] - times[delta_titles[i]]).total_seconds()*1e6} μs') for i in range(len(delta_titles)) if i < len(delta_titles) - 1]


# TASK: amend the above, printing out the time when the proccess
#       started and stopped as well as each time along the way
#       e.g., start...                             09:05:05.000027
#             start    -          pre-boot: 23 μs, 09:05:05.000050
#             pre-boot -              boot: 73 μs, 09:05:05.000123
#               [ ... SNIP SNIP SNIP... ]
#                        ... ready for use         09:05:05.004231
# NOTE: the format for the first and last line are different

# !! Why does formatting not work with times[...] outside the list comprehension?

print(f"start... \t\t \t\t\t\t\t{times['start']}")

[print(f'{delta_titles[i]:<20} - {delta_titles[i+1]:>20}: {(times[delta_titles[i+1]] - times[delta_titles[i]]).total_seconds()*1e6:>10} μs,\
       {times[delta_titles[i]]}') for i in range(len(delta_titles)) if i < len(delta_titles) - 1]
print(f"\t\t  ...{delta_titles[-1]:>20}:\t\t\t{times[delta_titles[-1]]}")


