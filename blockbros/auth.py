from .request import Internal
from .errors import NoMatch, MissingGamer, ValidationException
from .types import auth, gamer

class Auth:
    @staticmethod
    def login(id: int, password: str) -> auth.LoginType:
        '''
            login via id and password

            Args:
                id (int): long id. Example: (6529423364063232)
                password (str): the long password not altPassword

            Returns:
                returns auth.LoginType 
        '''
        req = Internal.requestSend("auth/login", {
            "id": id,
            "password": password
        })
        data = req.json()

        if data.get("reason"): # most likely is a error
            reason = req.json()["reason"]
            if reason == "no_match":
                raise NoMatch
            elif reason == "missing_gamer":
                raise MissingGamer
            elif reason == "validation_exception":
                raise ValidationException
            
        return auth.LoginType(
            gamer=auth.GamerType(
                adminLevel=data["updated"]["gamer"]["adminLevel"],
                altPassword=data["updated"]["gamer"]["altPassword"],
                avatar=data["updated"]["gamer"]["avatar"],
                builderPt=data["updated"]["gamer"]["builderPt"],
                campaigns=data["updated"]["gamer"]["campaigns"],
                channel=data["updated"]["gamer"]["channel"],
                clearCount=data["updated"]["gamer"]["clearCount"],
                commentableAt=data["updated"]["gamer"]["commentableAt"],
                country=data["updated"]["gamer"]["country"],
                createdAt=data["updated"]["gamer"]["createdAt"],
                emblemCount=data["updated"]["gamer"]["emblemCount"],
                followerCount=data["updated"]["gamer"]["followerCount"],
                gamerId=data["updated"]["gamer"]["gamerId"],
                gem=data["updated"]["gamer"]["gem"],
                hasUnfinishedIAP=data["updated"]["gamer"]["hasUnfinishedIAP"],
                id=data["updated"]["gamer"]["id"],
                inventory=data["updated"]["gamer"]["inventory"],
                lang=data["updated"]["gamer"]["lang"],
                lastLoginAt=data["updated"]["gamer"]["lastLoginAt"],
                levelCount=data["updated"]["gamer"]["levelCount"],
                maxVideoId=data["updated"]["gamer"]["maxVideoId"],
                nameVersion=data["updated"]["gamer"]["nameVersion"],
                nickname=data["updated"]["gamer"]["nickname"],
                playerPt=data["updated"]["gamer"]["playerPt"],
                researches=data["updated"]["gamer"]["researches"],
                visibleAt=data["updated"]["gamer"]["visibleAt"]
            )
        )
    
    @staticmethod
    def alt_login(gamer_id: int, altPassword: str) -> auth.AltLoginType:
        '''
            login via gamer_id and altPassword 

            Args:
                gamer_id (int): the short gamer id
                altPassword (str): the short password

            Returns:
                returns auth.AltLoginType
        '''
        req = Internal.requestSend("auth/alt_login", {
            "gamer_id": str(gamer_id),
            "password": altPassword
        })

        data = req.json()

        if data.get("reason"): # most likely is a error
            reason = req.json()["reason"]
            if reason == "no_match":
                raise NoMatch
            elif reason == "missing_gamer":
                raise MissingGamer
            elif reason == "validation_exception":
                raise ValidationException
            
        return auth.AltLoginType(
            gamer=auth.AltGamerType(
                adminLevel=data["updated"]["gamer"]["adminLevel"],
                password=data["updated"]["gamer"]["password"],
                avatar=data["updated"]["gamer"]["avatar"],
                builderPt=data["updated"]["gamer"]["builderPt"],
                campaigns=data["updated"]["gamer"]["campaigns"],
                channel=data["updated"]["gamer"]["channel"],
                clearCount=data["updated"]["gamer"]["clearCount"],
                commentableAt=data["updated"]["gamer"]["commentableAt"],
                country=data["updated"]["gamer"]["country"],
                createdAt=data["updated"]["gamer"]["createdAt"],
                emblemCount=data["updated"]["gamer"]["emblemCount"],
                followerCount=data["updated"]["gamer"]["followerCount"],
                gamerId=data["updated"]["gamer"]["gamerId"],
                gem=data["updated"]["gamer"]["gem"],
                hasUnfinishedIAP=data["updated"]["gamer"]["hasUnfinishedIAP"],
                id=data["updated"]["gamer"]["id"],
                inventory=gamer.InventoryType(
                    avatars = data["updated"]["gamer"]["inventory"]["avatars"]
                ),
                lang=data["updated"]["gamer"]["lang"],
                lastLoginAt=data["updated"]["gamer"]["lastLoginAt"],
                levelCount=data["updated"]["gamer"]["levelCount"],
                maxVideoId=data["updated"]["gamer"]["maxVideoId"],
                nameVersion=data["updated"]["gamer"]["nameVersion"],
                nickname=data["updated"]["gamer"]["nickname"],
                playerPt=data["updated"]["gamer"]["playerPt"],
                researches=data["updated"]["gamer"]["researches"],
                visibleAt=data["updated"]["gamer"]["visibleAt"]
            )
        )