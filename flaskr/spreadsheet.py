import gspread
from oauth2client.service_account import ServiceAccountCredentials
import copy

i = 0
j = 0

class euroData(object):
    email = " "
    access_code = 0
    turkey = 0

sampleData = euroData()

allData = []
 
# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('test-fdf5881a3f8d.json', scope)
client = gspread.authorize(creds)
 
# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("EU").sheet1

# gspead.models.worksheet

# temp = sheet.get_all_values()



while i < 5:

    i += 1
    sampleData.email = sheet.cell(i,2).value
    sampleData.access_code = sheet.cell(i,3).value
    sampleData.turkey = sheet.cell(i,4).value

    allData.append(copy.copy(sampleData))

i = 0 

for sampleData in allData:
    print(allData[i].email)
    print(allData[i].access_code)
    print(allData[i].turkey)
    i += 1

# print temp

# Structure of data
# Date and Time | Email | Access Code | Scores
