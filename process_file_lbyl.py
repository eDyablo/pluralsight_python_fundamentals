import os

p = "/path/to/datafile.dat"


def process_file(path):
    pass


if os.path.exists(p):
    process_file(p)
else:
    print("No such file as {}".format(p))
