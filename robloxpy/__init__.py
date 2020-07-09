import requests,json,time,datetime

#Created and maintained by Kristan Smout
#Github URL = https://github.com/KristanSmout/RobloxPyOfficial

Version = '0.0.97'


APIURL = "https://api.roblox.com/"
SettingsURL = "https://www.roblox.com/my/settings/json"
MobileAPI = "https://www.roblox.com/mobileapi/"
EconomyURL = "https://economy.roblox.com/v1/"
FriendsURL = "https://friends.roblox.com/v1/"
InventoryURL = "https://inventory.roblox.com/v2/assets/"
GamesURL = "https://games.roblox.com/v1/"
RBXCityInventURL = "https://data.rbxcity.com/user-inventories/fetch/history/"
UserAPI = APIURL + "users/"
UserAPIV1 = 'https://users.roblox.com/v1/users/'
GroupAPI = APIURL + "groups/"
GroupAPIV1 = "https://groups.roblox.com/v1/groups/"


#Internal
def CheckForUpdate():
    response = requests.get('https://pypi.org/pypi/robloxpy/json')
    LatestVersion = response.json()['info']['version']
    if(Version == LatestVersion):
        return 'You are up to date!'
    else:
        return f'Version {LatestVersion} is now availible'

def CheckVersion():
    return Version
    
def HowToUpdate():
    return 'pip install robloxpy --upgrade'

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
    IDList = []
    Grouplist = json.loads(response.text)
    for group in Grouplist:
        FullList.append(group['Name'])
        IDList.append(group['Id'])
    return FullList,IDList

def DoesNameExist(UserName):
    response = requests.get(UserAPI + 'get-by-username?username=' + str(UserName))
    if('errorMessage' in response.text):
        return ('Availible')
    else:   
        if(response.json()['Username'].lower() == UserName.lower()):
            return('Unavailible')
        elif (response.json()['Username'].lower() != UserName.lower()):
            return('Availible')

def IsBanned(UserID):
   response = requests.get(UserAPIV1 + str(UserID))
   return response.json()['isBanned']

def UserCreationDate(UserID,WantedData):
    WantedData = WantedData.lower()
    CreationDate = requests.get(UserAPIV1 + str(UserID)).json()['created']
    CreationDate = CreationDate.split('T')
    CreationDate = CreationDate[0].split('-')
    
    if(WantedData == ('year'.lower())):
        return str(CreationDate[0])
    elif(WantedData == 'month'.lower()):
        return str(CreationDate[1])
    elif(WantedData == 'day'.lower()):
        return str(CreationDate[2])
        

def AccountAgeDays(UserID):
    CreationDate = requests.get(UserAPIV1 + str(UserID)).json()['created']
    CreationDate = CreationDate.split('T')
    CreationDate = CreationDate[0].split('-')
    CurrentDate = datetime.date.today()
    CreationDate = datetime.date(int(CreationDate[0]),int(CreationDate[1]),int(CreationDate[2]))
    Days = ((datetime.date.today()) - (CreationDate))
    Days = str(Days).split(' ')
    return Days[0]


#endregion

#region RAP

def GetUserRAP(UserID):
    response = requests.get(RBXCityInventURL + str(UserID))
    for data in response.json()['data']:
        return data['recentAveragePrice']
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

def IsGroupOwned(GroupID):
    response = requests.get(GroupAPIV1 + str(GroupID))
    
    if(str(response.json()['owner']) == 'None'):
        return False
    else:
        return True

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


#region External Place API's

def GetUniverseData(UniverseID):
    response = requests.get(GamesURL + 'games?universeIds=' + str(UniverseID))
    return response.json()['data'][0]

def GetUniverseVotes(UniverseID):
    response = requests.get(GamesURL + 'games/votes?universeIds=' + str(UniverseID))
    return response.json()['data'][0]

def GetUniverseFavourites(UniverseID):
    response = requests.get(GamesURL + 'games/' + str(UniverseID) + '/favorites/count')
    return response.json()['favoritesCount']

def GetCurrentUniversePlayers(UniverseID):
    GameData = GetUniverseData(str(UniverseID))
    return GameData['playing']

def GetUniverseVisits(UniverseID):
    GameData = GetUniverseData(str(UniverseID))
    return GameData['visits']

def GetUniverseLikes(UniverseID):
    GetVotes = GetUniverseVotes(str(UniverseID))
    return GetVotes['upVotes']

def GetUniverseDislikes(UniverseID):
    GetVotes = GetUniverseVotes(str(UniverseID))
    return GetVotes['downVotes']



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
    data = Post.json()
    try:
        return data['success']
    except:
        return data['errors']

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


def SendFriendRequest(Cookie,UserID):
    session = SetCookie(Cookie)
    Post = session.post(FriendsURL + 'users/' + UserID + '/request-friendship',data={'targetUserID': UserID})
    try:
        return Post.json()['success']
    except:
        return Post.json()['errors'][0]['message']

def Unfriend(Cookie,UserID):
    session = SetCookie(Cookie)
    Post = session.post(FriendsURL + 'users/' + UserID + '/unfriend',data={'targetUserID': UserID})
    try:
        return 'Sent'
    except:
        return 'Error'

