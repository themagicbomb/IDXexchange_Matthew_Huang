import pandas as pd
import numpy as np



listing202401 = pd.read_csv("data/CRMLSListing202401.csv")
listing202402 = pd.read_csv("data/CRMLSListing202402.csv")
listing202403 = pd.read_csv("data/CRMLSListing202403.csv")
listing202404 = pd.read_csv("data/CRMLSListing202404.csv")
listing202405 = pd.read_csv("data/CRMLSListing202405.csv")
listing202406 = pd.read_csv("data/CRMLSListing202406.csv")
listing202407 = pd.read_csv("data/CRMLSListing202407.csv")
listing202408 = pd.read_csv("data/CRMLSListing202408.csv")
listing202409 = pd.read_csv("data/CRMLSListing202409.csv")
listing202410 = pd.read_csv("data/CRMLSListing202410.csv")
listing202411 = pd.read_csv("data/CRMLSListing202411.csv")
listing202412 = pd.read_csv("data/CRMLSListing202412.csv")

listing202501 = pd.read_csv("data/CRMLSListing202501.csv")
listing202502 = pd.read_csv("data/CRMLSListing202502.csv")
listing202503 = pd.read_csv("data/CRMLSListing202503.csv")
listing202504 = pd.read_csv("data/CRMLSListing202504.csv")
listing202505 = pd.read_csv("data/CRMLSListing202505.csv")
listing202506 = pd.read_csv("data/CRMLSListing202506.csv")
listing202507 = pd.read_csv("data/CRMLSListing202507.csv")
listing202508 = pd.read_csv("data/CRMLSListing202508.csv")
listing202509 = pd.read_csv("data/CRMLSListing202509.csv")
listing202510 = pd.read_csv("data/CRMLSListing202510.csv")
listing202511 = pd.read_csv("data/CRMLSListing202511.csv")
listing202512 = pd.read_csv("data/CRMLSListing202512.csv")

listing202601 = pd.read_csv("data/CRMLSListing202601.csv")
listing202602 = pd.read_csv("data/CRMLSListing202602.csv", encoding='cp1252')
listing202603 = pd.read_csv("data/CRMLSListing202603.csv", encoding='cp1252')

sold202401 = pd.read_csv("data/CRMLSSold202401.csv")
sold202402 = pd.read_csv("data/CRMLSSold202402.csv")
sold202403 = pd.read_csv("data/CRMLSSold202403.csv")
sold202404 = pd.read_csv("data/CRMLSSold202404.csv", low_memory=False) # mixed types
sold202405 = pd.read_csv("data/CRMLSSold202405.csv")
sold202406 = pd.read_csv("data/CRMLSSold202406.csv")
sold202407 = pd.read_csv("data/CRMLSSold202407.csv")
sold202408 = pd.read_csv("data/CRMLSSold202408.csv")
sold202409 = pd.read_csv("data/CRMLSSold202409.csv")
sold202410 = pd.read_csv("data/CRMLSSold202410.csv")
sold202411 = pd.read_csv("data/CRMLSSold202411.csv")
sold202412 = pd.read_csv("data/CRMLSSold202412.csv")

sold202501 = pd.read_csv("data/CRMLSSold202501.csv")
sold202502 = pd.read_csv("data/CRMLSSold202502.csv")
sold202503 = pd.read_csv("data/CRMLSSold202503.csv")
sold202504 = pd.read_csv("data/CRMLSSold202504.csv")
sold202505 = pd.read_csv("data/CRMLSSold202505.csv")
sold202506 = pd.read_csv("data/CRMLSSold202506.csv", low_memory=False) # mixed types
sold202507 = pd.read_csv("data/CRMLSSold202507.csv")
sold202508 = pd.read_csv("data/CRMLSSold202508.csv")
sold202509 = pd.read_csv("data/CRMLSSold202509.csv")
sold202510 = pd.read_csv("data/CRMLSSold202510.csv")
sold202511 = pd.read_csv("data/CRMLSSold202511.csv")
sold202512 = pd.read_csv("data/CRMLSSold202512.csv")

