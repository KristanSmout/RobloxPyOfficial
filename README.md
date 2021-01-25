
# RobloxPy 0.2.9
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

### User
The user functions are how you interact with specific users to gather data as well as how you interact with roblox as a specific user based on the currently used cookie.

#### Internal
* **SetCookie(Cookie,Details)**
This function will set the cookie to be used with any internal commands of robloxpy. The details argument is optional allowing you to pre-fill a wide range of data of the current account as the cookie is set 
>Example Usage
>```python
>robloxpy.User.Internal.SetCookie("_WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items._XXXXXXXXXXXXX",True)
>```
>
>Example Output
>```
> Cookie Set
> ```

The additional data that is set when you set a cookie is as follows:
> RawCookie
> UserID
> Username
> Robux
> Thumbnail
> isBuildersclub
> isPremium
> canChangeUsername
> isAdmin
> isEmailOnFile
> isEmailVerified
> isPhoneFeatureEnabled
> isSuperSafePrivacyMode
> IsAppChatSettingEnabled
> IsGameChatSettingEnabled
> IsContentRatingsSettingEnabled
> IsParentalControlsTabEnabled
> IsSetPasswordNotificationEnabled
> ChangePasswordRequiresTwoStepVerification
> ChangeEmailRequiresTwoStepVerification
> UserEmail
> UserEmailMasked
> UserEmailVerified
> CanHideInventory
> CanTrade
> MissingParentEmail
> IsUpdateEmailSectionShown
> IsUnder13UpdateEmailMessageSectionShown
> IsUserConnectedToFacebook
> IsTwoStepToggleEnabled
> AgeBracket
> UserAbove13
> ClientIpAddress
> UserAge
> IsBcRenewalMembership
> IsAccountPinEnabled
> IsAccountRestrictionsFeatureEnabled
> IsAccountRestrictionsSettingEnabled
> IsAccountSettingsSocialNetworksV2Enabled
> InApp
> HasFreeNameChange
> IsAgeDownEnabled
> ReceiveNewsletter

This data can be called as a standard variable as needed such as the following:
```python
print(robloxpy.User.Internal.CanTrade)
Output > True
```
* **GetDetails(Details)**
This function will collect the data of the current cookie, this is only useful is you decide not to collec it by default when setting the cookie.
>Example Usage
>```python
>robloxpy.User.Internal.GetDetails(True)
>```
>
>Example Output
>```
> Data Gathered
> ```

* **isFollowing(targetUserID)**
This function will check if the user is following a different user
>Example Usage
>```python
>robloxpy.User.Internal.isFollowing(1)
>```
>
>Example Output
>```
> True
> ```

* **FollowUser(targetUserID)**
This function will follow the target user
>Example Usage
>```python
>robloxpy.User.Internal.FollowUser(1)
>```
>
>Example Output
>```
> success
> ```

* **UnfollowUser(targetUserID)**
This function will unfollow the target user
>Example Usage
>```python
>robloxpy.User.Internal.UnfollowUser(1)
>```
>
>Example Output
>```
> success
> ```

* **BlockUser(targetUserID)**
This function will block the target user
>Example Usage
>```python
>robloxpy.User.Internal.BlockUser(1)
>```
>
>Example Output
>```
> success
> ```

* **UnblockUser(targetUserID)**
This function will unblock the target user
>Example Usage
>```python
>robloxpy.User.Internal.UnblockUser(1)
>```
>
>Example Output
>```
> success
> ```

* **GetBlockedUsers()**
This function will return a list of all blocked users
>Example Usage
>```python
>robloxpy.User.Internal.GetBlockedUsers
>```
>
>Example Output
>```
> ['Roblox','Builderman']
> ```

* **SendMessage(targetUserID,Subject,Body)**
This function will send a customised message to the target user
>Example Usage
>```python
>robloxpy.User.Internal.SendMessage(1,"HI THERE","This is a private message sent with robloxpy")
>```
>
>Example Output
>```
> Sent
> ```

* **JoinGame(PlaceID)**
This function will make the current user join a game
>Example Usage
>```python
>robloxpy.User.Internal.JoinGame(1762345)
>```
>
>Example Output
>```
> The game will open
> ```

### External
* **GetID(Username)**
This function will return the userID of a user based on their name
>Example Usage
>```python
>robloxpy.User.External.GetID("kristan99")
>```
>
>Example Output
>```
> 1368140
> ```

* **GetUserName(UserID)**
This function will return the username of a user based on their ID
>Example Usage
>```python
>robloxpy.User.External.GetID(1368140)
>```
>
>Example Output
>```
> kristan99
> ```

* **UsernameHistory(UserID)**
This function will return a username history of a user
>Example Usage
>```python
>robloxpy.User.External.UsernameHistory(1368140)
>```
>
>Example Output
>```
> ['kristan99']
> ```

