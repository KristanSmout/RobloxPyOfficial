

# RobloxPyOfficial - v0.1.7
 RobloxPy is a python API wrapper for the roblox web api's. This allows for quick and easy integration of these API's into a python project. This library also supports global proxy integration

<sup><center>If you need any help using RobloxPy or want to request an additional please join the discord server at https://www.kristansmout.com/discord</center></sup>
 
 ## Table of Contents


* [Getting Started](#Getting-Started)
  * [Prerequisites](#Prerequisites)
  * [Installation](#Installation)
  * [RobloxPy Features](#RobloxPy)
* [Usage](#Usage)
  * [Current Features](#Features)
  * [Usage Examples](#Examples)
	  * [Utilities](#Utilities)
    * [External Functions](#External-Functions)
        * [User Functions](#User-Functions)
            * [LimitedRelated](#Limited-Functions)
        * [Group Functions](#Group-Functions)
        * [Asset Functions](#Asset-Functions)
	        * [Limited Assets](#Limited-Assets) 
        * [Game Functions](#Place-Functions)
    * [Internal Functions](#Internal-Functions)
        * [User Functions](#Internal-User-Functions)
        * [Group Functions](#Internal-Group-Functions)
        * [Game Functions](#Internal-Game-Functions)

# Getting-Started
To use the wrapper you will need to download and import robloxpy into your current project. The project has not external requirements that is not included within the defaults of a python install.

## Prerequisites
```python
pip install requests
```

## Installation
Before you can import robloxpy you will first need to install it through pip
Requirements:
```python
pip install requests
```

```python
pip install robloxpy
```

If you wish to update robloxpy in the future you can also do this through pip
```python
pip install robloxpy --upgrade
```
# RobloxPy
RobloxPy includes some simple functions to help you get the information you need about it, these functions can be used as a check to ensure that the user is using a minimum version you deem necesarry for your RobloxPy project to work.

* CheckForUpdate
This function can provide two different outputs, one that the current version being used it the latest or the current version that is availible to update to
```python
robloxpy.CheckForUpdate()
Output > You are up to date!
```
```python
robloxpy.CheckForUpdate()
Output > Version 0.0.94 is now availible
```

* CheckVersion
```python
robloxpy.CheckVersion()
Output > 0.0.93
```

A function can also be called to give the user instructions on how to update RobloxPy. This function will provide the latest reccomended way to upgrade RobloxPy
* HowToUpdate
```python
robloxpy.HowToUpdate()
Output > pip install robloxpy --upgrade
```

# Usage
This section will cover what is currently supported by the API and how they can be used

# Features
* RobloxPy
  * CheckForUpdate()
  * CheckVersion()
  * HowToUpdate()
 * Utilities
	 * SetProxy(ProxyIP)
	 * CheckProxy(ProxyAddress) 
* External
    * User
        * NameToID(UserName) 
        * GetName(UserID)
        * DoesNameExist(UserName)
        * IsOnline(UserID)
        * GetFriends(UserID)
        * GetOnlineFriends(UserID)
        * GetOfflineFriends(UserID)
        * GetUserGroups(UserID)
        * DoesNameExist(UserName)
        * IsBanned(UserID)
        * AccountAgeDays(UserID)
        * UserCreationDate(UserID)
        * GetFollowingCount(UserID)
        * GetFollowersCount(UserID)
        * GetFollowers(UserID,Ammount)
        * GetFollowing(UserID,Ammount)
    * RAP
        * GetUserRap(UserID)
        * GetUserLimitedValue(UserID)
        * GetUserNoDemandLimiteds(UserID)
        * GetUserLowDemandLimiteds(UserID)
        * GetUserNormalDemandLimiteds(UserID)
        * GetUserGoodDemandLimiteds(UserID)
        * GetUserTerribleDemandLimiteds(UserID)
    * Group
        * IsGroupOwned(GroupID)
        * GetGroupName(GroupID)
        * GetGroupDescription(GroupID)
        * GetGroupShout(GroupID)
        * IsGroupOpen(GroupID)
        * GetGroupMembers(GroupID)
        * GetGroupAllies(GroupID)
        * GetGroupEnemies(GroupID)
    * Assets
        * CanManage(UserID,GroupID)
    * Limiteds
	    * GetLimitedRemaining(LimitedID)
	    * GetLimitedTotal(LimitedID)
	    * GetLimitedSales(LimitedID)
	    * GetLimitedRAP(LimitedID)
	    * GetLimitedSalePrice(LimitedID)
	    * GetLimitedChangePercentage(LimitedID)
    * Game
        * GetUniverseFavourites(UniverseID)
        * GetCurrentUniversePlayers(UniverseID)
        * GetUniverseVisits(UniverseID)
        * GetUniverseLikes(UniverseID)
        * GetUniverseDislikes(UniverseID)

* Internal
    * User
        * CheckCookie(Cookie)
        * GetUserID(Cookie)
        * GetUserName(Cookie)
        * GetEmail(Cookie)
        * IsEmailVerified(Cookie)
        * CanTrade(Cookie)
        * IsOver13(Cookie)
        * IsTwoStepEnabled(Cookie)
        * IsAccountPinEnabled(Cookie)
        * GetRobux(Cookie)
        * IsPremium(Cookie)
        * GetAvatar(Cookie)
        * IsFollowing(Cookie, UserID)
        * FollowUser(Cookie, UserID)
        * UnfollowUser(Cookie, UserID)
        * BlockUser(Cookie, UserID)
        * UnblockUser(Cookie, UserID)
        * SendFriendRequest(Cookie,UserID)
        * Unfriend(Cookie,UserID)
        * TotalFriends(Cookie)
        * GetBlockedUsers(Cookie)
        * SendMessage(Cookie,UserID,MessageSubject,Body)
    * Group
        * ClaimGroup(Cookie,GroupID)
        * JoinGroup(Cookie,GroupID)
        * LeaveGroup(Cookie,GroupID)
        * GetFunds(Cookie,GroupID)
        * PayGroupFunds(Cookie,GroupID,UserID,RobuxAmount)
        * PayGroupPercentage(Cookie,GroupID,UserID,Percentage)
        * PostGroupWall(Cookie,GroupID,Text)
        * ChangeGroupRank(Cookie,GroupID,UserID,RoleID)
    * Game
        * GetCurrentGamePlayers(Cookie,PlaceID)
        * GetGameVisits(Cookie,PlaceID)
        * GetGameLikes(Cookie,PlaceID)
        * GetGameDislikes(Cookie,PlaceID)
        * GetGameFavourites(Cookie,PlaceID)
        * ChangeGroupShout(Cookie,GroupID,StatusString)
        * ChangeGroupDescription(Cookie,GroupID,DescriptionString)

# Examples
Below are examples of how to use each of the functions within robloxpy
#Utilities
These functions are used by other functions within the library, You can use these separately  if needed but you don't need to specifically call them to use them.

# Utilities
* ## Proxy Functions
These functions are not needed to be used and can be called within functions in the last argument, they can also be used globally. When a proxy is set this will encompass all traffic in the application using this API even if any additional libraries do not support it.
* SetProxy(ProxyIP)
```python
robloxpy.SetProxy('127.0.0.1:1111') #Set global proxy for the current application
Output > None
```
* CheckProxy(ProxyAddress) 
```python
robloxpy.CheckProxy('127.0.0.1:1111') #Set and Check the shown address of the proxy address
Output > 127.0.0.1
```

```python
robloxpy.CheckProxy() #Check shown address of the currently used proxy
Output > 127.0.0.1
```

All functions can be run through a proxy, by adding an additional variable for the proxy if it is desired.
```python
robloxpy.GetName(1368140,'127.0.0.1:1111') #Run the function through the proxy 127.0.0.1:1111
Output > kristan99
```

# External-Functions
These functions do not require any cookies can be used without any data, these are limited to GET based on what roblox provides
* ## User-Functions
These functions allow you to get data in regards to a specific user through the use of their UserID or UserName

* NameToID(UserName) 
```python
robloxpy.NameToID('kristan99') #Get the UserID of the roblox user with the name kristan99
Output > 1368140
```

* GetName(UserID)
```python
robloxpy.GetName(1368140) #Get the name of the roblox user with the ID of 1368140
Output > kristan99
```

* DoesNameExist(UserName)
```python
robloxpy.DoesNameExist('kristan99') #Check if the username 'kristan99' is availible to take
Output > Unavailible
```

* IsOnline(UserID)
```python
robloxpy.IsOnline(1368140) #Check if the user with the ID 1368140 is online
Output > False
```

* GetFriends(UserID)
```python
robloxpy.GetFriends(1368140) #Return a list of all friends of the roblox user with the ID 1368140
Output > ['SlimemingPlayz', 'E_xitium', 'Kawaii_Katicorn99', 'KatieeLouisee99', 'Yung_nignogpaddywog', 'BigDDave', 'Nosowl', 'Mirro_rs', 'Gareth1990', 'Voxxes', 'matantheman', 'ItzDishan', 'Xulfite', 'CinnabonNinja', 'hotrod56478', 'roxo_pl', 'VIPOrder', 'GlowwLikeThat', 'BritishP0litics', 'Nicolas9970', 'YunPlant', 'sirjoshh', 'iMistifye', 'Scorp1x', 'Fribbzdaman', 'xMcKenziee', 'AjinKovac', 'Angels_Develop', 'RonerRehnskiold', 'Natty32', 'agnen', 'yusufrad22', 'RocketValkyrie', 'methanshacked', 'GingyWyven', 'KingsmanSS', 'glitch19']
```
* GetOnlineFriends(UserID)
```python
robloxpy.GetOnlineFriends(1368140) #Get a list of online friends of the roblox user with the ID 1368140
Output > ['Mirro_rs', 'Natty32']
```

* GetOfflineFriends(UserID) 
```python
robloxpy.GetOfflineFriends(1368140) #Get a list of offline friends of the roblox user with the ID 1368140
Output > ['SlimemingPlayz', 'E_xitium', 'Kawaii_Katicorn99', 'KatieeLouisee99', 'Yung_nignogpaddywog', 'BigDDave', 'Nosowl', 'Gareth1990', 'Voxxes', 'matantheman', 'ItzDishan', 'Xulfite', 'CinnabonNinja', 'hotrod56478', 'roxo_pl', 'VIPOrder', 'GlowwLikeThat', 'BritishP0litics', 'Nicolas9970', 'YunPlant', 'sirjoshh', 'iMistifye', 'Scorp1x', 'Fribbzdaman', 'xMcKenziee', 'AjinKovac', 'Angels_Develop', 'RonerRehnskiold', 'agnen', 'yusufrad22', 'RocketValkyrie', 'methanshacked', 'GingyWyven', 'KingsmanSS', 'glitch19']
```

* GetUserGroups(UserID) 
```python
robloxpy.GetUserGroups(1368140) #Get a list of groups which the user belongs too
Output > (['Simple Studio', 'BlackRock Studio', 'White Wolf Hounds', '🌶️Hot Pepper Clothes', 'Twisted Murder er Official Group', 'StarCraft®', 'United Alliance Of Roblox', 'NEVER WALK ALONE'], [3297855, 847360, 1201505, 3206677
 1225381, 1132763, 14195, 916576])
```

* IsBanned(UserID)
```python
robloxpy.IsBanned(1368140) # Get whether user ID belongs to a terminated account
Output > False
```

* AccountAgeDays(UserID)
```python
robloxpy.AccountAgeDays(1) #How many days ago was the account with the ID or 1 created
Output > 5246
```

* UserCreationDate(UserID,WantedData)
The WantedData variable for this function is not case sensistive however it must be spelt correctly
    * Year
    * Month
    * Day
```python
robloxpy.UserCreationDate(1,'Year') # Request the year the account was created
Output > 2006
```

* GetFollowingCount(UserID)
```python
robloxpy.GetFollowingCount(1368140) #Get ammount of followers of user 1368140
Output > 16
```

* GetFollowerCount(UserID)
```python
robloxpy.GetFollowingCount(1368140) #Get ammount of followers of user 1368140
Output > 12578
```

* GetFollowing(UserID,Ammount)
```python
robloxpy.GetFollowing(1368140,10) # Get first 10 people being followed by 1368140
Output > (['takeovertom', 'dino5aur', 'iClanTech', '1waffle1', 'ForyxeV', 'Imaginze', 'StoryBased', 'LoneTraveler', 'beanme100', 'enyahs7'], [1096520, 649206, 65797433, 75323, 9622035, 17256624, 27572897, 3304627, 485933, 336048])
```

* GetFollowers(UserID,Ammount)
```python
robloxpy.GetFollowing(1368140,10) # Get first 10 people being following user id 1368140
Output > (['builderman', 'Gaming112', 'snowbeat54321', 'BobHag', 'lilmigithunter', 'UchihaSasukePat', 'Alessi7953', 'GarraSabakuno', 'jangofettt', 'Garty983chub'], [156, 1359952, 2918062, 3149494, 2899616, 2937573, 2754369, 2982496, 20169, 169558])
```


* # Limited-Functions
These functions relate to getting the value of a user based on their limiteds
* GetUserRAP(UserID)
```python
robloxpy.GetUserRap(1368140) # Get the RAP of the user with the ID 1368140
Output > 298202
```

* GetUserLimitedValue(UserID)
```python
robloxpy.GetUserLimitedValue(1368140) # Get the RAP of the user with the ID 1368140
Output > 389539
```

All the functions to determine the quality of a users items are the same just switching the type each providing a similiar output
* GetUserNoDemandLimiteds(UserID)
* GetUserLowDemandLimiteds(UserID)
* GetUserNormalDemandLimiteds(UserID)
* GetUserGoodDemandLimiteds(UserID)
* GetUserTerribleDemandLimiteds(UserID)
```python
robloxpy.GetUserTerribleDemandLimiteds(1368140) # Get limiteds considered terrible and undesired by the user with the ID 1368140
Output > 0
```


* ## Group-Functions
These functions allow you to get data in regards to a specific group

IsGroupOwned(GroupID)
```python
robloxpy.IsGroupOwned(916576) # Check if the group of the ID 916576 is owned
Output > True
```
* GetGroupName(GroupID)
```python
robloxpy.GetGroupName(916576) # Get the name of the group of the ID 916576
Output > NEVER WALK ALONE
```

* GetGroupDescription(GroupID)
```python
robloxpy.GetGroupDescription(916576) # Get the description of the group of the ID 916576
Output > [NWA]Never Walk Alone
NWA is a PMC style group that aims for perfection and are looking for all types of members to join to help us with our goal.

We like active members at NWA and have a wide range of bots to help the group function with things such as
 - Automatic Promotion
 - Inactivity Detector

[Automatic Promotions]
{Temp Down Will Be Up Within 1 Week}

[Inactivity Kicked]
{Online - Set to 30 Days}
```

* GetGroupShout(GroupID)
```python
robloxpy.GetGroupShout(916576) # Get the current shout of the group of the ID 916576
Output > How are you?
```

* IsGroupOpen(GroupID)
```python
robloxpy.IsGroupOpen(916576) # Check if the group of the ID 916576 is open to join
Output > True
```

* GetGroupMembers(GroupID)
```python
robloxpy.GetGroupMembers(916576) # Get member count of the group of the ID 916576
Output > 1361
```
* GetGroupAllies(GroupID)
```python
robloxpy.GetGroupAllies(916576) # Get all the allies associated with the group of the ID 916576
Output > ['Akios', 'Dank']
```

* GetGroupEnemies(GroupID)
```python
robloxpy.GetGroupAllies(916576) # Get all the enemies associated with the group of the ID 916576
Output > ['United Alliance Of Roblox']
```

## Asset-Functions
These functions allow you to get data in regards to a specific asset

* CanManage(UserID,AssetID)
```python
robloxpy.CanManage(1368140,240351460)
Output > True
```
## Limited-Assets
These functions allow you to get information about Limited and LimitedU items that are sold on the roblox marketplace.

* GetLimitedPriceData(LimitedID)
```python
robloxpy.GetLimitedPriceData(102627682)
output> [{'value': 4880, 'date': '2020-08-25T05:00:00Z'}, {'value': 4879, 'date': '2020-08-23T05:00:00Z'}, {'value': 2300, 'date': '2020-08-22T05:00:00Z'}, {'value': 4850, 'date': '2020-08-21T05:00:00Z'}, {'value': 4250, 'date': '2020-08-20T05:00:00Z'}, {'value': 1000, 'date': '2020-08-18T05:00:00Z'}, {'value': 4224, 'date': '2020-08-17T05:00:00Z'}, {'value': 4249, 'date': '2020-08-15T05:00:00Z'}, {'value': 4249, 'date': '2020-08-12T05:00:00Z'}, {'value': 1847, 'date': '2020-08-08T05:00:00Z'}, {'value': 3077, 'date': '2020-08-05T05:00:00Z'}, {'value': 4000, 'date': '2020-07-26T05:00:00Z'}, {'value': 4498, 'date': '2020-07-23T05:00:00Z'}, {'value': 1891, 'date': '2020-07-20T05:00:00Z'}, {'value': 2249, 'date': '2020-07-17T05:00:00Z'}, {'value': 4200, 'date': '2020-07-12T05:00:00Z'}, {'value': 2021, 'date': '2020-07-11T05:00:00Z'}, {'value': 1660, 'date': '2020-07-08T05:00:00Z'}, {'value': 4849, 'date': '2020-07-06T05:00:00Z'}, {'value': 4300, 'date': '2020-07-05T05:00:00Z'}, {'value': 4290, 'date': '2020-07-04T05:00:00Z'}, {'value': 2627, 'date': '2020-07-02T05:00:00Z'}, {'value': 4224, 'date': '2020-06-30T05:00:00Z'}, {'value': 4254, 'date': '2020-06-29T05:00:00Z'}, {'value': 3500, 'date': '2020-06-28T05:00:00Z'}, {'value': 3000, 'date': '2020-06-21T05:00:00Z'}, {'value': 4289, 'date': '2020-06-19T05:00:00Z'}, {'value': 2000, 'date': '2020-06-16T05:00:00Z'}, {'value': 2129, 'date': '2020-06-15T05:00:00Z'}, {'value': 3400, 'date': '2020-06-13T05:00:00Z'}, {'value': 1500, 'date': '2020-06-12T05:00:00Z'}, {'value': 2150, 'date': '2020-06-10T05:00:00Z'}, {'value': 2500, 'date': '2020-06-08T05:00:00Z'}, {'value': 1505, 'date': '2020-06-03T05:00:00Z'}, {'value': 2000, 'date': '2020-05-30T05:00:00Z'}, {'value': 1999, 'date': '2020-05-27T05:00:00Z'}, {'value': 1850, 'date': '2020-05-26T05:00:00Z'}, {'value': 899, 'date': '2020-05-24T05:00:00Z'}, {'value': 1000, 'date': '2020-05-23T05:00:00Z'}, {'value': 1500, 'date': '2020-05-19T05:00:00Z'}, {'value': 899, 'date': '2020-05-13T05:00:00Z'}, {'value': 1323, 'date': '2020-05-07T05:00:00Z'}, {'value': 1181, 'date': '2020-05-03T05:00:00Z'}, {'value': 1222, 'date': '2020-04-30T05:00:00Z'}, {'value': 1000, 'date': '2020-04-28T05:00:00Z'}, {'value': 999, 'date': '2020-04-26T05:00:00Z'}, {'value': 1000, 'date': '2020-04-24T05:00:00Z'}, {'value': 1998, 'date': '2020-04-21T05:00:00Z'}, {'value': 1500, 'date': '2020-04-20T05:00:00Z'}, {'value': 977, 'date': '2020-04-19T05:00:00Z'}, {'value': 900, 'date': '2020-04-18T05:00:00Z'}, {'value': 1535, 'date': '2020-04-15T05:00:00Z'}, {'value': 920, 'date': '2020-04-13T05:00:00Z'}, {'value': 1143, 'date': '2020-04-11T05:00:00Z'}, {'value': 1999, 'date': '2020-04-10T05:00:00Z'}, {'value': 1499, 'date': '2020-04-05T05:00:00Z'}, {'value': 1599, 'date': '2020-03-30T05:00:00Z'}, {'value': 1500, 'date': '2020-03-29T05:00:00Z'}, {'value': 1350, 'date': '2020-03-25T05:00:00Z'}, {'value': 1366, 'date': '2020-03-24T05:00:00Z'}, {'value': 1100, 'date': '2020-03-23T05:00:00Z'}, {'value': 999, 'date': '2020-03-20T05:00:00Z'}, {'value': 1900, 'date': '2020-03-14T05:00:00Z'}, {'value': 1200, 'date': '2020-03-11T05:00:00Z'}, {'value': 1999, 'date': '2020-03-04T06:00:00Z'}, {'value': 1200, 'date': '2020-02-28T06:00:00Z'}]
```

*GetLimitedRemaining(LimitedID)
```python
robloxpy.GetLimitedRemaining(102627682)
output > 0
```

*GetLimitedTotal(LimitedID)
```python
robloxpy.GetLimitedTotal(102627682)
output > 750
```

*GetLimitedSales(LimitedID)
```python
robloxpy.GetLimitedSales(102627682)
output > 747
```

*GetLimitedRAP(LimitedID)
```python
robloxpy.GetLimitedRAP(102627682)
output > 3606
```

*GetLimitedSalePrice(LimitedID)
```python
robloxpy.GetLimitedSalePrice(102627682)
output > 500
```

*GetLimitedChangePercentage(LimitedID)
```python
robloxpy.GetLimitedChangePercentage(102627682)
output > 621.2%
```

## Game-Functions
These functions are to get data about roblox games, this functions require a universeID which can only be obtained when using a cookie. If you wish to automate this and instead use the GameID please use the [internal](#Internal-Game-Functions) version of these functions.

GetCurrentUniversePlayers(UniverseID)
```python
robloxpy.GetCurrentUniversePlayers(113491250) #Get current player count of the universe with the ID of 113491250
output > 6754
```

GetCurrentUniverseVisits(UniverseID)
```python
robloxpy.GetCurrentUniverseVisits(113491250) #Get the total visits of the universe with the ID of 113491250
output > 896375390
```

GetUniverseFavourites(UniverseID)
```python
robloxpy.GetUniverseFavourites(113491250) #Get favourites of the universe with the ID of 113491250
output > 3971956
```

GetUniverseLikes(UniverseID)
```python
robloxpy.GetUniverseLikes(113491250) #Get likes of the universe with the ID of 113491250
output > 1515099
```

GetUniverseDislikes(UniverseID
```python
robloxpy.GetUniverseDislikes(113491250) #Get favourites of the universe with the ID of 113491250
output > 113053
```

---
---
---
---
# Internal-Functions
These functions require a cookie of the user account they wish to be run on as a variable. These functions allow support for both POST and GET requests allowing actions to be taken on an account.
# Internal-User-Functions
These functions are specific to actions related to the account of the cookies being used.
Since roblox cookies are looooooong I will be using 'ExampleCookie' as a placeholder, below is an example of how you may do this within your program. This cookie is not real and randomly generated following the requirements
```python
ExampleCookie = '_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_A292F2A0D15508456743D0472FCBF81E081677B96500C348C08C6D3009975DA56D4D1BE762BB225C26A960FEC6746A932C46CFD7364B2F646758731949B6F8C8288F9C628D6AD4DB90C7F1A1BD1EA54AD4169C51AD081561E230C31974366ADEF1726A4490940262EB9D694457C58E48C8385C9D426F0C2A247206DF0E149F675107EB0B60DE5173E5D8556F93CFD6104E786727E6C86A8E8F4CF3B8DEEA0CCE447159BE0D7AB6E16FD193C85526E2BC928F7B90EA5146EC7A243AF98D72EDBCF2154839A8078DAA60F048FFDC67B7367C5E6EE6F7BC5AF902CAB331F66B96310015BB93225E9D4242CD5A4FC2D20321576D268F84A3EBBD752FA80CAF30D73525A9C764FFFE718345EF864235F910EAEB49ED5537AD2432A3A74F9A3AF1B4F5B9C5B2C0'
```

* CheckCookie(Cookie)
```python
robloxpy.CheckCookie(ExampleCookie) #Check if cookie is valid
Output > Valid
```


* GetUserID(Cookie)
```python
robloxpy.GetUserID(ExampleCookie) #Get ID of the current cookie in use
Output > 156
```

* GetUserName(Cookie)
```python
robloxpy.GetUserName(ExampleCookie) #Get Name of the current cookie in use
Output > Builderman
```

* GetEmail(Cookie)
```python
robloxpy.GetEmail(ExampleCookie) #Get Email of the current cookie in use
Output > Fa********@email.com
```

---
Each of these functions will return a true or false relevant to what is being checked
* IsEmailVerified(Cookie)
* CanTrade(Cookie)
* IsOver13(Cookie)
* IsTwoStepEnabled(Cookie)
* IsAccountPinEnabled(Cookie)
---
* GetRobux(Cookie)
```python
robloxpy.GetUserName(ExampleCookie) #Get Robux of the current cookie in use
Output > 5000
```
* IsPremium(Cookie)
```python
robloxpy.IsPremium(ExampleCookie) #Check if cookie user is premium
Output > True
```

RobloxPy has the ability to follow and unfollow users for the cookie currently being used, these functions will provide a true or false value based on if it was a success; alternatively any errors that occur will be returned to the user also.
* IsFollowing(Cookie, UserID)
```python
robloxpy.IsFollowing(ExampleCookie,1368140) #Check if cookie user is following user with the ID 1368140
Output > True
```

* FollowUser(Cookie, UserID)
```python
robloxpy.FollowUser(ExampleCookie,1368140) #Follow user with ID 1368140
Output > True
```

* UnfollowUser(Cookie, UserID)
```python
robloxpy.UnfollowUser(ExampleCookie,1368140) #Unfollow user with ID 1368140
Output > True
```
RobloxPy has the ability to block and unblock users for the cookie currently being used, these functions will provide a true or false value based on if it was a success; alternatively any errors that occur will be returned to the user also

* BlockUser(Cookie, UserID)
```python
robloxpy.BlockUser(ExampleCookie,1368140) #Block the user with ID 1368140
Output > True
```

* UnblockUser(Cookie, UserID)
```python
robloxpy.UnblockUser(ExampleCookie,1368140) #Unblock the user with ID 1368140
Output > True
```

Robloxpy allows you to send friend requests to users or to unfriend or cancel a friend request. The 'SendFriendRequest' function will provide the output of success or return an error message. The 'Unfriend' function will return either a sent confirmation or error depending on the response from the server.

* SendFriendRequest(Cookie, UserID)
```python
robloxpy.SendFriendRequest(ExampleCookie,1368140) #Send a friend request to the user with ID 1368140
Output > success
```

* Unfriend(Cookie, UserID)
```python
robloxpy.Unfriend(ExampleCookie,1368140) #Unfriend the user with ID 1368140
Output > sent
```

* TotalFriends(Cookie, UserID)
```python
robloxpy.TotalFriends(ExampleCookie) #Total friends of the local user
Output > 5
```

* GetBlockedUsers(Cookie)
This function allows you to get just the ID of the users or also the names by parsing the returning data from when called
```python
robloxpy.GetBlockedUsers(ExampleCookie) #Get a list of ID's and Names of users blocked by the cookie account
Output > [1267895826, 1604596527, 1731797857], ['MiguelXXcoolXXplayz', 'CaduboyYT', 'Edson5380']
```

* SendMessage(Cookie,UserID,MessageSubject,Body)
```python
robloxpy.* SendMessage(ExampleCookie,1368140,'Important Message','Hey I sent this message using robloxpy') #Send a message to the user of id 1368140 with the subject 'Important Message' and a body of text of 'Hey I sent this message using robloxpy'

Output > Success
```

# Internal-Group-Functions
The functions require the use of a cookie that can be used to get the information required.

* ClaimGroup(Cookie,GroupID)
```python
robloxpy.JoinGroup(ExampleCookie,916576) #Claim ownership of group with the ID 916576 if possible
Output > Sent
```

* JoinGroup(Cookie,GroupID)
```python
robloxpy.JoinGroup(ExampleCookie,916576) #Join group with the ID 916576 if possible
Output > Joined
```

* LeaveGroup(Cookie,GroupID)
```python
robloxpy.LeaveGroup(ExampleCookie,916576) #Leave group with the ID 916576 if possible
Output > Left
```

* GetFunds(Cookie,GroupID)
```python
robloxpy.GetFunds(ExampleCookie,916576) #Get funds of 916576 if they can be spent
Output > 583
```

RobloxPy supports the payout of group funds in both a percentage and value capacity. The functions also support a small ammount of error checking confirming if the payment was reported as being sent or not.
* PayGroupFunds(Cookie,GroupID,UserID,RobuxAmmount)
```python
robloxpy.PayGroupFunds(ExampleCookie,916576,1368140,100) #Get 100 robux from group ID 916576 if they can be spent
Output > Sent
```

* PayGroupPercentage(Cookie,GroupID,UserID,RobuxAmmount)
```python
robloxpy.PayGroupPercentage(ExampleCookie,916576,1368140,100) #Get 100 robux from group ID 916576 if they can be spent
Output > Sent
```

* PostGroupWall(Cookie,GroupID,Text)
```python
robloxpy.PostGroupWall(ExampleCookie,916576,'Hello World') #Send a post to the wall of group ID 916576
Output > Sent
```

ChangeGroupRank(Cookie,GroupID,UserID,RoleID)
```python
robloxpy.ChangeGroupRank(ExampleCookie,916576,1368140,5725003) #Change User 1368140 Role in group 916576 to RoleID 5725003
Output > Sent
```

ChangeGroupShout(Cookie,GroupID,StatusString)
```python
robloxpy.ChangeGroupShout(ExampleCookie,916576,'This is a new group shout') #Set the group shout to 'This is a new group shout' in the group with the ID 916576
Output > Sent
```
ChangeGroupDescription(Cookie,GroupID,DescriptionString)
```python
robloxpy.ChangeGroupDescription(ExampleCookie,916576,'This is a new group description') #Set the group shout to 'This is a new group description' in the group with the ID 916576
Output > Sent
```

## Internal-Game-Functions
These functions require the use of a cookie to authenticate with the roblox server to allow it to get the UniverseID for games, if you already have the UniverseeID you can use the [external functions](#Game-Functions) above.

* GetUniverseID(Cookie,GameID)
```python
robloxpy.GetUniverseID(ExampleCookie,292439477) #Convert GameID to UniverseID
Output > 113491250
```

* GetCurrentGamePlayers(Cookie,GameID)
```python
robloxpy.GetCurrentGamePlayers(ExampleCookie,292439477) #Get current playercount of game
Output > 6754
```

robloxpy.GetGameVisits(ExampleCookie,GameID)
``` python
robloxpy.GetGameVisits(ExampleCookie,292439477) #Get total visits of the game
output > 896375390
```

* GetGameLikes(Cookie,GameID)
```python
robloxpy.GetGameLikes(ExampleCookie,292439477) #Get game likes
Output > 1515099
```

* GetGameDislikes(Cookie,GameID)
```python
robloxpy.GetGameDislikes(ExampleCookie,292439477) #Get game dislikesD
Output > 113053
```

* GetGameFavourites(Cookie,GameID)
```python
robloxpy.GetGameFavourites(ExampleCookie,292439477) #Get game favourites
Output > 3971956
```

Licence : Attribution-NonCommercial-ShareAlike 4.0 International
