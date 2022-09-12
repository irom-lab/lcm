import pickle

with open('lcmlog_2022_09_06_00.pkl', 'rb') as f:
    data = pickle.load(f)

print(data)
