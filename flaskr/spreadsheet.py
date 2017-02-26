import gspread
from oauth2client.service_account import ServiceAccountCredentials

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

while i < sheet.col_count:
    while j < sheet.row_count:
        if i == 2:
            sampleData.email = str(sheet.cell(i,j))
            i += 1
        if i == 3:
            sampleData.access_code = sheet.cell(i,j).value
            i += 1
        if i == 4:
            sampleData.turkey = sheet.cell(i,j).value
            i += 1
        i += 1
        j += 1
    allData.append(sampleData)

i = 0

for sampleData in allData:
    print(allData[i].email)
    print(allData[i].access_code)
    print(allData[i].turkey)
    i += 1

# Structure of data
# Date and Time | Email | Access Code | Scores
