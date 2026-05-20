import pandas as pd

sold = pd.read_csv("data/sold_enriched.csv", low_memory=False)
listing = pd.read_csv("data/listing_enriched.csv", low_memory=False)



print("Converting Date Columns to DateTime!\n")

sold["CloseDate"] = pd.to_datetime(sold["CloseDate"])
sold["PurchaseContractDate"] = pd.to_datetime(sold["PurchaseContractDate"])
sold["ListingContractDate"] = pd.to_datetime(sold["ListingContractDate"])
sold["ContractStatusChangeDate"] = pd.to_datetime(sold["ContractStatusChangeDate"])

listing["CloseDate"] = pd.to_datetime(listing["CloseDate"])
listing["PurchaseContractDate"] = pd.to_datetime(listing["PurchaseContractDate"])
listing["ListingContractDate"] = pd.to_datetime(listing["ListingContractDate"])
listing["ContractStatusChangeDate"] = pd.to_datetime(listing["ContractStatusChangeDate"])



# Listing after Purchase, Purachase after Close Date, Listing after Close Date
# Listing after Close should be redudant, but just in case:
sold["listing_after_close_flag"] = ((sold["ListingContractDate"] > sold["CloseDate"]))
sold["purchase_after_close_flag"] = ((sold["PurchaseContractDate"] > sold["CloseDate"]))
sold["negative_timeline_flag"] = ((sold["ListingContractDate"] > sold["PurchaseContractDate"]) | (sold["PurchaseContractDate"] > sold["CloseDate"]) | (sold["ListingContractDate"] > sold["CloseDate"]))

# Less than 1% of data has negative timeline -> FILTER OUT!
print("Percent of Sold Data with negative timelines:", sold[sold["negative_timeline_flag"]][["ListingContractDate", "PurchaseContractDate", "CloseDate"]].shape[0] / sold.shape[0] * 100, "%")

listing["listing_after_close_flag"] = ((listing["ListingContractDate"] > listing["CloseDate"]))
listing["purchase_after_close_flag"] = ((listing["PurchaseContractDate"] > listing["CloseDate"]))
listing["negative_timeline_flag"] = ((listing["ListingContractDate"] > listing["PurchaseContractDate"]) | (listing["PurchaseContractDate"] > listing["CloseDate"]) | (listing["ListingContractDate"] > listing["CloseDate"]))

# Less than 1% of data has negative timeline -> FILTER OUT!
listing[listing["negative_timeline_flag"]][["ListingContractDate", "PurchaseContractDate", "CloseDate"]].shape[0] / listing.shape[0] * 100
print("Percent of Listing Data with negative timelines:", listing[listing["negative_timeline_flag"]][["ListingContractDate", "PurchaseContractDate", "CloseDate"]].shape[0] / listing.shape[0] * 100, "%")

print("Sold Rows (before):", sold.shape[0])
print("Listing Rows (before):", listing.shape[0])
sold = sold[~sold["negative_timeline_flag"] & ~sold["purchase_after_close_flag"] & ~sold["listing_after_close_flag"]]
listing = listing[~listing["negative_timeline_flag"] & ~listing["purchase_after_close_flag"] & ~listing["listing_after_close_flag"]]
print("Sold Rows (after):", sold.shape[0])
print("Listing Rows (after):", listing.shape[0])

print("Filtered out data with negative timelines!\n")



sold_corr = sold.select_dtypes(include='number').corr()
listing_corr = listing.select_dtypes(include='number').corr()

print("Returning columns with correlations with another variable greater than 0.5\n")
print("Sold:")
for col in sold_corr:
    if any(abs(sold_corr[col]).sort_values(ascending=False).iloc[1:] > 0.5):
        print(abs(sold_corr[col]).sort_values(ascending=False).iloc[:5])
        print()
        
        
        
all(sold["ListingKeyNumeric"] == sold["ListingKey"])
# DROP!!! ListingKeyNumeric
sold.drop("ListingKeyNumeric", axis = 1, inplace = True)
print("Dropped \"ListingKeyNumeric\"!\n")



