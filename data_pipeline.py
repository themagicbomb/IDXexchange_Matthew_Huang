    # PART 1! Combining Datasets, Filtering out non residential
import pandas as pd
import numpy as np

print("Reading in data...\n")
# Listing Dataframes below
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
listing202602 = pd.read_csv("data/CRMLSListing202602.csv")
listing202603 = pd.read_csv("data/CRMLSListing202603.csv")
listing202604 = pd.read_csv("data/CRMLSListing202604.csv")



# Sold Dataframes below
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
sold202602 = pd.read_csv("data/CRMLSSold202602.csv")
sold202603 = pd.read_csv("data/CRMLSSold202603.csv")
sold202604 = pd.read_csv("data/CRMLSSold202604.csv")



# Checking row counts of datasets before and after concat below:
listing_list = [listing202401, listing202402, listing202403, listing202404, listing202405, listing202406,
                     listing202407, listing202408, listing202409, listing202410, listing202411, listing202412,
                     listing202501, listing202502, listing202503, listing202504, listing202505, listing202506,
                     listing202507, listing202508, listing202509, listing202510, listing202511, listing202512,
                     listing202601, listing202602, listing202603, listing202604]
sold_list = [sold202401, sold202402, sold202403, sold202404, sold202405, sold202406,
                  sold202407, sold202408, sold202409, sold202410, sold202411, sold202412,
                  sold202501, sold202502, sold202503, sold202504, sold202505, sold202506,
                  sold202507, sold202508, sold202509, sold202510, sold202511, sold202512,
                  sold202601, sold202602, sold202603, sold202604]

print("LISTING row counts by month:")
total = 0
for i in range(len(listing_list)):
    year = 2024 + i // 12
    month = (i + 1) % 12
    if month == 0:
        month = 12
    print(f"Month {month}, {year}:", listing_list[i].shape[0])
    total += listing_list[i].shape[0]
print("Total:", total, "rows")

listing = pd.concat([listing202401, listing202402, listing202403, listing202404, listing202405, listing202406,
                     listing202407, listing202408, listing202409, listing202410, listing202411, listing202412,
                     listing202501, listing202502, listing202503, listing202504, listing202505, listing202506,
                     listing202507, listing202508, listing202509, listing202510, listing202511, listing202512,
                     listing202601, listing202602, listing202603, listing202604], ignore_index=True)

print("LISTING Post *concat* Total:", listing.shape[0], "rows\n")

print("SOLD row counts by month:")
total = 0
for i in range(len(sold_list)):
    year = 2024 + i // 12
    month = (i + 1) % 12
    if month == 0:
        month = 12
    print(f"Month {month}, {year}:", sold_list[i].shape[0])
    total += sold_list[i].shape[0]
print("Total:", total, "rows")

sold = pd.concat([sold202401, sold202402, sold202403, sold202404, sold202405, sold202406,
                  sold202407, sold202408, sold202409, sold202410, sold202411, sold202412,
                  sold202501, sold202502, sold202503, sold202504, sold202505, sold202506,
                  sold202507, sold202508, sold202509, sold202510, sold202511, sold202512,
                  sold202601, sold202602, sold202603, sold202604], ignore_index=True)
print("SOLD Post *concat* Total:", sold.shape[0], "rows\n")

print("Same Unique Property Types in both Datasets? ---", list(pd.Series(listing["PropertyType"].unique()).sort_values()) == list(pd.Series(sold["PropertyType"].unique()).sort_values()))

print("\nUnique Property Types in Datasets:")
print(list(listing["PropertyType"].unique()))

print("Listing Total:", listing.shape[0], "rows")
print("Sold Total:", sold.shape[0], "rows")

# Combining Datasets, checking row counts, and creating new csv files below
listing_combined = listing[listing["PropertyType"] == "Residential"]
sold_combined = sold[sold["PropertyType"] == "Residential"]

print("Filtered Listing Total (Post PropertyType = Residential):", listing_combined.shape[0], "rows")
print("Filtered Sold Total (Post PropertyType = Residential):", sold_combined.shape[0], "rows")

print()
print("-----------------------------------------------------------------------------------------------")
print()










    # PART 2! Filtering out duplicate columns, selecting useful columns, removing columns with extreme missingness
listing = listing_combined.copy()
sold = sold_combined.copy()



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

print()
print("-----------------------------------------------------------------------------------------------")
print()










    # PART 3! enrich with Mortgage Data
# Step 1 – Fetch the mortgage rate data from FRED
print("Fetching Mortgage Data...\n")

url = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=MORTGAGE30US"
mortgage = pd.read_csv(url, parse_dates=['observation_date'])
mortgage.columns = ['date', 'rate_30yr_fixed']



# Step 2 – Resample weekly rates to monthly averages
print("Creating monthly averages...\n")

mortgage['year_month'] = mortgage['date'].dt.to_period('M')
mortgage_monthly = (
mortgage.groupby('year_month')['rate_30yr_fixed']
.mean()
.reset_index()
)



# COPYING CLEAN DATSETS
listings = listing_clean.copy()
sold = sold_clean.copy()



# Step 3 – Create a matching year_month key on the MLS datasets
print("Creating year_month keys...\n")
# Sold dataset — key off CloseDate
sold['year_month'] = pd.to_datetime(sold['CloseDate']).dt.to_period('M')
# Listings dataset — key off ListingContractDate
listings['year_month'] = pd.to_datetime(
listings['ListingContractDate']
).dt.to_period('M')



# Step 4 – Merge
print("Merging on year_month...\n")
sold_with_rates = sold.merge(mortgage_monthly, on='year_month', how='left')
listings_with_rates = listings.merge(mortgage_monthly, on='year_month', how='left')



# Step 5 – Validate the merge
print("Checking Null Rate:")
# Check for any unmatched rows (rate should not be null)
print("SOLD Null rate of 'rate_30yr_fixed':", sold_with_rates['rate_30yr_fixed'].isnull().sum())
print("LISTING Null rate of 'rate_30yr_fixed':", listings_with_rates['rate_30yr_fixed'].isnull().sum())

print()
print("-----------------------------------------------------------------------------------------------")
print()










    # PART 4! prepare data, remove redudent columns, impute missingness, check impossible values
listing = listings_with_rates.copy()
sold = sold_with_rates.copy()

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

print()
print("-----------------------------------------------------------------------------------------------")
print()










    # PART 5! feature engineering and summary tables
listing = filtered_listing.copy()
sold = filtered_sold.copy()

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

print()
print("-----------------------------------------------------------------------------------------------")
print()










    # PART 6! FINAL! IQR filtering
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