* **IsOnline(UserID)**
This function will return if a user is seen as online
>Example Usage
>```python
>robloxpy.User.External.IsOnline(1368140)
>```
>
>Example Output
>```
> True
> ```

* **Isbanned(UserID)**
This function will return if a user is banned
>Example Usage
>```python
>robloxpy.User.External.Isbanned(1368140)
>```
>
>Example Output
>```
> False
> ```

* **GetDescription(UserID)**
This function will return a users description
>Example Usage
>```python
>robloxpy.User.External.GetDescription(1368140)
>```
>
>Example Output
>```
> No longer really play Roblox, I am however working on RobloxPy a python wrapper for Roblox. You can check it out on GitHub @KristanSmout or install through 'pip install robloxpy'
>
>I also provide python tutorials and free software on my youtube channel which you can find somewhere here :P
> ```

* **GetAge(UserID)**
This function will return a users age in days
>Example Usage
>```python
>robloxpy.User.External.GetAge(1368140)
>```
>
>Example Output
>```
> 4470
> ```

* **CreationDate(UserID,Style)**
This function will return a users creation date, if you use the wrong format and need the month first set the style to 1
>Example Usage
>```python
>robloxpy.User.External.CreationDate(1368140)
>```
>
>Example Output
>```
> 30/10/2008
> ```

* **GetRAP(UserID)**
This function will return the RAP of a user in robux
>Example Usage
>```python
>robloxpy.User.External.GetRAP(1368140)
>```
>
>Example Output
>```
> 432908
> ```

* **GetLimiteds(UserID)**
This function will return the an array of limiteds of a user and the corresponding item ID's
>Example Usage
>```python
>robloxpy.User.External.GetLimiteds(1368140)
>```
>
>Example Output
>```
>(['Racing Helmet', 'Summertime 2009 R&R&R', 'Tee Vee', 'Gobble Gobble', 'Gobble Gobble', 'Clown School Dropout', 'Chrome Egg of Speeding Bullet', 'Norseman', 'Fiery Egg of Egg Testing', 'Brass Top Hat', 'Crocheted Cthulhu', 'Staff of Celestial Light', 'Swordpack', 'Ornate Valkyrie', 'Police Badge', 'Shady Business Hat', 'Rogue Masquerader', "Cupid's Beloved Blade", "Cupid's Beloved Blade", "Cupid's Beloved Blade", "Cupid's Beloved 
>Blade", "Cupid's Beloved Blade", "Cupid's Beloved Blade", "Cupid's Beloved Blade", 'The Last Egg of 2013', 'Deluxe Game Headset', 'Green Starface ', 'Captain Steelshanks Recruiting Staff', 'Fawkes Face', 'Gold Visor', 'Mr X', 'Mr X', 'Egg of Verticality', 'Golden Crown', 'Classy ROBLOX Bow Tie', 'Furry Rock Star Hat', 'Skull of Robloxians Past', 'Halloween Baseball Cap 2014', "Merely's Green Sparkle Time Hoverboard", "St Patrick's 
>Day Fairy", 'Bluesteel Katana', 'Bluesteel Katana', 'Overseer Collar', 'Periastron Crown', 'True Love Smile', "Brighteyes' Top Hat", "Brighteye's Bloxy Cola Hat", 'Valkyrie Helm', 'Neon Green Beautiful Hair', 'Virtual Commando', 'The Crown of Warlords', 'Chiefjustus Gavel', 'ROBLOX Madness Face', "Overseer Warlord's Sword", 'Cursed Korblox Pendant ', 'Purple Wistful Wink', 'Blue Wistful Wink', 'Bacon Face', "DJ Remix's Goldphones", 'Red Goof ', 'Noob Attack: Laser Scythe Scuffle'], [6379764, 13334984, 15857936, 18448414, 18448414, 21392863, 24826640, 24941896, 27345567, 35685137, 35685477, 49491781, 19398258, 23634704, 82358339, 89624140, 93078804, 106064277, 106064277, 106064277, 106064277, 106064277, 106064277, 106064277, 111776247, 100425864, 119812738, 71597060, 134522901, 134087261, 125861676, 125861676, 152980639, 1081300, 162069243, 163496075, 181354245, 184745025, 215392741, 226189871, 243791145, 243791145, 343585127, 343585234, 362051405, 169454280, 24114402, 1365767, 151786902, 362081769, 2264398, 120749528, 130213380, 483308034, 483899424, 583722710, 583721561, 399021751, 102618797, 1191125008, 2566105661])
> ```

