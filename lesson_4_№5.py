import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv('BTC_data.csv')

df['time'] = pd.to_datetime(df['time'])
df = df.sort_values('time')

plt.figure(figsize=(14, 7))
plt.plot(df['time'], df['close'], color='orange', linewidth=1)

ax = plt.gca()
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%y'))  
ax.xaxis.set_major_locator(mdates.AutoDateLocator())           
plt.xticks(rotation=45)                                        

plt.title('Исторический график цены биткоина (2018–2023)')
plt.xlabel('Дата')
plt.ylabel('Цена закрытия, USD')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()