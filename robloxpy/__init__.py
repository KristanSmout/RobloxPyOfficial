import requests,json,time,datetime

#Created and maintained by Kristan Smout
#Github URL = https://github.com/KristanSmout/RobloxPyOfficial

Version = '0.1.5'


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
PrivateMessageAPIV1 = "https://privatemessages.roblox.com/v1/"


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
    try:
       return response.json()['Id']
    except:
       return response.json()['errorMessage']


def GetName(UserID):
    response = requests.get(UserAPI + str(UserID))
    try:
        return response.json()['Username']
    except:
        return 'User not found'

def IsOnline(UserID):
    response = requests.get(UserAPI + str(UserID))
    try:
        return response.json()['IsOnline']
    except:
        return 'User not found'

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
    try:
        return response.json()['isBanned']
    except:
        return response.json()['errors'][0]['message']

def UserCreationDate(UserID,WantedData):
    WantedData = WantedData.lower()
    response = requests.get(UserAPIV1 + str(UserID))
    try:
        CreationDate = response.json()['created']
        CreationDate = CreationDate.split('T')
        CreationDate = CreationDate[0].split('-')
        
        if(WantedData == ('year'.lower())):
            return str(CreationDate[0])
        elif(WantedData == 'month'.lower()):
            return str(CreationDate[1])
        elif(WantedData == 'day'.lower()):
            return str(CreationDate[2])
    except:
        return response.json()['errors'][0]['message']
        

def AccountAgeDays(UserID):
    response = requests.get(UserAPIV1 + str(UserID))
    try:
        CreationDate = response.json()['created']
        CreationDate = CreationDate.split('T')
        CreationDate = CreationDate[0].split('-')
        CreationDate = datetime.date(int(CreationDate[0]),int(CreationDate[1]),int(CreationDate[2]))
        Days = ((datetime.date.today()) - (CreationDate))
        Days = str(Days).split(' ')
        return Days[0]
    except:
        return response.json()['errors'][0]['message']

def GetFollowingCount(UserID):
    response = requests.get(FriendsURL + 'users/' + str(UserID) + '/followings/count')
    try:
        return response.json()['count']
    except:
        return 'UserID Invalid'

def GetFollowersCount(UserID):
    response = requests.get(FriendsURL + 'users/' + str(UserID) + '/followers/count')
    try:
        return response.json()['count']
    except:
        return response.json()['errors'][0]['message']
    
def GetFollowers(UserID,Ammount):
    response = requests.get(FriendsURL + '/users/' + str(UserID) + '/followers?sortOrder=Asc&limit=100')
    try:
        CurrentAmmount = 0
        NameList = []
        IDList = []
        Cursor = 'None'
        while Cursor !=  'null':
            if(Cursor is None):
                Cursor = 'null'
            else:
                try:
                    Cursor = response.json()['nextPageCursor']
                except:
                    Cursor = 'null'
            for Follower in response.json()['data']:
                if(CurrentAmmount < Ammount):
                    NameList.append(Follower['name'])
                    IDList.append(Follower['id'])
                    CurrentAmmount = CurrentAmmount + 1
                else:
                    return NameList,IDList
            if(Cursor is None):
                Cursor = 'null'
            else:
                try:
                    response = requests.get(FriendsURL + '/users/' + str(UserID) + '/followers?sortOrder=Asc&limit=100&cursor=' + str(Cursor))
                except:
                    Cursor = 'null'
        return NameList,IDList
    except:
        return response.json()['errors'][0]['message']

def GetFollowing(UserID,Ammount):
    response = requests.get(FriendsURL + '/users/' + str(UserID) + '/followings?sortOrder=Asc&limit=100')
    try:
        CurrentAmmount = 0
        NameList = []
        IDList = []
        Cursor = 'None'
        while Cursor !=  'null':
            if(Cursor is None):
                Cursor = 'null'
            else:
                try:
                    Cursor = response.json()['nextPageCursor']
                except:
                    Cursor = 'null'
            for Follower in response.json()['data']:
                if(CurrentAmmount < Ammount):
                    NameList.append(Follower['name'])
                    IDList.append(Follower['id'])
                    CurrentAmmount = CurrentAmmount + 1
                else:
                    return NameList,IDList
            if(Cursor is None):
                Cursor = 'null'
            else:
                try:
                    response = requests.get(FriendsURL + '/users/' + str(UserID) + '/followers?sortOrder=Asc&limit=100&cursor=' + str(Cursor))
                except:
                    Cursor = 'null'
        return NameList,IDList
    except:
        return response.json()['errors'][0]['message']


