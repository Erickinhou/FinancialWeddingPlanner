from pydantic import BaseModel, Field

class EnvironmentModel(BaseModel):
    """Represents the environment settings for the program."""
    language: str = Field("en", description="Language of the program (en or pt-br)")
    currency: str = Field("USD", description="Currency format (USD or BRL)")

    def validate_environment(self):
        """Ensures that the environment variables are supported, otherwise, defaults are applied."""
        if self.language not in {"en", "pt-br"}:
            self.language = "en"
        if self.currency not in {"USD", "BRL"}:
            self.currency = "USD"
