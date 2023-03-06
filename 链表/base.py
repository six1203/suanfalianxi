from dataclasses import dataclass
from typing import Optional


@dataclass
class LinkedList:
    val: int
    next: Optional["LinkedList"] = None
