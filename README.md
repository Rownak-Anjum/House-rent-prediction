
# 🏠 House Price Prediction using Linear Regression

This simple Python script uses **Linear Regression** (via `scikit-learn`) to predict the price of a house based on its area (in square feet).

---

## 📋 Overview

The model is trained on a small sample dataset of house area vs. price. After training, it accepts user input (area in square feet) and predicts the estimated price using the trained model.

---

## 📊 Sample Data

The training data used is hardcoded as follows:

| Area (sqft) | Price (Tk) |
| ----------- | ---------- |
| 1000        | 20000      |
| 1500        | 30000      |
| 2000        | 40000      |
| 2500        | 50000      |
| 3000        | 60000      |

---

## 🚀 How It Works

1. The script creates a DataFrame using `pandas`.
2. A `LinearRegression` model is trained on the data.
3. The user is prompted to input the area of a house.
4. The model predicts the price based on the provided area.
5. The predicted price is printed in a formatted output.

---

## 🛠 Requirements

To run the script, make sure you have the following Python packages installed:

```bash
pip install pandas scikit-learn
```

---

## 🧾 Usage

Run the script using a Python interpreter:

```bash
python house_price_predictor.py
```

You'll be prompted to enter the area of the house:

```
Enter the area of the house in square feet:
2200
```

Output:

```
predicted price: Tk 44,000.00
predicted price: Tk 44,000
```

---

## 📁 Code Summary

```python
from sklearn.linear_model import LinearRegression
import pandas as pd

data = {
    'Area': [1000, 1500, 2000, 2500, 3000],
    'Price': [20000, 30000, 40000, 50000, 60000]
}

df = pd.DataFrame(data)

x = df[['Area']]
y = df['Price']

model = LinearRegression()
model.fit(x, y)

area = float(input("Enter the area of the house in square feet: \n"))
predicted_price = model.predict([[area]])

print(f"predicted price: Tk {predicted_price[0]:,.2f}")
print(f"predicted price: Tk {int(predicted_price[0]):,}")
```

---