only_two_values = sold[sold[["LotSizeSquareFeet", "LotSizeAcres", "LotSizeArea"]].isna().sum(axis = 1) == 1][["LotSizeSquareFeet", "LotSizeAcres", "LotSizeArea"]]
one_one_value = sold[sold[["LotSizeSquareFeet", "LotSizeAcres", "LotSizeArea"]].isna().sum(axis = 1) == 2][["LotSizeSquareFeet", "LotSizeAcres", "LotSizeArea"]]
acre = 43560
# smallest apartment let's say is 150 sqft
def sq_feet(acres, unknown):
    if acres == acres:
        return acres * acre
    if unknown == unknown:
        if unknown < 150:
            return unknown * acre
        else:
            return unknown
    return None

print("Using function to impute Missing \"LotSizeSquareFeet\" by converting \"LotSizeAcres\" or \"LotSizeArea\" if avaialable.")
print("NOTE: For \"LotSizeArea\", if the value was less than 150, it was assumed to be acres rather than square footage")

print("\nMissingness Before:")
print(sold[["LotSizeSquareFeet", "LotSizeAcres", "LotSizeArea"]].isna().sum())

sold["LotSizeSquareFeet"] = sold.apply(lambda row: sq_feet(row["LotSizeAcres"], row["LotSizeArea"]) if row["LotSizeSquareFeet"] != row["LotSizeSquareFeet"] else row["LotSizeSquareFeet"], axis=1)

print("\nImputed Sold LotSize!")

print("\nMissingness After:")
print(sold[["LotSizeSquareFeet", "LotSizeAcres", "LotSizeArea"]].isna().sum())

print("Before dropping the redudent columns, let's check for impossible values (acres < square feet)...\n")

print(sold[sold["LotSizeAcres"] > sold["LotSizeSquareFeet"]])

print("There are no LotSizeAcres values larger than LotSizeSquareFeet! We are good to drop!")

sold.drop(["LotSizeAcres", "LotSizeArea"], axis = 1, inplace = True)

print("\nDropped LotSizeAcres and LotSizeArea !")



print("\nListing:")
for col in listing_corr:
    if any(abs(listing_corr[col]).sort_values(ascending=False).iloc[1:] > 0.5):
        print(abs(listing_corr[col]).sort_values(ascending=False).iloc[:5])
        print()  
        
        
        
all(listing["ListingKeyNumeric"] == listing["ListingKey"])
# DROP!!! ListingKeyNumeric
listing.drop("ListingKeyNumeric", axis = 1, inplace = True)
print("Dropped \"ListingKeyNumeric\"!\n")



print("Using function to impute Missing \"LotSizeSquareFeet\" by converting \"LotSizeAcres\" or \"LotSizeArea\" if avaialable.")
print("NOTE: For \"LotSizeArea\", if the value was less than 150, it was assumed to be acres rather than square footage")

print("\nMissingness Before:")
print(listing[["LotSizeSquareFeet", "LotSizeAcres", "LotSizeArea"]].isna().sum())
listing["LotSizeSquareFeet"] = listing.apply(lambda row: sq_feet(row["LotSizeAcres"], row["LotSizeArea"]) if row["LotSizeSquareFeet"] != row["LotSizeSquareFeet"] else row["LotSizeSquareFeet"], axis=1)

print("\nImputed Listing LotSize!")

print("\nMissingness After:")
print(listing[["LotSizeSquareFeet", "LotSizeAcres", "LotSizeArea"]].isna().sum())

print("Before dropping the redudent columns, let's check for impossible values (acres < square feet)...\n")

print(listing[listing["LotSizeAcres"] > listing["LotSizeSquareFeet"]])

print("There are no LotSizeAcres values larger than LotSizeSquareFeet! We are good to drop!")

listing.drop(["LotSizeAcres", "LotSizeArea"], axis = 1, inplace = True)

print("\nDropped LotSizeAcres and LotSizeArea !\n")



#ClosePrice <= 0, LivingArea <= 0, DaysOnMarket < 0, negative Bedrooms or Bathrooms

# Both All invalid values equal to zero
sold[sold["ClosePrice"] <= 0]["ClosePrice"].value_counts()
sold[sold["LivingArea"] <= 0]["LivingArea"].value_counts()

print(f"Only {sold[sold["ClosePrice"] <= 0]["ClosePrice"].shape[0]} ClosePrice less than/equal to 0, and only {sold[sold["LivingArea"] <= 0]["LivingArea"].shape[0]} LivingArea less than/equal to zero -> DROP!")

print("Rows before dropping invalid ClosePrice:", sold.shape[0])

