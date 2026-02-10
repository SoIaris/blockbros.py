from typing import NamedTuple, List, Optional

class HomeLevelType(NamedTuple):
    levelId: int
    map: List[int]
    theme: int

class InventoryType(NamedTuple):
    avatars: List[int]

class UpdatedGamerType(NamedTuple):
    adminLevel: int
    avatar: int
    builderPt: int
    channel: str
    commentableAt: int
    country: str
    createdAt: int
    emblemCount: int
    followerCount: int
    gamerId: int
    homeLevel: Optional[HomeLevelType]
    id: int
    inventory: InventoryType
    lastLoginAt: int
    levelCount: int
    nickname: str
    playerPt: int
    visibleAt: int

class GamerType(NamedTuple):
    adminLevel: int
    avatar: int
    builderPt: int
    channel: str
    commentableAt: int
    country: str
    createdAt: int
    emblemCount: int
    followerCount: int
    gamerId: int
    homeLevel: Optional[HomeLevelType]
    id: int
    inventory: InventoryType
    lastLoginAt: int
    levelCount: int
    nickname: str
    playerPt: int
    userId: str
    visibleAt: int