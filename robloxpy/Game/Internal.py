import robloxpy.User.Internal as Internal
import robloxpy.Utils as Utils
import robloxpy.Game.External as External

def GetUniverseID(PlaceID):
    try:
         response = session.get(f"{Utils.GamesAPI}games/multiget-place-details?placeIds={str(PlaceID)}")
         try:
            return response.json()['data'][0]
        except:
            return 'Universe Not Found'
    except Exception as e:
        return e

def GetCurrentPlayers(PlaceID):
    try:
        UniverseID = GetUniverseID(PlaceID)
        GameData = External.GetCurrentUniversePlayers(UniverseID)
        return GameData['playing']
    except:
        return GameData

def GetGameVisits(PlaceID):
    try:
        UniverseID = GetUniverseID(PlaceID)
        GameData = External.GetUniverseData(UniverseID)
        return GameData['visits']
    except:
        return GameData

def GetGameLikes(PlaceID):
    try:
        UniverseID = GetUniverseID(PlaceID)
        return External.GetUniverseVotes(UniverseID)['upVotes']
    except:
        return GameData

def GetGameDislikes(PlaceID):
    try:
        UniverseID = GetUniverseID(PlaceID)
        return External.GetUniverseVotes(UniverseID)['downVotes']
    except:
        return GameData

def GetGameFavourites(PlaceID):
    try:
        UniverseID = GetUniverseID(PlaceID)
        return GetUniverseFavourites(UniverseID)
    except:
        return GameData