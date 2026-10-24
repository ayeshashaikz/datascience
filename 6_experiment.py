"""
Experiment 6: Total Purchase Cost Calculation with Discount and Tax Using Arithmetic Operations
Dataset: exp6.csv
"""
import pandas as pd

df = pd.read_csv("exp6.csv")
print("Dataset preview:")
print(df.head())
print("\nColumns:", list(df.columns))

# Normalize column names for flexible matching.
normalized = {str(c).strip().lower().replace(" ", "_"): c for c in df.columns}
def find_col(candidates):
    for candidate in candidates:
        for norm, original in normalized.items():
            if candidate in norm:
                return original
    return None

qty_col = find_col(["quantity", "qty", "units"])
price_col = find_col(["unit_price", "price", "cost"])
discount_col = find_col(["discount"])
tax_col = find_col(["tax", "gst"])

if qty_col is None or price_col is None:
    print("\nCould not automatically identify quantity and unit price columns.")
    print("Edit qty_col and price_col in the script to match the CSV column names.")
else:
    df[qty_col] = pd.to_numeric(df[qty_col], errors="coerce")
    df[price_col] = pd.to_numeric(df[price_col], errors="coerce")
    subtotal = df[qty_col] * df[price_col]
    discount = pd.to_numeric(df[discount_col], errors="coerce").fillna(0) if discount_col else 0
    tax = pd.to_numeric(df[tax_col], errors="coerce").fillna(0) if tax_col else 0

    # Discount and tax are treated as percentages when values are between 0 and 100.
    discount_amount = subtotal * (discount / 100) if hasattr(discount, "fillna") else subtotal * discount
    after_discount = subtotal - discount_amount
    tax_amount = after_discount * (tax / 100) if hasattr(tax, "fillna") else after_discount * tax
    total = after_discount + tax_amount

    result = df.copy()
    result["Subtotal"] = subtotal
    result["Discount Amount"] = discount_amount
    result["Tax Amount"] = tax_amount
    result["Total Purchase Cost"] = total
    print("\nCalculated purchase costs:")
    print(result.to_string(index=False))
    print(f"\nGrand total: {total.sum():.2f}")
