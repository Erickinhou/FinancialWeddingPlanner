from datetime import date
from typing import List

from pydantic import BaseModel, Field

from src.model.field.contributor.contributor_model import ContributorModel
from src.model.field.date_limit_model import DateLimitModel
from src.model.field.enviroment_model import EnvironmentModel
from src.model.field.expense_model import ExpenseModel


class WeddingBudgetModel(BaseModel):
    """Represents the overall financial planning for a wedding, including contributors, expenses, and a deadline."""
    contributors: List[ContributorModel] = Field(..., description="List of contributors")
    expenses: List[ExpenseModel] = Field(..., description="List of expenses")
    date_limit: DateLimitModel = Field(..., description="Financial planning deadline")
    environment: EnvironmentModel = Field(default_factory=EnvironmentModel, description="Program environment settings")
    translations: dict = Field(default_factory=dict, description="Language translations")

    def total_initial_contributions(self) -> float:
        return sum(
            sum(contribution.contribution_value.initial for contribution in contributor.contributions)
            for contributor in self.contributors
        )

    def total_monthly_contributions(self) -> float:
        return sum(
            sum(contribution.contribution_value.monthly.value for contribution in contributor.contributions)
            for contributor in self.contributors
        )

    def total_expenses(self) -> float:
        return sum(expense.value for expense in self.expenses)

    def months_until_date_limit(self) -> int:
        today = date.today()
        target_date = self.date_limit.to_date()
        return (target_date.year - today.year) * 12 + (target_date.month - today.month)

    def projected_savings(self) -> float:
        months = self.months_until_date_limit()
        total_savings = self.total_initial_contributions()

        for contributor in self.contributors:
            for contribution in contributor.contributions:
                monthly_value = contribution.contribution_value.monthly.value
                interest_rate = contribution.contribution_value.monthly.interest_rate

                for _ in range(months):
                    total_savings += monthly_value
                    total_savings *= (1 + interest_rate)

        return total_savings

    def is_budget_sufficient(self) -> bool:
        return self.projected_savings() >= self.total_expenses()

    def missing_budget(self) -> float:
        return max(0.0, self.total_expenses() - self.projected_savings())

    def profit(self) -> float:
        return self.projected_savings() - self.total_expenses() if self.is_budget_sufficient() else 0.0

    def format_currency(self, amount: float) -> str:
        """Formats a given amount based on the selected currency."""
        currency_symbol = "R$" if self.environment.currency == "BRL" else "$"
        return f"{currency_symbol} {amount:.2f}"

    def get_translation(self, key: str) -> str:
        """Gets the translated text based on the environment language."""
        return self.translations.get(self.environment.language, {}).get(key, key)
