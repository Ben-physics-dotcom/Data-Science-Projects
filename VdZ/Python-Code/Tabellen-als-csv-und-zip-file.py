####################################
# Created by: Ben                  # 
# Date: 15.08.23                   #
# Info: Der Code wurde speziell    #
#       für Google Colab           #
#       geschrieben                #
####################################

# Importe
# Installation von Paketen
!pip install PyPDF4
!pip install tabula-py

# Importe
import pandas as pd
import requests
import tabula
import PyPDF4

# Funktionen
def download_pdf(url):                      # Funktion zum Download von PDF Dateien
  local_filename = url.split('/')[-1]       # funktioniert nicht für engl. sprachige
                                            # Inhalte mit requests
  with requests.get(url) as r:
    with open(local_filename,'wb') as f:
      f.write(r.content)

  return local_filename

# PDF Dateien laden, am Beispiel Kölner Zoo
# urls
GB_22 = 'https://www.koelnerzoo.de/images/pdf/Geschaeftsbericht/KoelnerZoo-Geschaeftsbericht2022.pdf'
GB_21 = 'https://www.koelnerzoo.de/images/pdf/Geschaeftsbericht/KoelnerZoo-Geschaeftsbericht2021.pdf'
GB_20 = 'https://www.koelnerzoo.de/images/pdf/Geschaeftsbericht/KoelnerZoo-Geschaeftsbericht2020.pdf'

# Download
GB_22_koln = download_pdf(GB_22)
GB_21_koln = download_pdf(GB_21)
GB_20_koln = download_pdf(GB_20)

# Tabellen herausfiltern
tables_koln_22 = tabula.read_pdf(GB_22_koln,pages='all')
tables_koln_21 = tabula.read_pdf(GB_21_koln,pages='all')
tables_koln_20 = tabula.read_pdf(GB_20_koln,pages='all')

# Tabellen als csv-Dateien
# Folder-Struktur beachten: /content/GB_as_csv/
for i in range(len(tables_koln_20)):
  tables_koln_20[i].to_csv(f"/content/GB_as_csv/tables_koln_20_{i}.csv", sep=',', index=False, encoding='utf-8')

for i in range(len(tables_koln_21)):
  tables_koln_21[i].to_csv(f"/content/GB_as_csv/tables_koln_21_{i}.csv", sep=',', index=False, encoding='utf-8')

for i in range(len(tables_koln_22)):
  tables_koln_22[i].to_csv(f"/content/GB_as_csv/tables_koln_22_{i}.csv", sep=',', index=False, encoding='utf-8')


# Folder als Zip-Dokument umwandeln:
!zip -r /content/GB_as_csv.zip /content/GB_as_csv

# Folder herunterladen und veröffentlichen, wenn gewollt.
