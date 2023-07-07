import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv('data_grafik.csv')

counts = data.groupby(['wilayah', 'jenis_usaha']).size().reset_index(name='jumlah')

sums = counts.groupby('wilayah').sum().reset_index()

fig = counts.plot(kind='bar', figsize=(10,6)).get_figure()

plt.bar(sums['wilayah'], sums['jumlah'])

plt.title('Jumlah Usaha Berdasarkan Wilayah di Jakarta')
plt.xlabel('Wilayah')
plt.ylabel('Jumlah')

plt.show()

fig