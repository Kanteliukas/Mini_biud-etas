import os, pickle

os.chdir("C:\\Users\\daini\\PycharmProjects\\Mini_biudžetas\\pickle_database")

# Padedam į pickle failą
def append_new_amount(amount_list, filename):
    with open(filename, 'wb') as f:
        pickle.dump(amount_list, f)