import requests, sys, webbrowser, time, random
from . import Utils, errors, asset, group
from typing import List, Tuple, Type, Union

robloxpy = sys.modules['robloxpy']
ClientId = None

class BaseUser():
    __slots__ = ('id', 'name', 'display_name', 'description', 'created_at', 'banned')

    def __init__(self, id: Union[int, str], fetch: bool = True):
        self._update(id, fetch)

    def __repr__(self) -> str:
        return self.name or str(self.id)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, (BaseUser, PartialUser, User, ClientUser)):
            return self.id == other.id
        return False

    def _update(self, id: Union[int, str], fetch: bool) -> None:
        if type(id) != int:
            id = requests.get(Utils.APIURL + f'users/get-by-username?username={id}').json()['Id']
        if fetch:
            data = requests.get(f"{Utils.UserAPIV1}/{id}")
            try:
                rawData = data.json()
                self.id = id
                self.name = rawData['name']
                self.display_name = rawData['displayName']
                self.description = rawData['description']
                self.created_at = rawData['created']
                self.banned = rawData['isBanned']
            except (KeyError, AttributeError):
                raise errors.InvalidId
        else:
            self.id = id
            self.name = None
            self.display_name = None
            self.description = None
            self.created_at = None
            self.banned = None

    @property
    def online(self) -> bool:
        """
        Returns if the user is online.
        """
        data = requests.get(f"{Utils.UserAPI}{self.id}/onlinestatus")
        return data.json()['IsOnline']

    @property
    def name_history(self) -> List[str]:
        """
        Returns the users previous names.
        """
        Cursor = ""
        Done = False
        PastNames = []
        while(Done == False):
            response = requests.get(Utils.UserAPIV1 + f"{self.id}/username-history?limit=100&sortOrder=Asc&cursor={Cursor}")
            Names = response.json()['data']
            if((response.json()['nextPageCursor'] == "null") or response.json()['nextPageCursor'] == None):
                Done = True
            else:
                Done = False
                Cursor = response.json()['nextPageCursor']
            for Name in Names:
                PastNames.append(Name['name'])
            if(response.json()['nextPageCursor'] == 'None'):
                Done = True
        return PastNames

    @property
    def rap(self) -> int:
        """
        Returns the users recent average price.
        """
        TotalValue = 0
        Cursor = ""
        Done = False
        while(Done == False):
            try:
                response = requests.get(Utils.Inventory1URL + f"/{self.id}/assets/collectibles?sortOrder=Asc&limit=100&cursor={Cursor}")
                Items = response.json()
                if response.json()['nextPageCursor'] == "null" or response.json()['nextPageCursor'] == None:
                    Done = True
                else:
                    Done = False
                    Cursor = response.json()['nextPageCursor']
                for Item in Items["data"]:
                    try:
                        RAP = int(Item['recentAveragePrice'])
                        TotalValue = TotalValue + RAP
                    except:
                        TotalValue = TotalValue
                if response.json()['nextPageCursor'] == 'None':
                    Done = True
            except Exception as ex:
                Done = True
        return TotalValue

    @property
    def status(self) -> str:
        """
        Returns the users status.
        """
        response = requests.get(f"{Utils.UserAPIV1}{str(self.id)}/status")
        return response.json()['status']

    def _headshot(self, size: int = 720) -> str:
        response = requests.get(f"{Utils.ThumnnailAPIV1}users/avatar-headshot?userIds={self.id}&size={size}x{size}&format=png")
        return response.json()['data'][0]['imageUrl']

    @property
    def headshot(self) -> Type[asset.ImageAsset]:
        """
        Returns the users headshot as an ImageAsset.
        """
        return asset.ImageAsset(self._headshot())

    def _bust(self, size: int = 420) -> str:
        response = requests.get(f"{Utils.ThumnnailAPIV1}users/avatar-bust?userIds={self.id}&size={size}x{size}&format=png")
        return response.json()['data'][0]['imageUrl']

    @property
    def bust(self) -> Type[asset.ImageAsset]:
        """
        Returns the users bust as an ImageAsset.
        """
        return asset.ImageAsset(self._bust())

    def groups(self) -> Type[group.Group]:
        """
        Returns the groups the user is in
        """
        groups = []
        raw = requests.get(f"{Utils.GroupAPIV2}users/{self.id}/groups/roles")
        data = raw.json()
        for _group in data['data']:
            groups.append(group.Group(_group['group']['id']))
        return groups

    def limiteds(self) -> List[Type[asset.MarketAsset]]:
        """
        Returns the users limited items 
        """
        Limiteds = []
        Cursor = ""
        Done = False
        while(Done == False):
            try:
                response = requests.get(f"{Utils.InventoryURLV1}users/{self.id}/assets/collectibles?limit=100&sortOrder=Asc")
                Items = response.json()
                if response.json()['nextPageCursor'] == "null" or response.json()['nextPageCursor'] == None:
                    Done = True
                else:
                    Done = False
                    Cursor = response.json()['nextPageCursor']
                for Item in Items["data"]:
                    try:
                        Limiteds.append(asset.MarketAsset(Item['assetId']))
                    except:
                        continue
                if response.json()['nextPageCursor'] == 'None':
                    Done = True
                
            except Exception as ex:
                Done = True
        return Limiteds

