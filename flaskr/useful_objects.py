from collections import defaultdict
import sys

class email_validation ():
    email = ''
    token = 0
    used = False

    def __init__(self, email, token, used=False):
        self.email = email
        self.token = token
        self.used = used
        return

class email_reader (object):

    email_list = []

    def __init__(self):
        self.email_list.append("Minecrafthomes@gmail.com", 4474)
        return
    
    def check_email_and_token(self, email, token):
        
        while i < len(email_list):
            if self.email_list[i].token == token:
                if self.email_list[i].email == email:
                    return True
                return False
            return False
        return False
    
