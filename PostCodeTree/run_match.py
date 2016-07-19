import csv, re

pcFile = "postcodes.csv"

# # Output all BT codes
# reg = re.compile("BT[0-9]{1,2} [0-9][A-Z]{2}")

# Output all BT codes where the first part ends in 8 and the second part begins with 0
reg = re.compile("BT[0-9]8 0[A-Z]{2}")

with open(pcFile) as csvfile:
    pcReader = csv.DictReader(csvfile)
    for row in pcReader:
        postcode = row['Postcode']
        match = reg.match(postcode)
        if match:
            print (postcode)
        
