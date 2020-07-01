# RobloxPyOfficial
 RobloxPy is a python API wrapper for the roblox web api's. This allows for quick and easy integration of these API's into a python project.
 
 ## Table of Contents


* [Getting Started](#Getting-Started)
  * [Prerequisites](#Prerequisites)
  * [Installation](#Installation)
* [Usage](#Usage)
  * [Current Features](#Features)
  * [Usage Examples](#Examples)


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

# Examples
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
robloxpy.GetOfflineFriends(1368140) # Get a list of offline friends of the roblox user with the ID 1368140
Output > ['SlimemingPlayz', 'E_xitium', 'Kawaii_Katicorn99', 'KatieeLouisee99', 'Yung_nignogpaddywog', 'BigDDave', 'Nosowl', 'Gareth1990', 'Voxxes', 'matantheman', 'ItzDishan', 'Xulfite', 'CinnabonNinja', 'hotrod56478', 'roxo_pl', 'VIPOrder', 'GlowwLikeThat', 'BritishP0litics', 'Nicolas9970', 'YunPlant', 'sirjoshh', 'iMistifye', 'Scorp1x', 'Fribbzdaman', 'xMcKenziee', 'AjinKovac', 'Angels_Develop', 'RonerRehnskiold', 'agnen', 'yusufrad22', 'RocketValkyrie', 'methanshacked', 'GingyWyven', 'KingsmanSS', 'glitch19']
```

