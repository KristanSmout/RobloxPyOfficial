import requests
from . import Utils
from typing import List, Type, Union

User = None
PartialUser = None

class Group():
    __slots__ = ('id', 'name', 'description', 'owner', 'member_count', 'builders_club_only', 'public_entry')
    def __init__(self, id: int) -> None:
        self._update(id)

    def __repr__(self) -> str:
        return self.name

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Group):
            return self.id == other.id
        return False

    def _update(self, id: int) -> None:
        raw_json = requests.get(f"{Utils.GroupAPIV1}{id}").json()
        self.id = raw_json['id']
        self.name = raw_json['name']
        self.description = raw_json['description']
        if raw_json['owner'] != None:
            self.owner = User(raw_json['owner']['userId'])
        else:
            self.owner = None
        self.member_count = raw_json['memberCount']
        self.builders_club_only = raw_json['isBuildersClubOnly']
        self.public_entry = raw_json['publicEntryAllowed']

    @property
    def allies(self) -> List['Group']:
        """
        Returns the groups allies as a list of Group instances.
        """
        _allies = []
        data = requests.get(f"{Utils.GroupAPIV1}{self.id}/relationships/allies?model.startRowIndex=0&model.maxRows=100000").json()
        for group in data['relatedGroups']:
            _allies.append(Group(group['id']))
        return _allies

    @property
    def enemies(self) -> List['Group']:
        """
        Returns the groups enemies as a list of Group instances.
        """
        _enemies = []
        data = requests.get(f"{Utils.GroupAPIV1}{self.id}/relationships/enemies?model.startRowIndex=0&model.maxRows=100000").json()
        for group in data['relatedGroups']:
            _enemies.append(Group(group['id']))
        return _enemies

    def members(self, fetch: bool = False) -> Union[List['PartialUser'], List['User']]:
        """
        Returns a list of all members in the group. this method can be extraordinarily slow depending on group size.
        by default the members are not fetched and do not contain any attributes, this can be changed be setting fetch to True, be aware this has a high chance of being rate limited
        """
        Cursor = ""
        Done = False
        _members = []
        while(Done == False):
            response = requests.get(f"{Utils.GroupAPIV1}{self.id}/users?limit=100&sortOrder=Asc&cursor={Cursor}")
            _users = response.json()['data']
            if((response.json()['nextPageCursor'] == "null") or response.json()['nextPageCursor'] == None):
                Done = True
            else:
                Done = False
                Cursor = response.json()['nextPageCursor']
            for _user in _users:
                try:
                    if not fetch:
                        _members.append(PartialUser(_user['user']['userId']))
                        continue
                    _members.append(User(_user['user']['userId']))
                except:
                    pass
            if(response.json()['nextPageCursor'] == 'None'):
                Done = True
        return _members

def _get_user():
    global User
    global PartialUser
    from . import user as usr
    User = usr.User
    PartialUser = usr.PartialUser
_get_user()