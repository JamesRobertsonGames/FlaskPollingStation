import gspread
from oauth2client.service_account import ServiceAccountCredentials

i = 0

class euroData:
    email = " "
    access_code = " "
    turkey = 0
 
# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('test-fdf5881a3f8d.json', scope)
client = gspread.authorize(creds)
 
# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("EU").sheet1

print type(sheet) # gspead.models.worksheet
 
# Extract and print all of the values
list_of_hashes = sheet.cell(2,2)]

# Structure of data
# Date and Time | Email | Access Code | Scores

print(list_of_hashes)
