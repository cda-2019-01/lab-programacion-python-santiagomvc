##
## Imprima el valor maximo y minimo por cada letra de la columa 1.
##
## A,9,1
## B,9,1
## C,9,0
## D,7,1
## E,9,1
##
import pandas as pd
df = pd.read_csv('data.csv', sep = '\t', names=list(range(1,6)))
temp = df.groupby(1)[2].agg(['max','min'])
print(temp.to_csv(header=False),end='')
