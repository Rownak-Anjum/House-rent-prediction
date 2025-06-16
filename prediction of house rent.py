from sklearn.linear_model import LinearRegression
import pandas as pd

#sample data:Area vs Price
data={
    'Area':[1000,1500,2000,2500,3000],
    'Price':[20000,30000,40000,50000,60000]

}

df=pd.DataFrame(data)

#show frist 5 rows
print("Data Preview:")
print(df.head())

#step 3:Train a simple model
x= df[['Area']]
y= df['Price']


#create and train the model
model=LinearRegression()
model.fit(x,y)

#take user input for area
area=float(input("Enter the area of the house in square feet: \n"))

#predict price of a 2200 sqft house
predicted_price = model.predict([[area]])

print(f"predicted price: Tk {predicted_price[0]:,.2f}\n")
print(f"predicted price: Tk {int(predicted_price[0]):,}")