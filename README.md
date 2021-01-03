
# RobloxPy 0.2.0
RobloxPy is a python API wrapper for roblox. This allows for quick and easy integration of these API's into a python project.
<sup><center>If you need any help using RobloxPy or want to request an additional please join the discord server at https://www.kristansmout.com/discord
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
* Internal
	* 
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
	* IsOnline
	* Isbanned
	* GetDescription
	* GetAge
	* CreationDate
	* GetRAP
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
