
# RobloxPy 0.2.0
RobloxPy is a python API wrapper for roblox. This allows for quick and easy integration of these API's into a python project.
<sup><center>If you need any help using RobloxPy or want to request an additional please join the discord server at 
	https://www.kristansmout.com/discord
Accept The Terms & Create a ticket</center></sup>

## Table Of Contents

* [Getting Started](#Getting-Started)
  * [Prerequisites](#Prerequisites)
  * [Installation](#Installation)
 * [Feature List](#Features)
	 * [Game](#Game)
	 * [Group](#Group)
	 * [Market](#Market)
	 * [User](#User)
		 * [User.Friends](#User.Friends)
		 * [User.Groups](#User.Groups)
 * [Usage Examples](#Usage-Examples)
	 *  [Utilities](#Utilities)
	 *  [Game](#Game)
#

## Getting-Started
To use the wrapper you will need to download and import robloxpy into your current project. The project has been designed to not include external requirements that are not included within the base installation of python.

### Prerequisites
> None
### Installation
```python
pip install robloxpy
```
If you wish to update robloxpy in the future you can also do this through pip
```python
pip install robloxpy --upgrade
```
### Requests
Robloxpy is built on community feedback, if you have a feature you want added please make it known on the discord and we will see if we can implement it for you. Not all features can be added and some are emitted to prevent abuse.
#
## Feature List
#### Utilities
* GetVersion
* CheckForUpdate
* UpdateInstructions
* SetProxy
* CheckProxy
* CheckCookie
#### Game
* External
	* GetUniverseData
	* GetUniverseVotes
	* GetUniverseFavourites
	* GetCurrentUniversePlayers
	* GetUniverseVisits
	* GetUniverseLikes
	* GetUniverseDislikes
* Internal
	* GetUniverseID
	* GetCurrentPlayers
	* GetGameVisits
	* GetGameLikes
	* GetGameDislikes
	* GetGameFavourites
	* GetMyGameData
#### Group
* External
	* IsGroupOwned
	* GetName
	* GetOwner
	* GetDescription
	* GetEmblem
	* GetRoles
	* GetAllies
	* GetEnemies
	* GetMemberCount
	* isPublic
	* isBCOnly
	* GetMembersList
	* GetMembersinRoleList

#### Market
* External
	* CanManageAsset
	* GetLimitedPriceData
	* GetLimitedRemaining
	* GetLimitedTotal
	* GetLimitedSales
	* GetLimitedRAP
	* GetLimitedSalePrice
	* GetLimitedChangePercentage
	* GetAssetImage
* Internal
	* BuyItem
#### User
* External
	* GetID
	* GetUserName
	* UsernameHistory
	* DoesNameExist
	* IsOnline
	* Isbanned
	* GetDescription
	* GetAge
	* CreationDate
	* GetRAP
	* GetLimiteds
	* GetBust
	* GetHeadshot
	* GetStatus
* Internal
	* SetCookie
	* GetDetails
	* isFollowing
	* FollowUser
	* UnfollowUser
	* BlockUser
	* UnblockUser
	* GetBlockedUsers
	* SendMessage
	* JoinGame
#### User.Friends
* External
	* GetAll
	* GetCount
	* GetOnline
	* GetOffline
	* GetFollowerCount
	* GetFollowers
	* GetFollowingCount
	* GetFollowing
* Internal
	* SendFriendRequest
	* Unfriend
	* TotalFriends
#### User.Groups
* External
	* GetGroups
* Internal
	* Claim
	* Join
	* Leave
	* GetFunds
	* Payout
	* PercentagePayout
	* SendWallPost
	* SendGroupShout
	* ChangeDescription
	* ChangeRank
#
## Usage-Examples
This section will cover the usage of robloxpy, it will provide examples for commands and the expected outputs to help you achieve what you want to achieve with robloxpy.

### Utilities
The utiliy functions are set to be used more for checking stuff within robloxpy as well as being used a reference point for robloxpy to store values between different areas of the API such as a central place for URL's.

> Utilities are called by standard as 
> ```
> robloxpy.Utils.<UTILITYFUNCTION>
> ```
> Not all functions require arguments however some do, you will be alerted to this in your IDE providing it supports intellisense.

* **CheckForUpdate()**
This function checks to see if an update is available for robloxpy, an internet connection will be required for this to work. If you wish to display this you will need to print it.
>Example Usage
>```python
>robloxpy.Utils.CheckForUpdate()
>```
>
>Example Output
>```
>You are up to date!
>```

* **GetVersion()**
This function returns the current version of robloxpy that is being used for the current project.
>Example Usage
>```python
>robloxpy.Utils.GetVersion()
>```
>
>Example Output
>```
>0.2.8
>```

* **UpdateInstructions(Version)**
This function returns instructions on how to update robloxpy, this can be used to show users of software how to get to the latest version. Alternatively if your tool was designed for a specific version of robloxpy you can give the user instructions on how to get to that version
>Example Usage
>```python
>robloxpy.Utils.UpdateInstructions()
>```
>
>Example Output
>```
>Update robloxpy through pip using following command: 'pip install robloxpy --upgrade'
>```
If you wish for your users to use a specific version of robloxpy you can have the instructions given to them on how to reach that specific version using the following.
>Example Usage
>```python
>robloxpy.Utils.UpdateInstructions("0.2.8")
>```
>
>Example Output
>```
>This software is intended to work on robloxpy version 0.2.8 please install using the following command
>'pip install robloxpy==0.2.8'
 >If you get an error with this command the developer of this tool has not provided a valid version   
>```

* **SetProxy(ProxyIP)**
This function will set a global proxy to be used within the python program and is not just limited to robloxpy. The expected format is IP:PORT
>Example Usage
>```python
>robloxpy.Utils.SetProxy("144.217.101.245:3129")
>```
>
>Example Output
>```
> OUTPUT NOT GIVEN
>```

* **CheckProxy(proxyAddress)**
This function will check the current proxy and provided the IP Shown to external sites.This function does not need an argument, if none is provided then the currently set proxy will be used. The expected format is IP:PORT if an argument is provided
>Example Usage
>```python
>robloxpy.Utils.CheckProxy("144.217.101.245:3129")
>```
>
>Example Output
>```
> 144.217.101.245
>```

* **CheckCookie(Cookie)**
This function will check if a cookie is valid, if no cookie is provided it will use the current cookie which has been set using the **SetCookie()** function.
>Example Usage
>```python
>robloxpy.Utils.CheckCookie()
>```
>
>Example Output
>```
> Valid Cookie
>```

### Game
The Game functions are functions geared towards getting data from games/universes. This group of functions has both internal and external commands. The internal commands will utilize the external commands while having an easier way to input data due to the way roblox has locked some API's behind the need to be logged in.

#### Internal
* **GetUniverseID(PlaceID)**
This function will convert a placeID to a universe ID to allow it to be used with external functions
>Example Usage
>```python
>robloxpy.Game.Internal.GetUniverseID(164118757)
>```
>
>Example Output
>```
> 23476326
>```

* **GetCurrentPlayers(PlaceID)**
This function will return the amount of players in a game
>Example Usage
>```python
>robloxpy.Game.Internal.GetCurrentPlayers(164118757)
>```
>
>Example Output
>```
> 52
>```

* **GetGameVisits(PlaceID)**
This function will return the amount of visits a game has
>Example Usage
>```python
>robloxpy.Game.Internal.GetGameVisits(164118757)
>```
>
>Example Output
>```
> 97
>```

* **GetGameLikes(PlaceID)**
This function will return the amount of likes a game has
>Example Usage
>```python
>robloxpy.Game.Internal.GetGameLikes(164118757)
>```
>
>Example Output
>```
> 6
>```

* **GetGameDislikes(PlaceID)**
This function will return the amount of dislikes a game has
>Example Usage
>```python
>robloxpy.Game.Internal.GetGameDislikes(164118757)
>```
>
>Example Output
>```
> 2
>```

* **GetGameFavourites(PlaceID)**
This function will return the amount of favourites a game has
>Example Usage
>```python
>robloxpy.Game.Internal.GetGameFavourites(164118757)
>```
>
>Example Output
>```
> 8
>```

* **GetMyGameData(PlaceID)**
This function will return a range of data of a game owned by the current set cookie. The PlaceID must be a game that the current user has permissions for to edit.
>Example Usage
>```python
>robloxpy.Game.Internal.GetMyGameData(164118757)
>```
>
>Example Output
>```
> Saved
>```
This function will save the games data in a sort of cache to be accessed when needed. This is the data which this function will collect and be used as needed:
> * maxPlayerCount
>  * socialSlotType
>  * customSocialSlotsCount
>  * allowCopying
>  * currentSavedVersion
>  * name
>  * isRootPlace
>  * descriptionisRootPlace

These variables can then be used as needed such as the following
```python
print(robloxpy.Game.Internal.MyGame.maxPlayerCount)
```

#### External
* **GetUniverseData(UniverseID)**
This function will provide a range of data for a game which you can then parse to get what information you need.
>Example Usage
>```python
>robloxpy.Game.External.GetUniverseData(1069201198)
>```
>
>Example Output
>```
> {'id': 1069201198, 'rootPlaceId': 2960777560, 'name': '🎄CHRISTMAS🎄Treasure Quest', 'description': '❗ Christmas Event ends on Friday, January 29
>th! ❗ \r\n\r\n🎉 UPDATE 28!🎉\r\n❄️ New event boss! Team up to defeat Hyperfrost and earn limited time rewards!\r\n🍬 New Candy currency! Earn them from dungeons and quests!\r\n🎄 New Event shop! Limited time items that can be purchased using Candy!\r\n☃️ New Winter Lobby!\r\n🎁 New Orname
>nt Hunt around the lobby! Find all 6 for a limited time cosmetic!\r\n🏆 New Prize Wheel items!\r\n⚡ New Energy Blade Quest rewards!\r\n🛠️ 4 new  
>crafting recipes!\r\n💀 New Miniboss - Tank!\r\n💥 New Ability - Stomp!\r\n💰 New Mythical Festive Pack!\r\n\r\n⚔️ Welcome to Treasure Quest! Ste
>al treasure, battle monsters, and complete unique quests as you and your friends become the ultimate treasure hunters! Fight as a Wizard or a Warrior, the choice is yours!\r\n\r\n🎁 Join the group "Nosniy Games" for a Chat tag, Royalty Sword, and the ability to spin the Prize Wheel in the 
>game!\r\nhttps://www.roblox.com/groups/3461453/CLICK-HERE', 'creator': {'id': 3461453, 'name': 'Nosniy Games™', 'type': 'Group'}, 'price': None, 
>'allowedGearGenres': ['RPG'], 'allowedGearCategories': [], 'playing': 1463, 'visits': 247185224, 'maxPlayers': 40, 'created': '2019-03-15T04:27:24.327Z', 'updated': '2021-01-25T05:40:11.4420701Z', 'studioAccessToApisAllowed': False, 'createVipServersAllowed': False, 'universeAvatarType': 'MorphToR15', 'genre': 'RPG'}
>```

* **GetUniverseVotes(UniverseID)**
This function will return data about the votes of a game
>Example Usage
>```python
>robloxpy.Game.External.GetUniverseVotes(1069201198)
>```
>
>Example Output
>```
> {'id': 1069201198, 'upVotes': 170780, 'downVotes': 25066}
>```

* **GetCurrentUniversePlayers(UniverseID)**
This function will return the amount of players in a game
>Example Usage
>```python
>robloxpy.Game.External.GetCurrentUniversePlayers(164118757)
>```
>
>Example Output
>```
> 52
>```

* **GetGameVisits(UniverseID)**
This function will return the amount of visits a game has
>Example Usage
>```python
>robloxpy.Game.Internal.GetGameVisits(164118757)
>```
>
>Example Output
>```
> 97
>```

* **GetUniverseFavourites(UniverseID)**
This function will return the amount of likes a game has
>Example Usage
>```python
>robloxpy.Game.External.GetUniverseFavourites(164118757)
>```
>
>Example Output
>```
> 643534
>```

* **GetUniverseVisits(UniverseID)**
This function will return the amount of visits a game has
>Example Usage
>```python
>robloxpy.Game.External.GetUniverseVisits(164118757)
>```
>
>Example Output
>```
> 24536342543
>```

* **GetCurrentUniversePlayers(UniverseID)**
This function will return the amount of current players a game has
>Example Usage
>```python
>robloxpy.Game.External.GetCurrentUniversePlayers(164118757)
>```
>
>Example Output
>```
> 8535
>```

* **GetUniverseLikes(UniverseID)**
This function will return the amount of likes a game has
>Example Usage
>```python
>robloxpy.Game.External.GetUniverseLikes(164118757)
>```
>
>Example Output
>```
> 85
>```

* **GetUniverseDislikes(UniverseID)**
This function will return the amount of dislikes a game has
>Example Usage
>```python
>robloxpy.Game.External.GetUniverseDislikes(164118757)
>```
>
>Example Output
>```
> 73
>```

### Group
The Group functions are aimed towards gathering data from groups. These functions allow you get all the data needed about groups. This section contains bugs which will be fixed shortly.

**THIS SECTION OF ROBLOXPY IS PLANNED TO CHANGE IN NEAR FUTURE UPDATES**

#### Internal
_There are currently no Internal functions_
#### External
These functions allow you gather group data without needing an active cookie set
* **IsGroupOwned(GroupID)**
This function whether a group is current owned
>Example Usage
>```python
>robloxpy.Group.External.IsGroupOwned(916576)
>```
>
>Example Output
>```
> True
>```

* **GetName(GroupID)**
This function returns the name of a group
>Example Usage
>```python
>robloxpy.Group.External.GetName(916576)
>```
>
>Example Output
>```
> NEVER WALK ALONE
>```

* **GetOwner(GroupID)**
This function returns the name of an owner of a group
>Example Usage
>```python
>robloxpy.Group.External.GetOwner(916576)
>```
>
>Example Output
>```
> kristan99
>```

* **GetDescription(GroupID)**
This function provides the description of a group
>Example Usage
>```python
>robloxpy.Group.External.GetDescription(916576)
>```
>
>Example Output
>```
> [NWA]Never Walk Alone
>NWA is a PMC style group that aims for perfection and are looking for all types of members to join to help us with our goal.
>
>We like active members at NWA and have a wide range of bots to help the group function with things such as
> - Automatic Promotion
 >- Inactivity Detector
>
>[Automatic Promotions]
>{Temp Down Will Be Up Within 1 Week}
>
>[Inactivity Kicked]
>{Online - Set to 30 Days}
>```

* **GetEmblem(GroupID)**
This function will provide a url to a group emblem
>Example Usage
>```python
>robloxpy.Group.External.GetEmblem(916576)
>```
>
>Example Output
>```
> http://www.roblox.com/asset/?id=176186568
>```

* **GetRoles(GroupID)**
This function is to generate the roles and a permission value
>Example Usage
>```python
>robloxpy.Group.External.GetRoles(916576)
>```
>
>Example Output
>```
> (['[LR I] Recruit', '[LR II] Trooper', '[LR III] Specialist', '[MR I] Squad Leader', '[MR II] Operative', '[OiT] Officer in Training', '[MP]Military Police', '[HR I] Officer', '[HR II] Chief', '[GN I] Lieutenant General', '[GN II] General', '[DP] Diplomat', '[HC] High Command', '[CC] Co - 
>Commander', '[CM] Commander'], [1, 180, 190, 195, 196, 200, 205, 210, 220, 230, 240, 245, 250, 254, 255])
>```

* **GetAllies(GroupID)**
This function to generate a allies list of a group
>Example Usage
>```python
>robloxpy.Group.External.GetAllies(916576)
>```
>
>Example Output
>```
> ['Akios', 'Dank']
>```

* **GetEnemies(GroupID)**
This function to generate a enemies list of a group
>Example Usage
>```python
>robloxpy.Group.External.GetEnemies(916576)
>```
>
>Example Output
>```
> ["US Military 1940's", 'United Alliance Of Roblox']
>```

* **GetMemberCount(GroupID)**
This function to provide total members in a group
>Example Usage
>```python
>robloxpy.Group.External.GetMemberCount(916576)
>```
>
>Example Output
>```
> 2347
>```

* **isPublic(GroupID)**
This function whether a group is availible to join by anyone
>Example Usage
>```python
>robloxpy.Group.External.isPublic(916576)
>```
>
>Example Output
>```
> BUG
>```

* **isBCOnly(GroupID)**
This function whether a group is only availible to join by BC members
>Example Usage
>```python
>robloxpy.Group.External.isBCOnly(916576)
>```
>
>Example Output
>```
> BUG
>```

* **GetMembersList(GroupID,Limit)**
This function will generate a members list, the limit is optional; if none if provided it will generate a full list from the group
>Example Usage
>```python
>robloxpy.Group.External.GetMemberCount(916576,20)
>```
>
>Example Output
>```
> BUG
>```

* **GetMembersinRoleList(GroupID,RoleID,Limit)**
This function will generate a members list from a specifc role, the limit is optional; if none if provided it will generate a full list from the group
>Example Usage
>```python
>robloxpy.Group.External.GetMembersinRoleList(916576,32148,100)
>```
>
>Example Output
>```
> BUG
>```

### Market
The Market functions are based around the roblox market place. These functions allow you to make actions on these items as well retrieve data from each.

#### Internal
* **BuyItem(MarketID)**
This function will buy the item denoted by the market id
>Example Usage
>```python
>robloxpy.Market.Internal.BuyItem(363119963)
>```
>
>Example Output
>```
> True

#### External
* **CanManageAsset(UserID,AssetID)**
This function will return if a user can manage a selected asset
>Example Usage
>```python
>robloxpy.Market.External.CanManageAsset(1368140,363119963)
>```
>
>Example Output
>```
> Purchased

* **GetLimitedPriceData(LimitedID)**
This function will return a set of data points of the limited price over time
>Example Usage
>```python
>robloxpy.Market.External.GetLimitedPriceData(1081300)
>```
>
>Example Output
>```
> [{'value': 1826, 'date': '2021-01-25T06:00:00Z'}, {'value': 1648, 'date': '2021-01-24T06:00:00Z'}, {'value': 1767, 'date': '2021-01-23T06:00:00Z'}, {'value': 1984, 'date': '2021-01-22T06:00:00Z'}, {'value': 1786, 'date': '2021-01-21T06:00:00Z'}, {'value': 1599, 'date': '2021-01-20T06:00:00Z'}, {'value': 1604, 'date': '2021-01-19T06:00:00Z'}, {'value': 1736, 'date': '2021-01-18T06:00:00Z'}, {'value': 1889, 'date': '2021-01-17T06:00:00Z'}, {'value': 1798, 'date': '2021-01-16T06:00:00Z'}, {'value': 1892, 'date': '2021-01-15T06:00:00Z'}, {'value': 2041, 'date': '2021-01-14T06:00:00Z'}, {'value': 1796, 'date': '2021-01-13T06:00:00Z'}, {'value': 1843, 'date': '2021-01-12T06:00:00Z'}, {'value': 1834, 'date': '2021-01-11T06:00:00Z'}, {'value': 2081, 'date': '2021-01-10T06:00:00Z'}, {'value': 1931, 'date': '2021-01-09T06:00:00Z'}, {'value': 2110, 'date': '2021-01-08T06:00:00Z'}, {'value': 1871, 'date': '2021-01-07T06:00:00Z'}, {'value': 1983, 'date': '2021-01-06T06:00:00Z'}, {'value': 1971, 'date': '2021-01-05T06:00:00Z'}, {'value': 2048, 'date': '2021-01-04T06:00:00Z'}, {'value': 2055, 'date': '2021-01-03T06:00:00Z'}, {'value': 2251, 'date': '2021-01-02T06:00:00Z'}, {'value': 2458, 'date': '2021-01-01T06:00:00Z'}, {'value': 3541, 'date': '2020-12-31T06:00:00Z'}, {'value': 2239, 'date': '2020-12-30T06:00:00Z'}, {'value': 2041, 'date': '2020-12-29T06:00:00Z'}, {'value': 2519, 'date': '2020-12-28T06:00:00Z'}, {'value': 2224, 'date': '2020-12-27T06:00:00Z'}, {'value': 2570, 'date': '2020-12-26T06:00:00Z'}, {'value': 2725, 'date': '2020-12-25T06:00:00Z'}, {'value': 2137, 'date': '2020-12-24T06:00:00Z'}, {'value': 1781, 'date': '2020-12-23T06:00:00Z'}, {'value': 1611, 'date': '2020-12-22T06:00:00Z'}, {'value': 1819, 'date': 
>'2020-12-21T06:00:00Z'}, {'value': 1727, 'date': '2020-12-20T06:00:00Z'}, {'value': 1508, 'date': '2020-12-19T06:00:00Z'}, {'value': 1555, 'date': '2020-12-18T06:00:00Z'}, {'value': 1558, 'date': '2020-12-17T06:00:00Z'}, {'value': 1647, 'date': '2020-12-16T06:00:00Z'}, {'value': 1337, 'date': '2020-12-15T06:00:00Z'}, {'value': 1842, 'date': '2020-12-14T06:00:00Z'}, {'value': 1570, 'date': '2020-12-13T06:00:00Z'}, {'value': 1435, 'date': '2020-12-12T06:00:00Z'}, {'value': 1649, 'date': '2020-12-11T06:00:00Z'}, {'value': 1402, 'date': '2020-12-10T06:00:00Z'}, {'value': 1538, 
>'date': '2020-12-09T06:00:00Z'}, {'value': 1437, 'date': '2020-12-08T06:00:00Z'}, {'value': 1333, 'date': '2020-12-07T06:00:00Z'}, {'value': 1534, 'date': '2020-12-06T06:00:00Z'}, {'value': 1182, 'date': '2020-12-05T06:00:00Z'}, {'value': 1382, 'date': '2020-12-04T06:00:00Z'}, {'value': 1515, 'date': '2020-12-03T06:00:00Z'}, {'value': 1467, 'date': '2020-12-02T06:00:00Z'}, {'value': 1606, 'date': '2020-12-01T06:00:00Z'}, {'value': 
>1428, 'date': '2020-11-30T06:00:00Z'}, {'value': 1598, 'date': '2020-11-29T06:00:00Z'}, {'value': 1614, 'date': '2020-11-28T06:00:00Z'}, {'value': 3101, 'date': '2020-11-27T06:00:00Z'}, {'value': 1503, 'date': '2020-11-26T06:00:00Z'}, {'value': 1383, 'date': '2020-11-25T06:00:00Z'}, {'value': 1455, 'date': '2020-11-24T06:00:00Z'}, {'value': 1217, 'date': '2020-11-23T06:00:00Z'}, {'value': 1425, 'date': '2020-11-22T06:00:00Z'}, {'value': 1587, 'date': '2020-11-21T06:00:00Z'}, {'value': 2308, 'date': '2020-11-20T06:00:00Z'}, {'value': 1557, 'date': '2020-11-19T06:00:00Z'}, {'value': 1401, 'date': '2020-11-18T06:00:00Z'}, {'value': 1388, 'date': '2020-11-17T06:00:00Z'}, {'value': 1631, 'date': '2020-11-16T06:00:00Z'}, 
>{'value': 1811, 'date': '2020-11-15T06:00:00Z'}, {'value': 1583, 'date': '2020-11-14T06:00:00Z'}, {'value': 1366, 'date': '2020-11-13T06:00:00Z'}, {'value': 1197, 'date': '2020-11-12T06:00:00Z'}, {'value': 1426, 'date': '2020-11-11T06:00:00Z'}, {'value': 1494, 'date': '2020-11-10T06:00:00Z'}, {'value': 1594, 'date': '2020-11-09T06:00:00Z'}, {'value': 1526, 'date': '2020-11-08T06:00:00Z'}, {'value': 1347, 'date': '2020-11-07T06:00:00Z'}, {'value': 1355, 'date': '2020-11-06T06:00:00Z'}, {'value': 1315, 'date': '2020-11-05T06:00:00Z'}, {'value': 1204, 'date': '2020-11-04T06:00:00Z'}, {'value': 1016, 'date': '2020-11-03T06:00:00Z'}, {'value': 1332, 'date': '2020-11-02T06:00:00Z'}, {'value': 1274, 'date': '2020-11-01T05:00:00Z'}, {'value': 1407, 'date': '2020-10-31T05:00:00Z'}, {'value': 1270, 'date': '2020-10-30T05:00:00Z'}, {'value': 1205, 'date': '2020-10-29T05:00:00Z'}, {'value': 1216, 'date': '2020-10-28T05:00:00Z'}, {'value': 1246, 'date': '2020-10-27T05:00:00Z'}, {'value': 1124, 'date': '2020-10-26T05:00:00Z'}, {'value': 1338, 'date': '2020-10-25T05:00:00Z'}, {'value': 1107, 'date': '2020-10-24T05:00:00Z'}, {'value': 1164, 'date': '2020-10-23T05:00:00Z'}, {'value': 1089, 'date': '2020-10-22T05:00:00Z'}, {'value': 1041, 'date': '2020-10-21T05:00:00Z'}, {'value': 962, 'date': '2020-10-20T05:00:00Z'}, {'value': 1054, 'date': '2020-10-19T05:00:00Z'}, {'value': 1117, 'date': '2020-10-18T05:00:00Z'}, {'value': 1328, 'date': '2020-10-17T05:00:00Z'}, {'value': 1129, 'date': '2020-10-16T05:00:00Z'}, {'value': 1191, 'date': '2020-10-15T05:00:00Z'}, {'value': 1120, 'date': '2020-10-14T05:00:00Z'}, {'value': 1262, 'date': '2020-10-13T05:00:00Z'}, {'value': 1147, 'date': '2020-10-12T05:00:00Z'}, {'value': 1264, 'date': '2020-10-11T05:00:00Z'}, {'value': 988, 'date': '2020-10-10T05:00:00Z'}, {'value': 1467, 'date': '2020-10-09T05:00:00Z'}, {'value': 2389, 'date': '2020-10-08T05:00:00Z'}, {'value': 1283, 'date': '2020-10-07T05:00:00Z'}, {'value': 1078, 'date': '2020-10-06T05:00:00Z'}, {'value': 1404, 'date': '2020-10-05T05:00:00Z'}, {'value': 1312, 'date': '2020-10-04T05:00:00Z'}, {'value': 1305, 'date': '2020-10-03T05:00:00Z'}, {'value': 1234, 'date': '2020-10-02T05:00:00Z'}, {'value': 1222, 'date': '2020-10-01T05:00:00Z'}, {'value': 1166, 'date': '2020-09-30T05:00:00Z'}, {'value': 1082, 'date': '2020-09-29T05:00:00Z'}, {'value': 1081, 'date': '2020-09-28T05:00:00Z'}, {'value': 1311, 'date': '2020-09-27T05:00:00Z'}, {'value': 1378, 'date': '2020-09-26T05:00:00Z'}, {'value': 1374, 'date': '2020-09-25T05:00:00Z'}, {'value': 1252, 'date': '2020-09-24T05:00:00Z'}, {'value': 1271, 'date': '2020-09-23T05:00:00Z'}, {'value': 1206, 'date': '2020-09-22T05:00:00Z'}, {'value': 1290, 'date': '2020-09-21T05:00:00Z'}, {'value': 1101, 'date': '2020-09-20T05:00:00Z'}, {'value': 1065, 'date': '2020-09-19T05:00:00Z'}, {'value': 1229, 'date': '2020-09-18T05:00:00Z'}, {'value': 945, 'date': '2020-09-17T05:00:00Z'}, {'value': 1053, 'date': '2020-09-16T05:00:00Z'}, {'value': 1192, 'date': '2020-09-15T05:00:00Z'}, {'value': 
>1299, 'date': '2020-09-14T05:00:00Z'}, {'value': 1292, 'date': '2020-09-13T05:00:00Z'}, {'value': 1338, 'date': '2020-09-12T05:00:00Z'}, {'value': 1360, 'date': '2020-09-11T05:00:00Z'}, {'value': 1077, 'date': '2020-09-10T05:00:00Z'}, {'value': 1273, 'date': '2020-09-09T05:00:00Z'}, {'value': 1101, 'date': '2020-09-08T05:00:00Z'}, {'value': 1234, 'date': '2020-09-07T05:00:00Z'}, {'value': 1175, 'date': '2020-09-06T05:00:00Z'}, {'value': 1229, 'date': '2020-09-05T05:00:00Z'}, {'value': 1329, 'date': '2020-09-04T05:00:00Z'}, {'value': 1216, 'date': '2020-09-03T05:00:00Z'}, {'value': 1298, 'date': '2020-09-02T05:00:00Z'}, {'value': 1247, 'date': '2020-09-01T05:00:00Z'}, {'value': 1094, 'date': '2020-08-31T05:00:00Z'}, 
>{'value': 1178, 'date': '2020-08-30T05:00:00Z'}, {'value': 1176, 'date': '2020-08-29T05:00:00Z'}, {'value': 1190, 'date': '2020-08-28T05:00:00Z'}, {'value': 1257, 'date': '2020-08-27T05:00:00Z'}, {'value': 1094, 'date': '2020-08-26T05:00:00Z'}, {'value': 1113, 'date': '2020-08-25T05:00:00Z'}, {'value': 1057, 'date': '2020-08-24T05:00:00Z'}, {'value': 1279, 'date': '2020-08-23T05:00:00Z'}, {'value': 1289, 'date': '2020-08-22T05:00:00Z'}, {'value': 1109, 'date': '2020-08-21T05:00:00Z'}, {'value': 1054, 'date': '2020-08-20T05:00:00Z'}, {'value': 981, 'date': '2020-08-19T05:00:00Z'}, {'value': 1088, 'date': '2020-08-18T05:00:00Z'}, {'value': 1003, 'date': '2020-08-17T05:00:00Z'}, {'value': 1088, 'date': '2020-08-16T05:00:00Z'}, {'value': 1070, 'date': '2020-08-15T05:00:00Z'}, {'value': 968, 'date': '2020-08-14T05:00:00Z'}, {'value': 934, 'date': '2020-08-13T05:00:00Z'}, {'value': 919, 'date': '2020-08-12T05:00:00Z'}, {'value': 970, 'date': '2020-08-11T05:00:00Z'}, {'value': 909, 'date': '2020-08-10T05:00:00Z'}, {'value': 1046, 'date': '2020-08-09T05:00:00Z'}, {'value': 1038, 'date': '2020-08-08T05:00:00Z'}, {'value': 1098, 'date': '2020-08-07T05:00:00Z'}, {'value': 1062, 'date': '2020-08-06T05:00:00Z'}, {'value': 1138, 'date': '2020-08-05T05:00:00Z'}, {'value': 1072, 'date': '2020-08-04T05:00:00Z'}, {'value': 1080, 'date': '2020-08-03T05:00:00Z'}, {'value': 1161, 'date': '2020-08-02T05:00:00Z'}, {'value': 1227, 'date': '2020-08-01T05:00:00Z'}, {'value': 1169, 'date': '2020-07-31T05:00:00Z'}, {'value': 1023, 'date': '2020-07-30T05:00:00Z'}, {'value': 1017, 'date': '2020-07-29T05:00:00Z'}]
> ```

* **GetLimitedRemaining(LimitedID)**
This function the reaming limiteds for sale
>Example Usage
>```python
>robloxpy.Market.External.GetLimitedRemaining(1081300)
>```
>
>Example Output
>```
> 0
> ```

* **GetLimitedTotal(LimitedID)**
This function returns the total amount of the limited sold. If the item did not use to be limited this function will always return None
>Example Usage
>```python
>robloxpy.Market.External.GetLimitedTotal(1081300)
>```
>
>Example Output
>```
> None
> ```

* **GetLimitedSales(LimitedID)**
This function returns the total amount of the limited which are for sale currently.
>Example Usage
>```python
>robloxpy.Market.External.GetLimitedSales(1081300)
>```
>
>Example Output
>```
> 37813
> ```

* **GetLimitedRAP(LimitedID)**
This function returns the total recent average price of a limited in robux
>Example Usage
>```python
>robloxpy.Market.External.GetLimitedRAP(1081300)
>```
>
>Example Output
>```
> 1707
> ```

* **GetLimitedSalePrice(LimitedID)**
This function returns the price of a limited when it first went on sale, items which were not origionally limited will return None
>Example Usage
>```python
>robloxpy.Market.External.GetLimitedSalePrice(4390890198)
>```
>
>Example Output
>```
> 12000
> ```

* **GetLimitedChangePercentage(LimitedID)**
This function returns the price change of a limited price currently to what it origionally sold at
>Example Usage
>```python
>robloxpy.Market.External.GetLimitedChangePercentage(4390890198)
>```
>
>Example Output
>```
> 191.3%
> ```

* **GetAssetImage(LimitedID,Width,Height)**
This function returns the a link to the image of an asset
>Example Usage
>```python
>robloxpy.Market.External.GetAssetImage(4390890198,420,420)
>```
>
>Example Output
>```
> https://tr.rbxcdn.com/c4f5ec2e849306ebe3cb4dccaf1369f8/420/420/Hat/Png
> ```
