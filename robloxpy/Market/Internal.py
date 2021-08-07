import requests,json
import robloxpy.User.Internal as Internal
import robloxpy.Utils as Utils

def BuyItem(MarketID: int) -> str:
    Data = requests.get(f"https://api.roblox.com/marketplace/productinfo?assetId={MarketID}").json()
    sellerId = Data['Creator']['Id']
    Price = Data['PriceInRobux']
    if(Price == None):
        Price = 0
    productId = Data['ProductId']
    response = Internal.CurrentCookie.post(f"https://economy.roblox.com/v1/purchases/products/{productId}",data={"expectedCurrency":1,"expectedPrice":Price,"expectedSellerId":sellerId})
    return response.json()['reason']