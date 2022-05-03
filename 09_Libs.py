import numpy as np
import pandas as pa

def show_numpy():
    numpy_array = np.array([4, 5, 6, 7, 8, 9, 10])
    print(numpy_array)
    print(f"Numpy type: {type(numpy_array)}")

def show_pandas():
    pandas_array = pa.Series([14, 15, 16, 17, 18, 19, 20])
    print(pandas_array)
    print(f"Pandas type: {type(pandas_array)}")
    print(f"Pandas first element: {pandas_array[1]}")

def main():
    show_numpy()
    print("--------------------------------------------------")
    show_pandas()
    return 0

if __name__ == '__main__':
    main()