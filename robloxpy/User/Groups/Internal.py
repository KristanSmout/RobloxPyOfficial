import robloxpy.Utils as Utils
import robloxpy.User.Internal as Internal

def Claim(GroupID: int) -> str:
    try:
        response = Internal.CurrentCookie.post(f"{Utils.GroupAPIV1}{GroupID}/claim-ownership")
        return 'Sent'
    except:
        return response.json()

def Join(GroupID: int) -> str:
    try:
        response = Internal.CurrentCookie.post(f"{Utils.GroupAPIV1}{GroupID}/users")
        if('captcha test' in response.content.decode()): #Credit https://github.com/PurityWasHere
            return 'Captcha'
        else:
            return 'Join request sent'
    except:
        return response.json()

def Leave(GroupID: int) -> str:
    try:
        response = Internal.CurrentCookie.delete(f"{Utils.GroupAPIV1}{GroupID}/users/{Internal.UserID}")
        return 'Sent'
    except:
        return response.json()

def GetFunds(GroupID: int) -> int:
    try:
        response = Internal.CurrentCookie.get(f"{Utils.EconomyURL}/groups/{GroupID}/currency/")
        return response.json()['robux']
    except:
        return response.json()

def Payout(GroupID: int, targetUserID: int, RobuxAmount: int) -> str:
    try:
        data = {
            "PayoutType": "FixedAmount",
            "Recipients": [
                {
                    "recipientId": str(targetUserID),
                    "recipientType": "User",
                    "amount": str(RobuxAmount)
                }
            ]
        }
        response = Internal.CurrentCookie.post(f"{Utils.GroupAPIV1}{GroupID}/payouts", json=data)
        if(response.status_code == 200):
            return 'Sent'
        else:
            return response.json()
    except Exception as e:
        return e

def PercentagePayout(GroupID: int, targetUserID: int, Percentage: int) -> str:
    try:
        data = {
            "PayoutType": "Percentage",
            "Recipients": [
                {
                    "recipientId": str(targetUserID),
                    "recipientType": "User",
                    "amount": str(Percentage)
                }
            ]
        }
        response = Internal.CurrentCookie.post(f"{Utils.GroupAPIV1}{GroupID}/payouts", json=data)
        if(response.status_code == 200):
            return 'Sent'
        else:
            return response.json()
    except Exception as e:
        return e

def SendWallPost(GroupID: int, PostText: str) -> str:
    try:
        response = Internal.CurrentCookie.post(f"{Utils.GroupAPIV1}{GroupID}/wall/posts", data={'body': PostText})
        return 'Sent'
    except:
        return response.json()

def SendGroupShout(GroupID: int, ShoutText: str) -> str:
    try:
        response = Internal.CurrentCookie.patch(f"{Utils.GroupAPIV1}{GroupID}/status", data={'message': ShoutText})
        return 'Sent'
    except:
        return response.json()

def ChangeDescription(GroupID: int, DescriptionText: str) -> str:
    try:
        response = Internal.CurrentCookie.patch(f"{Utils.GroupAPIV1}{GroupID}/description", data={'description': DescriptionText})
        return 'Sent'
    except:
        return response.json()

def ChangeRank(GroupID: int, targetUserID: int, RoleID: int) -> str:
    try:
        response = Internal.CurrentCookie.patch(f"{Utils.GroupAPIV1}{GroupID}/users/{targetUserID}", data={'roleId': RoleID})
        return 'Sent'
    except:
        return response.json()



