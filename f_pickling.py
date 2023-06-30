import pickle


def adder(operand1, operand2):
    return operand1 + operand2


with open("f_pickle.pkl", "wb") as f:
    pickle.dump(adder, f)

if __name__ == "__main__":
    numbers = (40, 2)
    print(adder(*numbers))
