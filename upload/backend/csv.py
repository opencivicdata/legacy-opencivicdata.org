import csv


def csv_dict_reader(stream):
    stream = stream.decode('utf-8').splitlines()
    ret = csv.DictReader(stream)
    return ret
