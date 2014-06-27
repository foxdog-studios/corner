from contextlib import contextmanager
import csv


__all__ = ['csv_bool', 'csv_reader', 'csv_writer', 'default']


def csv_bool(obj):
    return 1 if obj else 0


@contextmanager
def csv_reader(path):
    with path.open(newline='') as file_:
        yield csv.reader(file_)


@contextmanager
def csv_writer(path):
    with path.open('w', newline='') as file_:
        yield csv.writer(file_)


def default(obj, default_obj):
    return default_obj if obj is None else obj

