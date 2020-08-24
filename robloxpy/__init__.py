import requests
import json
import time
import datetime
import os

# Created and maintained by Kristan Smout
# Github URL = https://github.com/KristanSmout/RobloxPyOfficial

Version = '0.1.6'


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


# Internal
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


def SetProxy(ProxyIP):
    if(ProxyIP != None):
        proxy = 'http://' + str(ProxyIP)
        os.environ['http_proxy'] = proxy
        os.environ['https_proxy'] = proxy



def CheckProxy(proxyAddress=None):
    SetProxy(proxyAddress)
    response = requests.get('https://api.ipify.org/?format=json')
    return response.json()['ip']

#print(CheckProxy())
#print(CheckProxy('144.217.101.245:3129'))

# region External

# region External User API's


def NameToID(UserName, Proxy=None):
    SetProxy(Proxy)
    response = requests.get(
        UserAPI + 'get-by-username?username=' + str(UserName))
    try:
        return response.json()['Id']
    except:
        return response.json()['errorMessage']


def GetName(UserID, Proxy=None):
    SetProxy(Proxy)
    response = requests.get(UserAPI + str(UserID))
    try:
        return response.json()['Username']
    except:
        return 'User not found'


def IsOnline(UserID, Proxy=None):
    SetProxy(Proxy)
    response = requests.get(UserAPI + str(UserID))
    try:
        return response.json()['IsOnline']
    except:
        return 'User not found'


def GetFriends(UserID, Proxy=None):
    SetProxy(Proxy)
    FullList = []
    response = requests.get(UserAPI + str(UserID) + "/friends")
    Friendslist = json.loads(response.text)
    for friend in Friendslist:
        FullList.append(friend['Username'])
    return FullList


def GetOnlineFriends(UserID, Proxy=None):
    SetProxy(Proxy)
    FullList = []
    response = requests.get(UserAPI + str(UserID) + "/friends")
    Friendslist = json.loads(response.text)
    for friend in Friendslist:
        if(str(friend['IsOnline']) in 'True'):
            FullList.append(friend['Username'])
    return FullList


def GetOfflineFriends(UserID, Proxy=None):
    SetProxy(Proxy)
    FullList = []
    response = requests.get(UserAPI + str(UserID) + "/friends")
    Friendslist = json.loads(response.text)
    for friend in Friendslist:
        if(str(friend['IsOnline']) in 'False'):
            FullList.append(friend['Username'])
    return FullList


def GetUserGroups(UserID, Proxy=None):
    SetProxy(Proxy)
    response = requests.get(UserAPI + str(UserID) + "/groups")
    FullList = []
    IDList = []
    Grouplist = json.loads(response.text)
    for group in Grouplist:
        FullList.append(group['Name'])
        IDList.append(group['Id'])
    return FullList, IDList


def DoesNameExist(UserName, Proxy=None):
    SetProxy(Proxy)
    response = requests.get(
        UserAPI + 'get-by-username?username=' + str(UserName))
    if('errorMessage' in response.text):
        return ('Availible')
    else:
        if(response.json()['Username'].lower() == UserName.lower()):
            return('Unavailible')
        elif (response.json()['Username'].lower() != UserName.lower()):
            return('Availible')


def IsBanned(UserID, Proxy=None):
    SetProxy(Proxy)
    response = requests.get(UserAPIV1 + str(UserID))
    try:
        return response.json()['isBanned']
    except:
        return response.json()['errors'][0]['message']


def UserCreationDate(UserID, WantedData, Proxy=None):
    SetProxy(Proxy)
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


def AccountAgeDays(UserID, Proxy=None):
    SetProxy(Proxy)
    response = requests.get(UserAPIV1 + str(UserID))
    try:
        CreationDate = response.json()['created']
        CreationDate = CreationDate.split('T')
        CreationDate = CreationDate[0].split('-')
        CreationDate = datetime.date(int(CreationDate[0]), int(
            CreationDate[1]), int(CreationDate[2]))
        Days = ((datetime.date.today()) - (CreationDate))
        Days = str(Days).split(' ')
        return Days[0]
    except:
        return response.json()['errors'][0]['message']


def GetFollowingCount(UserID, Proxy=None):
    SetProxy(Proxy)
    response = requests.get(FriendsURL + 'users/' +
                            str(UserID) + '/followings/count')
    try:
        return response.json()['count']
    except:
        return 'UserID Invalid'


