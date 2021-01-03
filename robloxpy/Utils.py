import requests,os
import robloxpy.User.Internal

TestCookie = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_72CF40D1580F4350501DF50BCD106230C1CF01A556822406213DE05D3816FD485802126A5561D4407F449FDC535799C2B1E01046F41332C3AB601402E7579BDA1B5E470A5B4D4BA429CAB1F9A88F4E3A4EFBC918DA6B33E3DC3A293AEA39CEFF7F1AA6900514F43319A76DCB5B8E8E42002DFCDB4AD740459AEE25F8A13D4D62257517FCFAD6A05BE76E33D102DF568FC11230B0126434FD63BD07F2D02BF9168DD9915FD42135F4937421A7B0FCA10D24D68BF5CEA0805676375916991D56ACA1EFDC4A6544ED5CA36CF38998D516D8E762C597B4187F07EA749FB3DD60696FA8DED8606BE897229F808F2E009A384C2701FD9F4C75E1720D9B521871A706840BE846A3426B546A12C46167C6953B5F4895E774592E9FE8D4325AC44D72274900FB256F"


#URL List

MobileAPI = "https://www.roblox.com/mobileapi/"
FriendsAPI = "https://friends.roblox.com/v1/users/"
APIURL = "https://api.roblox.com/"
UserAPI = "https://api.roblox.com/users/"
UserAPIV1 = "https://users.roblox.com/v1/users/"
GroupAPIV1 = "https://groups.roblox.com/v1/"
GroupAPIV2 = "https://groups.roblox.com/v2/"
EconomyURL = "https://economy.roblox.com/v1/"
EconomyURLV2 = "https://economy.roblox.com/v2/"
InventoryURL = "https://inventory.roblox.com/v2/assets/"
Inventory1URL = "https://inventory.roblox.com/v1/users/"
SettingsURL = "https://www.roblox.com/my/settings/json"
PrivateMessageAPIV1 = "https://privatemessages.roblox.com/v1/"
GamesAPI = "https://games.roblox.com/v1/"
GameAuthUrl = "https://auth.roblox.com/v1/authentication-ticket/"



Version = "0.2.0"
WIP = "Not Implemented Yet"

def CheckForUpdate():
    """
    Returns whether a new version of robloxpy is availible.
    """
    response = requests.get('https://pypi.org/pypi/robloxpy/json')
    LatestVersion = response.json()['info']['version']
    if(Version == LatestVersion):
        return 'You are up to date!'
    else:
        return f'Version {LatestVersion} is now availible'

def GetVersion():
    """
    Returns the current version of robloxpy that is being used.
    """
    return Version

def UpdateInstructions():
    """
    Provides Instructions to update robloxpy
    """
    return "Update robloxpy through pip using following command: \n'pip install robloxpy --upgrade'"

def SetProxy(ProxyIP):
    """
    Set the proxy to currently be used, this is global
    Format: IP:Port
    """
    #Format 144.217.101.245:3129
    if(ProxyIP != None):
        proxy = 'http://' + str(ProxyIP)
        os.environ['http_proxy'] = proxy
        os.environ['https_proxy'] = proxy

def CheckProxy(proxyAddress=None):
    """
    Check the current IP address being given by the program
    """
    SetProxy(proxyAddress)
    response = requests.get('https://api.ipify.org/?format=json')
    return response.json()['ip']

def CheckCookie(Cookie = None):
    """
    If you want to check the current used cookie just run the function without any variable, if you wish to check a specific cookie then enter the cookie as a string
    """
    try:
        if(Cookie == None):
            session = robloxpyreborn.User.Internal.CurrentCookie
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
