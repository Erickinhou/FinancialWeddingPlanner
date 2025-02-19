from pydantic import BaseModel, Field

class ExpenseModel(BaseModel):
    """Represents an expense related to the wedding budget."""
    name: str = Field(..., description="Expense name")
    value: float = Field(..., description="Expense amount")
