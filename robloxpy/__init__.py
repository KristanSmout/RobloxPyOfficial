import requests
import json


APIURL = "https://api.roblox.com/"
InventoryURL = "https://inventory.roblox.com"
UserAPI = APIURL + "users/"
GroupAPI = APIURL + "groups/"
TestUserID = 1368140
TestGroupID = 916576
TestAssetID = 240351460


#region External User API's

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


def GetOfflineFriends(UserID):
    FullList = []
    response = requests.get(UserAPI + str(UserID) + "/friends")
    Friendslist = json.loads(response.text)
    for friend in Friendslist:
        if(str(friend['IsOnline']) in 'False'):
            FullList.append(friend['Username'])
    return FullList

def GetUserGroups(UserID):
    response = requests.get(UserAPI + str(UserID) + "/groups")
    FullList = []
    Grouplist = json.loads(response.text)
    for group in Grouplist:
        FullList.append(group['Name'])
    return FullList



#endregion

#region External Group API's

def GetGroupAllies(GroupID):
    response = requests.get(GroupAPI + str(GroupID) + "/allies")
    FullList = []
    Grouplist = json.loads(response.text)
    Grouplist = Grouplist['Groups']
    for group in Grouplist:
        FullList.append(group['Name'])
    return FullList

def GetGroupEnemies(GroupID):
    response = requests.get(GroupAPI + str(GroupID) + "/enemies")
    FullList = []
    Grouplist = json.loads(response.text)
    Grouplist = Grouplist['Groups']
    for group in Grouplist:
        FullList.append(group['Name'])
    return FullList

#endregion


#region External Asset API's

def CanManage(UserID,AssetID):
    response = requests.get(UserAPI + str(UserID) + '/canmanage/' + str(AssetID))
    return response.json()['CanManage']
#endregion

print(CanManage(TestUserID,TestAssetID))
