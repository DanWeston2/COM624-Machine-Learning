import pandas as pd

'''
Nazario 5 identifies whether it is phishing or not by "label" where 1 is malicious and 0 is safe
'''

dfNazario = pd.read_csv("Nazario_5.csv")

pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 120)

dfNazario.drop_duplicates()

print(dfNazario[dfNazario["label"] == 0][["sender","subject","body","urls"]].sample(1))
