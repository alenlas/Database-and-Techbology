import pandas as pd

# Load cleaned file; ensure 'district' stays string
df = pd.read_excel("cleaned_data.xlsx", dtype={"district": str})

# --- Missingness summary ---
# Top 20 with most missing:
print("\nTop 20 columns by missing count:")
print(df.isnull().sum().sort_values(ascending=False).head(20))

# Only columns that have any missing:
missing_cols = df.isnull().sum().sort_values(ascending=False)
missing_cols = missing_cols[missing_cols > 0]
print("\nColumns with any missing values:")
print(missing_cols)

# --- Optional sanity checks you can add now ---

# 1) Duplicates
print("\nDuplicate full rows:", df.duplicated().sum())
if "district" in df.columns:
    print("Duplicate district IDs:", df["district"].duplicated().sum())

# 2) Keep only 5-digit district IDs (drop Land/Kreise aggregates)
if "district" in df.columns:
    before = len(df)
    df = df[df["district"].astype(str).str.fullmatch(r"\d{5}")]
    after = len(df)
    print(f"\nFiltered to 5-digit districts: {before} -> {after}")

# 3) Quick type check
print("\nData types:")
print(df.dtypes.head(20))

# 4) Save a districts-only file (optional)
df.to_excel("districts_only.xlsx", index=False)
print("\nSaved: districts_only.xlsx")

dup_ids = df[df['district'].duplicated(keep=False)]
print(dup_ids[['district', 'name', 'land']].sort_values('district'))