#endregion

#region RAP

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

def IsGroupOwned(GroupID):
    response = requests.get(GroupAPIV1 + str(GroupID))
    try:
        if(str(response.json()['owner']) == 'None'):
            return False
        else:
            return True
    except:
        return response.json()['errors'][0]['message']


def GetGroupName(GroupID):
    response = requests.get(GroupAPIV1 + str(GroupID))
    try:
        return response.json()['name']
    except:
        return response.json()['errors'][0]['message']

def GetGroupDescription(GroupID):
    response = requests.get(GroupAPIV1 + str(GroupID))
    try:
        return response.json()['description']
    except:
        return response.json()['errors'][0]['message']

def GetGroupShout(GroupID):
    response = requests.get(GroupAPIV1 + str(GroupID))
    try:
        return response.json()['shout']
    except:
        return response.json()['errors'][0]['message']

def IsGroupOpen(GroupID):
    response = requests.get(GroupAPIV1 + str(GroupID))
    try:
        return response.json()['publicEntryAllowed']
    except:
        return response.json()['errors'][0]['message']

def GetGroupMembers(GroupID):
    response = requests.get(GroupAPIV1 + str(GroupID))
    try:
        return response.json()['memberCount']
    except:
        return response.json()['errors'][0]['message']

def GetGroupAllies(GroupID):
    response = requests.get(GroupAPI + str(GroupID) + "/allies")
    try:
        FullList = []
        Grouplist = json.loads(response.text)
        Grouplist = Grouplist['Groups']
        for group in Grouplist:
            FullList.append(group['Name'])
        return FullList
    except:
        return response.json()['errors'][0]['message']

##CONTIUE HERE =======================================================================================

def GetGroupEnemies(GroupID):
    response = requests.get(GroupAPI + str(GroupID) + "/enemies")
    try:
        FullList = []
        Grouplist = json.loads(response.text)
        Grouplist = Grouplist['Groups']
        for group in Grouplist:
            FullList.append(group['Name'])
        return FullList
    except:
        return response.json()['errors'][0]['message']
#endregion

#region External Asset API's

def CanManage(UserID,AssetID):
    response = requests.get(UserAPI + str(UserID) + '/canmanage/' + str(AssetID))
    try:
        return response.json()['CanManage']
    except:
        return response.json()['ErrorMessage']

def GetSerialList(AssetID):
    IsAll = False
    FullList = []
    Owners = []
    NextPage = 'N/A'
    try:
        try:
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
                    Owners.append(owner['id'])

                if(NextPage == None):
                    IsAll = True
        except:
            return response.json()['errors'][0]['message']


        return FullList,Owners
    except:
        return response.json()['errors'][0]['message']


#endregion


#region External Place API's

def GetUniverseData(UniverseID):
    response = requests.get(GamesURL + 'games?universeIds=' + str(UniverseID))
    try:
        return response.json()['data'][0]
    except:
        return 'Universe Not Found'

def GetUniverseVotes(UniverseID):
    response = requests.get(GamesURL + 'games/votes?universeIds=' + str(UniverseID))
    try:
        return response.json()['data'][0]
    except:
        return 'Universe Not Found'

def GetUniverseFavourites(UniverseID):
    response = requests.get(GamesURL + 'games/' + str(UniverseID) + '/favorites/count')
    try:
        return response.json()['favoritesCount']
    except:
        return 'Universe Not Found'

def GetCurrentUniversePlayers(UniverseID):
    GameData = GetUniverseData(str(UniverseID))
    try:
        return GameData['playing']
    except:
        return 'Universe Not Found'

