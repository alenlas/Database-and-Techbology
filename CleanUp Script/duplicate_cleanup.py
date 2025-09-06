import pandas as pd

df = pd.read_excel("cleaned_data.xlsx", dtype={"district": str})

# --- Duplicates: overview ---
dup_mask = df["district"].duplicated(keep=False)
dup_ids_df = df.loc[dup_mask, ["district", "name", "land"]].sort_values(["district", "name"])

print("\nDuplicate district rows (preview):")
print(dup_ids_df.head(20))

print("\nDuplicate district ID counts:")
print(dup_ids_df["district"].value_counts())

print("\nUnique duplicate district IDs:")
print(dup_ids_df["district"].unique())

# Optional: grouped view for quick inspection
print("\nGrouped view (district -> list of names):")
grouped = dup_ids_df.groupby("district")["name"].apply(list)
print(grouped)