###
# Skriv et program som finner minste og lengste samtaletid som er loggført for uke 24.
# Svaret skrives til skjerm med informativ tekst.
###

import pandas as pd

df = pd.read_excel('support_uke_24.xlsx')

varighet = df['Varighet']
min_varighet = varighet.min()
max_varighet = varighet.max()

print("Minimum varighet:", min_varighet)

print("Maksimum varighet:", max_varighet)