sold202601 = pd.read_csv("data/CRMLSSold202601.csv", low_memory=False) # mixed types
sold202602 = pd.read_csv("data/CRMLSSold202602.csv", encoding='cp1252')
sold202603 = pd.read_csv("data/CRMLSSold202603.csv", encoding='cp1252')

listing = pd.concat([listing202401, listing202402, listing202403, listing202404, listing202405, listing202406,
                     listing202407, listing202408, listing202409, listing202410, listing202411, listing202412,
                     listing202501, listing202502, listing202503, listing202504, listing202505, listing202506,
                     listing202507, listing202508, listing202509, listing202510, listing202511, listing202512,
                     listing202601, listing202602, listing202603], ignore_index=True)

sold = pd.concat([sold202401, sold202402, sold202403, sold202404, sold202405, sold202406,
                  sold202407, sold202408, sold202409, sold202410, sold202411, sold202412,
                  sold202501, sold202502, sold202503, sold202504, sold202505, sold202506,
                  sold202507, sold202508, sold202509, sold202510, sold202511, sold202512,
                  sold202601, sold202602, sold202603], ignore_index=True)



print("Same Unique Property Types in both Datasets? ---", list(pd.Series(listing["PropertyType"].unique()).sort_values()) == list(pd.Series(sold["PropertyType"].unique()).sort_values()))

print("\nUnique Property Types in Datasets:")
print(list(listing["PropertyType"].unique()))



# Filtering done in combine.py
listing = pd.read_csv("data/listing_combined.csv", low_memory=False)
sold = pd.read_csv("data/sold_combined.csv", low_memory=False)



print("\nNOTE! Sold dataset does not have any duplicate columns, but Listing dataset does. Combining when possible...\n")

print("Conflicting values means that they columns have different values AND at least one of those values isn't null\n(meaning when combined no information will be lost)\n")

def helper(df, dupe1, dupe2):
    no_na = df[[dupe1, dupe2]].dropna()
    return sum(no_na[dupe] != no_na[dupe])

dupes = listing.filter(like = ".1").columns

for dupe in dupes:
    print(dupe.split(".")[0], "has", helper(listing, dupe.split(".")[0], dupe), "conflting values with", dupe)
    print(dupe.split(".")[0], "number of different rows?", sum(listing[dupe.split(".")[0]] != listing[dupe]))
    print()
    
    

cols = np.array(list(dupes.str.split(".")))[:,0]
for col in cols:
    dot_name = col + ".1"
    listing[col] = listing[col].fillna(listing[dot_name])
listing.drop(dupes, axis = 1, inplace = True)



listing_NA_percent = listing.isna().sum() / listing.shape[0]
listing_removed = listing_NA_percent.index[listing_NA_percent > .9]
listing_clean = listing.drop(listing_removed, axis = 1)
print("Percent Missingness of Columns with more than 90% NA (listing):")
print(listing_NA_percent[listing_removed] * 100)
print("\nREMOVED!\n")



sold_NA_percent = sold.isna().sum() / sold.shape[0]
sold_removed = sold_NA_percent.index[sold_NA_percent > .9]
sold_clean = sold.drop(sold_removed, axis = 1)
print("Percent Missingness of Columns with more than 90% NA (sold):")
print(sold_NA_percent[sold_removed] * 100)
print("\nREMOVED!\n")



listing_clean.columns
nonnumeric = listing_clean[listing_clean.columns[(listing_clean.dtypes == "str") | (listing_clean.dtypes == "object")]]

