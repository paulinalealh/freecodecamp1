import numpy as np

calculations = {}
my_list = [0,1,2,3,4,5,6,7,8]

def calculate(list):
    try: 
        arr = np.array(list)
        matrix = arr.reshape(3,3)
        calculations = {
        "mean" : [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), float(matrix.mean())],
        "variance" : [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), float(matrix.var())], 
        "standard deviation" :[matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), float(matrix.std())],
        "max" : [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), float(matrix.max())], 
        "min" : [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), float(matrix.min())],
        "sum" : [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), float(matrix.sum())]
    }
        return calculations
    
    except ValueError: 
        print("List must contain nine numbers.")

print(calculate(my_list))