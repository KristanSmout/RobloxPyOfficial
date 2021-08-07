import robloxpy.Utils as Utils
import requests


def GetUniverseData(UniverseID: int) -> dict:
    response = requests.get(f"{Utils.GamesAPI}games?universeIds={str(UniverseID)}")
    try:
        return response.json()['data'][0]
    except:
        return 'Universe Not Found'

def GetUniverseVotes(UniverseID: int) -> dict:
    response = requests.get(f"{Utils.GamesAPI}games/votes?universeIds={str(UniverseID)}")
    try:
        return response.json()['data'][0]
    except:
        return 'Universe Not Found'

def GetUniverseFavourites(UniverseID: int) -> int:
    response = requests.get(f"{Utils.GamesAPI}games/{str(UniverseID)}/favorites/count")
    try:
        return response.json()['favoritesCount']
    except:
        return 'Universe Not Found'

def GetCurrentUniversePlayers(UniverseID: int) -> int:
    GameData = GetUniverseData(str(UniverseID))
    try:
        return GameData['playing']
    except:
        return 'Universe Not Found'

def GetUniverseVisits(UniverseID: int) -> int:
    GameData = GetUniverseData(str(UniverseID))
    try:
        return GameData['visits']
    except:
        return 'Universe Not Found'

def GetUniverseLikes(UniverseID: int) -> int:
    GetVotes = GetUniverseVotes(str(UniverseID))
    try:
        return GetVotes['upVotes']
    except:
        return 'Universe Not Found'

def GetUniverseDislikes(UniverseID: int) -> int:
    GetVotes = GetUniverseVotes(str(UniverseID))
    try:
        return GetVotes['downVotes']
    except:
        return 'Universe Not Found'