def GetFollowersCount(UserID, Proxy=None):
    SetProxy(Proxy)
    response = requests.get(FriendsURL + 'users/' +
                            str(UserID) + '/followers/count')
    try:
        return response.json()['count']
    except:
        return response.json()['errors'][0]['message']


def GetFollowers(UserID, Ammount, Proxy=None):
    SetProxy(Proxy)
    response = requests.get(FriendsURL + '/users/' +
                            str(UserID) + '/followers?sortOrder=Asc&limit=100')
    try:
        CurrentAmmount = 0
        NameList = []
        IDList = []
        Cursor = 'None'
        while Cursor != 'null':
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
                    return NameList, IDList
            if(Cursor is None):
                Cursor = 'null'
            else:
                try:
                    response = requests.get(FriendsURL + '/users/' + str(
                        UserID) + '/followers?sortOrder=Asc&limit=100&cursor=' + str(Cursor))
                except:
                    Cursor = 'null'
        return NameList, IDList
    except:
        return response.json()['errors'][0]['message']


def GetFollowing(UserID, Ammount, Proxy=None):
    SetProxy(Proxy)
    response = requests.get(FriendsURL + '/users/' +
                            str(UserID) + '/followings?sortOrder=Asc&limit=100')
    try:
        CurrentAmmount = 0
        NameList = []
        IDList = []
        Cursor = 'None'
        while Cursor != 'null':
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
                    return NameList, IDList
            if(Cursor is None):
                Cursor = 'null'
            else:
                try:
                    response = requests.get(FriendsURL + '/users/' + str(
                        UserID) + '/followers?sortOrder=Asc&limit=100&cursor=' + str(Cursor))
                except:
                    Cursor = 'null'
        return NameList, IDList
    except:
        return response.json()['errors'][0]['message']


# endregion

# region RAP

def GetUserRAP(UserID, Proxy=None):
    SetProxy(Proxy)
    response = requests.get(RBXCityInventURL + str(UserID))
    for data in response.json()['data']:
        return data['recentAveragePrice']


def GetUserLimitedValue(UserID, Proxy=None):
    SetProxy(Proxy)
    response = requests.get(RBXCityInventURL + str(UserID))
    for data in response.json()['data']:
        return data['value']


def GetUserNoDemandLimiteds(UserID, Proxy=None):
    SetProxy(Proxy)
    response = requests.get(RBXCityInventURL + str(UserID))
    for data in response.json()['data']:
        return data['LowDemandItems']


def GetUserNormalDemandLimiteds(UserID, Proxy=None):
    SetProxy(Proxy)
    response = requests.get(RBXCityInventURL + str(UserID))
    for data in response.json()['data']:
        return data['NormalDemandItems']


def GetUserGoodDemandLimiteds(UserID, Proxy=None):
    SetProxy(Proxy)
    response = requests.get(RBXCityInventURL + str(UserID))
    for data in response.json()['data']:
        return data['GoodDemandItems']


def GetUserAmazingDemandLimiteds(UserID, Proxy=None):
    SetProxy(Proxy)
    response = requests.get(RBXCityInventURL + str(UserID))
    for data in response.json()['data']:
        return data['AmazingDemandItems']


def GetUserTerribleDemandLimiteds(UserID, Proxy=None):
    SetProxy(Proxy)
    response = requests.get(RBXCityInventURL + str(UserID))
    for data in response.json()['data']:
        return data['TerribleDemandItems']


# endregion

# region External Group API's

def IsGroupOwned(GroupID, Proxy=None):
    SetProxy(Proxy)
    response = requests.get(GroupAPIV1 + str(GroupID))
    try:
        if(str(response.json()['owner']) == 'None'):
            return False
        else:
            return True
    except:
        return response.json()['errors'][0]['message']


def GetGroupName(GroupID, Proxy=None):
    SetProxy(Proxy)
    response = requests.get(GroupAPIV1 + str(GroupID))
    try:
        return response.json()['name']
    except:
        return response.json()['errors'][0]['message']


def GetGroupDescription(GroupID, Proxy=None):
    SetProxy(Proxy)
    response = requests.get(GroupAPIV1 + str(GroupID))
    try:
        return response.json()['description']
    except:
        return response.json()['errors'][0]['message']


def GetGroupShout(GroupID, Proxy=None):
    SetProxy(Proxy)
    response = requests.get(GroupAPIV1 + str(GroupID))
    try:
        return response.json()['shout']
    except:
        return response.json()['errors'][0]['message']


