from pydantic import BaseModel, Field

from src.model.field.contributor.contribution.value.contribution_value_model import ContributionValueModel

class ContributionModel(BaseModel):
    """Represents a single financial contribution made by a contributor."""
    name: str = Field(..., description="Contribution name")
    contribution_value: ContributionValueModel = Field(..., description="Contribution details")
