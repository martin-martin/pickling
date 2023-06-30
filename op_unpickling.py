import pickle


with open("op_pickle.pkl", "rb") as f:
    unpickled_adder = pickle.load(f)

if __name__ == "__main__":
    numbers = (10, 2)
    print(unpickled_adder(*numbers))
