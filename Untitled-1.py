from csv import writer
import numpy as np
import pandas as pd
import xlsxwriter

data = pd.read_html('https://www.officialcharts.com/chart-news/the-best-selling-albums-of-all-time-on-the-official-uk-chart__15551/', header=0)

############################################zmiana nagłówków############################################################
df = pd.DataFrame(data[0])
df.rename(columns={'TITLE':'TYTUŁ','ARTIST':'ARTYSTA','YEAR':'ROK' , 'HIGH POSN':'MAX POZ'}, inplace = True)
print(df)
#####################################################################################################################
##########################ilość pojedyńczych artystów################################################################
amount =df['ARTYSTA'].nunique()
print(f'Ilość zespołów: {amount}')

#####################################################################################################################
##########################najczęstsze zespoły################################################################
artist = df['ARTYSTA'].value_counts()
print(artist)
#####################################################################################################################
########################duże litery########################################################################
df.columns = df.columns.str.capitalize()
print(df)
#####################################################################################################################
########################usunięcie kolumny########################################################################
column_delete = df.drop('Max poz', axis=1, inplace=True)
print(df)
#####################################################################################################################
########################rok z najczęstszymi albumami########################################################################
year = df['Rok'].value_counts()
print(year)
#####################################################################################################################
########################rok z najnowszym albumem########################################################################
newest_year = df['Rok'].values.max()
print(f'Najmłodszy album wydany {newest_year} roku')
#####################################################################################################################
########################najstarsze albumy########################################################################
the_oldest= df.sort_values(by='Rok')
print(the_oldest)
#####################################################################################################################
########################zapisanie do pliku csv########################################################################

df.to_csv('myCsvFile.csv', index=False)
#####################################################################################################################
########################albumy między 1960-1990 ilość################################################################

a =df['Rok'].between(1960, 1990, inclusive=True).value_counts()

print(f' wartości true ilość tytułów z okresu 1960-1990 , wartości false z pozostałego: {a}')

a=0
for i in df['Rok']:
    if i >= 1960 and i <= 1990:
        a +=1
print(f'ilość tytułów miedzy 1960 a 1990 wynosi: {a}')