def GetUniverseVisits(UniverseID):
    GameData = GetUniverseData(str(UniverseID))
    try:
        return GameData['visits']
    except:
        return 'Universe Not Found'

def GetUniverseLikes(UniverseID):
    GetVotes = GetUniverseVotes(str(UniverseID))
    try:
        return GetVotes['upVotes']
    except:
        return 'Universe Not Found'

def GetUniverseDislikes(UniverseID):
    GetVotes = GetUniverseVotes(str(UniverseID))
    try:
        return GetVotes['downVotes']
    except:
        return 'Universe Not Found'


#endregion

#endregion


#region Internal

#region UserFunctions
def SetCookie(Cookie):
    try:
        session = requests.session()
        CurrentCookie = {'.ROBLOSECURITY': Cookie}
        requests.utils.add_dict_to_cookiejar(session.cookies, CurrentCookie)
        
        Header = session.post('https://www.roblox.com/api/item.ashx?')
        session.headers['X-CSRF-TOKEN'] = Header.headers['X-CSRF-TOKEN']
        return session
    except:
        return CheckCookie(Cookie)

def CheckCookie(Cookie):
    session = SetCookie(Cookie)
    response = session.get(MobileAPI + 'userinfo')
    try:
        Temp = response.json()['UserID']
        return "Valid Cookie"
    except:
        return "Invalid Cookie"


def GetUserInfo(Cookie):
    session = SetCookie(Cookie)
    try:
        Info = session.get('http://www.roblox.com/mobileapi/userinfo').json()
        return Info
    except:
        return CheckCookie(Cookie)


def GetUserID(Cookie):
    session = SetCookie(Cookie)
    try:
        response = session.get(MobileAPI + 'userinfo')
        return response.json()['UserID']
    except:
        return CheckCookie(Cookie)

def GetUserName(Cookie):
    session = SetCookie(Cookie)
    try:
        response = session.get(MobileAPI + 'userinfo')
        return response.json()['UserName']
    except:
        return CheckCookie(Cookie)

def GetEmail(Cookie):
    session = SetCookie(Cookie)
    try:
        response = session.get(SettingsURL)
        return response.json()['UserEmail']
    except:
        return CheckCookie(Cookie)

def IsEmailedVerified(Cookie):
    try:
        session = SetCookie(Cookie)
        response = session.get(SettingsURL)
        return response.json()['UserEmailVerified']
    except:
        return CheckCookie(Cookie)

def CanTrade(Cookie):
    try:
        session = SetCookie(Cookie)
        response = session.get(SettingsURL)
        return response.json()['CanTrade']
    except:
        return CheckCookie(Cookie)

def IsOver13(Cookie):
    try:
        session = SetCookie(Cookie)
        response = session.get(SettingsURL)
        return response.json()['UserAbove13']
    except:
        return CheckCookie(Cookie)

def IsTwoStepEnabled(Cookie):
    try:
        session = SetCookie(Cookie)
        response = session.get(SettingsURL)
        return response.json()['IsTwoStepEnabled']
    except:
        return CheckCookie(Cookie)

def IsAccountPinEnabled(Cookie):
    try:
        session = SetCookie(Cookie)
        response = session.get(SettingsURL)
        return response.json()['IsAccountPinEnabled']
    except:
        return CheckCookie(Cookie)

def GetRobux(Cookie):
    try:
        session = SetCookie(Cookie)
        response = session.get(MobileAPI + 'userinfo')
        return response.json()['RobuxBalance']
    except:
        return CheckCookie(Cookie)

def IsPremium(Cookie):
    try:
        session = SetCookie(Cookie)
        response = session.get(MobileAPI + 'userinfo')
        return response.json()['IsPremium']
    except:
        return CheckCookie(Cookie)

def GetAvatar(Cookie):
    try:
        session = SetCookie(Cookie)
        response = session.get(MobileAPI + 'userinfo')
        return response.json()['ThumbnailUrl']
    except:
        return CheckCookie(Cookie)

def IsFollowing(Cookie,UserID):
    try:
        session = SetCookie(Cookie)
        response = session.get(APIURL + 'user/following-exists?UserID=' + str(UserID) + '&followerUserID=' + str(GetUserID(Cookie)),data={'targetUserID': UserID})
        return response.json()['isFollowing']
    except:
        return "Error: ",CheckCookie(Cookie)

