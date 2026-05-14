import pandas as pd



listing = pd.read_csv("data/listing+features.csv", low_memory=False)
sold = pd.read_csv("data/sold+features.csv", low_memory=False)



for df in (listing, sold):
    for var in ("ClosePrice", "LivingArea", "DaysOnMarket"):
        Q1 = df[var].quantile(0.25)
        Q3 = df[var].quantile(0.75)

        IQR = Q3 - Q1

        lower = Q1 - 1.5 * IQR

        upper = Q3 + 1.5 * IQR

        df[var + "_in_IQR_Flag"] = (df[var] >= lower) & (df[var] <= upper)
        
        
        
filtered_listing = listing[listing[["ClosePrice_in_IQR_Flag", "LivingArea_in_IQR_Flag", "DaysOnMarket_in_IQR_Flag"]].all(axis = 1)]

filtered_sold = sold[sold[["ClosePrice_in_IQR_Flag", "LivingArea_in_IQR_Flag", "DaysOnMarket_in_IQR_Flag"]].all(axis = 1)]



print("Listing Dataset Size before IQR Filtering:", listing.shape[0])
print("Listing Variable Medians before IQR Filtering:")
print(listing.select_dtypes("number").median())

print("\nListing Dataset Size after IQR Filtering:", filtered_listing.shape[0])
print("Listing Variable Medians after IQR Filtering:")
print(filtered_listing.select_dtypes("number").median())

print("\nSold Dataset Size before IQR Filtering:", sold.shape[0])
print("Sold Variable Medians before IQR Filtering:")
print(sold.select_dtypes("number").median())

print("\nSold Dataset Size after IQR Filtering:", filtered_sold.shape[0])
print("Sold Variable Medians after IQR Filtering:")
print(filtered_sold.select_dtypes("number").median())



print("\nSaving CSVs...")

sold.to_csv("data/sold_final_flagged.csv", index = False)
listing.to_csv("data/lising_final_flagged.csv", index = False)

filtered_sold.to_csv("data/sold_final_filtered.csv", index = False)
filtered_listing.to_csv("data/lising_final_filtered.csv", index = False)

print("Done!")