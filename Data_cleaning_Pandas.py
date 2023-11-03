import pandas as pd
import numpy as np

df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN',
                               'londON_StockhOlm',
                               'Budapest_PaRis', 'Brussels_londOn'],
                   'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
                   'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
                   'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
                               '12. Air France', '"Swiss Air"']})


# Task 1
df['FlightNumber'].fillna(value=df['FlightNumber'].fillna(method="ffill")+10, inplace=True)
df['FlightNumber'] = df['FlightNumber'].astype(int)


# Task 2
df[['From', 'To']] = df['From_To'].str.split('_', expand=True)

# Task 3
df['From'] = df['From'].str.capitalize()
df['To'] = df['To'].str.capitalize()

# Task 4
df.drop('From_To', axis=1, inplace=True)

# Task 5
delays = pd.DataFrame(df['RecentDelays'].tolist(), columns=['delay_1', 'delay_2', 'delay_3'])
df = pd.concat([df, delays], axis=1)
df.drop('RecentDelays', axis=1, inplace=True)


print(df)