def IsGroupOpen(GroupID, Proxy=None):
    SetProxy(Proxy)
    response = requests.get(GroupAPIV1 + str(GroupID))
    try:
        return response.json()['publicEntryAllowed']
    except:
        return response.json()['errors'][0]['message']


def GetGroupMembers(GroupID, Proxy=None):
    SetProxy(Proxy)
    response = requests.get(GroupAPIV1 + str(GroupID))
    try:
        return response.json()['memberCount']
    except:
        return response.json()['errors'][0]['message']


def GetGroupAllies(GroupID, Proxy=None):
    SetProxy(Proxy)
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

# CONTIUE HERE =======================================================================================


def GetGroupEnemies(GroupID, Proxy=None):
    SetProxy(Proxy)
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
# endregion

# region External Asset API's


def CanManage(UserID, AssetID, Proxy=None):
    SetProxy(Proxy)
    response = requests.get(UserAPI + str(UserID) +
                            '/canmanage/' + str(AssetID))
    try:
        return response.json()['CanManage']
    except:
        return response.json()['ErrorMessage']


def GetSerialList(AssetID, Proxy=None):
    SetProxy(Proxy)
    IsAll = False
    FullList = []
    Owners = []
    NextPage = 'N/A'
    try:
        try:
            while (IsAll == False):
                if(NextPage == 'N/A'):
                    response = requests.get(
                        InventoryURL + str(AssetID) + '/owners')
                    NextPage = response.json()['nextPageCursor']
                elif(NextPage == 'Done'):
                    IsAll = True
                else:
                    response = requests.get(
                        InventoryURL + str(AssetID) + '/owners?&cursor=' + NextPage)
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

        return FullList, Owners
    except:
        return response.json()['errors'][0]['message']


# endregion


# region External Place API's

def GetUniverseData(UniverseID, Proxy=None):
    SetProxy(Proxy)
    response = requests.get(GamesURL + 'games?universeIds=' + str(UniverseID))
    try:
        return response.json()['data'][0]
    except:
        return 'Universe Not Found'


def GetUniverseVotes(UniverseID, Proxy=None):
    SetProxy(Proxy)
    response = requests.get(
        GamesURL + 'games/votes?universeIds=' + str(UniverseID))
    try:
        return response.json()['data'][0]
    except:
        return 'Universe Not Found'


def GetUniverseFavourites(UniverseID, Proxy=None):
    SetProxy(Proxy)
    response = requests.get(GamesURL + 'games/' +
                            str(UniverseID) + '/favorites/count')
    try:
        return response.json()['favoritesCount']
    except:
        return 'Universe Not Found'


def GetCurrentUniversePlayers(UniverseID, Proxy=None):
    SetProxy(Proxy)
    GameData = GetUniverseData(str(UniverseID))
    try:
        return GameData['playing']
    except:
        return 'Universe Not Found'


def GetUniverseVisits(UniverseID, Proxy=None):
    SetProxy(Proxy)
    GameData = GetUniverseData(str(UniverseID))
    try:
        return GameData['visits']
    except:
        return 'Universe Not Found'


def GetUniverseLikes(UniverseID, Proxy=None):
    SetProxy(Proxy)
    GetVotes = GetUniverseVotes(str(UniverseID))
    try:
        return GetVotes['upVotes']
    except:
        return 'Universe Not Found'


def GetUniverseDislikes(UniverseID, Proxy=None):
    SetProxy(Proxy)
    GetVotes = GetUniverseVotes(str(UniverseID))
    try:
        return GetVotes['downVotes']
    except:
        return 'Universe Not Found'


# endregion

# endregion


# region Internal

# region UserFunctions
def SetCookie(Cookie, Proxy=None):
    SetProxy(Proxy)
    try:
        session = requests.session()
        CurrentCookie = {'.ROBLOSECURITY': Cookie}
        requests.utils.add_dict_to_cookiejar(session.cookies, CurrentCookie)

        Header = session.post('https://www.roblox.com/api/item.ashx?')
        session.headers['X-CSRF-TOKEN'] = Header.headers['X-CSRF-TOKEN']
        return session
    except:
        return CheckCookie(Cookie)


def CheckCookie(Cookie, Proxy=None):
    session = SetCookie(Cookie,Proxy)
    response = session.get(MobileAPI + 'userinfo')
    try:
        Temp = response.json()['UserID']
        return "Valid Cookie"
    except:
        return "Invalid Cookie"


