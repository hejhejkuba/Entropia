from scipy.stats import entropy as en
import pandas as pd
import numpy as np
import math


if __name__ == '__main__':
    Suma = 0
    Series = input("Enter data:")
    a = list(Series)
    zasieg = len(a)
    print(zasieg)
    a = pd.Series(a)

    data = a.value_counts()
    print(data)
    for i in data.values:
        Suma += (1.0*i/zasieg)*math.log2(1.0*i/zasieg)
    print(-1.0*Suma)






