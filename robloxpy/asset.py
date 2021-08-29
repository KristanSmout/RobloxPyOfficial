import requests, sys
from . import user, Utils, errors
from typing import Union, Type, BinaryIO
from os import PathLike
from io import IOBase

robloxpy = sys.modules['robloxpy']

class ImageAsset():
    __slots__ = ('url')

    def __init__(self, url: str) -> None:
        self.url = url

    def __repr__(self):
        return self.url

    def __eq__(self, other: object) -> bool:
        if isinstance(other, ImageAsset):
            return self.url == other.url
        return False

    def read(self) -> bytes:
        """
        Returns the image in bytes.
        """
        return requests.get(self.url).content

    def save(self, fp: Union[BinaryIO, Type[PathLike]]) -> int:
        """
        Saves the image into a file-like object.
        """
        data = self.read()
        if isinstance(fp, IOBase) and fp.writable():
            return fp.write(data)
        else:
            with open(fp, 'wb') as f:
                return f.write(data)

class MarketAsset():
    __slots__ = ('id', 'name', 'description', 'creator', 'lowest_price', 'price', 'favorites')

    def __init__(self, id: int) -> None:
        self._update(id)

    def __repr__(self) -> str:
        return self.name

    def __eq__(self, other: object) -> bool:
        if isinstance(other, MarketAsset):
            return self.id == other.id
        return False

    def _update(self, id: int) -> None:
        if not robloxpy.CurrentCookie:
            raise errors.NoCookie
        try:
            data = robloxpy.CurrentCookie.post('https://catalog.roblox.com/v1/catalog/items/details', json={"items": [{"itemType": "Asset","id": id}]}).json()['data'][0]
        except IndexError:
            raise errors.InvalidId
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.creator = user.User(data['creatorTargetId'])
        try:
            self.lowest_price = data['lowestPrice']
        except:
            self.lowest_price = None
        try:
            self.price = data['price']
        except:
            self.price = self.lowest_price or None
        self.favorites = data['favoriteCount']

    def thumbnail(self) -> Type[ImageAsset]:
        """
        Returns the assets thumbnail as an ImageAsset.
        """
        data = requests.get(f"{Utils.ThumnnailAPIV1}assets?assetIds={self.id}&format=Png&isCircular=true&size=700x700").json()['data'][0]
        return ImageAsset(data['imageUrl'])

    def buy(self) -> None:
        """
        purchases the asset.

        untested
        """
        response = robloxpy.CurrentCookie.post(f"https://economy.roblox.com/v1/purchases/products/{self.id}",data={"expectedCurrency":1,"expectedPrice":self.lowest_price,"expectedSellerId":None})