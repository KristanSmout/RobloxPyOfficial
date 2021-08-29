import requests, webbrowser, time, sys, random
from . import Utils, asset, errors
from typing import Type, Tuple
robloxpy = sys.modules['robloxpy']

user = None

class Place():
    __slots__ = ('id', 'name', 'description', 'url', 'builder', 'playable', 'universe', 'price')

    def __init__(self, id: int) -> None:
        self._update(id)

    def __repr__(self) -> str:
        return self.name

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Place):
            return self.id == other.id
        return False

    def _update(self, id: int) -> None:
        if robloxpy.CurrentCookie == None:
            raise errors.NoCookie
        data = robloxpy.CurrentCookie.get(f"{Utils.GamesAPI}games/multiget-place-details?placeIds={id}").json()[0]
        self.id = data['placeId']
        self.name = data['name']
        self.description = data['description']
        self.url = data['url']
        self.builder = user.User(data['builderId'])
        self.playable = data['isPlayable']
        self.universe = Universe(data['universeId'])
        self.price = data['price']

    def _icon(self, size: int = 512) -> str:
        return requests.get(f"{Utils.ThumnnailAPIV1}places/gameicons?format=Png&isCircular=false&placeIds={self.id}&size={size}x{size}").json()['data'][0]['imageUrl']

    @property
    def icon(self) -> Type[asset.ImageAsset]:
        """
        Returns the places icon as an ImageAsset.
        """
        return asset.ImageAsset(self._icon())
    
    def _thumbnail(self, width: int = 768, height: int = 432) -> str:
        if self.universe == None:
            raise errors.NoUniverse
        return requests.get(f"{Utils.ThumnnailAPIV1}games/multiget/thumbnails?format=Png&isCircular=false&universeIds={self.universe.id}&size={width}x{height}").json()['data'][0]['imageUrl']

    @property
    def thumbnail(self) -> Type[asset.ImageAsset]:
        """
        Returns the places thumbnail as an ImageAsset.
        """
        return asset.ImageAsset(self._thumbnail())

    @property
    def playing(self) -> int:
        """
        Returns the current ammount of players in the places universe.
        """
        if self.universe == None:
            raise errors.NoUniverse
        return self.universe.playing

    @property
    def visits(self) -> int:
        """
        Returns the total visits for the places universe.
        """
        if self.universe == None:
            raise errors.NoUniverse
        return self.universe.visits

    @property
    def favorites(self) -> int:
        """
        Returns the total favorites for the places universe.
        """
        if self.universe == None:
            raise errors.NoUniverse
        return self.universe.favorites

    @property
    def votes(self) -> int:
        """
        Returns the "score" of the places universe (upvotes - downvotes).
        """
        dat = self.raw_votes()
        return dat[0] - dat[1]

    def raw_votes(self) -> Tuple[int]:
        """
        Returns the raw vote data from the api. Returned as (upvotes, downvotes)
        """
        if self.universe == None:
            raise errors.NoUniverse
        return self.universe.raw_votes()

    def join_game(self) -> None:
        """
        Joins the given game
        """
        if robloxpy.CurrentCookie == None:
            raise errors.NoCookie
        Gamesession = requests.session()
        Gamesession.cookies[".ROBLOSECURITY"] = robloxpy.RawCookie

        Gamesession = Gamesession.post(
        url = Utils.GameAuthUrl,
        headers = {
            "Referer": "https://www.roblox.com/",
            "X-CSRF-Token": Gamesession.post(
                url = Utils.GameAuthUrl
            ).headers["X-CSRF-Token"],
        }
        ).headers["RBX-Authentication-Ticket"]
        BrowserID = random.randint(10000000000, 99999999999)
        webbrowser.open(f"roblox-player:1+launchmode:play+gameinfo:{Gamesession}+launchtime:{int(time.time()*1000)}+placelauncherurl:https%3A%2F%2Fassetgame.roblox.com%2Fgame%2FPlaceLauncher.ashx%3Frequest%3DRequestGame%26browserTrackerId%3D{BrowserID}%26placeId%3D{self.id}%26isPlayTogetherGame%3Dfalse+browsertrackerid:{BrowserID}+robloxLocale:en_us+gameLocale:en_us")

