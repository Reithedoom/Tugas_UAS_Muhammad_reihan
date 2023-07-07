import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('data_grafik.csv')

counts = data.groupby(['kecamatan', 'jenis_usaha']).size().reset_index(name='jumlah')

sums = counts.groupby('kecamatan').sum().reset_index()

fig = counts.plot(kind='bar', figsize=(10,6)).get_figure()

plt.pie(sums['jumlah'], labels=sums['kecamatan'], autopct='%1.1f%%', startangle=90)

plt.title('Persentase Jenis Usaha di Setiap Kecamatan Jakarta')

plt.show()
fig