* **GetBust(UserID,Width,Height)**
This function will a url to a bust image of a user
>Example Usage
>```python
>robloxpy.User.External.GetBust(1368140)
>```
>
>Example Output
>```
> https://tr.rbxcdn.com/d4ff03e82298e804c89de3098e51abe6/420/420/AvatarBust/Png
> ```

* **GetHeadshot(UserID,Width,Height)**
This function will a url to a headshot image of a user
>Example Usage
>```python
>robloxpy.User.External.GetBust(1368140)
>```
>
>Example Output
>```
> https://tr.rbxcdn.com/b8864e930fcc0bfd4c3b19a558724841/420/420/AvatarHeadshot/Png
> ```

* **GetStatus(UserID)**
This function will return a users status
>Example Usage
>```python
>robloxpy.User.External.GetBust(1368140)
>```
>
>Example Output
>```
> Currently working on RobloxPy a python wrapper of the roblox API
> ```

* **DoesNameExist(username)**
This function will return if a name is being used or not
>Example Usage
>```python
>robloxpy.User.External.DoesNameExist("kristan99")
>```
>
>Example Output
>```
> Unavailible
> ```

### Friends
This is the sub category for functions for the user Friends.
### Internal
* **SendFriendRequest(UserID)**
This function will send a friend request to the target user
>Example Usage
>```python
>robloxpy.User.Friend.Internal.SendFriendRequest(1368140)
>```
>
>Example Output
>```
> Sent
> ```

* **Unfriend(UserID)**
This function will unfriend the target user
>Example Usage
>```python
>robloxpy.User.Friend.Internal.Unfriend(1368140)
>```
>
>Example Output
>```
> Sent
> ```

* **TotalFriends()**
This function will return a full list of a users friends
>Example Usage
>```python
>robloxpy.User.Friend.Internal.TotalFriends()
>```
>
>Example Output
>```
> 34
> ```

### External
* **GetAll(1368140)**
This function will return the total list of friends for the current user
>Example Usage
>```python
>robloxpy.User.Friend.External.GetAll(1368140)
>```
>
>Example Output
>```
> ['LocalFapper', 'SlimemingPlayz', 'E_xitium', 'Kawaii_Katicorn99', 'KatieeLouisee99', 'Yung_nignogpaddywog', 'BigDDave', 'Nosowl', 'Mirro_rs', 'Gareth1990', 'Voxxes', 'matantheman', 'ItzDishan', 'KioshiShimano', 'CinnabonNinja', 'roxo_pl', 'GlowwLikeThat', 'BritishP0litics', 'Nicolas9970', 'YunPlant', 'sirjoshh', 'iMistifye', 'Scorp1x', 'Fribbzdaman', 'xMcKenziee', 'AjinKovac', 'Angels_Develop', 'RonerRehnskiold', 'agnen', 'RocketValkyrie', 'methanshacked', 'GingyWyven', 'KingsmanSS', 'glitch19']
> ```

* **GetCount(UserID)**
This function will return the total number of friends for the current user
>Example Usage
>```python
>robloxpy.User.Friend.External.GetCount(1368140)
>```
>
>Example Output
>```
> 34
> ```

* **GetOnline(UserID)**
This function will return the total list of online friends for the current user
>Example Usage
>```python
>robloxpy.User.Friend.External.GetOnline(1368140)
>```
>
>Example Output
>```
> ['Mirro_rs', 'Angels_Develop']
> ```

* **GetOffline(UserID)**
This function will return the total list of offline friends for the current user
>Example Usage
>```python
>robloxpy.User.Friend.External.GetOffline(1368140)
>```
>
>Example Output
>```
> ['LocalFapper', 'SlimemingPlayz', 'E_xitium', 'Kawaii_Katicorn99', 'KatieeLouisee99', 'Yung_nignogpaddywog', 'BigDDave', 'Nosowl', 'Gareth1990', 
>'Voxxes', 'matantheman', 'ItzDishan', 'KioshiShimano', 'CinnabonNinja', 'roxo_pl', 'GlowwLikeThat', 'BritishP0litics', 'Nicolas9970', 'YunPlant', 'sirjoshh', 'iMistifye', 'Scorp1x', 'Fribbzdaman', 'xMcKenziee', 'AjinKovac', 'RonerRehnskiold', 'agnen', 'RocketValkyrie', 'methanshacked', 'GingyWyven', 'KingsmanSS', 'glitch19']
> ```

* **GetFollowerCount(UserID)**
This function will return the total follower count friends for the current user
>Example Usage
>```python
>robloxpy.User.Friend.External.GetOnline(1368140)
>```
>
>Example Output
>```
> 12607
> ```

