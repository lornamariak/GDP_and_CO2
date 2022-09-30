import pandas as pd
from matplotlib import pyplot as plt


data = pd.read_csv("https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv")
minidata = data[["Country Name", "Mortality rate, infant (per 1,000 live births)","GDP per capita (constant 2010 US$)"]]

plt.scatter(minidata["Mortality rate, infant (per 1,000 live births)"],minidata["GDP per capita (constant 2010 US$)"])
plt.title("Scatter on Mortality rate, infant (per 1,000 live births) and GDP per capita (constant 2010 US$)")
plt.show()
