import pickle
import operator


with open("op_pickle.pkl", "wb") as f:
    pickle.dump(operator.add, f)

if __name__ == "__main__":
    numbers = (40, 2)
    print(operator.add(*numbers))
