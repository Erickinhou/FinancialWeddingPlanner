from pydantic import BaseModel, Field

from src.model.field.contributor.contribution.value.monthly_contribution_model import MonthlyContributionModel


class ContributionValueModel(BaseModel):
    """Represents the value of a financial contribution, including initial and monthly values."""
    initial: float = Field(..., description="Initial contribution amount")
    monthly: MonthlyContributionModel = Field(..., description="Details of the monthly contribution")
