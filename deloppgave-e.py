###
# Supportvaktene i MORSE er delt inn i 2-timers bolker: kl 08-10, kl 10-12, kl 12-14 og kl 14-16.
# Skriv et program som finner det totale antall henvendelser supportavdelingen mottok for hver av
# tidsrommene 08-10, 10-12, 12-14 og 14-16 for uke 24. Resultatet visualiseres ved bruk av et
# sektordiagram (kakediagram).
###

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('support_uke_24.xlsx')

kl_slett = df['Klokkeslett']

tidsintervall = [0, 0, 0, 0]
for i in range(len(kl_slett)):
    tid = kl_slett[i].split(':')
    timer = int(tid[0])
    if (timer == 8 or timer == 9):
        tidsintervall[0] += 1
    elif (timer == 10 or timer == 11):
        tidsintervall[1] += 1
    elif (timer == 12 or timer == 13):
        tidsintervall[2] += 1
    elif (timer == 14 or timer == 15):
        tidsintervall[3] += 1

plt.pie(tidsintervall, labels=['08:00 - 10:00', '10:00 - 12:00',
        '12:00 - 14:00', '14:00 - 16:00'], autopct='%1.1f%%')
plt.title('Antall henvendelser per tidsintervall')
plt.show()
