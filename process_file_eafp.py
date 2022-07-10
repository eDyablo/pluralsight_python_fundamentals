p = "path/to/datafile.dat"


def process_file(path):
    pass


try:
    process_file(p)
except OSError as e:
    print("Could not precess file because {}".format(str(e)))
