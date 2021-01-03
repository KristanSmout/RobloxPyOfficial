import robloxpy.Utils as Utils
import robloxpy.User.Internal as Internal

def SendFriendRequest(targetUserID):
    """
    Send a friend request to the target
    """
    try:
        response = Internal.CurrentCookie.post(f"{Utils.FriendsAPI}users/{str(targetUserID)}/request-friendship", data={'targetUserID': targetUserID})
        try:
            return response.json()['success']
        except:
            return response.json()['errors']
    except Exception as e:
        return response.json()

def Unfriend(targetUserID):
    """
    Unfriend the target user
    """
    try:
        response = Internal.CurrentCookie.post(f"{Utils.FriendsAPI}users/{str(targetUserID)}/unfriend", data={'targetUserID': targetUserID})
        try:
            return response.json()['success']
        except:
            return response.json()['errors']
    except Exception as e:
        return response.json()

def TotalFriends():
    """
    Returns the total amount of friends
    """
    try:
        response = Internal.CurrentCookie.get(f"{Utils.FriendsAPI}my/friends/count")
        return response.json()['count']
    except:
        return response.json()