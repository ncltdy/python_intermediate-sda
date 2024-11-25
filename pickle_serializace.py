import pickle

data = {
    'a': [1, 2.0, 3, 4 + 6j],
    'b': ("Alice has a cat", "Python programming is great"),
    'c': [False, True, False]
}

with open('data.pickle', 'wb') as f:
    pickle.dump(data, f)