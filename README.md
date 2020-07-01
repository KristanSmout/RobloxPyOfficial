# RobloxPyOfficial
 RobloxPy is a python API wrapper for the roblox web api's. This allows for quick and easy integration of these API's into a python project.
 
 ## Table of Contents


* [Getting Started](#Getting-Started)
  * [Prerequisites](#Prerequisites)
  * [Installation](#Installation)
* [Usage](#Usage)
  * [Current Features](#Features)
  * [Usage Examples](#Examples)
    * [External Functions](#External-Functions)
        * [User Functions](#User-Functions)
        * [Group Functions](#Group-Functions)
        * [Asset Functions](#Asset-Functions)


# Getting-Started
To use the wrapper you will need to download and import robloxpy into your current project. The project has not external requirements that is not included within the defaults of a python install.

## Prerequisites
N/A

## Installation
Before you can import robloxpy you will first need to install it through pip
```python
pip install robloxpy
```

If you wish to update robloxpy in the future you can also do this through pip
```python
pip install robloxpy --upgrade
```

# Usage
This section will cover what is currently supported by the API and how they can be used

# Features
* External
    * User
        * GetName(UserID)
        * IsOnline(UserID)
        * GetFriends(UserID)
        * GetOnlineFriends(UserID)
        * GetOfflineFriends(UserID)
        * GetUserGroups(UserID)
    * Group
        * GetGroupName(GroupID)
        * GetGroupDescription(GroupID)
        * GetGroupShout(GroupID)
        * IsGroupOpen(GroupID)
        * GetGroupMembers(GroupID)
        * GetGroupAllies(GroupID)
        * GetGroupEnemies(GroupID)
    * Assets
        * CanManage(UserID,GroupID)

# Examples
Below are examples of how to use each of the functions within robloxpy
# External-Functions
These functions do not require any cookies can be used without any data, these are limited to GET based on what roblox provides
* ## User-Functions
These functions allow you to get data in regards to a specific user through the use of their UserID
* GetName(int UserID)
```python
robloxpy.GetName(1368140) #Get the name of the roblox user with the ID of 1368140
Output > kristan99
```

* IsOnline(int UserID)
```python
robloxpy.IsOnline(1368140) #Check if the user with the ID 1368140 is online
Output > False
```

* GetFriends(int UserID)
```python
robloxpy.GetFriends(1368140) #Return a list of all friends of the roblox user with the ID 1368140
Output > ['SlimemingPlayz', 'E_xitium', 'Kawaii_Katicorn99', 'KatieeLouisee99', 'Yung_nignogpaddywog', 'BigDDave', 'Nosowl', 'Mirro_rs', 'Gareth1990', 'Voxxes', 'matantheman', 'ItzDishan', 'Xulfite', 'CinnabonNinja', 'hotrod56478', 'roxo_pl', 'VIPOrder', 'GlowwLikeThat', 'BritishP0litics', 'Nicolas9970', 'YunPlant', 'sirjoshh', 'iMistifye', 'Scorp1x', 'Fribbzdaman', 'xMcKenziee', 'AjinKovac', 'Angels_Develop', 'RonerRehnskiold', 'Natty32', 'agnen', 'yusufrad22', 'RocketValkyrie', 'methanshacked', 'GingyWyven', 'KingsmanSS', 'glitch19']
```
* GetOnlineFriends(int UserID)
```python
robloxpy.GetOnlineFriends(1368140) #Get a list of online friends of the roblox user with the ID 1368140
Output > ['Mirro_rs', 'Natty32']
```

* GetOfflineFriends(int UserID) 
```python
robloxpy.GetOfflineFriends(1368140) #Get a list of offline friends of the roblox user with the ID 1368140
Output > ['SlimemingPlayz', 'E_xitium', 'Kawaii_Katicorn99', 'KatieeLouisee99', 'Yung_nignogpaddywog', 'BigDDave', 'Nosowl', 'Gareth1990', 'Voxxes', 'matantheman', 'ItzDishan', 'Xulfite', 'CinnabonNinja', 'hotrod56478', 'roxo_pl', 'VIPOrder', 'GlowwLikeThat', 'BritishP0litics', 'Nicolas9970', 'YunPlant', 'sirjoshh', 'iMistifye', 'Scorp1x', 'Fribbzdaman', 'xMcKenziee', 'AjinKovac', 'Angels_Develop', 'RonerRehnskiold', 'agnen', 'yusufrad22', 'RocketValkyrie', 'methanshacked', 'GingyWyven', 'KingsmanSS', 'glitch19']
```

* GetUserGroups(int UserID) 
```python
robloxpy.GetUserGroups(1368140) #Get a list of groups which the user belongs too
Output > ['Simple Studio', 'BlackRock Studio', 'White Wolf Hounds', '🌶️Hot Pepper Clothes', 'Twisted Murdere r Official Group', 'StarCraft®', 'United Alliance Of Roblox', 'NEVER WALK ALONE']
```

* ## Group-Functions
These functions allow you to get data in regards to a specific group

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


