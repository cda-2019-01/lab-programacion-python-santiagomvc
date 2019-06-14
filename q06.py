##
## Por cada clave de la columna 5 (cadena de tres letras), obtenga
## el valor mas pequeño y el valor mas grande asociado a esa clave.
##
## aaa,0,6
## bbb,4,7
## ccc,0,1
## ddd,5,5
## eee,0,0
## fff,4,9
## ggg,3,3
## hhh,6,8
## iii,2,7
## jjj,2,5
##
import pandas as pd

df = pd.read_csv('data.csv', sep = '	', names=list(range(1,6)))
values = df[5].str.split(',').tolist()
values_flat = [i for j in values for i in j] 
ser = pd.Series(values_flat)
df_vals = pd.DataFrame(ser.str.split(':').tolist())
print(df_vals.groupby(0)[1].agg(['min','max']).to_csv(header = False), end='')