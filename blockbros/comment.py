from .request import Internal
from .types.comment import CommentType, CommentList
from .types.gamer import GamerType, HomeLevelType, InventoryType

from typing import Optional

class Comment:
    def __init__(self, id: int, token: str):
        '''
            id and token is required for any requests
        '''
        self.id = id
        self.token = token

    def list(self, group_key: str, index: int=0, options: dict={}) -> CommentList:
        req = Internal.requestSend("/comment/list", {
            "index": index,
            "group_key": group_key,
            "options": options,
            "cursor": ""
        }, self.token, self.id)
        
        json = req.json()

        if not json["success"]:
            return False

        result = json["result"]
        all_loaded = result["all_loaded"]
        cursor = result.get("cursor", None)
        items = result["items"]

        comments = []
        for item in items:
            homeLevel = None
            gamer = item["gamer"]
            
            if gamer.get("homeLevel", None):
                homeLevel = HomeLevelType(
                    levelId=gamer["homeLevel"]["levelId"],
                    map=gamer["homeLevel"]["map"],
                    theme=gamer["homeLevel"]["theme"]
                )
        
            gamer = GamerType(
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
                inventory=InventoryType(
                    avatars=gamer["inventory"]["avatars"]
                ),
                lastLoginAt=gamer["lastLoginAt"],
                levelCount=gamer["levelCount"],
                nickname=gamer["nickname"],
                playerPt=gamer["playerPt"],
                userId=gamer["userId"],
                visibleAt=gamer["visibleAt"]
            )

            comment = CommentType(
                args=item["args"],
                commentId=item["commentId"],
                gamer=gamer,
                message=item["message"],
                type=item["type"]
            )
            comments.append(comment)

        return CommentList(
            cursor=cursor,
            all_loaded=all_loaded,
            comments=comments
        )
    
    def post(self, group_key: str, comment: str, options: dict={}) -> Optional[CommentType]:
        try:
            res = Internal.requestSend("/comment/post", {
                "group_key": group_key,
                "comment": comment,
                "options": options
            }, self.token, self.id)

            json = res.json()
            if json.get("reason"):
                reason = json["reason"]
                if reason == "comment_prevention":
                    return int(json["result"]["sec"])
            
            commentData = json["result"]["comment"]
            gamer = commentData["gamer"]
            homeLevel = None
            
            if gamer.get("homeLevel", None):
                homeLevel = HomeLevelType(
                    levelId=gamer["homeLevel"]["levelId"],
                    map=gamer["homeLevel"]["map"],
                    theme=gamer["homeLevel"]["theme"]
            )
        
            gamer = GamerType(
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
                inventory=InventoryType(
                    avatars=gamer["inventory"]["avatars"]
                ),
                lastLoginAt=gamer["lastLoginAt"],
                levelCount=gamer["levelCount"],
                nickname=gamer["nickname"],
                playerPt=gamer["playerPt"],
                userId=gamer["userId"],
                visibleAt=gamer["visibleAt"]
            )

            return CommentType(
                args=commentData["args"],
                commentId=commentData["commentId"],
                gamer=gamer,
                message=commentData["message"],
                type=commentData["type"]
            )
                
        except Exception as e:
            return None