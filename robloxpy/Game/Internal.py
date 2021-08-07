import robloxpy.User.Internal as Internal
import robloxpy.Utils as Utils
import robloxpy.Game.External as External
from typing import Union, Type

#Personal Game Vars
class MyGame(object):
    def __init__(self):
        self.maxPlayerCount = None
        self.socialSlotType = None
        self.customSocialSlotsCount = None
        self.allowCopying = None
        self.currentSavedVersion = None
        self.name = None
        self.isRootPlace = None
        self.descriptionisRootPlace = None

def GetUniverseID(PlaceID: int) -> Union[int, str]:
    try:
        response = Internal.CurrentCookie.get(f"{Utils.GamesAPI}games/multiget-place-details?placeIds={str(PlaceID)}")
        try:
            return response.json()['data'][0]
        except:
            return 'Universe Not Found'
    except Exception as e:
        return e

def GetCurrentPlayers(PlaceID: int) -> Union[int, str]:
    try:
        UniverseID = GetUniverseID(PlaceID)
        GameData = External.GetCurrentUniversePlayers(UniverseID)
        return GameData['playing']
    except:
        return "Error"

def GetGameVisits(PlaceID: int) -> Union[int, str]:
    try:
        UniverseID = GetUniverseID(PlaceID)
        GameData = External.GetUniverseData(UniverseID)
        return GameData['visits']
    except:
        return "Error"

def GetGameLikes(PlaceID: int) -> Union[int, str]:
    try:
        UniverseID = GetUniverseID(PlaceID)
        return External.GetUniverseVotes(UniverseID)['upVotes']
    except:
        return "Error"

def GetGameDislikes(PlaceID: int) -> Union[int, str]:
    try:
        UniverseID = GetUniverseID(PlaceID)
        return External.GetUniverseVotes(UniverseID)['downVotes']
    except:
        return "Error"

def GetGameFavourites(PlaceID: int) -> Union[int, str]:
    try:
        UniverseID = GetUniverseID(PlaceID)
        return External.GetUniverseFavourites(UniverseID)
    except:
        return "Error"

def GetMyGameData(PlaceID: int) -> Union[Type[MyGame], str]:
    try:
        response = Internal.CurrentCookie.get(Utils.DevelopAPIV2 + f"places/{PlaceID}")
        print((Utils.DevelopAPIV2 + f"places/{PlaceID}"))
        game = MyGame()
        game.maxPlayerCount = response.json()['maxPlayerCount']
        game.socialSlotType = response.json()['socialSlotType']
        game.customSocialSlotsCount = response.json()['customSocialSlotsCount']
        game.allowCopying = response.json()['allowCopying']
        game.currentSavedVersion = response.json()['currentSavedVersion']
        game.name = response.json()['name']
        game.descriptionisRootPlace = response.json()['description']
        game.isRootPlace = response.json()['isRootPlace']
        return game
    except:
        return response.json()['errors'][0]['message']