nonnumeric["ListAgentEmail"] # Not useful for any visualization -> DROP
nonnumeric["CloseDate"] # Can be datetime, let's keep -> KEEP
nonnumeric[["ListAgentFirstName", "ListAgentLastName", "ListAgentFullName"]].isna().sum(axis = 1).value_counts()
# Redundant, remove separate first and last names, but we should inpute full name missingness with first/last name if possible -> IMPUTE/DROP
nonnumeric["UnparsedAddress"] # Specific addresses not super useful -> DROP
nonnumeric["PropertyType"].nunique() # Only one since we cleaned the rest, so drop! -> DROP
nonnumeric["ListOfficeName"].value_counts() # Useful -> KEEP
nonnumeric[nonnumeric["BuyerOfficeName"] != nonnumeric["ListOfficeName"]][["ListOfficeName", "BuyerOfficeName"]].dropna() # They can be different, let's keep both -> KEEP
nonnumeric[(nonnumeric["CoListOfficeName"] != nonnumeric["BuyerOfficeName"]) | (nonnumeric["CoListOfficeName"] != nonnumeric["ListOfficeName"])][["CoListOfficeName", "ListOfficeName", "BuyerOfficeName"]].dropna() # All three can be different, let's keep all -> KEEP
nonnumeric[["CoListAgentFirstName", "CoListAgentLastName"]].isna().sum(axis = 1).value_counts() # Combine into one full CoListAgentName -> IMPUTE/DROP
nonnumeric["AssociationFeeFrequency"].unique() # Categorical -> KEEP
nonnumeric["BuyerAgentMlsId"].value_counts() # Generally unique, let's drop -> DROP
nonnumeric[['BuyerAgentFirstName', 'BuyerAgentLastName']].isna().sum(axis = 1).value_counts() # Combine into one BuyerAgentName -> IMPUTE/DROP
nonnumeric["AssociationFeeFrequency"].unique() # Categorical -> Keep
nonnumeric["MLSAreaMajor"].value_counts() # Can be usable -> Keep
nonnumeric["CountyOrParish"].unique() # Helpful -> Keep
nonnumeric["MlsStatus"].unique() # Categorical -> Keep
nonnumeric["ElementarySchool"].value_counts() # Not super meaningful, mostly other -> DROP
nonnumeric["AttachedGarageYN"].unique() # Discrete -> Keep
nonnumeric["PropertySubType"].unique() # Categorical -> Keep
nonnumeric["SubdivisionName"].value_counts() # Not super useful -> DROP
nonnumeric["BuyerOfficeAOR"].value_counts() # Could be useful -> Keep
nonnumeric["BuyerAgencyCompensationType"].unique() # Categorical -> Keep
nonnumeric["ListingId"].value_counts() # Pretty unique -> DROP
nonnumeric["City"].value_counts() # Useful -> Keep
nonnumeric["ContractStatusChangeDate"].unique() # helpful -> Keep
nonnumeric["PurchaseContractDate"].unique() # helpful -> Keep
nonnumeric["ListingContractDate"].unique() # helpful -> Keep
nonnumeric["StateOrProvince"].unique() # categorical -> Keep
nonnumeric["MiddleOrJuniorSchool"].unique() # less useful -> drop
nonnumeric["FireplaceYN"].unique() # discrete -> Keep
nonnumeric["HighSchool"].unique() # less useful -> drop
nonnumeric["Levels"].unique() # can be helpful/cleaned up -> Keep
nonnumeric["NewConstructionYN"].unique() # discrete -> Keep
nonnumeric["HighSchoolDistrict"].unique() # less useful -> drop
nonnumeric["PostalCode"].unique() # we need later -> KEEP

print("RESULTS:\n")

print("IMPUTE:")
print("ListAgentFullName from ListAgentFirstName and ListAgentLastName;")
print("Combine CoListAgentFirstName and CoListAgentLastName;")
print("Combine BuyerAgentFirstName and BuyerAgentLastName\n")

def combine(first, last):
    first = str(first)
    last = str(last)
    if first == "nan":
        first = ""
    if last == "nan":
        last = ""
    if first == "" and last == "":
        return None
    return " ".join([str(first), str(last)])

listing_clean["ListAgentFullName"] = listing_clean["ListAgentFullName"].fillna(listing_clean.apply(lambda row: combine(row['ListAgentFirstName'], row['ListAgentLastName']), axis = 1))

listing_clean["CoListAgentFullName"] = listing_clean.apply(lambda row: combine(row["CoListAgentFirstName"], row["CoListAgentLastName"]), axis = 1)

listing_clean["BuyerAgentFullName"] = listing_clean.apply(lambda row: combine(row["BuyerAgentFirstName"], row["BuyerAgentLastName"]), axis = 1)

print("Full names imputed!\n")




