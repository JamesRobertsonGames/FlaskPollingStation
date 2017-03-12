import gspread
from oauth2client.service_account import ServiceAccountCredentials
import copy
from useful_objects import *

class euroData(object):
    email = " "
    moldova = 0
    united_kingdom = 0
    access_code = 0

    def __init__ (self, email, access_code, moldova, united_kingdom):
        # This might turn into a monster but it is fine
        self.email = email
        self.access_code = access_code
        self.moldova = moldova
        self.united_kingdom = united_kingdom

    def print_all_values():
        # I can hide everything inside of This
        return


class euro_manager(object):

    sampleData = euroData()
    validation_checker = email_reader()

    records = []
 
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

        # Number of Votes
        number_of_records = 40

        # Itterate through rows
        while i < number_of_records:
            i += 1

            # All the data from the rows
            if self.sheet.cell(i,2).value =='':
                break

            self.sampleData(self.sheet.cell(i,2).value, self.sheet.cell(i,5).value, 
                            self.sheet.cell(i,3).value, self.sheet.cell(i,4).value)
            # self.sampleData.email = self.sheet.cell(i,2).value
            # self.sampleData.moldova = self.sheet.cell(i,3).value
            # self.sampleData.united_kingdom = self.sheet.cell(i,4).value
            # self.sampleData.access_code = self.sheet.cell(i,5).value

            # Append a copy of it to the end of the list
            self.records.append(copy.copy(self.sampleData))
        return

    def print_all_data(self):

        # Index set to zero
        i = 0 

        # Get all of the data and print it
        for self.sampleData in self.records:
            print(self.records[i].email)
            print(self.records[i].moldova)
            print(self.records[i].united_kingdom)
            print(self.records[i].access_code)

            # Increment Index
            i += 1
        return

    def pop_invalid_emails_out(self):
        
        i = 0 
        while i < len(self.records):
            if self.validation_checker.check_email_and_token(self.records[i].email,self.records[i].access_code):
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
