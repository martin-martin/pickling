import pickle

lambda_adder = lambda x, y: x + y

numbers = (40, 2)
print(lambda_adder(*numbers))

with open("f_pickle.pkl", "wb") as f:
    pickle.dump(lambda_adder, f)  # PicklingError
