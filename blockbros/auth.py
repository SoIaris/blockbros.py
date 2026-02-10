from .request import Internal
from .errors import NoMatchError
from .types.alt_login import AltLoginType, GamerType

class auth:
    @staticmethod
    def alt_login(gamer_id: int, password: str) -> AltLoginType:
        req = Internal.requestSend("auth/alt_login", {
            "gamer_id": str(gamer_id),
            "password": password
        })

        data = req.json()

        if data.get("reason"): # most likely is a error
            reason = req.json()["reason"]
            if reason == "no_match":
                raise NoMatchError
            
        return AltLoginType(
            gamer=GamerType(
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