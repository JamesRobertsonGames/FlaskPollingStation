import gspread
from oauth2client.service_account import ServiceAccountCredentials
import copy

class euroData(object):
    email = " "
    access_code = 0
    moldova = 0
    united_kingdom = 0

class euro_manager(object):

    sampleData = euroData()

    allData = []
 
    scope = 0
    creds = 0
    client = 0
    sheet = 0

    def __init__(self):
        return
    
    def open_data(self):

        # use creds to create a client to interact with the Google Drive API        
        self.scope = ['https://spreadsheets.google.com/feeds']
        self.creds = ServiceAccountCredentials.from_json_keyfile_name('test-fdf5881a3f8d.json', self.scope)
        self.client = gspread.authorize(self.creds)

        # Open the sheet
        self.sheet = self.client.open("EU").sheet1
        return
    
    def store_data_locally(self):
        # Index set to one
        i = 1

        # Width
        height_of_table = 3

        # Itterate through rows
        while i < height_of_table:
            i += 1

            # All the data from the rows
            self.sampleData.email = self.sheet.cell(i,2).value
            self.sampleData.moldova = self.sheet.cell(i,3).value
            self.sampleData.united_kingdom = self.sheet.cell(i,4).value
            self.sampleData.access_code = self.sheet.cell(i,5).value

            # Append a copy of it to the end of the list
            self.allData.append(copy.copy(self.sampleData))
        return

    def print_all_data(self):
        # Index set to zero
        i = 0 

        # Get all of the data and print it
        for self.sampleData in self.allData:
            print(self.allData[i].email)
            print(self.allData[i].moldova)
            print(self.allData[i].united_kingdom)
            print(self.allData[i].access_code)

            # Increment Index
            i += 1
        return
        
if __name__ == "__main__":
    manager = euro_manager()
    manager.open_data()
    manager.store_data_locally()
    manager.print_all_data()

# gspead.models.worksheet

# temp = sheet.get_all_values()

# print temp

# Structure of data
# Date and Time | Email | Access Code | Scores
