import csv


def csv_dict_reader(stream):
    stream = stream.decode('utf-8').splitlines()
    ret = csv.DictReader(stream)
    return ({k.lower(): v for (k, v) in x.items()} for x in ret)