def FollowUser(Cookie,UserID):
    try:
        session = SetCookie(Cookie)
        Post = session.post('https://friends.roblox.com/v1/users/' + str(UserID) + '/follow',data={'targetUserID': UserID})
        data = Post.json()
        try:
            return data['success']
        except:
            return data['errors']
    except:
        return CheckCookie(Cookie)

def UnfollowUser(Cookie,UserID):
    try:
        session = SetCookie(Cookie)
        Post = session.post('https://friends.roblox.com/v1/users/' + str(UserID) + '/unfollow',data={'targetUserID': UserID})
        try:
            return Post.json()['success']
        except:
            return 'Error: ',CheckCookie(Cookie)
    except:
        return CheckCookie(Cookie)

def BlockUser(Cookie,UserID): #Not Working Unsure Why
    try:
        session = SetCookie(Cookie)
        Post = session.post('http://api.roblox.com/userblock/block?userId=' + str(UserID),data={'targetUserID': UserID})
        return Post.json()['success']
    except:
        return 'Error: ',CheckCookie(Cookie)

def UnblockUser(Cookie,UserID):
    try:
        session = SetCookie(Cookie)
        Post = session.post('http://api.roblox.com/userblock/unblock?userId=' + str(UserID),data={'targetUserID': UserID})
        return Post.json()['success']
    except:
        return 'Error: ',CheckCookie(Cookie)


def SendFriendRequest(Cookie,UserID):
    try:
        session = SetCookie(Cookie)
        Post = session.post(FriendsURL + 'users/' + UserID + '/request-friendship',data={'targetUserID': UserID})
        try:
            return Post.json()['success']
        except:
            return Post.json()['errors'][0]['message']
    except:
        return 'Error: ',CheckCookie(Cookie)

def Unfriend(Cookie,UserID):
    try:
        session = SetCookie(Cookie)
        Post = session.post(FriendsURL + 'users/' + UserID + '/unfriend',data={'targetUserID': UserID})
        try:
            return 'Sent'
        except:
            return 'Error: ',CheckCookie(Cookie)
    except:
        return 'Error: ',CheckCookie(Cookie)

def TotalFriends(Cookie):
    try:
        session = SetCookie(Cookie)
        response = session.get(FriendsURL + 'my/friends/count')
        return response.json()['count']
    except:
        return 'Error: ',CheckCookie(Cookie)

def SendMessage(Cookie,UserID,MessageSubject,Body): #Credit to Soul for documentation URL
    try:
        LocalID = GetUserID(Cookie)
        session = SetCookie(Cookie)
        Post = session.post(PrivateMessageAPIV1 + 'messages/send/' ,data={
                            'userId' : LocalID,
                            'subject': MessageSubject,
                            'body': Body,
                            'recipientid': UserID,
                })
        return Post.json()['shortMessage']
    except:
        return 'Error: ',CheckCookie(Cookie)
    

def GetBlockedUsers(Cookie):
    try:
        session = SetCookie(Cookie)
        response = session.get(SettingsURL)
        Data = response.json()['BlockedUsersModel']['BlockedUsers']
        BlockedIDs = []
        BlockedNames = []
        
        for User in Data:
            BlockedIDs.append(User['uid'])
            BlockedNames.append(User['Name'])
        return BlockedIDs,BlockedNames
    except:
        return 'Error: ',CheckCookie(Cookie)

#endregion


#region GroupFunctions

def ClaimGroup(Cookie,GroupID):
    try:
        session = SetCookie(Cookie)
        Post = session.post(GroupAPIV1 + str(GroupID) + '/claim-ownership')
        return 'Sent'
    except:
        return 'Error: ',CheckCookie(Cookie)

def JoinGroup(Cookie,GroupID):
    try:
        session = SetCookie(Cookie)
        Post = session.post(GroupAPIV1 + str(GroupID) + '/users')
        return 'Joined'
    except:
        return 'Error: ',CheckCookie(Cookie)

