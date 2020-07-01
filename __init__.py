import requests
import json


APIURL = "https://api.roblox.com/"
InventoryURL = "https://inventory.roblox.com"
UserAPI = APIURL + "users/"
GroupAPI = APIURL + "groups/"


#User API's

def GetName(UserID):
    response = requests.get(UserAPI + str(UserID))
    return response.json()['Username']

def IsOnline(UserID):
    response = requests.get(UserAPI + str(UserID))
    return response.json()['IsOnline']

def GetFriends(UserID):
    FullList = []
    response = requests.get(UserAPI + str(UserID) + "/friends")
    Friendslist = json.loads(response.text)
    for friend in Friendslist:
        FullList.append(friend['Username'])
    return FullList

def GetOnlineFriends(UserID):
    FullList = []
    response = requests.get(UserAPI + str(UserID) + "/friends")
    Friendslist = json.loads(response.text)
    for friend in Friendslist:
        if(str(friend['IsOnline']) in 'True'):
            FullList.append(friend['Username'])
    return FullList

def GetofflineFriends(UserID):
    FullList = []
    response = requests.get(UserAPI + str(UserID) + "/friends")
    Friendslist = json.loads(response.text)
    for friend in Friendslist:
        if(str(friend['IsOnline']) in 'False'):
            FullList.append(friend['Username'])
    return FullList

def GetUserGroups(UserID):

