import robloxpy.Utils as Utils
import robloxpy.User.Internal as Internal

def Claim(GroupID):
     try:
        response = Internal.CurrentCookie.post(f"{Utils.GroupAPIV1}{GroupID}/claim-ownership")
        return 'Sent'
    except:
        return response.json()

def Join(GroupID):
     try:
        response = Internal.CurrentCookie.post(f"{Utils.GroupAPIV1}{GroupID}/users")
        return 'Sent'
    except:
        return response.json()

def Leave(GroupID):
     try:
        response = Internal.CurrentCookie.delete(f"{Utils.GroupAPIV1}{GroupID}/users/{Internal.UserID}")
        return 'Sent'
    except:
        return response.json()

def GetFunds(GroupID):
    try:
        response = Internal.CurrentCookie.delete(f"{Utils.EconomyURL}/groups/{GroupID}/currency/")
        return response.json()['robux']
    except:
        return response.json()

def Payout(GroupID,targetUserID,RobuxAmount):
    try:
        data = {
            "PayoutType": "FixedAmount",
            "Recipients": [
                {
                    "recipientId": str(UserID),
                    "recipientType": "User",
                    "amount": str(RobuxAmount)
                }
            ]
        }
        response = Internal.CurrentCookie.post(f"{utils.GroupAPIV1}{GroupID}/payouts", json=data)
        if(Post.status_code == 200):
            return 'Sent'
        else:
            return response.json()
    except Exception as e:
        return e

def PercentagePayout(GroupID,targetUserID,Percentage):
    try:
        data = {
            "PayoutType": "Percentage",
            "Recipients": [
                {
                    "recipientId": str(UserID),
                    "recipientType": "User",
                    "amount": str(Percentage)
                }
            ]
        }
        response = Internal.CurrentCookie.post(f"{utils.GroupAPIV1}{GroupID}/payouts", json=data)
        if(Post.status_code == 200):
            return 'Sent'
        else:
            return response.json()
    except Exception as e:
        return e

def SendWallPost(GroupID,PostText):
    try:
        response = Internal.CurrentCookie.post(f"{GroupAPIV1}{GroupID}/wall/posts", data={'body': PostText})
        return 'Sent'
    except:
        return response.json()

def SendGroupShout(GroupID,ShoutText):
    try:
        response = Internal.CurrentCookie.patch(f"{GroupAPIV1}{GroupID}/status", data={'message': ShoutText})
        return 'Sent'
    except:
        return response.json()

def ChangeDescription(GroupID, DescriptionText):
    try:
        response = Internal.CurrentCookie.patch(f"{GroupAPIV1}{GroupID}/description", data={'description': DescriptionText})
        return 'Sent'
    except:
        return response.json()

def ChangeRank(targetUserID,GroupID,RoleID):
    try:
        response = Internal.CurrentCookie.patch(f"{GroupAPIV1}{GroupID}/users/{targetUserID}", data={'roleId': roleId})
        return 'Sent'
    except:
        return response.json()





