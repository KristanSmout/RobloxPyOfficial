import requests
import json


APIURL = "https://api.roblox.com/"
InventoryURL = "https://inventory.roblox.com/v2/assets/"
RBXCityInventURL = "https://data.rbxcity.com/user-inventories/fetch/history/"
UserAPI = APIURL + "users/"
GroupAPI = APIURL + "groups/"
GroupAPIV1 = "https://groups.roblox.com/v1/groups/"
TestUserID = 1368140
TestGroupID = 916576
TestAssetID = 240351460
TestCatalogID = 16641274


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

def GetUserRAP(UserID):
    response = requests.get(RBXCityInventURL + str(UserID))
    for data in response.json()['data']:
        return data['recentAveragePrice']

def GetUserLimitedValue(UserID):
    response = requests.get(RBXCityInventURL + str(UserID))
    for data in response.json()['data']:
        return data['value']

def GetUserNoDemandLimiteds(UserID):
    response = requests.get(RBXCityInventURL + str(UserID))
    for data in response.json()['data']:
        return data['LowDemandItems']
    
def GetUserNormalDemandLimiteds(UserID):
    response = requests.get(RBXCityInventURL + str(UserID))
    for data in response.json()['data']:
        return data['NormalDemandItems']

def GetUserGoodDemandLimiteds(UserID):
    response = requests.get(RBXCityInventURL + str(UserID))
    for data in response.json()['data']:
        return data['GoodDemandItems']

def GetUserAmazingDemandLimiteds(UserID):
    response = requests.get(RBXCityInventURL + str(UserID))
    for data in response.json()['data']:
        return data['AmazingDemandItems']

def GetUserTerribleDemandLimiteds(UserID):
    response = requests.get(RBXCityInventURL + str(UserID))
    for data in response.json()['data']:
        return data['TerribleDemandItems']



#endregion

#region External Group API's

def GetGroupName(GroupID):
    response = requests.get(GroupAPIV1 + str(GroupID))
    return response.json()['name']

def GetGroupDescription(GroupID):
    response = requests.get(GroupAPIV1 + str(GroupID))
    return response.json()['description']

def GetGroupShout(GroupID):
    response = requests.get(GroupAPIV1 + str(GroupID))
    return response.json()['shout']

def IsGroupOpen(GroupID):
    response = requests.get(GroupAPIV1 + str(GroupID))
    return response.json()['publicEntryAllowed']

def GetGroupMembers(GroupID):
    response = requests.get(GroupAPIV1 + str(GroupID))
    return response.json()['memberCount']

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

def GetSerialList(AssetID):
    IsAll = False
    FullList = []
    NextPage = 'N/A'

    while (IsAll == False):
        if(NextPage == 'N/A'):
            response = requests.get(InventoryURL + str(AssetID) + '/owners')
            NextPage = response.json()['nextPageCursor']
        elif(NextPage == 'Done'):
            IsAll = True
        else:
            response = requests.get(InventoryURL + str(AssetID) + '/owners?&cursor=' + NextPage)
            NextPage = response.json()['nextPageCursor']
        
        OwnerList = json.loads(response.text)
        OwnerList = OwnerList['data']
        for owner in OwnerList:
            FullList.append(owner['serialNumber'])

        if(NextPage == None):
            IsAll = True


    return FullList
    #return response.json()['nextPageCursor']

#endregion

print(GetSerialList(TestCatalogID))

