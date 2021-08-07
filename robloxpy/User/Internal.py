import requests,json,random,webbrowser
from time import time
from robloxpy import Utils as Utils
from typing import Union

RawCookie = None
UserID = None
Username = None
Robux = None
Thumbnail = None
isBuildersclub = None
isPremium = None
canChangeUsername = None
isAdmin = None
isEmailOnFile = None
isEmailVerified = None
isPhoneFeatureEnabled = None
isSuperSafePrivacyMode = None
IsAppChatSettingEnabled = None
IsGameChatSettingEnabled = None
IsContentRatingsSettingEnabled = None
IsParentalControlsTabEnabled = None
IsSetPasswordNotificationEnabled = None
ChangePasswordRequiresTwoStepVerification = None
ChangeEmailRequiresTwoStepVerification = None
UserEmail = None
UserEmailMasked = None
UserEmailVerified = None
CanHideInventory = None
CanTrade = None
MissingParentEmail = None
IsUpdateEmailSectionShown = None
IsUnder13UpdateEmailMessageSectionShown = None
IsUserConnectedToFacebook = None
IsTwoStepToggleEnabled = None
AgeBracket = None
UserAbove13 = None
ClientIpAddress = None
UserAge = None
IsBcRenewalMembership = None
IsAccountPinEnabled = None
IsAccountRestrictionsFeatureEnabled = None
IsAccountRestrictionsSettingEnabled = None
IsAccountSettingsSocialNetworksV2Enabled = None
InApp = None
HasFreeNameChange = None
IsAgeDownEnabled = None
ReceiveNewsletter = None


def SetCookie(Cookie: str,Details: bool = True) -> str:
    """
    Set the current cookie for internal commands, if you wish to only perform an action set 'Details' to 'False' to prevent un-needed requests being made.
    """
    try:
        global RawCookie
        global CurrentCookie
        RawCookie = Cookie
        session = requests.session()
        CurrentCookie = {'.ROBLOSECURITY': Cookie}
        requests.utils.add_dict_to_cookiejar(session.cookies, CurrentCookie)
        Header = session.post('https://catalog.roblox.com/')
        session.headers['X-CSRF-TOKEN'] = Header.headers['X-CSRF-TOKEN']
        session.headers["Origin"] = "https://www.roblox.com"
        session.headers["Referer"] = "https://www.roblox.com/"
        CurrentCookie = session
        if(Utils.CheckCookie(CurrentCookie) == "Invalid"):
            return "Invalid Cookie"
        if(Details == True):
            GetDetails()
        else:
            GetDetails(False)
        return "Cookie Set"
    except:
        return "Error Setting Cookie"

