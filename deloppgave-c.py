import pandas as pd

df = pd.read_excel('support_uke_24.xlsx')

varighet = df['Varighet']
min_varighet = varighet.min()
max_varighet = varighet.max()

print("Minimum varighet:", min_varighet)

print("Maksimum varighet:", max_varighet)
