####################
# created by Ben   #
# Date: 10.08.2023 #
####################

import numpy as np
import pandas as pd

# dictionary für Unternehmensform
UF = {'GmbH':0, 'gGmbH':1, 'e.V./Verein':2, 'Stiftung':3, 'AG':4, 'gAG':5, 'öffentlich':6, 'unkown':7}

# Listen über VdZ-Mitglieder und deren Unternehmensformen
Name = ['Berliner Zoos','Tiergarten Heidelberg','Zoo Karlsruhe','Wilhelma','Nationalpark Bayerischer Wald','Augsburg Zoo', 'Hellabrunn',
    'Nürnberg Tierpark','Tiergarten Straubing','Tierpark Cottbus','Zoo Eberswalde','Zoo am Meer','Tierpark Hagenbeck','Zoo Vivarium',
    'Zoo Frankfurt','OPEL-ZOO','Vogelpark Marlow','Zoo Rostock','Zoo Schwerin','Deutsches Meeresmuseum Stralsund','Zoo Stralsund',
    'Tierpark Ueckermünde','Zoo Hannover','Serengeti-Park Hodenhagen','Tierpark Nordhorn','Zoo Osnabrück','Weltvogelpark Walsrode',
    'Wingster Waldzoo','Aachener Tierpark','Tierpark Bochum','Zoo Dortmund','Zoo Duisburg','Aquazoo Löbbecke Museum',
    'Zoom Erlebniswelt Gelsenkirchen','Tierpark Hamm','Zoo Köln','Zoo Krefeld','Zoo Münster','NaturZoo Rheine','Zoo Wuppertal',
    'Zoo Landau','Zoo Neuwied','Zoo Neunkirchen','Zoo Saarbrücken','Tierpark Chemnitz','Zoo Dresden','Naturschutz-Tierpark Görlitz',
    'Zoo, Kultur & Bildung Hoyerswerda','Zoo Leipzig','Tiergarten Bernburg','Zoo Halle','Zoo Magdeburg','Tierpark Neumünster',
    'Arche Warder','Zoo Erfurt','Tierwelt Herberstein','Zoo Innsbruck','Zoo Linz','Zoo Salzburg','Haus des Meeres',
    'Tiergarten Schönbrunn','Zoo Basel','Tierpark Bern','Tierpark Goldau','Walter Zoo','Papiliorama','Wildnispark Zürich',
    'Knies Kinderzoo','Zoo Zürich','Loro Parque'
]

Unternehmensform = [
    UF['AG'],UF['gGmbH'],UF['öffentlich'],UF['öffentlich'],UF['öffentlich'],UF['GmbH'],UF['AG'],UF['öffentlich'],UF['öffentlich'],
    UF['öffentlich'],UF['öffentlich'],UF['GmbH'],UF['gGmbH'],UF['öffentlich'],UF['öffentlich'],UF['Stiftung'],UF['gGmbH'],UF['gGmbH'],
    UF['gGmbH'],UF['Stiftung'],UF['öffentlich'],UF['e.V./Verein'],UF['gGmbH'],UF['GmbH'],UF['gGmbH'],UF['gGmbH'],UF['GmbH'],UF['GmbH'],
    UF['gAG'],UF['gGmbH'],UF['öffentlich'],UF['gGmbH'],UF['öffentlich'],UF['GmbH'],UF['gGmbH'],UF['AG'],UF['gGmbH'],UF['GmbH'],
    UF['e.V./Verein'],UF['öffentlich'],UF['unkown'],UF['e.V./Verein'],UF['GmbH'],UF['öffentlich'],UF['öffentlich'],UF['GmbH'],
    UF['öffentlich'],UF['gGmbH'],UF['GmbH'],UF['GmbH'],UF['GmbH'],UF['gGmbH'],UF['e.V./Verein'],UF['e.V./Verein'],UF['unkown'],
    UF['GmbH'],UF['e.V./Verein'],UF['e.V./Verein'],UF['gGmbH'],UF['GmbH'],UF['GmbH'],UF['AG'],UF['e.V./Verein'],UF['Stiftung'],
    UF['AG'],UF['Stiftung'],UF['Stiftung'],UF['AG'],UF['AG'],UF['unkown']
]

# Creating the data frame
Zoo_liste = pd.DataFrame({'Name':Name, 'Unternehmensform':Unternehmensform})
print(Zoo_liste.head())

# Histogram
UF_name = ['GmbH','gGmbH','e.V./Verein', 'Stiftung','AG','gAG','Öffentlich','Unkown'] # x ticksName

bins = np.array([0,1,2,3,4,5,6,7,8])-.5 # bin-Breite

Zoo_liste.hist(grid=False,bins=bins, range=(0, 8), align='mid',edgecolor='white')     # Histogram

plt.xticks(
    [0,1,2,3,4,5,6,7],
    UF_name,                                                                          # ticks Name benutzen
    rotation=90,color='white')
plt.yticks([0,4,8,12,16],
           color='white')
plt.ylabel('Anzahl',color='white')
plt.title('Unternehmensformen',color='white')                                          # Title
plt.tick_params(axis='both',color='white')
plt.box(on=False)
plt.show()
# plt.savefig('VdZ-Miglieder-Unternehmensform.png',dpi=600,transparent=True,bbox_inches = 'tight')

# Data Frame für die Zoo AGs
AG_index = []
for i in range(len(Zoo_liste)):
  if Zoo_liste['Unternehmensform'][i] == 4:
    AG_index.append(i)

AG = Zoo_liste.loc[lst]
AG.index = range(len(AG))

pritn(AG)

# prozentuale Verteilung der Unternehmensformen von Mitgliedern beim VdZ
prozent_Verteilung = {UF_name[0]:f'{round(15/70*100,1)}%',
                      UF_name[1]:f'{round(15/70*100,1)}%',
                      UF_name[2]:f'{round(8/70*100,1)}%',
                      UF_name[3]:f'{round(5/70*100,1)}%',
                      UF_name[4]:f'{round(7/70*100,1)}%',
                      UF_name[5]:f'{round(1/70*100,1)}%',
                      UF_name[6]:f'{round(16/70*100,1)}%',
                      UF_name[7]:f'{round(3/70*100,1)}%'}
print(prozent_Verteilung)
