import os, pickle

os.chdir("C:\\Users\\daini\\PycharmProjects\\Mini_biudžetas\\pickle_database")


def read_amounts(filename):
    saved_amount = []
    try:
        with open(filename, 'rb') as f:
            saved_amount = pickle.load(f)
    except FileNotFoundError as e:
        pass
    return saved_amount