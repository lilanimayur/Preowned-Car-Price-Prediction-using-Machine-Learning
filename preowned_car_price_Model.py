#%%

import pandas as pd

#%%

dataset=pd.read_excel(r'E:\Machine Learning\verzeo project\Data_Train (1).xlsx')
test=pd.read_excel(r'E:\Machine Learning\verzeo project\Data_Test (1).xlsx')
#%%
dataset['Mileage'].replace(regex=True, inplace=True, to_replace=r'[a-z]*[/][a-z]*', value=r'')
test['Mileage'].replace(regex=True, inplace=True, to_replace=r'[a-z]*[/][a-z]*', value=r'')
dataset['Mileage'].replace(regex=True, inplace=True, to_replace=r'[a-z]*[/][a-z]*', value=r'')
test['Mileage'].replace(regex=True, inplace=True, to_replace=r'[a-z]*[/][a-z]*', value=r'')
dataset['Mileage'].replace(regex=True, inplace=True, to_replace=r'[a-z]*', value=r'')
test['Mileage'].replace(regex=True, inplace=True, to_replace=r'[a-z]*', value=r'')
dataset['Mileage'].replace(regex=True, inplace=True, to_replace=r'[a-z]*', value=r'')
test['Mileage'].replace(regex=True, inplace=True, to_replace=r'[a-z]*', value=r'')
dataset['Mileage'].replace(regex=True, inplace=True, to_replace=r"[' ']*", value=r'')
test['Mileage'].replace(regex=True, inplace=True, to_replace=r"[' ']*", value=r'')
dataset['Mileage'].replace(regex=True, inplace=True, to_replace=r"[' ']*", value=r'')
test['Mileage'].replace(regex=True, inplace=True, to_replace=r"[' ']*", value=r'')

dataset['Engine'].replace(regex=True, inplace=True, to_replace=r"[' ']['CC']*", value=r'')
test['Engine'].replace(regex=True, inplace=True, to_replace=r"[' ']['CC']*", value=r'')
dataset['Power'].replace(regex=True, inplace=True, to_replace=r"[' ']['bhp']*", value=r'')
test['Power'].replace(regex=True, inplace=True, to_replace=r"[' ']['bhp']*", value=r'')
dataset['Power'].fillna(74.0, inplace=True)
test['Power'].fillna(74.0, inplace=True)
dataset['Power'].replace(regex=True, inplace=True, to_replace=r"['null']", value=74.0)
test['Power'].replace(regex=True, inplace=True, to_replace=r"['null']", value=74.0)
dataset['Engine'].replace(regex=True, inplace=True, to_replace=r"['null']", value=1346.0)
test['Engine'].replace(regex=True, inplace=True, to_replace=r"['null']", value=1346.0)
dataset['Mileage'].replace(regex=True, inplace=True, to_replace=r"['null']", value=21.5)
test['Mileage'].replace(regex=True, inplace=True, to_replace=r"['null']", value=21.5)

#%%
dataset['Mileage'].fillna(dataset['Mileage'].median(), inplace=True)
dataset['Engine'].fillna(dataset['Engine'].median(), inplace=True)
test['Mileage'].fillna(test['Mileage'].median(), inplace=True)
test['Engine'].fillna(test['Engine'].median(), inplace=True)
#%%
dataset['Seats'].fillna(5.0, inplace=True)
test['Seats'].fillna(5.0, inplace=True)

#%%
from sklearn.preprocessing import LabelEncoder
labelencoder_X= LabelEncoder()
dataset.iloc[:,1:2]=labelencoder_X.fit_transform(dataset.iloc[:,1:2])
dataset.iloc[:,4:5]=labelencoder_X.fit_transform(dataset.iloc[:, 4:5])
dataset.iloc[:, 5:6]=labelencoder_X.fit_transform(dataset.iloc[:, 5:6])
dataset.iloc[:, 6:7]=labelencoder_X.fit_transform(dataset.iloc[:,6:7])
test.iloc[:,1:2]=labelencoder_X.fit_transform(test.iloc[:,1:2])
test.iloc[:,4:5]=labelencoder_X.fit_transform(test.iloc[:, 4:5])
test.iloc[:, 5:6]=labelencoder_X.fit_transform(test.iloc[:, 5:6])
test.iloc[:, 6:7]=labelencoder_X.fit_transform(test.iloc[:,6:7])

#%%
dataset=dataset.drop('Name', axis=1)
dataset=dataset.drop('New_Price', axis=1)
test=test.drop('Name', axis=1)
test=test.drop('New_Price', axis=1)
#%%
X=dataset.iloc[:, :-1].values
Y=dataset.iloc[:, 10].values

#%%
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3,random_state=0)
#%%
from sklearn.metrics import r2_score
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
linreg=LinearRegression()
polynomial_features = PolynomialFeatures(degree=2)
x_poly = polynomial_features.fit_transform(X_train)
x_polyt = polynomial_features.fit_transform(X_test)
linreg.fit(x_poly, Y_train)
y_pred = linreg.predict(x_polyt)
print(f'R2 with PolyRegression: {r2_score(Y_test, y_pred)}')

x_poly = polynomial_features.transform(test)
y_pred = linreg.predict(x_poly)
#%%
test["Price"] = y_pred
#%%
test.to_excel(r"E:\Machine Learning\verzeo project\Predicted_test.xlsx")

