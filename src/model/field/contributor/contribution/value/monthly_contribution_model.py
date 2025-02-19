from pydantic import BaseModel, Field

class MonthlyContributionModel(BaseModel):
    """Represents a monthly contribution with an amount and an interest rate."""
    value: float = Field(..., description="Monthly contribution amount")
    interest_rate: float = Field(..., description="Monthly interest rate as a decimal (e.g., 0.01 for 1%)")