* **GetFollowers(UserID,Amount)**
This function will return a list of users following a user, limit the list size using the amount variable. This function also provides the user ID's of the followers
>Example Usage
>```python
>robloxpy.User.Friend.External.GetOnline(1368140,10)
>```
>
>Example Output
>```
> (['builderman', 'Gaming112', 'snowbeat54321', 'BobHag', 'lilmigithunter', 'UchihaSasukePat', 'Alessi7953', 'GarraSabakuno', 'jangofettt', 'Garty983chub'], [156, 1359952, 2918062, 3149494, 2899616, 2937573, 2754369, 2982496, 20169, 169558])
> ```

* **GetFollowingCount(UserID)**
This function will return the total amount of users followed by the current user
>Example Usage
>```python
>robloxpy.User.Friend.External.GetFollowingCount(1368140)
>```
>
>Example Output
>```
> 16
> ```

* **GetFollowing(UserID,Amount)**
This function will return a list of users being followed by the user, limit the list size using the amount variable. This function also provides the user ID's of the followers
>Example Usage
>```python
>robloxpy.User.Friend.External.GetFollowing(1368140,10)
>```
>
>Example Output
>```
> (['takeovertom', 'dino5aur', 'iClanTech', '1waffle1', 'ForyxeV', 'Imaginze', 'StoryBased', 'LoneTraveler', 'beanme100', 'enyahs7'], [1096520, 649206, 65797433, 75323, 9622035, 17256624, 27572897, 3304627, 485933, 336048])
> ```

### Groups
This is the sub category for functions for the user Groups.
### Internal
* **Claim(GroupID)**
This function will attempt to claim an unowned group
>Example Usage
>```python
>robloxpy.User.Groups.Internal.Claim(916576)
>```
>
>Example Output
>```
> Sent
> ```

* **Join(GroupID)**
This function will attempt to Join a group
>Example Usage
>```python
>robloxpy.User.Groups.Internal.Join(916576)
>```
>
>Example Output
>```
> Join request sent
> ```

* **Leave(GroupID)**
This function will attempt to Leave a group
>Example Usage
>```python
>robloxpy.User.Groups.Internal.Leave(916576)
>```
>
>Example Output
>```
> Sent
> ```

* **GetFunds(GroupID)**
This function will attempt to get the group funds (You need permission to see them)
>Example Usage
>```python
>robloxpy.User.Groups.Internal.GetFunds(916576)
>```
>
>Example Output
>```
> 17290
> ```

* **Payout(GroupID,targetUserID,RobuxAmount)**
This function will attempt to payout a specific amount of the group funds (You need permission to do so)
>Example Usage
>```python
>robloxpy.User.Groups.Internal.Payout(916576,1368140,1000)
>```
>
>Example Output
>```
> Sent
> ```

* **PercentagePayout(GroupID,targetUserID,Percentage)**
This function will attempt to payout a specific percentage of the group funds (You need permission to do so)
>Example Usage
>```python
>robloxpy.User.Groups.Internal.Payout(916576,1368140,5)
>```
>
>Example Output
>```
> Sent
> ```

* **SendWallPost(GroupID,PostText)**
This function will attempt to post on the group wall
>Example Usage
>```python
>robloxpy.User.Groups.Internal.SendWallPost(916576,"Hello World")
>```
>
>Example Output
>```
> Sent
> ```

* **SendGroupShout(GroupID,ShoutText)**
This function will attempt to post on the group wall
>Example Usage
>```python
>robloxpy.User.Groups.Internal.SendGroupShout(916576,"Hello World")
>```
>
>Example Output
>```
> Sent
> ```

* **ChangeDescription(GroupID,DescriptionText)**
This function will attempt to post on the group wall
>Example Usage
>```python
>robloxpy.User.Groups.Internal.ChangeDescription(916576,"Hello World")
>```
>
>Example Output
>```
> Sent
> ```

* **ChangeRank(GroupID,targetUserID,RoleID)**
This function will attempt to post on the group wall
>Example Usage
>```python
>robloxpy.User.Groups.Internal.ChangeDescription(916576,1368140,15728)
>```
>
>Example Output
>```
> Sent
> ```



### External
* **GetGroups(UserID)**
This function will Returnsthe list of groups a user is in with the group ID's
>Example Usage
>```python
>robloxpy.User.Groups.External.GetGroups(1368140)
>```
>
>Example Output
>```
> (['Simple Studio', 'BlackRock Studio', 'White Wolf Hounds', '🌶️Hot Pepper Clothes', 'Twisted Murder er Official Group', 'StarCraft®', 'United Alliance Of Roblox', 'NEVER WALK ALONE'], [3297855, 847360, 1201505, 3206677, 1225381, 1132763, 14195, 916576])
> ```


These docs should be complete, if you find something that is not included in the documentation please let me know and I will add it when I get a chance. If you see anything in the documentation that is incorrect please also make me aware and I resolve it ASAP.