class PartialUser():
    __slots__ = ('id')
    def __init__(self, id: int):
        self.id = id

    def __repr__(self) -> str:
        return str(self.id)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, (BaseUser, PartialUser, User, ClientUser)):
            return self.id == other.id
        return False

    def fetch(self) -> 'User':
        """
        Returns the User instance for the PartialUser
        """
        return User(self.id)

class User(BaseUser):
    def __init__(self, id: Union[int, str]):
        super().__init__(id)
            
    @property
    def following(self) -> bool:
        """
        returns if the client user is following this user.
        redundant, might be removed
        """
        response = robloxpy.CurrentCookie.post(f"{Utils.FriendsAPI}user/following-exists?UserID={str(self.id)}&followerUserID={self.id}", data={'targetUserIDs': str(self.id)})
        return response.json()['followings'][0]['isFollowing']

    def send_message(self, Subject: str, Body: str) -> Union[str, dict]:
        """
        Sends the given message to the given user
        """
        if robloxpy.CurrentCookie == None:
            raise errors.NoCookie

        response = None
        try:
            response = robloxpy.CurrentCookie.post(Utils.PrivateMessageAPIV1 + 'messages/send', data={
                                'userId': ClientId,
                                'subject': Subject,
                                'body': Body,
                                'recipientId': self.id,
                                })
            return response.json()
        except Exception as e:
            return response.json()

    def follow(self) ->  Union[bool, str]:
        """
        Follows a user.
        captcha blocked, might be removed.
        """
        if robloxpy.CurrentCookie == None:
            raise errors.NoCookie
        response = robloxpy.CurrentCookie.post(f"{Utils.FriendsAPI}users/{self.id}/follow", data={'targetUserID': self.id})
        try:
            return response.json()['success']
        except:
            return response.json()['errors']

    def unfollow(self) ->  Union[bool, str]:
        """
        unfollows the user
        """
        if robloxpy.CurrentCookie == None:
            raise errors.NoCookie
        response = robloxpy.CurrentCookie.post(f"{Utils.FriendsAPI}users/{self.id}/unfollow", data={'targetUserID': self.id})
        try:
            return response.json()['success']
        except:
            return response.json()['errors']

    def block(self) -> Union[bool, str]:
        """
        Blocks the user
        """
        if robloxpy.CurrentCookie == None:
            raise errors.NoCookie
        response = robloxpy.CurrentCookie.post(f"{Utils.APIURL}userblock/block?userId={self.id}", data={'targetUserID': self.id})
        try:
            return response.json()['success']
        except:
            return response.json()['errors']

    def unblock(self) -> Union[bool, str]:
        """
        Unlocks the user
        """
        if robloxpy.CurrentCookie == None:
            raise errors.NoCookie
        response = robloxpy.CurrentCookie.post(f"{Utils.APIURL}userblock/unblock?userId={self.id}", data={'targetUserID': self.id})
        try:
            return response.json()['success']
        except:
            return response.json()['errors']


class ClientUser(BaseUser):
    def __init__(self, id: Union[int, str]) -> None:
        super().__init__(id)
        global ClientId
        ClientId = self.id

    def blocked_users(self) -> List[Type[User]]:
        """
        Returns users which are blocked

        [UserID],[UserName]
        """
        if robloxpy.CurrentCookie == None:
            raise errors.NoCookie
        response = robloxpy.CurrentCookie.get(f"{Utils.SettingsURL}")
        Data = response.json()['BlockedUsersModel']['BlockedUsers']
        BlockedUsers = []

        for _User in Data:
            BlockedUsers.append(User(_User['uid']))
        return BlockedUsers

    def following_user(self, targetUser: Union[Type[User], int]) -> bool:
        """
        Checks if the current account is following a user
        """
        if robloxpy.CurrentCookie == None:
            raise errors.NoCookie
        if type(targetUser) == int:
            targetUser = User(targetUser)

        data = robloxpy.CurrentCookie.post(f"{Utils.FriendsAPI}user/following-exists?UserID={str(targetUser.id)}&followerUserID={self.id}", data={'targetUserIDs': str(targetUser.id)}).json()['followings'][0]
        return data['isFollowing']

    def join_game(self, PlaceId: int) -> None:
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
        webbrowser.open(f"roblox-player:1+launchmode:play+gameinfo:{Gamesession}+launchtime:{int(time.time()*1000)}+placelauncherurl:https%3A%2F%2Fassetgame.roblox.com%2Fgame%2FPlaceLauncher.ashx%3Frequest%3DRequestGame%26browserTrackerId%3D{BrowserID}%26placeId%3D{PlaceId}%26isPlayTogetherGame%3Dfalse+browsertrackerid:{BrowserID}+robloxLocale:en_us+gameLocale:en_us")


