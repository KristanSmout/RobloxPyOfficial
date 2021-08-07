import requests,json
from robloxpy import Utils as Utils
from typing import Union

def IsGroupOwned(GroupID: int) -> Union[bool, str]:
    """
    Returns whether a group is owned
    """
    response = requests.get(Utils.GroupAPIV1 + str(GroupID))
    try:
        if(str(response.json()['owner']) == 'None'):
            return False
        else:
            return True
    except:
        return response.json()['errors'][0]['message']

def GetName(GroupID: int) -> str:
    """
    Returns the name of a group
    """
    response = requests.get(Utils.GroupAPIV1 + str(GroupID))
    try:
        return response.json()['name']
    except:
        return response.json()['errors'][0]['message']

def GetOwner(GroupID: int) -> str:
    """
    Returns the name of the owner of a group
    """
    response = requests.get(Utils.GroupAPIV1 + str(GroupID))
    try:
        return response.json()['owner']['username']
    except:
        return response.json()['errors'][0]['message']

def GetDescription(GroupID: int) -> str:
    """
    Returns the description of a group
    """
    response = requests.get(Utils.GroupAPIV1 + str(GroupID))
    try:
        return response.json()['description']
    except:
        return response.json()['errors'][0]['message']

def GetEmblem(GroupID: int) -> str:
    """
    Returns the URL of the group emblem
    """
    response = requests.get(Utils.ThumnnailAPIV1 + f"groups/icons?groupIds={GroupID}&size=420x420&format=Png&isCircular=true")
    try:
        return response.json()['data'][0]['imageUrl']
    except:
        return response.json()['errors'][0]['message']

def GetRoles(GroupID: int) -> Union[tuple, dict]:
    """
    Returns the roles and ranks of a group

    [Role Names],[Role Ranks]
    """
    response = requests.get(Utils.GroupAPIV1 + str(GroupID) +"/roles")
    try:
        FullList = []
        RankList = []
        GroupRanks = response.json()['roles']
        for Rank in GroupRanks:
            FullList.append((Rank['name']))
            RankList.append((Rank['rank']))
        return FullList,RankList
    except:
        return response.json()

def GetAllies(GroupID: int) -> Union[list, str]:
    """
    Returns a list of groups that are allies
    """
    response = requests.get(Utils.GroupAPIV1 + str(GroupID) +"/relationships/allies")
    try:
        FullList = []
        Grouplist = json.loads(response.text)
        Grouplist = Grouplist['relatedGroups']
        for group in Grouplist:
            FullList.append(group['name'])
        return FullList
    except:
        return response.json()['errors'][0]['message']

def GetEnemies(GroupID: int) -> Union[list, str]:
    """
    Returns a list of groups that are enemies
    """
    response = requests.get(Utils.GroupAPIV1 + str(GroupID) +"/relationships/enemies")
    try:
        FullList = []
        Grouplist = json.loads(response.text)
        Grouplist = Grouplist['relatedGroups']
        for group in Grouplist:
            FullList.append(group['name'])
        return FullList
    except:
        return response.json()['errors'][0]['message']

def GetMemberCount(GroupID: int) -> Union[int, str]:
    """
    Returns a count of how many users are in a group
    """
    response = requests.get(Utils.GroupAPIV1 + str(GroupID))
    try:
        return response.json()['memberCount']
    except:
        return response.json()['errors'][0]['message']

def isPublic(GroupID: int) -> Union[bool, str]:
    """
    Returns if a group is public to join
    """
    response = requests.get(Utils.GroupAPIV1 + str(GroupID))
    try:
        return response.json()['publicEntryAllowed']
    except:
        return response.json()['errors'][0]['message']

def isBCOnly(GroupID: int) -> Union[bool, str]:
    """
    Returns if a group is Builderclub Only
    """
    response = requests.get(Utils.GroupAPIV1 + str(GroupID))
    try:
        return response.json()['isBuildersClubOnly']
    except:
        return response.json()['errors'][0]['message']

def GetMembersList(GroupID: int, Limit :int = (999999999999)) -> Union[tuple, str]:
    """
    Returns a full list of group members

    [Username],[ID]
    """
    MemberList = []
    IDList = []
    CurrentAmount = 0
    Cursor = 'None'
    response = requests.get(Utils.GroupAPIV1 + (f"{GroupID}/users?SortOrder=Asc&limit=100"))
    try:
        while (Cursor != 'null'):
            if(Cursor is None):
                Cursor = 'null'
            else:
                try:
                    Cursor = response.json()['nextPageCursor']
                except:
                    Cursor = 'null'
            for Member in response.json()['data']:
                if(CurrentAmount < Limit):
                    MemberList.append(Member['user']['username'])
                    IDList.append(Member['user']['userId'])
                    CurrentAmount +=1
                else:
                    return MemberList,IDList
            if(Cursor is None):
                Cursor = 'null'
            else:
                try:
                    response = requests.get(Utils.GroupAPIV1 + (f"groups/{GroupID}/users?SortOrder=Asc&limit=100&cursor={Cursor}"))
                except:
                    Cursor = 'null'
        return MemberList, IDList
    except:
        return response.json()['errors'][0]['message']

def GetMembersinRoleList(GroupID: int, RoleID: int, Limit: int = 999999999999) -> Union[tuple, str]:
    """
    Returns a list of users in a specific role
    [Username],[ID]
    """
    MemberList = []
    IDList = []
    CurrentAmount = 0
    Cursor = 'None'
    response = requests.get(Utils.GroupAPIV1 + (f"{GroupID}/roles/{RoleID}/users?SortOrder=Asc&limit=100"))
    #return response.json()
    try:
        while (Cursor != 'null'):
            if(Cursor is None):
                Cursor = 'null'
            else:
                try:
                    Cursor = response.json()['nextPageCursor']
                except:
                    Cursor = 'null'
            for Member in response.json()['data']:
                if(CurrentAmount < Limit):
                    MemberList.append(Member['username'])
                    IDList.append(Member['userId'])
                    CurrentAmount +=1
                else:
                    return MemberList,IDList
            if(Cursor is None):
                Cursor = 'null'
            else:
                try:
                    response = requests.get(Utils.GroupAPIV1 + (f"groups/{GroupID}/roles/{RoleID}/users?SortOrder=Asc&limit=100&cursor={Cursor}"))
                except:
                    Cursor = 'null'
        return MemberList, IDList
    except:
        return response.json()['errors'][0]['message']
