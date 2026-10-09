import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

df = pd.read_csv('BTC_data.csv')

df['time'] = pd.to_datetime(df['time'])
df = df.sort_values('time') 

x_num = mdates.date2num(df['time']) 
y = df['close'].values
coeffs = np.polyfit(x_num, y, 25)
poly = np.poly1d(coeffs)
x_smooth = np.linspace(x_num.min(), x_num.max(), 500)
y_smooth = poly(x_smooth)
plt.figure(figsize=(14, 7))
plt.plot(df['time'], df['close'], color='orange', linewidth=1, label='Цена закрытия')
plt.plot(mdates.num2date(x_smooth), y_smooth, color='blue', linewidth=2)


plt.title('Исторический график цены биткоина (2018–2023)')
plt.xlabel('Дата')
plt.ylabel('Цена закрытия, USD')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()