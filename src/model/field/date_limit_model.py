from pydantic import BaseModel, Field
from datetime import date

class DateLimitModel(BaseModel):
    """Represents the deadline date for the financial planning."""
    day: int = Field(..., description="Deadline day")
    month: int = Field(..., description="Deadline month")
    year: int = Field(..., description="Deadline year")

    def to_date(self) -> date:
        """Returns the deadline as a `date` object."""
        return date(self.year, self.month, self.day)