def TotalFriends(Cookie):
    session = SetCookie(Cookie)
    response = session.get(FriendsURL + 'my/friends/count')
    return response.json()['count']

def SendMessage(Cookie,UserID,MessageSubject,Body):
    session = SetCookie(Cookie)
    Post = session.post('https://www.roblox.com/messages/send',data={
                       'subject': MessageSubject,
                       'body': Body,
                       'recipientid': str(UserID),
                       'cacheBuster': str(int(time.time()))
               })
    return Post

def GetBlockedUsers(Cookie):
    session = SetCookie(Cookie)
    response = session.get(SettingsURL)
    Data = response.json()['BlockedUsersModel']['BlockedUsers']
    BlockedIDs = []
    BlockedNames = []
    
    for User in Data:
        BlockedIDs.append(User['uid'])
        BlockedNames.append(User['Name'])
    return BlockedIDs,BlockedNames

#endregion


#region GroupFunctions

def ClaimGroup(Cookie,GroupID):
    session = SetCookie(Cookie)
    Post = session.post(GroupAPIV1 + str(GroupID) + '/claim-ownership')
    return 'Sent'

def JoinGroup(Cookie,GroupID):
    session = SetCookie(Cookie)
    Post = session.post(GroupAPIV1 + str(GroupID) + '/users')
    return 'Joined'

def LeaveGroup(Cookie,GroupID):
    session = SetCookie(Cookie)
    LocalUserID = GetUserID(Cookie)
    Post = session.delete(GroupAPIV1 + str(GroupID) + '/users/' + str(LocalUserID))
    return 'Left'

def GetFunds(Cookie,GroupID):
    session = SetCookie(Cookie)
    response = session.get(EconomyURL + '/groups/' + str(GroupID) + '/currency')
    return response.json()['robux']

def PayGroupFunds(Cookie,GroupID,UserID,RobuxAmount):
    session = SetCookie(Cookie)
    
    data={
    "PayoutType": "FixedAmount",
    "Recipients": [
    {
        "recipientId": str(UserID),
        "recipientType": "User",
        "amount": str(RobuxAmount)
    }
 ]
}

    Post = session.post(GroupAPIV1 + str(GroupID) + '/payouts',json=data)
    if(Post.status_code == 200):
        return 'Sent'
    else:
        return 'Error'

def PayGroupPercentage(Cookie,GroupID,UserID,Percentage):
    session = SetCookie(Cookie)
    
    data={
    "PayoutType": "Percentage",
    "Recipients": [
    {
        "recipientId": str(UserID),
        "recipientType": "User",
        "amount": str(Percentage)
    }
 ]
}
    Post = session.post(GroupAPIV1 + str(GroupID) + '/payouts',json=data)
    if(Post.status_code == 200):
        return 'Sent'
    else:
        return 'Error'

def PostGroupWall(Cookie,GroupID,Text):
    session = SetCookie(Cookie)
    Post = session.post(GroupAPIV1 + str(GroupID) + '/wall/posts',data={'body': Text})
    return 'Sent'

def ChangeGroupRank(Cookie,GroupID,UserID,roleId):
    session = SetCookie(Cookie)
    Patch = session.patch(GroupAPIV1 + str(GroupID) + '/users/' + str(UserID),data={'roleId' : roleId})
    return 'Sent'

def ChangeGroupShout(Cookie,GroupID,StatusString):
    session = SetCookie(Cookie)
    Patch = session.patch(GroupAPIV1 + str(GroupID) + '/status',data={'message' : StatusString})
    return 'Sent'

def ChangeGroupDescription(Cookie,GroupID,DescriptionString):
    session = SetCookie(Cookie)
    Patch = session.patch(GroupAPIV1 + str(GroupID) + '/description',data={'description' : DescriptionString})
    return 'Sent'



#endregion


#region Internal Place API

def GetUniverseID(Cookie,PlaceID):
    session = SetCookie(Cookie)
    response = session.get(GamesURL + 'games/multiget-place-details?placeIds=' + str(PlaceID))
    return response.json()[0]['universeId']

def GetCurrentGamePlayers(Cookie,PlaceID):
    UniverseID = GetUniverseID(Cookie,PlaceID)
    GameData = GetUniverseData(UniverseID)
    return GameData['playing']

def GetGameVisits(Cookie,PlaceID):
    UniverseID = GetUniverseID(Cookie,PlaceID)
    GameData = GetUniverseData(UniverseID)
    return GameData['visits']

def GetGameLikes(Cookie,PlaceID):
    UniverseID = GetUniverseID(Cookie,PlaceID)
    return GetUniverseVotes(UniverseID)['upVotes']

def GetGameDislikes(Cookie,PlaceID):
    UniverseID = GetUniverseID(Cookie,PlaceID)
    return GetUniverseVotes(UniverseID)['downVotes']

def GetGameFavourites(Cookie,PlaceID):
    UniverseID = GetUniverseID(Cookie,PlaceID)
    response = requests.get(GamesURL + 'games/' + str(UniverseID) + '/favorites/count')
    return response.json()['favoritesCount']
    



#endregion

#endregion

