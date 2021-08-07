import requests,json
from robloxpy import Utils as Utils
from typing import Union

def CanManageAsset(UserID: int, AssetID: int) -> Union[bool, str]:
    """
    Returns whether a user can manage an asset
    """
    response = requests.get(Utils.APIURL + f"/users/{UserID}/canmanage/{AssetID}")
    try:
        return response.json()['CanManage']
    except:
        return response.json()['ErrorMessage']

def GetLimitedPriceData(LimitedID: int) -> list:
    """
    Returns price data of a limited
    """
    response = requests.get(Utils.EconomyURL + '/assets/' + str(LimitedID) + '/resale-data')
    return response.json()['priceDataPoints']

def GetLimitedRemaining(LimitedID: int) -> int:
    """
    Returns the amount of limiteds that are availible for sale
    """
    response = requests.get(Utils.EconomyURL + '/assets/' + str(LimitedID) + '/resale-data')
    return response.json()['numberRemaining']

def GetLimitedTotal(LimitedID: int) -> int:
    """
    Returns how many of a limited there are
    """
    response = requests.get(Utils.EconomyURL + '/assets/' + str(LimitedID) + '/resale-data')
    return response.json()['assetStock']

def GetLimitedSales(LimitedID: int) -> int:
    """
    Returns how many of a limited have been sold
    """
    response = requests.get(Utils.EconomyURL + '/assets/' + str(LimitedID) + '/resale-data')
    return response.json()['sales']

def GetLimitedRAP(LimitedID: int) -> int:
    """
    Returns the RAP of a limited
    """
    response = requests.get(Utils.EconomyURL + '/assets/' + str(LimitedID) + '/resale-data')
    return response.json()['recentAveragePrice']

def GetLimitedSalePrice(LimitedID: int) -> int:
    """
    Returns the sale price of a limited
    """
    response = requests.get(Utils.EconomyURL + '/assets/' + str(LimitedID) + '/resale-data')
    return response.json()['originalPrice']

def GetLimitedChangePercentage(LimitedID: int) -> str:
    """
    Returns the percentage change of the price of a limited
    """
    Change = round(((float(GetLimitedRAP(LimitedID))-GetLimitedSalePrice(LimitedID))/GetLimitedSalePrice(LimitedID))*100,3)
    return str(Change) + '%'

def GetAssetImage(AssetID,Width = 420,Height = 420) -> str:
    """
    Returns a url to an image of the limited

    Limited image size can be changed
    """
    response = requests.get(f"https://www.roblox.com/asset-thumbnail/image?assetId={AssetID}&width={Width}&height={Height}&format=png")
    return response.url