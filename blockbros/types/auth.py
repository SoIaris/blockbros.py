from typing import NamedTuple, Dict, Any, Optional

class AltGamerType(NamedTuple):
    adminLevel: int
    password: str
    avatar: int
    builderPt: int
    campaigns: Dict[str, Any]
    channel: str
    clearCount: int
    commentableAt: int
    country: str
    createdAt: int
    emblemCount: int
    followerCount: int
    gamerId: int
    gem: int
    hasUnfinishedIAP: bool
    id: int
    inventory: Dict[str, Any]
    lang: str
    lastLoginAt: int
    levelCount: int
    maxVideoId: int
    nameVersion: int
    nickname: str
    playerPt: int
    researches: Optional[Any]
    visibleAt: int

class GamerType(NamedTuple):
    adminLevel: int
    altPassword: str
    avatar: int
    builderPt: int
    campaigns: Dict[str, Any]
    channel: str
    clearCount: int
    commentableAt: int
    country: str
    createdAt: int
    emblemCount: int
    followerCount: int
    gamerId: int
    gem: int
    hasUnfinishedIAP: bool
    id: int
    inventory: Dict[str, Any]
    lang: str
    lastLoginAt: int
    levelCount: int
    maxVideoId: int
    nameVersion: int
    nickname: str
    playerPt: int
    researches: Optional[Any]
    visibleAt: int

class LoginType(NamedTuple):
    gamer: GamerType

class AltLoginType(NamedTuple):
    gamer: AltGamerType