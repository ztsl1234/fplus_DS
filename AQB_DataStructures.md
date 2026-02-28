
## Additional Question B: Data Structures

### Task

Write a **pseudocode solution** to report the **sum of all `Bond_Value`**, for all portfolio IDs that meet **both** of the following conditions:

1. The same `Bond_Ratings` appears in **more than one** portfolio.
2. The combination of (`No_of_holdings`, `No_UnqSec`) is **unique**, i.e., no other portfolio has the same pair.

> Note: Round each `Bond_Value` to **two decimal places** before summing.

---

pseudocode solution

For Condition 1:
1. Group by Bond_Ratings
2. count number of portfolio_ids for each Bond_Ratings
3. Retrieve all Bond_Ratings with count > 1

For Condition 2:
4. Group by No_of_holdings,No_UnqSec
5. count number of portfolio_id for each (`No_of_holdings`, `No_UnqSec`)
6. Retrieve all Bond_Ratings with count =1
  
7. Retrieve Bond_value from Table where Bond_Ratings exists in the lists in Step 3 and Step 6. Round Bond_Value to 2 decimal places before summing
   
8. Sum all the Bond_value in step 7
