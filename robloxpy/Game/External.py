import robloxpy.Utils as Utils


def GetUniverseData(UniverseID):
    response = requests.get(f"{Utils.GamesAPI}games?universeIds={str(UniverseID)}")
    try:
        return response.json()['data'][0]
    except:
        return 'Universe Not Found'

def GetUniverseVotes(UniverseID):
    response = requests.get(f"{Utils.GamesAPI}games/votes?universeIds={str(UniverseID)}")
    try:
        return response.json()['data'][0]
    except:
        return 'Universe Not Found'

def GetUniverseFavourites(UniverseID):
    response = requests.get(f"{Utils.GamesAPI}games/{str(UniverseID)}/favorites/count")
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