print("DROP (too unique/redundant):\nListAgentEmail, ListAgentFirstName, ListAgentLastName, CoListAgentFirstName, CoListAgentLastName,\nBuyerAgentFirstName, BuyerAgentLastName, UnparsedAddress, PropertyType (all residential), BuyerAgentMlsId, ElementarySchool,\nSubdivisionName, ListingId, MiddleOrJuniorSchool, HighSchool, HighSchoolDistrict\n")

listing_clean = listing_clean.drop(["ListAgentEmail", "ListAgentFirstName", "ListAgentLastName", "CoListAgentFirstName", "CoListAgentLastName", "BuyerAgentFirstName", "BuyerAgentLastName", "UnparsedAddress", "PropertyType", "BuyerAgentMlsId", "ElementarySchool", "SubdivisionName", "ListingId", "MiddleOrJuniorSchool", "HighSchool", "HighSchoolDistrict"], axis = 1)

print("DROPPED!\n")





nonnumeric = sold_clean[sold_clean.columns[(sold_clean.dtypes == "str") | (sold_clean.dtypes == "object")]]

nonnumeric["BuyerAgentAOR"].value_counts() # can be useful -> keep
nonnumeric["ListAgentAOR"].value_counts() # can be useful -> keep
nonnumeric["Flooring"].value_counts() # can be useful/cleaned up -> keep
nonnumeric["ViewYN"].value_counts() # discrete-> keep
nonnumeric["PoolPrivateYN"].value_counts() # discrete -> keep
nonnumeric["ListAgentEmail"].value_counts() # Not useful for any visualization -> DROP
nonnumeric["CloseDate"].unique() # can be needed later for timeseries visuals -> Keep
nonnumeric[["ListAgentFirstName", "ListAgentLastName", "ListAgentFullName"]].isna().sum(axis = 1).value_counts() # same as last time -> IMPUTE FULL NAME AND DROP REST
nonnumeric["UnparsedAddress"].value_counts() # Specific addresses not super useful -> DROP
nonnumeric["PropertyType"].value_counts() # already filtered, redudant -> DROP
nonnumeric["ListOfficeName"].value_counts() # Useful -> KEEP
nonnumeric[nonnumeric["BuyerOfficeName"] != nonnumeric["ListOfficeName"]][["ListOfficeName", "BuyerOfficeName"]].dropna() # They can be different, let's keep both -> KEEP
nonnumeric[(nonnumeric["CoListOfficeName"] != nonnumeric["BuyerOfficeName"]) | (nonnumeric["CoListOfficeName"] != nonnumeric["ListOfficeName"])][["CoListOfficeName", "ListOfficeName", "BuyerOfficeName"]].dropna() # All three can be different, let's keep all -> KEEP
nonnumeric[["CoListAgentFirstName", "CoListAgentLastName"]].isna().sum(axis = 1).value_counts() # Combine into one full CoListAgentName -> IMPUTE/DROP
nonnumeric["BuyerAgentMlsId"].value_counts() # Generally unique, let's drop -> DROP
nonnumeric[['BuyerAgentFirstName', 'BuyerAgentLastName']].isna().sum(axis = 1).value_counts() # Combine into one BuyerAgentName -> IMPUTE/DROP
nonnumeric["AssociationFeeFrequency"].unique() # Categorical -> Keep
nonnumeric["MLSAreaMajor"].value_counts() # Can be usable -> Keep
nonnumeric["CountyOrParish"].unique() # Helpful -> Keep
nonnumeric["MlsStatus"].unique() # REDUDENT -> DROP
nonnumeric["ElementarySchool"].value_counts() # Not super meaningful, mostly other -> DROP
nonnumeric["AttachedGarageYN"].unique() # Discrete -> Keep
nonnumeric["PropertySubType"].unique() # Categorical -> Keep
nonnumeric["SubdivisionName"].value_counts() # Not super useful -> DROP
nonnumeric["BuyerOfficeAOR"].value_counts() # Could be useful -> Keep
nonnumeric["ListingId"].value_counts() # Pretty unique -> DROP
nonnumeric["City"].value_counts() # Useful -> Keep
nonnumeric["ContractStatusChangeDate"].unique() # helpful -> Keep
nonnumeric["PurchaseContractDate"].unique() # helpful -> Keep
nonnumeric["ListingContractDate"].unique() # helpful -> Keep
nonnumeric["StateOrProvince"].unique() # categorical -> Keep
nonnumeric["MiddleOrJuniorSchool"].unique() # less useful -> drop
nonnumeric["FireplaceYN"].unique() # discrete -> Keep
nonnumeric["HighSchool"].unique() # less useful -> drop
nonnumeric["Levels"].unique() # can be helpful/cleaned up -> Keep
nonnumeric["NewConstructionYN"].unique() # discrete -> Keep
nonnumeric["HighSchoolDistrict"].unique() # less useful -> drop
nonnumeric["PostalCode"].unique() # we need later -> KEEP
nonnumeric["BuyerAgencyCompensationType"].unique() # categorical -> KEEP
nonnumeric["latfilled"].unique() # categorical -> KEEP
nonnumeric["lonfilled"].unique() # categorical -> KEEP

