import pandas as pd



listing = pd.read_csv("data/listing_prepared.csv", low_memory=False)
sold = pd.read_csv("data/sold_prepared.csv", low_memory=False)



print("Generating Metrics...")
listing["Price Ratio"] = listing["ClosePrice"] / listing["OriginalListPrice"]
sold["Price Ratio"] = sold["ClosePrice"] / sold["OriginalListPrice"]

listing["Price Per Sq Ft"] = listing["ClosePrice"] / listing["LivingArea"]
sold["Price Per Sq Ft"] = sold["ClosePrice"] / sold["LivingArea"]

listing["Days on Market"] = listing["DaysOnMarket"]
sold["Days on Market"] = sold["DaysOnMarket"]

listing["CloseDate"] = pd.to_datetime(listing["CloseDate"])
sold["CloseDate"] = pd.to_datetime(sold["CloseDate"])
listing["Year"] = listing["CloseDate"].dt.year.astype("Int64")
sold["Year"] = sold["CloseDate"].dt.year.astype("Int64")
listing["Month"] = listing["CloseDate"].dt.month.astype("Int64")
sold["Month"] = sold["CloseDate"].dt.month.astype("Int64")
listing["YrMo"] = listing["CloseDate"].dt.to_period("M")
sold["YrMo"] = sold["CloseDate"].dt.to_period("M")

listing["Close to Original List Ratio"] = listing["ClosePrice"] / listing["OriginalListPrice"]
sold["Close to Original List Ratio"] = sold["ClosePrice"] / sold["OriginalListPrice"]

listing["PurchaseContractDate"] = pd.to_datetime(listing["PurchaseContractDate"])
listing["ListingContractDate"] = pd.to_datetime(listing["ListingContractDate"])
sold["PurchaseContractDate"] = pd.to_datetime(sold["PurchaseContractDate"])
sold["ListingContractDate"] = pd.to_datetime(sold["ListingContractDate"])
listing["Listing to Contract Days"] = listing["PurchaseContractDate"] - listing["ListingContractDate"]
sold["Listing to Contract Days"] = sold["PurchaseContractDate"] - sold["ListingContractDate"]

listing["Contract to Close Days"] =listing["CloseDate"] - listing["PurchaseContractDate"]
sold["Contract to Close Days"] =sold["CloseDate"] - sold["PurchaseContractDate"]



print("\nSample Output of new column calculations (from Listing):")

print(listing[["Price Ratio", "ClosePrice", "OriginalListPrice", "Price Per Sq Ft", "ClosePrice", "LivingArea", "Days on Market", "DaysOnMarket", "Year", "Month" , "YrMo", "CloseDate", "Close to Original List Ratio", "ClosePrice", "OriginalListPrice", "Listing to Contract Days", "PurchaseContractDate", "ListingContractDate", "Contract to Close Days", "CloseDate", "PurchaseContractDate"]].dropna().head())



print("\nListing Metrics Grouped by PropertySubType (all PropertyType is Residential):")
print(listing.groupby("PropertySubType")[["Price Ratio", "Price Per Sq Ft", "Days on Market", "Year", "Month", "YrMo", "Close to Original List Ratio", "Listing to Contract Days", "Contract to Close Days"]].describe().T)
print()

print("Sold Metrics Grouped by PropertySubType (all PropertyType is Residential):")
print(sold.groupby("PropertySubType")[["Price Ratio", "Price Per Sq Ft", "Days on Market", "Year", "Month", "YrMo", "Close to Original List Ratio", "Listing to Contract Days", "Contract to Close Days"]].describe().T)
print()



print("Listing Metrics Grouped by CountyOrParish:")
print(listing.groupby("CountyOrParish")[["Price Ratio", "Price Per Sq Ft", "Days on Market", "Year", "Month", "YrMo", "Close to Original List Ratio", "Listing to Contract Days", "Contract to Close Days"]].describe().T)
print()

print("Sold Metrics Grouped by CountyOrParish:")
print(sold.groupby("CountyOrParish")[["Price Ratio", "Price Per Sq Ft", "Days on Market", "Year", "Month", "YrMo", "Close to Original List Ratio", "Listing to Contract Days", "Contract to Close Days"]].describe().T)
print()



print("Creating CSVs...")
listing.to_csv("data/listing+features.csv", index=False)

sold.to_csv("data/sold+features.csv", index=False)

print("Created!")