##
## Imprima la suma de la columna 2 por cada letra de la 
## primera columna, ordneados alfabeticamente.
##
## A,37
## B,36
## C,27
## D,23
## E,67
##
import pandas as pd
df = pd.read_csv('data.csv', sep = '\t', names=list(range(1,6)))
print(df.groupby(1)[2].sum().to_csv(header=False), end='')