dropped = sold.drop(sold[sold["ClosePrice"] <= 0]["ClosePrice"].index)

print("Rows before dropping invalid LivingArea:", dropped.shape[0])

#dropped[dropped["ClosePrice"] <= 0]
dropped.drop(dropped[dropped["LivingArea"] <= 0]["LivingArea"].index, inplace = True)

print("Rows after dropping both invalid ClosePrice and LivingArea:", dropped.shape[0])
print("\nReturning number of rows with LivingArea or ClosePrice less than or equal to 0:", dropped[(dropped["ClosePrice"] <= 0) | (dropped["LivingArea"] <= 0)].shape[0])


print("\nNegative Bathroom Count:", dropped[dropped["BathroomsTotalInteger"] < 0].shape[0])
print("Negative Bedroom Count:", dropped[dropped["BedroomsTotal"] < 0].shape[0])
print("No need to drop anything!")

print("\nNegative DaysOnMarket Count:", dropped[dropped["DaysOnMarket"] < 0].shape[0], "-> DROP!")

dropped.drop(dropped[dropped["DaysOnMarket"] < 0]["DaysOnMarket"].index, inplace = True)

print("Rows after dropping both invalid DaysOnMarket:", dropped.shape[0])

filtered_sold = dropped.copy()



#ClosePrice <= 0, LivingArea <= 0, DaysOnMarket < 0, negative Bedrooms or Bathrooms

# Both All invalid values equal to zero
listing[listing["ClosePrice"] <= 0]["ClosePrice"].value_counts()
listing[listing["LivingArea"] <= 0]["LivingArea"].value_counts()

print(f"\n{listing[listing["ClosePrice"] <= 0]["ClosePrice"].shape[0]} ClosePrice less than/equal to 0, and only {listing[listing["LivingArea"] <= 0]["LivingArea"].shape[0]} LivingArea less than/equal to zero -> DROP!")

print("Rows before dropping invalid ClosePrice:", listing.shape[0])

dropped = listing.drop(listing[listing["LivingArea"] <= 0]["LivingArea"].index)

print("Rows after dropping both invalid ClosePrice and LivingArea:", dropped.shape[0])
print("\nReturning number of rows with LivingArea or ClosePrice less than or equal to 0:", dropped[(dropped["ClosePrice"] <= 0) | (dropped["LivingArea"] <= 0)].shape[0])


print("\nNegative Bathroom Count:", dropped[dropped["BathroomsTotalInteger"] < 0].shape[0])
print("Negative Bedroom Count:", dropped[dropped["BedroomsTotal"] < 0].shape[0])
print("No need to drop anything!")

print("\nNegative DaysOnMarket Count:", dropped[dropped["DaysOnMarket"] < 0].shape[0], "-> DROP!")

dropped.drop(dropped[dropped["DaysOnMarket"] < 0]["DaysOnMarket"].index, inplace = True)

print("Rows after dropping both invalid DaysOnMarket:", dropped.shape[0])

filtered_listing = dropped.copy()



filtered_sold["invalid_coord_flag"] = (filtered_sold[["Latitude", "Longitude"]].isna().any(axis = 1)) | (filtered_sold[["Latitude", "Longitude"]] == 0).any(axis = 1) | (filtered_sold["Longitude"] > 0) | (filtered_sold["Longitude"] < -125) | (filtered_sold["Longitude"] > -113) | (filtered_sold["Latitude"] < 32) | (filtered_sold["Latitude"] > 42.5)
print("\nSold Data Invalid Coordinate Count:", filtered_sold["invalid_coord_flag"].sum())

filtered_listing["invalid_coord_flag"] = (filtered_listing[["Latitude", "Longitude"]].isna().any(axis = 1)) | (filtered_listing[["Latitude", "Longitude"]] == 0).any(axis = 1) | (filtered_listing["Longitude"] > 0) | (filtered_listing["Longitude"] < -125) | (filtered_listing["Longitude"] > -113) | (filtered_listing["Latitude"] < 32) | (filtered_listing["Latitude"] > 42.5)
print("Listing Data Invalid Coordinate Count:", filtered_listing["invalid_coord_flag"].sum())



filtered_listing.to_csv("data/listing_prepared.csv", index=False)

filtered_sold.to_csv("data/sold_prepared.csv", index=False)

print("\nCSVs Created!")