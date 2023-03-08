from dataclasses import dataclass
from typing import Optional


@dataclass
class LinkedList:
    val: int = 0
    next: Optional["LinkedList"] = None
