from . import group
from . import user
from . import Utils
from . import errors
from . import asset
from . import game
import requests
import sys

__version__ = "1.0.0.a1"

this = sys.modules[__name__]

this.CurrentCookie = None
this.RawCookie = None

def SetCookie(Cookie: str) -> None:
    """
    Set the current cookie for internal commands.
    """
    try:
        session = requests.session()
        CurrentCookie = {'.ROBLOSECURITY': Cookie}
        requests.utils.add_dict_to_cookiejar(session.cookies, CurrentCookie)
        Header = session.post('https://auth.roblox.com/')
        session.headers['x-csrf-token'] = Header.headers['x-csrf-token']
        session.headers["Origin"] = "https://www.roblox.com"
        session.headers["Referer"] = "https://www.roblox.com/"
    except:
        raise errors.InvalidCookie()
    if Utils.CheckCookie(Cookie) == False:
        raise errors.InvalidCookie()
    this.CurrentCookie = session
    this.RawCookie = Cookie
