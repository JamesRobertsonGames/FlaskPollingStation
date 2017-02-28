from collections import defaultdict
import sys

class email_validation ():
    email = ''
    token = ''
    used = False

class sheet_reader (object):

    template_email_val = email_validation()
    email_dict = defaultdict(template_email_val)

    def __init__(self):
            
    def read_sheets(self):
        # Read it in with "ALL CELLS"
        # It should be seporated by commas
        # Don't parse it here
        return

    def split_to_correct_data(self):
        # Parse into email_dict here
        # Figure out which ones are
        # Email and Token
        # Used is set to faulse by default
        return
    
    def check_email_and_token(self):
        # check that list against the txt file with a large array of emails and tokens
        # I'm just going to hard code it in though
        
        return

    def sequence(self):
        read_sheets()
        split_to_correct_data()
        check_email_and_token()

        # This is the theory but I have no idea if this

    
