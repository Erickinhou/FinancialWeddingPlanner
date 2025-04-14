from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import List
from enum import Enum
from collections import defaultdict

router = APIRouter()

class GuestType(str, Enum):
    FAMILY = "FAMILY"
    FRIEND = "FRIEND"


class Person(BaseModel):
    name: str
    is_child: bool = Field(default=False, alias="isChild")
    probably_give_up: bool = Field(default=False, alias="probably_give_up")


class PeopleByLevel(BaseModel):
    level: int = 1
    people: List[Person]


class GuestGroup(BaseModel):
    type: GuestType
    people_by_level: List[PeopleByLevel] = Field(alias="people_by_level")


@router.post("/process-guest-list")
async def process_guest_list(guest_groups: List[GuestGroup]):
    try:
        unique_names = set()
        total_children = 0
        total_probably_give_up = 0
        type_level_counter = defaultdict(lambda: defaultdict(int))

        for group in guest_groups:
            for level_group in group.people_by_level:
                for person in level_group.people:
                    name = person.name.strip()
                    if not name or name in unique_names:
                        continue
                    unique_names.add(name)
                    type_level_counter[group.type.value][level_group.level] += 1
                    if person.is_child:
                        total_children += 1
                    if person.probably_give_up:
                        total_probably_give_up += 1

        return {
            "total_guests": len(unique_names),
            "total_children": total_children,
            "total_probably_give_up": total_probably_give_up,
            "total_probably_not_give_up": len(unique_names) - total_probably_give_up,
            "breakdown": {
                guest_type: {
                    level: count for level, count in sorted(levels.items())
                } for guest_type, levels in type_level_counter.items()
            },
            "guest_names": sorted(list(unique_names))
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))