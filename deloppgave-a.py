###
# Skriv et program som leser inn filen ‘support_uke_24.xlsx’ og lagrer data fra kolonne 1 i en array med
# variablenavn ‘u_dag’, dataen i kolonne 2 lagres i arrayen ‘kl_slett’, data i kolonne 3 lagres i arrayen
# ‘varighet’ og dataen i kolonne 4 lagres i arrayen ‘score’.
###

import pandas as pd

df = pd.read_excel('support_uke_24.xlsx')

u_dag = df['Ukedag']

kl_slett = df['Klokkeslett']

varighet = df['Varighet']

score = df['Tilfredshet']