def GetDetails(Details: bool = True) -> str:
    """
    Internal function to get the details of the current cookie, can be used if you have statements to determine if you want the details or not
    """
    global Gamesession
    global UserID
    global Username
    global Robux
    global Thumbnail
    global isBuildersclub
    global isPremium
    global canChangeUsername
    global isAdmin
    global isEmailOnFile
    global isEmailVerified
    global isPhoneFeatureEnabled
    global isSuperSafePrivacyMode
    global IsAppChatSettingEnabled
    global IsGameChatSettingEnabled
    global IsContentRatingsSettingEnabled
    global IsParentalControlsTabEnabled
    global IsSetPasswordNotificationEnabled
    global ChangePasswordRequiresTwoStepVerification
    global ChangeEmailRequiresTwoStepVerification
    global UserEmail
    global UserEmailMasked
    global UserEmailVerified
    global CanHideInventory
    global CanTrade
    global MissingParentEmail
    global IsUpdateEmailSectionShown
    global IsUnder13UpdateEmailMessageSectionShown
    global IsUserConnectedToFacebook
    global IsTwoStepToggleEnabled
    global AgeBracket
    global UserAbove13
    global ClientIpAddress #Shows the IP address roblox sees
    global UserAge
    global IsBcRenewalMembership
    global IsAccountPinEnabled
    global IsAccountRestrictionsFeatureEnabled
    global IsAccountRestrictionsSettingEnabled
    global IsAccountSettingsSocialNetworksV2Enabled
    global InApp
    global HasFreeNameChange
    global IsAgeDownEnabled
    global ReceiveNewsletter
    if(Details == True):
        try:
            SettingsContainer = CurrentCookie.get(Utils.SettingsURL)
            SettingsContainer = SettingsContainer.json()

            BasicContainer = CurrentCookie.get(Utils.MobileAPI + 'userinfo')
            BasicContainer = BasicContainer.json()

            UserID = BasicContainer['UserID']
            Username = BasicContainer['UserName']
            Robux = BasicContainer['RobuxBalance']
            Thumbnail = BasicContainer['ThumbnailUrl']
            isBuildersclub = BasicContainer['IsAnyBuildersClubMember']
            isPremium = BasicContainer['IsPremium']
            canChangeUsername = SettingsContainer['ChangeUsernameEnabled']
            isAdmin = SettingsContainer['IsAdmin']
            isEmailOnFile = SettingsContainer['IsEmailOnFile']
            isEmailVerified = SettingsContainer['IsEmailVerified']
            isPhoneFeatureEnabled = SettingsContainer['IsPhoneFeatureEnabled']
            isSuperSafePrivacyMode = SettingsContainer['UseSuperSafePrivacyMode']
            IsAppChatSettingEnabled = SettingsContainer['IsAppChatSettingEnabled']
            isGameChatSettingEnabled = SettingsContainer['IsGameChatSettingEnabled']
            isContentRatingsSettingEnabled = SettingsContainer['IsContentRatingsSettingEnabled']
            isParentalControlsTabEnabled = SettingsContainer['IsParentalControlsTabEnabled']
            isSetPasswordNotificationEnabled = SettingsContainer['IsSetPasswordNotificationEnabled']
            ChangePasswordRequiresTwoStepVerification = SettingsContainer['ChangePasswordRequiresTwoStepVerification']
            ChangeEmailRequiresTwoStepVerification = SettingsContainer['ChangeEmailRequiresTwoStepVerification']
            UserEmail = SettingsContainer['UserEmail']
            UserEmailMasked = SettingsContainer['UserEmailMasked']
            UserEmailVerified = SettingsContainer['UserEmailVerified']
            CanHideInventory = SettingsContainer['CanHideInventory']
            CanTrade = SettingsContainer['CanTrade']
            MissingParentEmail = SettingsContainer['MissingParentEmail']
            isUnder13UpdateEmailMessageSectionShown = SettingsContainer['IsUnder13UpdateEmailMessageSectionShown']
            isUserConnectedToFacebook = SettingsContainer['IsUserConnectedToFacebook']
            isUpdateEmailSectionShown = SettingsContainer['IsUpdateEmailSectionShown']
            isTwoStepToggleEnabled = SettingsContainer['IsTwoStepToggleEnabled']
            AgeBracket = SettingsContainer['AgeBracket']
            UserAbove13 = SettingsContainer['UserAbove13']
            ClientIpAddress = SettingsContainer['ClientIpAddress']
            UserAge = SettingsContainer['AccountAgeInDays']
            isBcRenewalMembership = SettingsContainer['IsBcRenewalMembership']
            isAccountPinEnabled = SettingsContainer['IsAccountPinEnabled']
            isAccountRestrictionsFeatureEnabled = SettingsContainer['IsAccountRestrictionsFeatureEnabled']
            isAccountRestrictionsSettingEnabled = SettingsContainer['IsAccountRestrictionsSettingEnabled']
            isAccountSettingsSocialNetworksV2Enabled = SettingsContainer['IsAccountSettingsSocialNetworksV2Enabled']
            InApp = SettingsContainer['InApp']
            HasFreeNameChange = SettingsContainer['HasFreeNameChange']
            isAgeDownEnabled = SettingsContainer['IsAgeDownEnabled']
            ReceiveNewsletter = SettingsContainer['ReceiveNewsletter']

            Gamesession = requests.session()
            Gamesession.cookies[".ROBLOSECURITY"] = RawCookie

            Gamesession = Gamesession.post(
            url = Utils.GameAuthUrl,
            headers = {
                "Referer": "https://www.roblox.com/",
                "X-CSRF-Token": Gamesession.post(
                    url = Utils.GameAuthUrl
                ).headers["X-CSRF-Token"],
            }
            ).headers["RBX-Authentication-Ticket"]

            return "Data Gathered"
        except Exception as e:
            return f"Error {e}"
    else:
        UserID = None
        Username = None
        Robux = None
        Thumbnail = None
        isBuildersclub = None
        isPremium = None
        canChangeUsername = None
        isAdmin = None
        isEmailOnFile = None
        isEmailVerified = None
        isPhoneFeatureEnabled = None
        isSuperSafePrivacyMode = None
        IsAppChatSettingEnabled = None
        IsGameChatSettingEnabled = None
        IsContentRatingsSettingEnabled = None
        IsParentalControlsTabEnabled = None
        IsSetPasswordNotificationEnabled = None
        ChangePasswordRequiresTwoStepVerification = None
        ChangeEmailRequiresTwoStepVerification = None
        UserEmail = None
        UserEmailMasked = None
        UserEmailVerified = None
        CanHideInventory = None
        CanTrade = None
        MissingParentEmail = None
        IsUpdateEmailSectionShown = None
        IsUnder13UpdateEmailMessageSectionShown = None
        IsUserConnectedToFacebook = None
        IsTwoStepToggleEnabled = None
        AgeBracket = None
        UserAbove13 = None
        ClientIpAddress #Shows the IP address roblox sees = None
        UserAge = None
        IsBcRenewalMembership = None
        IsAccountPinEnabled = None
        IsAccountRestrictionsFeatureEnabled = None
        IsAccountRestrictionsSettingEnabled = None
        IsAccountSettingsSocialNetworksV2Enabled = None
        InApp = None
        HasFreeNameChange = None
        IsAgeDownEnabled = None
        ReceiveNewsletter = None
        return "Data Not Wanted"

