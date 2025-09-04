
import openpyxl as xl
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

df = pd.read_excel('data.xlsx', dtype={'District': str })
print(df.head())

