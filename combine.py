import pandas as pd

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
listing202602 = pd.read_csv("data/CRMLSListing202602.csv", encoding='cp1252')
listing202603 = pd.read_csv("data/CRMLSListing202603.csv", encoding='cp1252')



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
sold202602 = pd.read_csv("data/CRMLSSold202602.csv", encoding='cp1252')
sold202603 = pd.read_csv("data/CRMLSSold202603.csv", encoding='cp1252')



# Checking row counts of datasets before and after concat below:
listing_list = [listing202401, listing202402, listing202403, listing202404, listing202405, listing202406,
                     listing202407, listing202408, listing202409, listing202410, listing202411, listing202412,
                     listing202501, listing202502, listing202503, listing202504, listing202505, listing202506,
                     listing202507, listing202508, listing202509, listing202510, listing202511, listing202512,
                     listing202601, listing202602, listing202603]
sold_list = [sold202401, sold202402, sold202403, sold202404, sold202405, sold202406,
                  sold202407, sold202408, sold202409, sold202410, sold202411, sold202412,
                  sold202501, sold202502, sold202503, sold202504, sold202505, sold202506,
                  sold202507, sold202508, sold202509, sold202510, sold202511, sold202512,
                  sold202601, sold202602, sold202603]

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
                     listing202601, listing202602, listing202603], ignore_index=True)

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
                  sold202601, sold202602, sold202603], ignore_index=True)
print("SOLD Post *concat* Total:", sold.shape[0], "rows\n")



# Combining Datasets, checking row counts, and creating new csv files below
listing_filtered = listing[listing["PropertyType"] == "Residential"]
sold_filtered = sold[sold["PropertyType"] == "Residential"]

print("Filtered Listing Total:", listing_filtered.shape[0], "rows")
print("Filtered Sold Total:", sold_filtered.shape[0], "rows")

listing_filtered.to_csv("data/listing_combined.csv", index=False)

sold_filtered.to_csv("data/sold_combined.csv", index=False)

print("\nCompleted CSV files!")