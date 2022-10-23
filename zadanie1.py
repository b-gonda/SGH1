import pandas as pd

# wczytanie danych i krótki opis
url = "https://raw.githubusercontent.com/adam-54/class/main/common/beeps_c.csv"
df = pd.read_csv(url, encoding = 'ISO-8859-1', low_memory=False)

df = df[df['country'] == 'Portugal']

#Year Establishment Began Operations
zmienna_celu = 'b5'

# Does Establishment Have An Internationally-Recognized Quality Certification?
zmienna_ob_1 = 'b8'

#How Many Years of Experience Working In This Sector Does The Top Manager Have?
zmienna_ob_2 = 'b7'

df = df[['id', 'country', zmienna_celu, zmienna_ob_1, zmienna_ob_2]]
print(df)

