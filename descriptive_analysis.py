
import openpyxl as xl
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

df = pd.read_excel('data.xlsx', dtype={'District': str })

# print(df.head())
# print(df.shape)
# df.head()


def clean_column_names(cols):
    clean_cols = []
    for col in cols:
        # 1. Lowercase
        new_col = col.lower().strip()
        # 2. Replace dash separators only when surrounded by spaces
        new_col = new_col.replace(" - ", "_")
        # 3. Replace spaces with underscores
        new_col = new_col.replace(" ", "_")
        # 4. Remove problematic symbols (keep + and - inside text!)
        new_col = new_col.replace("(", "").replace(")", "").replace("%", "pct")
        clean_cols.append(new_col)
    return clean_cols

# Apply safe renaming
df.columns = clean_column_names(df.columns)

print(df.columns.tolist())

output_path = "cleaned_data.xlsx"
df.to_excel(output_path, index=False)
print(f"The file has been successfuly saved to {output_path}")