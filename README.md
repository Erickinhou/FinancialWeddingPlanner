# Wedding Budget Calculator

This project is a **wedding budget calculator** designed to help couples plan their finances for their wedding. The program calculates whether the projected savings from the contributors (e.g., the couple) will be sufficient to cover the planned expenses by a given deadline. If the budget is insufficient, the program will display the missing amount. If there is a surplus, it will show the extra profit.

## How It Works
1. The program reads a **JSON file (`input.json`)** that contains:
    - Contributors and their financial contributions.
    - Expected wedding expenses.
    - A deadline for savings.
    - Environment settings (language and currency).

2. Using the provided financial data, it:
    - Computes the **total initial contributions**.
    - Computes the **monthly contributions** (including interest).
    - Estimates the **total projected savings** by the deadline.
    - Compares savings against **total expenses**.
    - Displays either:
        - ✅ **Budget is sufficient**: Shows the remaining profit.
        - ❌ **Budget is insufficient**: Shows how much more is needed.

---

## Editing the Budget Data (`input.json`)
To customize the budget, open and edit the `input.json` file in the `data/` folder.

### **JSON Structure & Explanation**
```json
{
  "contributors": [
    {
      "person_name": "John Doe",
      "contributions": [
        {
          "name": "Contribution 1",
          "contribution_value": {
            "initial": 100,
            "monthly": {
              "value": 100,
              "interest_rate": 0.01
            }
          }
        }
      ]
    }
  ],
  "expenses": [
    {
      "name": "Expense 1",
      "value": 100
    }
  ],
  "date_limit": {
    "day": 1,
    "month": 4,
    "year": 2026
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

---

## How to Use
### **1. Install Dependencies**
Ensure you have Python installed. Then, install `pydantic` for data validation:
```sh
pip install pydantic
```

### **2. Edit the Budget (`input.json`)**
Modify the `data/input.json` file according to your needs.

### **3. Run the Program**
Execute the script:
```sh
python main.py
```

### **4. Interpret the Output**
The program will display financial summaries, including whether the budget is sufficient and how much extra or missing money there is.

---

## Example Outputs
### ✅ **Budget is Sufficient**
```
Total Initial Contributions: $ 5000.00
Total Monthly Contributions: $ 1200.00
Total Expenses: $ 15000.00
Months Until Deadline: 12
Projected Savings: $ 18000.50
Is the Budget Sufficient? Yes
Profit: $ 3000.50
```

### ❌ **Budget is Insufficient**
```
Total Initial Contributions: R$ 3000.00
Total Monthly Contributions: R$ 800.00
Total Expenses: R$ 20000.00
Months Until Deadline: 12
Projected Savings: R$ 15000.00
Is the Budget Sufficient? No
Missing Budget: R$ 5000.00
```

---

## Notes
- The program **does not modify `input.json`** automatically.
- Interest calculations are **compound interest applied monthly**.
- If `date_limit` is in the past, the program **still calculates projections** but assumes savings stopped.
- The **environment settings** determine the **language of the messages** and the **currency format** in the output.

---

## Contributing
Feel free to fork this project and submit pull requests if you want to improve it!

---

## License
This project is **open-source** under the MIT License.
