###
# Kundens tilfredshet loggføres som tall fra 1-10 hvor 1 indikerer svært misfornøyd og 10
# indikerer svært fornøyd. Disse tilbakemeldingene skal så overføres til NPS-systemet (Net Promoter Score).
###

import pandas as pd

df = pd.read_excel('support_uke_24.xlsx')

score = df['Tilfredshet']

negativ = score[score < 7]
neutral = score[(score >= 7) & (score <= 8)]
positiv = score[score > 8]

totalt_antall = negativ.count() + neutral.count() + positiv.count()

andel_negative = (negativ.count() / totalt_antall) * 100
andel_positive = (positiv.count() / totalt_antall) * 100

NPS = andel_positive - andel_negative

print(f"NPS score:{NPS:.2f}")
