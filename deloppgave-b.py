###
# Skriv et program som finner antall henvendelser for hver de 5 ukedagene.
# Resultatet visualiseres ved bruk av et søylediagram (stolpediagram).
##

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('support_uke_24.xlsx')

u_dag = df['Ukedag']

dager = ['Mandag', 'Tirsdag', 'Onsdag', 'Torsdag', 'Fredag']
henvendelser = [0, 0, 0, 0, 0]

for i in range(len(u_dag)):
    if u_dag[i] == 'Mandag':
        henvendelser[0] += 1
    elif u_dag[i] == 'Tirsdag':
        henvendelser[1] += 1
    elif u_dag[i] == 'Onsdag':
        henvendelser[2] += 1
    elif u_dag[i] == 'Torsdag':
        henvendelser[3] += 1
    elif u_dag[i] == 'Fredag':
        henvendelser[4] += 1


plt.bar(dager, henvendelser)
plt.title('Antall henvendelser per dag')
plt.xlabel('Ukedag')
plt.ylabel('Henvendelser')
plt.show()
