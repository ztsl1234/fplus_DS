
## Additional Question B: Data Structures – 10 Minutes

### Table Schema

| Column Name     | Type                |
|-----------------|---------------------|
| Portfolio_id    | Int                 |
| No_of_holdings  | Int                 |
| No_UnqSec       | Int                 |
| Bond_Ratings    | String              |
| Bond_Value      | Float (Decimal 20,5)|

- `Portfolio_id` is the primary key (i.e., contains unique values).
- Each row represents one portfolio.

---

### Column Descriptions:

- **Portfolio_id**: Unique ID of the portfolio.
- **No_of_holdings**: Number of unique holdings.
- **No_UnqSec**: Number of unique sectors.
- **Bond_Ratings**: Rating of the bond for that portfolio.
- **Bond_Value**: Value of the bond at the end of the financial year.

---

### Task

Write a **pseudocode solution** to report the **sum of all `Bond_Value`**, for all portfolio IDs that meet **both** of the following conditions:

1. The same `Bond_Ratings` appears in **more than one** portfolio.
2. The combination of (`No_of_holdings`, `No_UnqSec`) is **unique**, i.e., no other portfolio has the same pair.

> Note: Round each `Bond_Value` to **two decimal places** before summing.

---

### Output Format

Return a **single float** value, representing the **sum** of all qualifying `Bond_Value`s.

---

### Example

**Input Table:**

| Portfolio_id | Bond_Ratings | Bond_Value | No_of_holdings | No_UnqSec |
|--------------|--------------|------------|----------------|-----------|
| 1            | AA           | 0.5        | 11             | 11        |
| 2            | AAA          | 2.0        | 12             | 12        |
| 3            | AA           | 3.0        | 12             | 12        |
| 4            | AA           | 4.0        | 14             | 14        |

**Output:**

```
4.5
```

> Portfolios 1 and 4 meet both criteria, so the result is 0.5 + 4.0 = **4.5**.
