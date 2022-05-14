import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
has = pd.read_csv(r"C:\Users\Sjbzx\Downloads\Aquaponics Water Quality Tests Data - Log 01_01_2022 - 12_31_2022.csv")

plt.figure(figsize=(12,8))
plt.title('Aquaponics Water Quality Tests from January to April')

plt.plot(has['Date:'], has['Ammonia (ppm):'], label='Ammonia (ppm)')
plt.plot(has['Date:'], has['Nitrite (ppm):'], label='Nitrite (ppm)')
plt.plot(has['Date:'], has['Dissolved Oxygen (ppm)'], label='Dissolved Oxygen (ppm)')
plt.xticks(has['Date:'][::11])
plt.yticks(np.arange(0, 12, step=0.5))
plt.xlabel('Date')
plt.ylabel('ppm')


plt.legend()
plt.show()
