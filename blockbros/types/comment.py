from typing import NamedTuple, List, Optional, List
from .gamer import GamerType

class CommentType(NamedTuple):
    args: dict
    commentId: int
    gamer: GamerType
    message: str
    type: str

class CommentList(NamedTuple):
    cursor: str
    all_loaded: bool
    comments: List[CommentType]