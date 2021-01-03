HasRequests = False
HasJson = False

#Check Requirements Exist
try:
    import requests
    HasRequests = True
except:
    HasRequests = False

try:
    import json
    HasJson = True
except:
    HasJson = False

if(HasRequests == False and HasJson == False):
    print("Missing requests and json")
elif(HasRequests == False and HasJson == True):
    print("Please run the following command in cmd/terminal")
    print("pip install requests")
elif(HasJson == False):
    print("Python installation error | json missing")

import robloxpy.Utils as Utils
import robloxpy.Game as Game
import robloxpy.User as User
import robloxpy.Market as Market    
import robloxpy.Group as Group