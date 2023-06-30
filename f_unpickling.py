import pickle

# Uncomment the import below for the code to work
# from f_pickling import adder


with open("f_pickle.pkl", "rb") as f:
    unpickled_adder = pickle.load(f)

if __name__ == "__main__":
    numbers = (10, 2)
    print(unpickled_adder(*numbers))