def GetUserInfo(Cookie, Proxy=None):
    session = SetCookie(Cookie,Proxy)
    try:
        Info = session.get('http://www.roblox.com/mobileapi/userinfo').json()
        return Info
    except:
        return CheckCookie(Cookie)


def GetUserID(Cookie, Proxy=None):
    session = SetCookie(Cookie,Proxy)
    try:
        response = session.get(MobileAPI + 'userinfo')
        return response.json()['UserID']
    except:
        return CheckCookie(Cookie)


def GetUserName(Cookie, Proxy=None):
    session = SetCookie(Cookie,Proxy)
    try:
        response = session.get(MobileAPI + 'userinfo')
        return response.json()['UserName']
    except:
        return CheckCookie(Cookie)


def GetEmail(Cookie, Proxy=None):
    session = SetCookie(Cookie,Proxy)
    try:
        response = session.get(SettingsURL)
        return response.json()['UserEmail']
    except:
        return CheckCookie(Cookie)


def IsEmailedVerified(Cookie, Proxy=None):
    try:
        session = SetCookie(Cookie,Proxy)
        response = session.get(SettingsURL)
        return response.json()['UserEmailVerified']
    except:
        return CheckCookie(Cookie)


def CanTrade(Cookie, Proxy=None):
    try:
        session = SetCookie(Cookie,Proxy)
        response = session.get(SettingsURL)
        return response.json()['CanTrade']
    except:
        return CheckCookie(Cookie)


def IsOver13(Cookie, Proxy=None):
    try:
        session = SetCookie(Cookie,Proxy)
        response = session.get(SettingsURL)
        return response.json()['UserAbove13']
    except:
        return CheckCookie(Cookie)


def IsTwoStepEnabled(Cookie, Proxy=None):
    try:
        session = SetCookie(Cookie,Proxy)
        response = session.get(SettingsURL)
        return response.json()['IsTwoStepEnabled']
    except:
        return CheckCookie(Cookie)


def IsAccountPinEnabled(Cookie, Proxy=None):
    try:
        session = SetCookie(Cookie,Proxy)
        response = session.get(SettingsURL)
        return response.json()['IsAccountPinEnabled']
    except:
        return CheckCookie(Cookie)


def GetRobux(Cookie, Proxy=None):
    try:
        session = SetCookie(Cookie,Proxy)
        response = session.get(MobileAPI + 'userinfo')
        return response.json()['RobuxBalance']
    except:
        return CheckCookie(Cookie)


def IsPremium(Cookie, Proxy=None):
    try:
        session = SetCookie(Cookie,Proxy)
        response = session.get(MobileAPI + 'userinfo')
        return response.json()['IsPremium']
    except:
        return CheckCookie(Cookie)


def GetAvatar(Cookie, Proxy=None):
    try:
        session = SetCookie(Cookie,Proxy)
        response = session.get(MobileAPI + 'userinfo')
        return response.json()['ThumbnailUrl']
    except:
        return CheckCookie(Cookie)


def IsFollowing(Cookie, UserID, Proxy=None):
    try:
        session = SetCookie(Cookie,Proxy)
        response = session.get(APIURL + 'user/following-exists?UserID=' + str(
            UserID) + '&followerUserID=' + str(GetUserID(Cookie)), data={'targetUserID': UserID})
        return response.json()['isFollowing']
    except:
        return "Error: ", CheckCookie(Cookie)


def FollowUser(Cookie, UserID, Proxy=None):
    try:
        session = SetCookie(Cookie,Proxy)
        Post = session.post('https://friends.roblox.com/v1/users/' +
                            str(UserID) + '/follow', data={'targetUserID': UserID})
        data = Post.json()
        try:
            return data['success']
        except:
            return data['errors']
    except:
        return CheckCookie(Cookie)


def UnfollowUser(Cookie, UserID, Proxy=None):
    try:
        session = SetCookie(Cookie,Proxy)
        Post = session.post('https://friends.roblox.com/v1/users/' +
                            str(UserID) + '/unfollow', data={'targetUserID': UserID})
        try:
            return Post.json()['success']
        except:
            return 'Error: ', CheckCookie(Cookie)
    except:
        return CheckCookie(Cookie)


def BlockUser(Cookie, UserID, Proxy=None):  # Not Working Unsure Why
    try:
        session = SetCookie(Cookie,Proxy)
        Post = session.post('http://api.roblox.com/userblock/block?userId=' +
                            str(UserID), data={'targetUserID': UserID})
        return Post.json()['success']
    except:
        return 'Error: ', CheckCookie(Cookie)


