# Wedding Budget Calculator API

This project is a **wedding budget calculator API** designed to help couples plan their finances for their wedding. The API calculates whether the projected savings from the contributors (e.g., the couple) will be sufficient to cover the planned expenses by a given deadline. If the budget is insufficient, the API will return the missing amount. If there is a surplus, it will show the extra profit.

## How It Works

1. The API receives a request with the following data:
    - Contributors and their financial contributions
    - Expected wedding expenses
    - A deadline for savings
    - Environment settings (language and currency)

2. Using the provided financial data, it:
    - Computes the **total initial contributions**
    - Computes the **monthly contributions** (including interest)
    - Estimates the **total projected savings** by the deadline
    - Compares savings against **total expenses**
    - Returns either:
        - ✅ **Budget is sufficient**: Shows the remaining profit
        - ❌ **Budget is insufficient**: Shows how much more is needed

## Installation

1. Clone the repository
2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
.\venv\Scripts\activate  # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the API

To start the server, run:
```bash
uvicorn src.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Endpoints

### Budget Calculation
#### POST /api/v1/budget/calculate

Calculates the wedding budget based on provided data.

**Example Request:**
```json
{
  "contributors": [
    {
      "person_name": "John Doe",
      "contributions": [
        {
          "name": "Initial Contribution",
          "contribution_value": {
            "initial": 5000.0,
            "monthly": {
              "value": 1000.0,
              "interest_rate": 0.01
            }
          }
        }
      ]
    }
  ],
  "expenses": [
    {
      "name": "Catering",
      "value": 15000.0
    }
  ],
  "date_limit": {
    "day": 1,
    "month": 12,
    "year": 2024
  },
  "environment": {
    "language": "en",
    "currency": "USD"
  }
}
```

### **Fields Explanation**
- **`contributors`**: A list of people contributing to the wedding budget.
    - **`person_name`**: The name of the contributor.
    - **`contributions`**: A list of financial contributions made by this person.
        - **`name`**: Name of the specific contribution (for identification).
        - **`contribution_value`**:
            - **`initial`**: The starting amount this person is contributing.
            - **`monthly`**:
                - **`value`**: How much they add **every month**.
                - **`interest_rate`**: Monthly interest applied to savings (as a decimal, e.g., `0.01` for 1%).

- **`expenses`**: A list of expected wedding costs.
    - **`name`**: Description of the expense.
    - **`value`**: How much it costs.

- **`date_limit`**: The deadline for saving up.
    - **`day`**, **`month`**, **`year`**: The target date.

- **`environment`**: Defines language and currency settings.
    - **`language`**: The program's language (`"en"` for English, `"pt-br"` for Portuguese).
    - **`currency`**: The currency format (`"USD"` for dollars, `"BRL"` for reais).

**Response:**
```json
{
  "total_initial": 5000.0,
  "total_monthly": 1000.0,
  "total_expenses": 15000.0,
  "months_until": 8,
  "projected_savings": 13310.0,
  "budget_sufficient": false,
  "missing_budget": 1690.0,
  "profit": null,
  "currency": "USD"
}
```

### Guest List Management
#### POST /api/v1/guest-list/manage

Manages the wedding guest list, including RSVPs and meal preferences.

**Example Request:**
```json
{
  "guests": [
    {
      "name": "Jane Smith",
      "email": "jane@example.com",
      "is_attending": true,
      "meal_preference": "vegetarian",
      "plus_one": true
    }
  ]
}
```

**Response:**
```json
{
  "total_guests": 1,
  "attending_guests": 1,
  "vegetarian_meals": 1,
  "plus_ones": 1
}
```

## Project Structure

```
.
├── src/
│   ├── model/
│   │   ├── field/
│   │   │   ├── contributor/
│   │   │   ├── date_limit_model.py
│   │   │   ├── enviroment_model.py
│   │   │   └── expense_model.py
│   │   └── wedding_budget_model.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── budget_router.py
│   │   └── guest_list_router.py
│   └── main.py
├── requirements.txt
└── README.md
```

## Notes
- The API uses **compound interest applied monthly** for calculations
- If `date_limit` is in the past, the API still calculates projections but assumes savings stopped
- The **environment settings** determine the **language of the messages** and the **currency format** in the output

## Contributing
Feel free to fork this project and submit pull requests if you want to improve it!

## License
This project is **open-source** under the MIT License.
