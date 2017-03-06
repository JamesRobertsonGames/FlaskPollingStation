import gspread
from oauth2client.service_account import ServiceAccountCredentials
import copy

i = 0
j = 0

class euroData(object):
    email = " "
    access_code = 0
    moldova = 0
    united_kingdom = 0

class euro_manager(object):

    sampleData = euroData()

    allData = []
 
    # use creds to create a client to interact with the Google Drive API
    scope = 0
    creds = 0
    client = 0
 
    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    sheet = 0

    def __init__(self):
        open_data()
        return
    
    def open_data(self):
        self.scope = ['https://spreadsheets.google.com/feeds']
        self.creds = ServiceAccountCredentials.from_json_keyfile_name('test-fdf5881a3f8d.json', self.scope)
        self.client = gspread.authorize(self.creds)

        self.sheet = self.client.open("EU").sheet1
        return
    
    def store_data_locally(self):
        i = 1
        while i < 3:
            i += 1
            self.sampleData.email = sheet.cell(i,2).value
            self.sampleData.moldova = sheet.cell(i,3).value
            self.sampleData.united_kingdom = sheet.cell(i,4).value
            self.sampleData.access_code = sheet.cell(i,5).value

            self.allData.append(copy.copy(sampleData))
        return

    def print_all_data(self):
        i = 0 
        for sampleData in allData:
            print(allData[i].email)
            print(allData[i].moldova)
            print(allData[i].united_kingdom)
            print(allData[i].access_code)
            i += 1
        return
        



# gspead.models.worksheet

# temp = sheet.get_all_values()

# print temp

# Structure of data
# Date and Time | Email | Access Code | Scores