def isFollowing(targetUserID: int) -> Union[bool, str]:
    """
    Checks if the current account is following a user
    """
    try:
        response = CurrentCookie.get(f"{Utils.APIURL}user/following-exists?UserID={str(targetUserID)}&followerUserID={UserID}", data={'targetUserID': targetUserID})
        return response.json()['isFollowing']
    except Exception as e:
        return e

def FollowUser(targetUserID: int) -> Union[bool, str]:
    """
    Follows a user
    """
    try:
        response = CurrentCookie.post(f"{Utils.FriendsAPI}{str(targetUserID)}/follow", data={'targetUserID': targetUserID})
        try:
            return response.json()['success']
        except:
            return response.json()['errors']
    except Exception as e:
        return e

def UnfollowUser(targetUserID: int) -> Union[dict, str]:
    """
    unfollows a user
    """
    try:
        response = CurrentCookie.post(f"{Utils.FriendsAPI}{str(targetUserID)}/unfollow", data={'targetUserID': targetUserID})
        try:
            return response.json()['success']
        except:
            return response.json()['errors']
    except Exception as e:
        return response.json()

def BlockUser(targetUserID: int) -> Union[bool, str]:
    """
    Blocks a user
    """
    try:
        response = CurrentCookie.post(f"{Utils.APIURL}userblock/block?userId={str(targetUserID)}", data={'targetUserID': targetUserID})
        try:
            return response.json()['success']
        except:
            return response.json()['errors']
    except Exception as e:
        return response.json()

def GetBlockedUsers() -> Union[tuple, dict]:
    """
    Returns users which are blocked

    [UserID],[UserName]
    """
    try:
        response = CurrentCookie.get(f"{Utils.SettingsURL}")
        Data = response.json()['BlockedUsersModel']['BlockedUsers']
        BlockedIDs = []
        BlockedNames = []

        for User in Data:
            BlockedIDs.append(User['uid'])
            BlockedNames.append(User['Name'])
        return BlockedIDs, BlockedNames
    except:
        return response.json()

def UnblockUser(targetUserID: int) -> Union[bool, dict]:
    """
    unblocks a user
    """
    try:
        #response = CurrentCookie.post(f"{Utils.APIURL}userblock/unblock?userId={str(targetUserID)}", data={'targetUserID': targetUserID})
        response = CurrentCookie.post(f"https://accountsettings.roblox.com/v1/users/{targetUserID}/unblock", data={'targetUserID': targetUserID})
        try:
            return response.json()['success']
        except:
            return response.json()['errors']
    except Exception as e:
        return response.json()

def SendMessage(targetUserID: int, Subject: str, Body: str) -> Union[str, dict]:
    response = None
    try:
        response = CurrentCookie.post(Utils.PrivateMessageAPIV1 + 'messages/send/', data={
                            'userId': UserID,
                            'subject': Subject,
                            'body': Body,
                            'recipientid': targetUserID,
                            })
        return response.json()['message']
    except Exception as e:
        return response.json()

def JoinGame(PlaceId: int):
    BrowserID = random.randint(10000000000, 99999999999)
    webbrowser.open(f"roblox-player:1+launchmode:play+gameinfo:{Gamesession}+launchtime:{int(time()*1000)}+placelauncherurl:https%3A%2F%2Fassetgame.roblox.com%2Fgame%2FPlaceLauncher.ashx%3Frequest%3DRequestGame%26browserTrackerId%3D{BrowserID}%26placeId%3D{PlaceId}%26isPlayTogetherGame%3Dfalse+browsertrackerid:{BrowserID}+robloxLocale:en_us+gameLocale:en_us")

















