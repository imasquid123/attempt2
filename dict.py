#compatability package recommended in google api thing
import credential_holder
import oauth2client
from __future__ 
import print_function
#lets me open spreadsheet by url :D
import gspread from oauth2client
#pandas- lib for data analysis
import pandas as pd
#hold secretysecret file
import json


#using Storage for json authorization instead of SignedJwtAssertionCredentials b/c the internet was angry; it's been discontinued
credinstance = oauth2client.file.Storage()
class CredentialExchange:
#put creds in holder

def putcredentials(credinstance):
    storecreds.locked_put(json)
