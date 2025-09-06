import pandas as pd

# Load the file you inspected
df = pd.read_excel("districts_only.xlsx", dtype={"district": str})

# 1) Keep only real districts: exactly 5 digits
before = len(df)
df = df[df["district"].astype(str).str.fullmatch(r"\d{5}")]
after = len(df)
print(f"Filtered to 5-digit districts: {before} -> {after}")

# 2) Drop exact duplicate rows (safety)
df = df.drop_duplicates()

# 3) Re-check duplicate district IDs
dup_count = df["district"].duplicated().sum()
print("Duplicate district IDs after filtering:", dup_count)

if dup_count > 0:
    dup_view = df[df["district"].duplicated(keep=False)].sort_values(["district","name"])
    print("\nRemaining duplicates (sample):")
    print(dup_view[["district","name","land"]].head(20))

# 4) (Optional) Auto-resolve remaining dup IDs by keeping the row with most non-missing values
if dup_count > 0:
    df["_non_nulls"] = df.notna().sum(axis=1)
    df = df.sort_values(["district", "_non_nulls"], ascending=[True, False])\
           .drop_duplicates(subset=["district"], keep="first")\
           .drop(columns=["_non_nulls"])
    print("Resolved duplicates by keeping most complete row per district.")

# 5) Convert any object numerics (example: area)
if "area_in_km2" in df.columns and df["area_in_km2"].dtype == "object":
    df["area_in_km2"] = pd.to_numeric(df["area_in_km2"], errors="coerce")

# 6) Save clean districts-only file
df.to_excel("districts_clean_final.xlsx", index=False)
print("Saved: districts_clean_final.xlsx")