import json
from pathlib import Path
from pydantic import ValidationError

from src.model.wedding_budget_model import WeddingBudgetModel

def load_wedding_budget() -> WeddingBudgetModel:
    """
    Loads and parses the wedding budget JSON file, returning a validated WeddingBudgetModel instance.

    :return: An instance of WeddingBudgetModel with the parsed and validated data.
    :raises FileNotFoundError: If the file does not exist.
    :raises ValueError: If there is an error in JSON parsing or validation.
    """
    input_file = Path("../data/input.json")

    if not input_file.exists():
        raise FileNotFoundError(f"The file {input_file} was not found!")

    with open(input_file, "r", encoding="utf-8") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError as e:
            raise ValueError(f"Error loading JSON: {e}")

    try:
        return WeddingBudgetModel(**data)
    except ValidationError as e:
        raise ValueError(f"Validation error in JSON data: {e}")



def load_translations() -> dict:
    """Loads translations from a JSON file."""
    path = Path("../data/translations.json")
    if path.exists():
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    return {}

if __name__ == "__main__":
    budget = load_wedding_budget()

    budget.environment.validate_environment()

    translations = load_translations()
    budget.translations = translations

    print(budget.get_translation("total_initial") + ":", budget.format_currency(budget.total_initial_contributions()))
    print(budget.get_translation("total_monthly") + ":", budget.format_currency(budget.total_monthly_contributions()))
    print(budget.get_translation("total_expenses") + ":", budget.format_currency(budget.total_expenses()))
    print(budget.get_translation("months_until") + ":", budget.months_until_date_limit())
    print(budget.get_translation("projected_savings") + ":", budget.format_currency(budget.projected_savings()))
    print(budget.get_translation("budget_sufficient") + ":", budget.get_translation("yes") if budget.is_budget_sufficient() else budget.get_translation("no"))

    if not budget.is_budget_sufficient():
        print(budget.get_translation("missing_budget") + ":", budget.format_currency(budget.missing_budget()))
    else:
        print(budget.get_translation("profit") + ":", budget.format_currency(budget.profit()))
