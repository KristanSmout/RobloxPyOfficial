import requests,json
from robloxpy import Utils as Utils
from typing import Union

def GetAll(UserID: int) -> list:
    """
    Returns a full list of a users friends
    """
    FullList = []
    response = requests.get(Utils.UserAPI + str(UserID) + "/friends")
    response = requests.get(Utils.FriendsAPI + f'{UserID}/friends')
    Friendslist = json.loads(response.text)
    for friend in Friendslist['data']:
        FullList.append(friend['displayName'])
    return FullList

def GetCount(UserID: int) -> Union[int, str]:
    """
    Returns the total number of friends a user has
    """
    response = requests.get(Utils.FriendsAPI + f"{UserID}/friends/count")
    try:
        return response.json()['count']
    except:
        return response.json()['errors'][0]['message']

def GetOnline(UserID: int) -> Union[list, str]:
    """
    Returns a full list of a users friends that are currently online
    """
    FullList = []
    response = requests.get(Utils.FriendsAPI + f"{UserID}/friends/")
    try:
        Friendslist = json.loads(response.text)
        for friend in Friendslist['data']:
            if(friend['isOnline'] == True):
                FullList.append(friend['displayName'])
        return FullList
    except:
        return response.json()['errors'][0]['message']

def GetOffline(UserID: int) -> Union[list, str]:
    """
    Returns a full list of a users friends that are currently offline
    """
    FullList = []
    response = requests.get(Utils.FriendsAPI + f"{UserID}/friends/")
    try:
        Friendslist = json.loads(response.text)
        for friend in Friendslist['data']:
            if(friend['isOnline'] == False):
                FullList.append(friend['displayName'])
        return FullList
    except:
        return response.json()['errors'][0]['message']

def GetFollowerCount(UserID: int) -> Union[int, str]:
    """
    Returns a count of how many users a person is following
    """
    response = requests.get(Utils.FriendsAPI + f"{UserID}/followers/count")
    try:
        return response.json()['count']
    except:
        return response.json()['errors'][0]['message']

def GetFollowers(UserID: int, Amount: int) -> tuple:
    """
    Returns a full list of people that the user follows

    [Username],[ID]
    """
    response = requests.get(Utils.FriendsAPI + str(UserID) + '/followers?sortOrder=Asc&limit=100')
    try:
        CurrentAmount = 0
        NameList = []
        IDList = []
        Cursor = 'None'
        #print(str(Utils.FriendsAPI + str(UserID) + '/followers?sortOrder=Asc&limit=100'))
        while Cursor != 'null':
            if(Cursor is None):
                Cursor = 'null'
            else:
                try:
                    Cursor = response.json()['nextPageCursor']
                except:
                    Cursor = 'null'
            for Follower in response.json()['data']:
                if(CurrentAmount < Amount):
                    NameList.append(Follower['name'])
                    IDList.append(Follower['id'])
                    CurrentAmount = CurrentAmount + 1
                else:
                    return NameList, IDList
            if(Cursor is None):
                Cursor = 'null'
            else:
                try:
                    response = requests.get(Utils.FriendsAPI + 'users/' + str(UserID) + '/followers?sortOrder=Asc&limit=100&cursor=' + str(Cursor))
                except:
                    Cursor = 'null'
        return NameList, IDList
    except:
        return NameList, IDList

def GetFollowingCount(UserID: int) -> Union[int, str]:
    """
    Returns a count of how many users a person is following
    """
    response = requests.get(Utils.FriendsAPI + f"{UserID}/followings/count")
    try:
        return response.json()['count']
    except:
        return response.json()['errors'][0]['message']

def GetFollowing(UserID: int, Amount: int) -> tuple:
    """
    Returns a full list of people that follow the user

    [Username],[ID]
    """
    response = requests.get(Utils.FriendsAPI + str(UserID) + '/followings?sortOrder=Asc&limit=100')
    try:
        CurrentAmount = 0
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
                if(CurrentAmount < Amount):
                    NameList.append(Follower['name'])
                    IDList.append(Follower['id'])
                    CurrentAmount = CurrentAmount + 1
                else:
                    return NameList, IDList
            if(Cursor is None):
                Cursor = 'null'
            else:
                try:
                    response = requests.get(Utils.FriendsAPI + str(UserID) + '/followers?sortOrder=Asc&limit=100&cursor=' + str(Cursor))
                except:
                    Cursor = 'null'
        return NameList, IDList
    except:
        return NameList, IDList