def UnblockUser(Cookie, UserID, Proxy=None):
    try:
        session = SetCookie(Cookie,Proxy)
        Post = session.post('http://api.roblox.com/userblock/unblock?userId=' +
                            str(UserID), data={'targetUserID': UserID})
        return Post.json()['success']
    except:
        return 'Error: ', CheckCookie(Cookie)


def SendFriendRequest(Cookie, UserID, Proxy=None):
    try:
        session = SetCookie(Cookie,Proxy)
        Post = session.post(FriendsURL + 'users/' + UserID +
                            '/request-friendship', data={'targetUserID': UserID})
        try:
            return Post.json()['success']
        except:
            return Post.json()['errors'][0]['message']
    except:
        return 'Error: ', CheckCookie(Cookie)


def Unfriend(Cookie, UserID, Proxy=None):
    try:
        session = SetCookie(Cookie,Proxy)
        Post = session.post(FriendsURL + 'users/' + UserID +
                            '/unfriend', data={'targetUserID': UserID})
        try:
            return 'Sent'
        except:
            return 'Error: ', CheckCookie(Cookie)
    except:
        return 'Error: ', CheckCookie(Cookie)


def TotalFriends(Cookie, Proxy=None):
    try:
        session = SetCookie(Cookie,Proxy)
        response = session.get(FriendsURL + 'my/friends/count')
        return response.json()['count']
    except:
        return 'Error: ', CheckCookie(Cookie)


# Credit to Soul for documentation URL
def SendMessage(Cookie, UserID, MessageSubject, Body, Proxy=None):
    try:
        LocalID = GetUserID(Cookie)
        session = SetCookie(Cookie,Proxy)
        Post = session.post(PrivateMessageAPIV1 + 'messages/send/', data={
                            'userId': LocalID,
                            'subject': MessageSubject,
                            'body': Body,
                            'recipientid': UserID,
                            })
        return Post.json()['shortMessage']
    except:
        return 'Error: ', CheckCookie(Cookie)


def GetBlockedUsers(Cookie, Proxy=None):
    SetProxy(Proxy)
    try:
        session = SetCookie(Cookie,Proxy)
        response = session.get(SettingsURL)
        Data = response.json()['BlockedUsersModel']['BlockedUsers']
        BlockedIDs = []
        BlockedNames = []

        for User in Data:
            BlockedIDs.append(User['uid'])
            BlockedNames.append(User['Name'])
        return BlockedIDs, BlockedNames
    except:
        return 'Error: ', CheckCookie(Cookie)

# endregion


# region GroupFunctions

def ClaimGroup(Cookie, GroupID, Proxy=None):
    SetProxy(Proxy)
    try:
        session = SetCookie(Cookie,Proxy)
        Post = session.post(GroupAPIV1 + str(GroupID) + '/claim-ownership')
        return 'Sent'
    except:
        return 'Error: ', CheckCookie(Cookie)


def JoinGroup(Cookie, GroupID, Proxy=None):
    SetProxy(Proxy)
    try:
        session = SetCookie(Cookie,Proxy)
        Post = session.post(GroupAPIV1 + str(GroupID) + '/users')
        return 'Joined'
    except:
        return 'Error: ', CheckCookie(Cookie)


def LeaveGroup(Cookie, GroupID, Proxy=None):
    try:
        session = SetCookie(Cookie,Proxy)
        LocalUserID = GetUserID(Cookie)
        Post = session.delete(GroupAPIV1 + str(GroupID) +
                              '/users/' + str(LocalUserID))
        return 'Left'
    except:
        return 'Error: ', CheckCookie(Cookie)


def GetFunds(Cookie, GroupID, Proxy=None):
    try:
        session = SetCookie(Cookie,Proxy)
        response = session.get(EconomyURL + '/groups/' +
                               str(GroupID) + '/currency')
        return response.json()['robux']
    except:
        return 'Error: ', CheckCookie(Cookie)


def PayGroupFunds(Cookie, GroupID, UserID, RobuxAmount, Proxy=None):
    try:
        session = SetCookie(Cookie,Proxy)

        data = {
            "PayoutType": "FixedAmount",
            "Recipients": [
                {
                    "recipientId": str(UserID),
                    "recipientType": "User",
                    "amount": str(RobuxAmount)
                }
            ]
        }

        Post = session.post(GroupAPIV1 + str(GroupID) + '/payouts', json=data)
        if(Post.status_code == 200):
            return 'Sent'
        else:
            return 'Error: ', CheckCookie(Cookie)
    except:
        return 'Error: ', CheckCookie(Cookie)


