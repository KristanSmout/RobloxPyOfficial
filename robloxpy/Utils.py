import requests,os
import robloxpy.User.Internal

TestCookie = ""


#URL List

MobileAPI = "https://www.roblox.com/mobileapi/"
FriendsAPI = "https://friends.roblox.com/v1/users/"
APIURL = "https://api.roblox.com/"
UserAPI = "https://api.roblox.com/users/"
UserAPIV1 = "https://users.roblox.com/v1/users/"
GroupAPIV1 = "https://groups.roblox.com/v1/groups/"
GroupAPIV2 = "https://groups.roblox.com/v2/"
EconomyURL = "https://economy.roblox.com/v1/"
EconomyURLV2 = "https://economy.roblox.com/v2/"
InventoryURL = "https://inventory.roblox.com/v2/assets/"
Inventory1URL = "https://inventory.roblox.com/v1/users/"
SettingsURL = "https://www.roblox.com/my/settings/json"
PrivateMessageAPIV1 = "https://privatemessages.roblox.com/v1/"
GamesAPI = "https://games.roblox.com/v1/"
DevelopAPIV2 = "https://develop.roblox.com/v2/"
GameAuthUrl = "https://auth.roblox.com/v1/authentication-ticket/"
ThumnnailAPIV1 = "https://thumbnails.roblox.com/v1/"



Version = "0.2.21"
WIP = "Not Implemented Yet"

def CheckForUpdate() -> str:
    """
    Returns whether a new version of robloxpy is availible.
    """
    response = requests.get('https://pypi.org/pypi/robloxpy/json')
    LatestVersion = response.json()['info']['version']
    if(Version == LatestVersion):
        return 'You are up to date!'
    else:
        return f'Version {LatestVersion} is now availible'

def GetVersion() -> str:
    """
    Returns the current version of robloxpy that is being used.
    """
    return Version

def UpdateInstructions(Version: str="Latest") -> str:
    """
    Provides Instructions to update robloxpy
    """
    Version = str(Version)
    if(Version == "Latest"):
        return "Update robloxpy through pip using following command: \n'pip install robloxpy --upgrade'"
    else:
        return f"This software is intended to work on robloxpy version {Version} please install using the following command \n'pip install robloxpy=={Version}'\n If you get an error with this command the developer of this tool has not provided a valid version"

def SetProxy(ProxyIP: str) -> None:
    """
    Set the proxy to currently be used, this is global
    Format: IP:Port
    """
    #Format 144.217.101.245:3129
    if(ProxyIP != None):
        proxy = 'http://' + str(ProxyIP)
        os.environ['http_proxy'] = proxy
        os.environ['https_proxy'] = proxy

def CheckProxy(proxyAddress: str = None) -> str:
    """
    Check the current IP address being given by the program
    """
    SetProxy(proxyAddress)
    response = requests.get('https://api.ipify.org/?format=json')
    return response.json()['ip']

def CheckCookie(Cookie: str = None) -> str:
    """
    If you want to check the current used cookie just run the function without any variable, if you wish to check a specific cookie then enter the cookie as a string
    """
    try:
        if(Cookie == None):
            session = robloxpy.User.Internal.CurrentCookie
        else:
            session = requests.session()
            CurrentCookie = {'.ROBLOSECURITY': Cookie}
            requests.utils.add_dict_to_cookiejar(session.cookies, CurrentCookie)
            Header = session.post('https://catalog.roblox.com/')
            session.headers['X-CSRF-TOKEN'] = Header.headers['X-CSRF-TOKEN']
        response = session.get(MobileAPI + 'userinfo')
        try:
            Temp = response.json()['UserID']
            #return response.json()
            return "Valid Cookie"
        except:
            return "Invalid Cookie"
    except:
        return "No Cookie Set"
