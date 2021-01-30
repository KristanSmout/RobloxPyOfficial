import requests,json
from robloxpy import Utils as Utils


global Owner
global Name
global isOwned
global Description
global Shout
global Roles
global isPublic
global isBc


def IsGroupOwned(GroupID):
    """
    Returns whether a group is owned
    """
    response = requests.get(Utils.GroupAPIV1 + str(GroupID))
    try:
        if(str(response.json()['Owner']) == 'None'):
            return False
        else:
            return True
    except:
        return response.json()['errors'][0]['message']

def GetName(GroupID):
    """
    Returns the name of a group
    """
    response = requests.get(Utils.APIURL + f"groups/{GroupID}")
    try:
        return response.json()['Name']
    except:
        return response.json()['errors'][0]['message']

def GetOwner(GroupID):
    """
    Returns the name of the owner of a group
    """
    response = requests.get(Utils.APIURL + f"groups/{GroupID}")
    try:
        return response.json()['Owner']
    except:
        return response.json()['errors'][0]['message']

def GetDescription(GroupID):
    """
    Returns the description of a group
    """
    response = requests.get(Utils.APIURL + f"groups/{GroupID}")
    try:
        return response.json()['Description']
    except:
        return response.json()['errors'][0]['message']

def GetEmblem(GroupID):
    """
    Returns the URL of the group emblem
    """
    response = requests.get(Utils.APIURL + f"groups/{GroupID}")
    try:
        return response.json()['EmblemUrl']
    except:
        return response.json()['errors'][0]['message']

def GetRoles(GroupID):
    """
    Returns the roles and ranks of a group

    [Role Names],[Role Ranks]
    """
    response = requests.get(Utils.APIURL + f"groups/{GroupID}")
    try:
        FullList = []
        RankList = []
        GroupRanks = response.json()['Roles']
        for Rank in GroupRanks:
            FullList.append((Rank['Name']))
            RankList.append((Rank['Rank']))
        return FullList,RankList
    except:
        return response.json()

def GetAllies(GroupID):
    """
    Returns a list of groups that are allies
    """
    response = requests.get(Utils.APIURL + f"groups/{GroupID}/allies")
    try:
        FullList = []
        Grouplist = json.loads(response.text)
        Grouplist = Grouplist['Groups']
        for group in Grouplist:
            FullList.append(group['Name'])
        return FullList
    except:
        return response.json()['errors'][0]['message']

def GetEnemies(GroupID):
    """
    Returns a list of groups that are enemies
    """
    response = requests.get(Utils.APIURL + f"groups/{GroupID}/enemies")
    try:
        FullList = []
        Grouplist = json.loads(response.text)
        Grouplist = Grouplist['Groups']
        for group in Grouplist:
            FullList.append(group['Name'])
        return FullList
    except:
        return response.json()['errors'][0]['message']

def GetMemberCount(GroupID):
    """
    Returns a count of how many users are in a group
    """
    response = requests.get(Utils.GroupAPIV1 + f"groups/{GroupID}")
    try:
        return response.json()['memberCount']
    except:
        return response.json()['errors'][0]['message']

def isPublic(GroupID):
    """
    Returns if a group is public to join
    """
    response = requests.get(Utils.GroupAPIV1 + f"groups/{GroupID}")
    try:
        return response.json()['publicEntryAllowed']
    except:
        return response.json()['errors'][0]['message']

def isBCOnly(GroupID):
    """
    Returns if a group is Builderclub Only
    """
    response = requests.get(Utils.GroupAPIV1 + f"groups/{GroupID}")
    try:
        return response.json()['isBuildersClubOnly']
    except:
        return response.json()['errors'][0]['message']

def GetMembersList(GroupID, Limit = (999999999999)):
    """
    Returns a full list of group members

    [Username],[ID]
    """
    MemberList = []
    IDList = []
    CurrentAmount = 0
    Cursor = 'None'
    response = requests.get(Utils.GroupAPIV1 + (f"groups/{GroupID}/users?SortOrder=Asc&limit=100"))
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

def GetMembersinRoleList(GroupID,RoleID,Limit= (999999999999)):
    """
    Returns a list of users in a specific role
    [Username],[ID]
    """
    MemberList = []
    IDList = []
    CurrentAmount = 0
    Cursor = 'None'
    response = requests.get(Utils.GroupAPIV1 + (f"groups/{GroupID}/roles/{RoleID}/users?SortOrder=Asc&limit=100"))
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
