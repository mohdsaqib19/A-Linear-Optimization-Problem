# A-Linear-Optimization-Problem
This project models and solves a Linear Programming Problem (LPP) to determine the optimal number of Executive, Office, and Student desks a company should manufacture in order to maximize profit. The model takes into account the limited working hours available in the Cabinet Shop, Finishing Shop, and Crating Shop.
# Desk Manufacturing Profit Optimization

This project models and solves a **Linear Programming Problem (LPP)** to determine the optimal number of desks (Executive, Office, and Student models) a company should produce in order to **maximize total profit** while staying within the available production time constraints.

---

## 📈 Problem Overview

A company manufactures three types of desks:

* **Executive Desk**
* **Office Desk**
* **Student Desk**

Each desk requires a certain number of hours in three production shops:

* Cabinet Shop
* Finishing Shop
* Crating Shop

Each type of desk yields a different profit. The company has limited total available hours in each shop. The goal is to determine how many of each type of desk to produce to maximize profits.

---

## 🎯 Objective

> Maximize total profit from desk production without exceeding available shop time.

---

## 📊 Data Table

| Desk Type | Cabinet (hrs) | Finishing (hrs) | Crating (hrs) | Profit (₹) |
| --------- | ------------- | --------------- | ------------- | ---------- |
| Executive | 2.0           | 2.0             | 1.0           | 1600       |
| Office    | 1.5           | 1.0             | 2.0           | 1300       |
| Student   | 1.0           | 1.5             | 0.5           | 600        |

**Available Shop Hours**:

* Cabinet: 20 hours
* Finishing: 24 hours
* Crating: 20 hours

---

## 💡 Model Formulation

### Decision Variables:

Let:

* `x` = number of Executive desks
* `y` = number of Office desks
* `z` = number of Student desks

### Objective Function:

```
Maximize P = 1600x + 1300y + 600z
```

### Constraints:

```
2x + 1.5y + 1z   <= 20   (Cabinet Shop)
2x + 1y   + 1.5z <= 24   (Finishing Shop)
1x + 2y   + 0.5z <= 20   (Crating Shop)
x >= 0, y >= 0, z >= 0   (Non-negativity)
```

---

## 🚀 How to Run

### 1. Install Dependencies:

```
pip install pulp
```

### 2. Run the Script:

```
python desk_profit_optimization.py
```

---

## 📁 Files Included

* `desk_profit_optimization.py` : Python script implementing the model using PuLP
* `README.md` : This documentation file

---

## 🚜 Future Enhancements

* Add user input for custom constraints and profits
* Visualize feasible region for 2-variable version
* Export results to CSV or Excel

---

---

## 📖 References

* [PuLP Documentation](https://coin-or.github.io/pulp/)
