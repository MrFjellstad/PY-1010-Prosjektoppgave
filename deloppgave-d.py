###
# Skriv et program som regner ut gjennomsnittlig samtaletid basert på alle henvendelser i uke 24.
###

import pandas as pd


def konvertert_tid_til_sekunder(tid):
    timer, minutter, sekunder = map(int, tid.split(':'))
    return (timer * 3600) + (minutter * 60) + sekunder


def konverter_sekunder_til_tid(sekunder):
    timer = sekunder // 3600
    sekunder %= 3600
    minutter = sekunder // 60
    sekunder %= 60
    return f"{timer:02}:{minutter:02}:{sekunder:02}"


df = pd.read_excel('support_uke_24.xlsx')

varighet = df['Varighet']

total_sekunder = 0

for i in range(len(varighet)):
    varighet_i_sekunder = konvertert_tid_til_sekunder(varighet[i])
    total_sekunder += varighet_i_sekunder

gjennomsnitt_i_sekunder = total_sekunder / len(varighet)
gjennomsnitt = konverter_sekunder_til_tid(int(gjennomsnitt_i_sekunder))

print("Gjennomsnittlig varighet:", gjennomsnitt)
