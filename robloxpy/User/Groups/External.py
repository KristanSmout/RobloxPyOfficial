import requests,json
from robloxpy import Utils as Utils

def GetGroups(UserID: int) -> tuple:
    """
    Returns the list of groups a user is in
    [Name],[ID]
    """
    response = requests.get(Utils.APIURL + f"users/{UserID}/groups")
    FullList = []
    IDList = []
    Grouplist = json.loads(response.text)
    for group in Grouplist:
        FullList.append(group['Name'])
        IDList.append(group['Id'])
    return FullList, IDList