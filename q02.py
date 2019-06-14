##
## Imprima la cantidad de registros por letra para la 
## primera columna, ordenados alfabeticamente.
##
## A,8
## B,7
## C,5
## D,6
## E,14
##
import pandas as pd
df = pd.read_csv('data.csv', sep = '\t', names=list(range(1,6)))
print(df.groupby(1)[2].apply(lambda x: len(x)).to_csv(header = False), end='')
