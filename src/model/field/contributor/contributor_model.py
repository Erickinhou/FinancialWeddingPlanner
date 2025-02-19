from pydantic import BaseModel, Field
from typing import List

from src.model.field.contributor.contribution.contribution_model import ContributionModel


class ContributorModel(BaseModel):
    """Represents a person contributing to the wedding budget."""
    person_name: str = Field(..., description="Contributor's name")
    contributions: List[ContributionModel] = Field(..., description="List of contributions made by the contributor")
