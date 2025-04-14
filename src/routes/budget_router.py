from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, ValidationError
from typing import List, Optional

from src.model.wedding_budget_model import WeddingBudgetModel
from src.model.field.contributor.contributor_model import ContributorModel
from src.model.field.expense_model import ExpenseModel
from src.model.field.date_limit_model import DateLimitModel
from src.model.field.enviroment_model import EnvironmentModel

router = APIRouter()

class BudgetResponse(BaseModel):
    total_initial: float
    total_monthly: float
    total_expenses: float
    months_until: int
    projected_savings: float
    budget_sufficient: bool
    missing_budget: Optional[float]
    profit: Optional[float]
    currency: str

@router.post("/budget/calculate", response_model=BudgetResponse)
async def calculate_budget(
    contributors: List[ContributorModel],
    expenses: List[ExpenseModel],
    date_limit: DateLimitModel,
    environment: EnvironmentModel = EnvironmentModel()
):
    try:
        budget = WeddingBudgetModel(
            contributors=contributors,
            expenses=expenses,
            date_limit=date_limit,
            environment=environment
        )

        return BudgetResponse(
            total_initial=budget.total_initial_contributions(),
            total_monthly=budget.total_monthly_contributions(),
            total_expenses=budget.total_expenses(),
            months_until=budget.months_until_date_limit(),
            projected_savings=budget.projected_savings(),
            budget_sufficient=budget.is_budget_sufficient(),
            missing_budget=budget.missing_budget() if not budget.is_budget_sufficient() else None,
            profit=budget.profit() if budget.is_budget_sufficient() else None,
            currency=budget.environment.currency
        )
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=str(e)) 