def LeaveGroup(Cookie,GroupID):
    try:
        session = SetCookie(Cookie)
        LocalUserID = GetUserID(Cookie)
        Post = session.delete(GroupAPIV1 + str(GroupID) + '/users/' + str(LocalUserID))
        return 'Left'
    except:
        return 'Error: ',CheckCookie(Cookie)

def GetFunds(Cookie,GroupID):
    try:
        session = SetCookie(Cookie)
        response = session.get(EconomyURL + '/groups/' + str(GroupID) + '/currency')
        return response.json()['robux']
    except:
        return 'Error: ',CheckCookie(Cookie)

def PayGroupFunds(Cookie,GroupID,UserID,RobuxAmount):
    try:
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
            return 'Error: ',CheckCookie(Cookie)
    except:
        return 'Error: ',CheckCookie(Cookie)

def PayGroupPercentage(Cookie,GroupID,UserID,Percentage):
    try:
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
            return 'Error: ',CheckCookie(Cookie)
    except:
        return 'Error: ',CheckCookie(Cookie)

def PostGroupWall(Cookie,GroupID,Text):
    try:
        session = SetCookie(Cookie)
        Post = session.post(GroupAPIV1 + str(GroupID) + '/wall/posts',data={'body': Text})
        return 'Sent'
    except:
        return 'Error: ',CheckCookie(Cookie)

def ChangeGroupRank(Cookie,GroupID,UserID,roleId):
    try:
        session = SetCookie(Cookie)
        Patch = session.patch(GroupAPIV1 + str(GroupID) + '/users/' + str(UserID),data={'roleId' : roleId})
        return 'Sent'
    except:
        return 'Error: ',CheckCookie(Cookie)

def ChangeGroupShout(Cookie,GroupID,StatusString):
    try:
        session = SetCookie(Cookie)
        Patch = session.patch(GroupAPIV1 + str(GroupID) + '/status',data={'message' : StatusString})
        return 'Sent'
    except:
        return 'Error: ',CheckCookie(Cookie)

def ChangeGroupDescription(Cookie,GroupID,DescriptionString):
    try:
        session = SetCookie(Cookie)
        Patch = session.patch(GroupAPIV1 + str(GroupID) + '/description',data={'description' : DescriptionString})
        return 'Sent'
    except:
        return 'Error: ',CheckCookie(Cookie)



#endregion


#region Internal Place API

def GetUniverseID(Cookie,PlaceID):
    try:
        session = SetCookie(Cookie)
        response = session.get(GamesURL + 'games/multiget-place-details?placeIds=' + str(PlaceID))
        return response.json()[0]['universeId']
    except:
        return 'Error: ',CheckCookie(Cookie)

def GetCurrentGamePlayers(Cookie,PlaceID):
    try:
        UniverseID = GetUniverseID(Cookie,PlaceID)
        GameData = GetUniverseData(UniverseID)
        return GameData['playing']
    except:
        return 'Error: ',CheckCookie(Cookie)

def GetGameVisits(Cookie,PlaceID):
    try:
        UniverseID = GetUniverseID(Cookie,PlaceID)
        GameData = GetUniverseData(UniverseID)
        return GameData['visits']
    except:
        return 'Error: ',CheckCookie(Cookie)

def GetGameLikes(Cookie,PlaceID):
    try:
        UniverseID = GetUniverseID(Cookie,PlaceID)
        return GetUniverseVotes(UniverseID)['upVotes']
    except:
        return 'Error: ',CheckCookie(Cookie)

def GetGameDislikes(Cookie,PlaceID):
    try:
        UniverseID = GetUniverseID(Cookie,PlaceID)
        return GetUniverseVotes(UniverseID)['downVotes']
    except:
        return 'Error: ',CheckCookie(Cookie)

def GetGameFavourites(Cookie,PlaceID):
    try:
        UniverseID = GetUniverseID(Cookie,PlaceID)
        response = requests.get(GamesURL + 'games/' + str(UniverseID) + '/favorites/count')
        return response.json()['favoritesCount']
    except:
        return 'Error: ',CheckCookie(Cookie)


#endregion

#endregion

