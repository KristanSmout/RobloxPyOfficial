import robloxpy.User.Internal as Internal
import robloxpy.Utils as Utils
import robloxpy.Game.External as External

#Personal Game Vars
class MyGame(object):
    def __init__(self):
        self.maxPlayerCount
        self.socialSlotType
        self.customSocialSlotsCount
        self.allowCopying
        self.currentSavedVersion
        self.name
        self.isRootPlace
        self.descriptionisRootPlace

def GetUniverseID(PlaceID: int) -> int:
    try:
        response = Internal.CurrentCookie.get(f"{Utils.GamesAPI}games/multiget-place-details?placeIds={str(PlaceID)}")
        try:
            return response.json()['data'][0]
        except:
            return 'Universe Not Found'
    except Exception as e:
        return e

def GetCurrentPlayers(PlaceID: int) -> int:
    try:
        UniverseID = GetUniverseID(PlaceID)
        GameData = External.GetCurrentUniversePlayers(UniverseID)
        return GameData['playing']
    except:
        return "Error"

def GetGameVisits(PlaceID: int) -> int:
    try:
        UniverseID = GetUniverseID(PlaceID)
        GameData = External.GetUniverseData(UniverseID)
        return GameData['visits']
    except:
        return "Error"

def GetGameLikes(PlaceID: int) -> int:
    try:
        UniverseID = GetUniverseID(PlaceID)
        return External.GetUniverseVotes(UniverseID)['upVotes']
    except:
        return "Error"

def GetGameDislikes(PlaceID: int) -> int:
    try:
        UniverseID = GetUniverseID(PlaceID)
        return External.GetUniverseVotes(UniverseID)['downVotes']
    except:
        return "Error"

def GetGameFavourites(PlaceID: int) -> int:
    try:
        UniverseID = GetUniverseID(PlaceID)
        return External.GetUniverseFavourites(UniverseID)
    except:
        return "Error"

def GetMyGameData(PlaceID: int) -> str:
    try:
        response = Internal.CurrentCookie.get(Utils.DevelopAPIV2 + f"places/{PlaceID}")
        print((Utils.DevelopAPIV2 + f"places/{PlaceID}"))
        MyGame.maxPlayerCount = response.json()['maxPlayerCount']
        MyGame.socialSlotType = response.json()['socialSlotType']
        MyGame.customSocialSlotsCount = response.json()['customSocialSlotsCount']
        MyGame.allowCopying = response.json()['allowCopying']
        MyGame.currentSavedVersion = response.json()['currentSavedVersion']
        MyGame.name = response.json()['name']
        MyGame.descriptionisRootPlace = response.json()['description']
        MyGame.isRootPlace = response.json()['isRootPlace']
        return "Saves"
    except:
        return response.json()['errors'][0]['message']