def PayGroupPercentage(Cookie, GroupID, UserID, Percentage, Proxy=None):
    try:
        session = SetCookie(Cookie,Proxy)

        data = {
            "PayoutType": "Percentage",
            "Recipients": [
                {
                    "recipientId": str(UserID),
                    "recipientType": "User",
                    "amount": str(Percentage)
                }
            ]
        }
        Post = session.post(GroupAPIV1 + str(GroupID) + '/payouts', json=data)
        if(Post.status_code == 200):
            return 'Sent'
        else:
            return 'Error: ', CheckCookie(Cookie)
    except:
        return 'Error: ', CheckCookie(Cookie)


def PostGroupWall(Cookie, GroupID, Text, Proxy=None):
    try:
        session = SetCookie(Cookie,Proxy)
        Post = session.post(GroupAPIV1 + str(GroupID) +
                            '/wall/posts', data={'body': Text})
        return 'Sent'
    except:
        return 'Error: ', CheckCookie(Cookie)


def ChangeGroupRank(Cookie, GroupID, UserID, roleId, Proxy=None):
    try:
        session = SetCookie(Cookie,Proxy)
        Patch = session.patch(GroupAPIV1 + str(GroupID) +
                              '/users/' + str(UserID), data={'roleId': roleId})
        return 'Sent'
    except:
        return 'Error: ', CheckCookie(Cookie)


def ChangeGroupShout(Cookie, GroupID, StatusString, Proxy=None):
    try:
        session = SetCookie(Cookie,Proxy)
        Patch = session.patch(GroupAPIV1 + str(GroupID) +
                              '/status', data={'message': StatusString})
        return 'Sent'
    except:
        return 'Error: ', CheckCookie(Cookie)


def ChangeGroupDescription(Cookie, GroupID, DescriptionString, Proxy=None):
    try:
        session = SetCookie(Cookie,Proxy)
        Patch = session.patch(GroupAPIV1 + str(GroupID) +
                              '/description', data={'description': DescriptionString})
        return 'Sent'
    except:
        return 'Error: ', CheckCookie(Cookie)


# endregion


# region Internal Place API

def GetUniverseID(Cookie, PlaceID, Proxy=None):
    try:
        session = SetCookie(Cookie,Proxy)
        response = session.get(
            GamesURL + 'games/multiget-place-details?placeIds=' + str(PlaceID))
        return response.json()[0]['universeId']
    except:
        return 'Error: ', CheckCookie(Cookie)


def GetCurrentGamePlayers(Cookie, PlaceID, Proxy=None):
    SetProxy(Proxy)
    try:
        UniverseID = GetUniverseID(Cookie, PlaceID)
        GameData = GetUniverseData(UniverseID)
        return GameData['playing']
    except:
        return 'Error: ', CheckCookie(Cookie)


def GetGameVisits(Cookie, PlaceID, Proxy=None):
    SetProxy(Proxy)
    try:
        UniverseID = GetUniverseID(Cookie, PlaceID)
        GameData = GetUniverseData(UniverseID)
        return GameData['visits']
    except:
        return 'Error: ', CheckCookie(Cookie)


def GetGameLikes(Cookie, PlaceID, Proxy=None):
    SetProxy(Proxy)
    try:
        UniverseID = GetUniverseID(Cookie, PlaceID)
        return GetUniverseVotes(UniverseID)['upVotes']
    except:
        return 'Error: ', CheckCookie(Cookie)


def GetGameDislikes(Cookie, PlaceID, Proxy=None):
    SetProxy(Proxy)
    try:
        UniverseID = GetUniverseID(Cookie, PlaceID)
        return GetUniverseVotes(UniverseID)['downVotes']
    except:
        return 'Error: ', CheckCookie(Cookie)


def GetGameFavourites(Cookie, PlaceID, Proxy=None):
    SetProxy(Proxy)
    try:
        UniverseID = GetUniverseID(Cookie, PlaceID)
        response = requests.get(GamesURL + 'games/' +
                                str(UniverseID) + '/favorites/count')
        return response.json()['favoritesCount']
    except:
        return 'Error: ', CheckCookie(Cookie)


# endregion

# endregion
