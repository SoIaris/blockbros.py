from .request import Internal
from .errors import MissingGamer, TokenMismatch, ValidationException

from typing import Optional, List, Dict
from .types import gamer

class Gamer:
    def __init__(self, id: int, token: str):
        '''
            id and token is required for any requests
        '''
        self.id = id
        self.token = token

    def setChannelUrl(self, url: str) -> Optional[gamer.UpdatedGamerType]:
        '''
            sets channel link

            Args:
                url (str): Url should be something like this "/@MrBeast"

            Returns:
                if unsccessful, returns False. If successful, returns updated gamer data
        '''
        send = Internal.requestSend("gamer/channel/set", {
            "url": url
        }, token=self.token, id=self.id)

        
        if send.json().get("reason"):
            reason = send.json()["reason"]
            if reason == "missing_gamer":
                raise MissingGamer
            elif reason == "token_mismatch":
                raise TokenMismatch
            elif reason == "validation_exception":
                raise ValidationException
        
        data = send.json()
        if not data["success"]:
            return False
        
        homeLevel = None
        gamerData = data["updated"]["gamer"]
            
        if gamerData.get("homeLevel", None):
            homeLevel = gamerData.HomeLevelType(
                levelId=gamerData["homeLevel"]["levelId"],
                map=gamerData["homeLevel"]["map"],
                theme=gamerData["homeLevel"]["theme"]
            )
        
        return gamer.UpdatedGamerType(
            adminLevel=gamerData["adminLevel"],
            avatar=gamerData["avatar"],
            builderPt=gamerData["builderPt"],
            channel=gamerData["channel"],
            commentableAt=gamerData["commentableAt"],
            country=gamerData["country"],
            createdAt=gamerData["createdAt"],
            emblemCount=gamerData["emblemCount"],
            followerCount=gamerData["followerCount"],
            gamerId=gamerData["gamerId"],
            homeLevel=homeLevel,
            id=gamerData["id"],
            inventory=gamer.InventoryType(
                avatars=gamerData["inventory"]["avatars"]
            ),
            lastLoginAt=gamerData["lastLoginAt"],
            levelCount=gamerData["levelCount"],
            nickname=gamerData["nickname"],
            playerPt=gamerData["playerPt"],
            visibleAt=gamerData["visibleAt"]
        )

    def unblockGamer(self, gamer_id: int) -> Optional[List[int]]:
        '''
            unblocks a gamer

            Args:
                gamer_id (int): The long ID. Example: 6266323782074368

            Returns:
                If unsuccessful, returns False. If successful, returns a list of accounts that the user blocks.
        ''' 
        send = Internal.requestSend("gamer/follow/put", {
            "gamer_id": gamer_id,
            "action": "unblock"
        }, token=self.token, id=self.id)

        if send.json().get("reason"):
            reason = send.json()["reason"]
            if reason == "missing_gamer":
                raise MissingGamer
            elif reason == "token_mismatch":
                raise TokenMismatch
            elif reason == "validation_exception":
                raise ValidationException
        
        data = send.json()
        if not data["success"]:
            return False
        
        return data["updated"]["follows"]["blocks"]
    
    def blockGamer(self, gamer_id: int) -> Optional[List[int]]:
        '''
            blocks a gamer

            Args:
                gamer_id (int): The long ID. Example: 6266323782074368

            Returns:
                If unsuccessful, returns False. If successful, returns a list of accounts that the user blocks.
        ''' 
        send = Internal.requestSend("gamer/follow/put", {
            "gamer_id": gamer_id,
            "action": "block"
        }, token=self.token, id=self.id)

        if send.json().get("reason"):
            reason = send.json()["reason"]
            if reason == "missing_gamer":
                raise MissingGamer
            elif reason == "token_mismatch":
                raise TokenMismatch
            elif reason == "validation_exception":
                raise ValidationException
        
        data = send.json()
        if not data["success"]:
            return False
        
        return data["updated"]["follows"]["blocks"]
    
    def unfollowGamer(self, gamer_id: int) -> Optional[List[int]]:
        '''
            unfollows a gamer

            Args:
                gamer_id (int): The long ID. Example: 6266323782074368

            Returns:
                If unsuccessful, returns False. If successful, returns a list of accounts that the user follows.
        ''' 
        send = Internal.requestSend("gamer/follow/put", {
            "gamer_id": gamer_id,
            "action": "unfollow"
        }, token=self.token, id=self.id)

        if send.json().get("reason"):
            reason = send.json()["reason"]
            if reason == "missing_gamer":
                raise MissingGamer
            elif reason == "token_mismatch":
                raise TokenMismatch
            elif reason == "validation_exception":
                raise ValidationException
        
        data = send.json()
        if not data["success"]:
            return False
        
        return data["updated"]["follows"]["follows"]

    def followGamer(self, gamer_id: int) -> Optional[List[int]]:
        '''
            follows a gamer

            Args:
                gamer_id (int): The long ID. Example: 6266323782074368

            Returns:
                If unsuccessful, returns False. If successful, returns a list of accounts that the user follows.
        ''' 
        send = Internal.requestSend("gamer/follow/put", {
            "gamer_id": gamer_id,
            "action": "follow"
        }, token=self.token, id=self.id)

        if send.json().get("reason"):
            reason = send.json()["reason"]
            if reason == "missing_gamer":
                raise MissingGamer
            elif reason == "token_mismatch":
                raise TokenMismatch
        
        data = send.json()
        if not data["success"]:
            return False
        
        return data["updated"]["follows"]["follows"]

    def search(self, nickname: str) -> Optional[gamer.GamerType]:
        '''
            Search for a gamer

            Returns:
                Returns None if no gamer exists, otherwise, returns the gamer's data.
        '''
        send = Internal.requestSend("gamer/search", {
            "nickname": nickname
        }, token=self.token, id=self.id)
        
        if send.json().get("reason"):
            reason = send.json()["reason"]
            if reason == "missing_gamer":
                raise MissingGamer
            elif reason == "token_mismatch":
                raise TokenMismatch
        
        data = send.json()
        if not data.get("success", False):
            return None
        
        results = data.get('result', {}).get('items', [])
        if not results:
            return None
        
        gamer = results[0]
        homeLevel = None
        if gamer.get("homeLevel", None):
            homeLevel = gamer.HomeLevelType(
                levelId=gamer["homeLevel"]["levelId"],
                map=gamer["homeLevel"]["map"],
                theme=gamer["homeLevel"]["theme"]
            )
        
        return gamer.GamerType(
            adminLevel=gamer["adminLevel"],
            avatar=gamer["avatar"],
            builderPt=gamer["builderPt"],
            channel=gamer["channel"],
            commentableAt=gamer["commentableAt"],
            country=gamer["country"],
            createdAt=gamer["createdAt"],
            emblemCount=gamer["emblemCount"],
            followerCount=gamer["followerCount"],
            gamerId=gamer["gamerId"],
            homeLevel=homeLevel,
            id=gamer["id"],
            inventory=gamer.InventoryType(
                avatars=gamer["inventory"]["avatars"]
            ),
            lastLoginAt=gamer["lastLoginAt"],
            levelCount=gamer["levelCount"],
            nickname=gamer["nickname"],
            playerPt=gamer["playerPt"],
            userId=gamer["userId"],
            visibleAt=gamer["visibleAt"]
        )