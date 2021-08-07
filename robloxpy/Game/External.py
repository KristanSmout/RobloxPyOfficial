import robloxpy.Utils as Utils
from typing import Union
import requests


def GetUniverseData(UniverseID: int) -> Union[dict, str]:
    response = requests.get(f"{Utils.GamesAPI}games?universeIds={str(UniverseID)}")
    try:
        return response.json()['data'][0]
    except:
        return 'Universe Not Found'

def GetUniverseVotes(UniverseID: int) -> Union[dict, str]:
    response = requests.get(f"{Utils.GamesAPI}games/votes?universeIds={str(UniverseID)}")
    try:
        return response.json()['data'][0]
    except:
        return 'Universe Not Found'

def GetUniverseFavourites(UniverseID: int) -> Union[int, str]:
    response = requests.get(f"{Utils.GamesAPI}games/{str(UniverseID)}/favorites/count")
    try:
        return response.json()['favoritesCount']
    except:
        return 'Universe Not Found'

def GetCurrentUniversePlayers(UniverseID: int) -> Union[int, str]:
    GameData = GetUniverseData(str(UniverseID))
    try:
        return GameData['playing']
    except:
        return 'Universe Not Found'

def GetUniverseVisits(UniverseID: int) -> Union[int, str]:
    GameData = GetUniverseData(str(UniverseID))
    try:
        return GameData['visits']
    except:
        return 'Universe Not Found'

def GetUniverseLikes(UniverseID: int) -> Union[int, str]:
    GetVotes = GetUniverseVotes(str(UniverseID))
    try:
        return GetVotes['upVotes']
    except:
        return 'Universe Not Found'

def GetUniverseDislikes(UniverseID: int) -> Union[int, str]:
    GetVotes = GetUniverseVotes(str(UniverseID))
    try:
        return GetVotes['downVotes']
    except:
        return 'Universe Not Found'