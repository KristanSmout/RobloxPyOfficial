import requests,json
from robloxpy import Utils as Utils

def CanManageAsset(UserID,AssetID):
    """
    Returns whether a user can manage an asset
    """
    response = requests.get(Utils.APIURL + f"/users/{UserID}/canmanage/{AssetID}")
    try:
        return response.json()['CanManage']
    except:
        return response.json()['ErrorMessage']

def GetLimitedPriceData(LimitedID):
    """
    Returns price data of a limited
    """
    response = requests.get(Utils.EconomyURL + '/assets/' + str(LimitedID) + '/resale-data')
    return response.json()['priceDataPoints']

def GetLimitedRemaining(LimitedID):
    """
    Returns the amount of limiteds that are availible for sale
    """
    response = requests.get(Utils.EconomyURL + '/assets/' + str(LimitedID) + '/resale-data')
    return response.json()['numberRemaining']

def GetLimitedTotal(LimitedID):
    """
    Returns how many of a limited there are
    """
    response = requests.get(Utils.EconomyURL + '/assets/' + str(LimitedID) + '/resale-data')
    return response.json()['assetStock']

def GetLimitedSales(LimitedID):
    """
    Returns how many of a limited have been sold
    """
    response = requests.get(Utils.EconomyURL + '/assets/' + str(LimitedID) + '/resale-data')
    return response.json()['sales']

def GetLimitedRAP(LimitedID):
    """
    Returns the RAP of a limited
    """
    response = requests.get(Utils.EconomyURL + '/assets/' + str(LimitedID) + '/resale-data')
    return response.json()['recentAveragePrice']

def GetLimitedSalePrice(LimitedID):
    """
    Returns the sale price of a limited
    """
    response = requests.get(Utils.EconomyURL + '/assets/' + str(LimitedID) + '/resale-data')
    return response.json()['originalPrice']

def GetLimitedChangePercentage(LimitedID):
    """
    Returns the percentage change of the price of a limited
    """
    Change = round(((float(GetLimitedRAP(LimitedID))-GetLimitedSalePrice(LimitedID))/GetLimitedSalePrice(LimitedID))*100,3)
    return str(Change) + '%'

def GetAssetImage(AssetID,Width = 420,Height = 420):
    """
    Returns a url to an image of the limited

    Limited image size can be changed
    """
    response = requests.get(f"https://www.roblox.com/asset-thumbnail/image?assetId={AssetID}&width={Width}&height={Height}&format=png")
    return response.url