print("RESULTS:\n")

print("IMPUTE:")
print("ListAgentFullName from ListAgentFirstName and ListAgentLastName;")
print("Combine CoListAgentFirstName and CoListAgentLastName;")
print("Combine BuyerAgentFirstName and BuyerAgentLastName\n")

sold_clean["ListAgentFullName"] = sold_clean["ListAgentFullName"].fillna(sold_clean.apply(lambda row: combine(row['ListAgentFirstName'], row['ListAgentLastName']), axis = 1))

sold_clean["CoListAgentFullName"] = sold_clean.apply(lambda row: combine(row["CoListAgentFirstName"], row["CoListAgentLastName"]), axis = 1)

sold_clean["BuyerAgentFullName"] = sold_clean.apply(lambda row: combine(row["BuyerAgentFirstName"], row["BuyerAgentLastName"]), axis = 1)

print("Full names imputed!\n")




print("DROP (too unique/redundant):\nListAgentEmail, ListAgentFirstName, ListAgentLastName, CoListAgentFirstName, CoListAgentLastName,\nBuyerAgentFirstName, BuyerAgentLastName, UnparsedAddress, PropertyType (all residential), BuyerAgentMlsId,\nMlsStatus, ElementarySchool, SubdivisionName, ListingId, MiddleOrJuniorSchool, HighSchool, HighSchoolDistrict\n")

sold_clean = sold_clean.drop(["ListAgentEmail", "ListAgentFirstName", "ListAgentLastName", "CoListAgentFirstName", "CoListAgentLastName", "BuyerAgentFirstName", "BuyerAgentLastName", "UnparsedAddress", "PropertyType", "BuyerAgentMlsId", "MlsStatus", "ElementarySchool", "SubdivisionName", "ListingId", "MiddleOrJuniorSchool", "HighSchool", "HighSchoolDistrict"], axis = 1)

print("DROPPED!\n")



listing_missingness = listing_clean.isna().sum()
sold_missingness = sold_clean.isna().sum()

set(list(listing_missingness.index) + list(sold_missingness.index))
missingness = pd.DataFrame(columns = ["Variable", "Listing_Missingness", "Sold_Missingness"])

index = 0
for var in set(list(listing_missingness.index) + list(sold_missingness.index)):
    try:
        listing_count = listing_missingness[var]
    except:
        listing_count = None
    try:
        sold_count = sold_missingness[var]
    except:
        sold_count = None
    missingness.loc[index] = [var, listing_count, sold_count]
    index += 1
    
print("Missingness Summary (NA/None means variable was removed/not present in other dataset):")
print(missingness)




listing_summary = listing_clean[["ClosePrice", "LivingArea", "DaysOnMarket"]].describe().loc[["min", "max", "mean", "50%", "25%", "75%"]]
listing_summary.index = ['min', 'max', 'mean', 'median/50%', '25%', '75%']
print("Listing Summary:")
print(listing_summary)

sold_summary = sold_clean[["ClosePrice", "LivingArea", "DaysOnMarket"]].describe().loc[["min", "max", "mean", "50%", "25%", "75%"]]
sold_summary.index = ['min', 'max', 'mean', 'median/50%', '25%', '75%']
print("\nSold Summary:")
print(sold_summary)




listing_clean.to_csv("data/listing_clean.csv", index=False)

sold_clean.to_csv("data/sold_clean.csv", index=False)


print("\nCSVs Created!")