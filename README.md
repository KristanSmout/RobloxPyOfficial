
# RobloxPy 1.0

RobloxPy is a python API wrapper for roblox. This allows for quick and easy integration of these API's into a python project.
<sup><center>If you need any help using RobloxPy or want to request an additional please join the discord server at 
	https://discord.gg/dSDc3vTWr9
Accept The Terms & Create a ticket</center></sup>

## BaseUser
* #### id - attr 
* #### name - attr 
* #### display_name - attr 
* #### description - attr
* #### created_at - attr
* #### banned - attr
* #### online - property
* #### name_history - property
* #### rap - property
* #### status - property
* #### headshot - property
* #### bust - property
* #### groups - method
* #### limiteds - method

## PartialUser
* #### id - attr 
* #### fetch - method (returns User)

## User (subclasses BaseUser)
* #### send_message - method
* #### follow method (captcha blocked, might be removed)
* #### unfollow - method
* #### block - method
* #### unblock - method

## ClientUser (subclasses BaseUser)
* #### following_user - method
* #### blocked_users - method
* #### join_game - method

## Group
* #### id - attr
* #### name - attr
* #### description - attr
* #### owner - attr
* #### member_count - attr
* #### builders_club_only - attr
* #### public_entry - attr
* #### members - method

## ImageAsset
* #### url - attr
* #### read - method
* #### save - method

## MarketAsset
* #### id - attr
* #### name - attr
* #### description - attr
* #### creator - attr
* #### lowest_price - attr
* #### favorites - attr
* #### thumbnail - method

## Place
* #### id - attr
* #### name - attr
* #### description - attr
* #### url - attr
* #### builder - attr (User)
* #### playable - attr
* #### universe - attr (Universe)
* #### price - attr
* #### playing - property
* #### visits - property
* #### favorites - property
* #### votes - property
* #### raw_votes - method (upvotes, downvotes))
* ####  join_game - method

## Universe
* #### id - attr
* #### name - attr
* #### description - attr
* #### creator - attr
* #### price - attr
* #### allowed_gear_genres - attr
* #### genre_enforced - attr
* #### copying_allowed - attr
* #### max_players - attr
* #### created_at - attr
* #### updated_at - attr
* #### vip_servers - attr
* #### avatar_type - attr
* #### genre - attr
* #### all_genre - attr
* #### rating - attr
* #### root_place - property
* #### playing - property
* #### visits - property
* #### favorites - property
* #### votes - property
* #### raw_votes - property
* #### icon - property
* #### join_game - method

## errors
* #### InvalidId
* #### InvalidName
* #### InvalidCookie
* #### NoCookie