class Universe():
    __slots__ = ('id', 'name', 'description', 'creator', 'price', 'allowed_gear_genres', 'genre_enforced', 'copying_allowed', 'max_players', 'created_at', 'updated_at', 'vip_servers', 'avatar_type', 'genre', 'all_genre', 'rating')
    
    def __init__(self, id: int) -> None:
        self._update(id)

    def __repr__(self) -> str:
        return self.name

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Universe):
            return self.id == other.id
        return False
        
    def _update(self, id: int) -> None:
        data = requests.get(f"{Utils.GamesAPI}games?universeIds={id}").json()['data'][0]
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.creator = user.User(data['creator']['id'])
        self.price = data['price']
        self.allowed_gear_genres = data["allowedGearGenres"]
        self.genre_enforced = data['isGenreEnforced']
        self.copying_allowed = data['copyingAllowed']
        self.max_players = data['maxPlayers']
        self.created_at = data['created']
        self.updated_at = data['updated']
        self.vip_servers = data['createVipServersAllowed']
        self.avatar_type = data['universeAvatarType']
        self.genre = data['genre']
        self.all_genre = data['isAllGenre']
        self.rating = data['gameRating']

    @property
    def root_place(self) -> Type[Place]:
        """
        Returns the root place as a Place
        """
        return Place(requests.get(f"{Utils.GamesAPI}games?universeIds={self.id}").json()['data'][0]['rootPlaceId'])
    
    @property
    def playing(self) -> int:
        """
        Returns the current ammount of players in the universe
        """
        return requests.get(f"{Utils.GamesAPI}games?universeIds={self.id}").json()['data'][0]['playing']

    @property
    def visits(self) -> int:
        """
        Returns the total visits for the universe.
        """
        return requests.get(f"{Utils.GamesAPI}games?universeIds={self.id}").json()['data'][0]['visits']

    @property
    def favorites(self) -> int:
        """
        Returns the total favorites for the universe.
        """
        return requests.get(f"{Utils.GamesAPI}games?universeIds={self.id}").json()['data'][0]['favoritedCount']

    @property
    def votes(self) -> int:
        """
        Returns the "score" for the universe (upvotes - downvotes).
        """
        dat = self.raw_votes()
        return dat[0] - dat[1]

    def raw_votes(self) -> Tuple[int]:
        """
        Returns the raw vote data from the api. Returned as (upvotes, downvotes)
        """
        data = requests.get(f"{Utils.GamesAPI}games/votes?universeIds={self.id}").json()['data'][0]
        return (data['upVotes'], data['downVotes'])

    def _icon(self, size: int = 512) -> str:
        return requests.get(f"{Utils.ThumnnailAPIV1}games/icons?format=Png&isCircular=false&size={size}x{size}&universeIds={self.id}").json()['data'][0]['imageUrl']

    @property
    def icon(self) -> Type[asset.ImageAsset]:
        """
        Returns the universes icon as an ImageAsset
        """
        return asset.ImageAsset(self._icon())

    def join_game(self) -> None:
        """
        Joins the given game
        """
        if robloxpy.CurrentCookie == None:
            raise errors.NoCookie
        Gamesession = requests.session()
        Gamesession.cookies[".ROBLOSECURITY"] = robloxpy.RawCookie

        Gamesession = Gamesession.post(
        url = Utils.GameAuthUrl,
        headers = {
            "Referer": "https://www.roblox.com/",
            "X-CSRF-Token": Gamesession.post(
                url = Utils.GameAuthUrl
            ).headers["X-CSRF-Token"],
        }
        ).headers["RBX-Authentication-Ticket"]
        BrowserID = random.randint(10000000000, 99999999999)
        webbrowser.open(f"roblox-player:1+launchmode:play+gameinfo:{Gamesession}+launchtime:{int(time.time()*1000)}+placelauncherurl:https%3A%2F%2Fassetgame.roblox.com%2Fgame%2FPlaceLauncher.ashx%3Frequest%3DRequestGame%26browserTrackerId%3D{BrowserID}%26placeId%3D{self.root_place.id}%26isPlayTogetherGame%3Dfalse+browsertrackerid:{BrowserID}+robloxLocale:en_us+gameLocale:en_us")

def _get_user():
    global user
    from . import user as usr
    user = usr
_get_user()