import requests
import json


APIURL = "https://api.roblox.com/"
SettingsURL = "https://www.roblox.com/my/settings/json"
MobileAPI = "https://www.roblox.com/mobileapi/"
EconomyURL = "https://economy.roblox.com/v1/"
InventoryURL = "https://inventory.roblox.com/v2/assets/"
RBXCityInventURL = "https://data.rbxcity.com/user-inventories/fetch/history/"
UserAPI = APIURL + "users/"
GroupAPI = APIURL + "groups/"
GroupAPIV1 = "https://groups.roblox.com/v1/groups/"
TestUserID = 1368140
TestGroupID = 916576
TestAssetID = 240351460
TestCatalogID = 16641274

f = open("Cookie.txt","r")
TestCookie =  f.read()


#region External

#region External User API's

def NameToID(UserName):
     response = requests.get(UserAPI + 'get-by-username?username=' + str(UserName))
     return response.json()['Id']

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
        print(data)
        return 'Test'
        #return data['recentAveragePrice']

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

#endregion


#region Internal

#region UserFunctions
def SetCookie(Cookie):
    session = requests.session()
    CurrentCookie = {'.ROBLOSECURITY': Cookie}
    requests.utils.add_dict_to_cookiejar(session.cookies, CurrentCookie)
    
    Header = session.post('https://www.roblox.com/api/item.ashx?')
    session.headers['X-CSRF-TOKEN'] = Header.headers['X-CSRF-TOKEN']
    return session

def GetUserInfo(cookie):
    session = SetCookie(cookie)
    Info = session.get('http://www.roblox.com/mobileapi/userinfo').json()
    return Info

def GetUserID(Cookie):
    session = SetCookie(Cookie)
    response = session.get(MobileAPI + 'userinfo')
    return response.json()['UserID']

def GetUserName(Cookie):
    session = SetCookie(Cookie)
    response = session.get(MobileAPI + 'userinfo')
    return response.json()['UserName']

def GetEmail(Cookie):
    session = SetCookie(Cookie)
    response = session.get(SettingsURL)
    return response.json()['UserEmail']

def IsEmailedVerified(Cookie):
    session = SetCookie(Cookie)
    response = session.get(SettingsURL)
    return response.json()['UserEmailVerified']

def CanTrade(Cookie):
    session = SetCookie(Cookie)
    response = session.get(SettingsURL)
    return response.json()['CanTrade']

def IsOver13(Cookie):
    session = SetCookie(Cookie)
    response = session.get(SettingsURL)
    return response.json()['UserAbove13']

def IsTwoStepEnabled(Cookie):
    session = SetCookie(Cookie)
    response = session.get(SettingsURL)
    return response.json()['IsTwoStepEnabled']

def IsAccountPinEnabled(Cookie):
    session = SetCookie(Cookie)
    response = session.get(SettingsURL)
    return response.json()['IsAccountPinEnabled']

def GetRobux(Cookie):
    session = SetCookie(Cookie)
    response = session.get(MobileAPI + 'userinfo')
    return response.json()['RobuxBalance']

def IsPremium(Cookie):
    session = SetCookie(Cookie)
    response = session.get(MobileAPI + 'userinfo')
    return response.json()['IsPremium']

def GetAvatar(Cookie):
    session = SetCookie(Cookie)
    response = session.get(MobileAPI + 'userinfo')
    return response.json()['ThumbnailUrl']

def IsFollowing(Cookie,UserID):
    session = SetCookie(Cookie)
    response = session.get(APIURL + 'user/following-exists?UserID=' + str(UserID) + '&followerUserID=' + str(GetUserID(Cookie)),data={'targetUserID': UserID})
    return response.json()['isFollowing']

def FollowUser(Cookie,UserID):
    session = SetCookie(Cookie)
    Post = session.post('https://friends.roblox.com/v1/users/' + str(UserID) + '/follow',data={'targetUserID': UserID})
    return Post.json()['success']

def UnfollowUser(Cookie,UserID):
    session = SetCookie(Cookie)
    Post = session.post('https://friends.roblox.com/v1/users/' + str(UserID) + '/unfollow',data={'targetUserID': UserID})
    return Post.json()['success']

def BlockUser(Cookie,UserID): #Not Working Unsure Why
    session = SetCookie(Cookie)
    Post = session.post('http://api.roblox.com/userblock/block?userId=' + str(UserID),data={'targetUserID': UserID})
    return Post.json()['success']

def UnblockUser(Cookie,UserID):
    session = SetCookie(Cookie)
    Post = session.post('http://api.roblox.com/userblock/unblock?userId=' + str(UserID),data={'targetUserID': UserID})
    return Post.json()['success']

#endregion

#region GroupFunctions

def JoinGroup(Cookie,GroupID):
    session = SetCookie(Cookie)
    Post = session.post(GroupAPIV1 + str(GroupID) + '/users')
    return Post.text

def GetFunds(Cookie,GroupID):
    session = SetCookie(Cookie)
    response = session.get(EconomyURL + '/groups/' + str(GroupID) + '/currency')
    return response.json()['robux']

def PostGroupWall(Cookie,GroupID,Text):
    session = SetCookie(Cookie)
    Post = session.post(GroupAPIV1 + str(GroupID) + '/wall/posts',data={'body': Text})
    return 'Sent'

#endregion

#endregion

print(JoinGroup(TestCookie,TestGroupID))