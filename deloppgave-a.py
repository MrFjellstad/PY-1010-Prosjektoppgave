import pandas as pd

df = pd.read_excel('support_uke_24.xlsx')

u_dag = df['Ukedag']

kl_slett = df['Klokkeslett']

varighet = df['Varighet']

score = df['Tilfredshet']
