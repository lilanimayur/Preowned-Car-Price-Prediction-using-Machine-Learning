#%%
import pandas as pd
dataset=pd.read_excel(r'Data_Train (1).xlsx')
#%%
dataset['Mileage'].replace(regex=True, inplace=True, to_replace=r'[a-z]*[/][a-z]*', value=r'')
dataset['Mileage'].replace(regex=True, inplace=True, to_replace=r'[a-z]*[/][a-z]*', value=r'')
dataset['Mileage'].replace(regex=True, inplace=True, to_replace=r'[a-z]*', value=r'')
dataset['Mileage'].replace(regex=True, inplace=True, to_replace=r'[a-z]*', value=r'')
dataset['Mileage'].replace(regex=True, inplace=True, to_replace=r"[' ']*", value=r'')
dataset['Mileage'].replace(regex=True, inplace=True, to_replace=r"[' ']*", value=r'')

dataset['Engine'].replace(regex=True, inplace=True, to_replace=r"[' ']['CC']*", value=r'')
dataset['Power'].replace(regex=True, inplace=True, to_replace=r"[' ']['bhp']*", value=r'')
dataset['Power'].fillna(74.0, inplace=True)
dataset['Power'].replace(regex=True, inplace=True, to_replace=r"['null']", value=74.0)
dataset['Engine'].replace(regex=True, inplace=True, to_replace=r"['null']", value=1346.0)
dataset['Mileage'].replace(regex=True, inplace=True, to_replace=r"['null']", value=21.5)

#%%
dataset['Mileage'].fillna(dataset['Mileage'].median(), inplace=True)
dataset['Engine'].fillna(dataset['Engine'].median(), inplace=True)
#%%
dataset['Seats'].fillna(5.0, inplace=True)

#%%
from sklearn.preprocessing import LabelEncoder
labelencoder_X= LabelEncoder()
dataset.iloc[:,1:2]=labelencoder_X.fit_transform(dataset.iloc[:,1:2])
dataset.iloc[:,4:5]=labelencoder_X.fit_transform(dataset.iloc[:, 4:5])
dataset.iloc[:, 5:6]=labelencoder_X.fit_transform(dataset.iloc[:, 5:6])
dataset.iloc[:, 6:7]=labelencoder_X.fit_transform(dataset.iloc[:,6:7])

#%%
dataset=dataset.drop('Name', axis=1)
dataset=dataset.drop('New_Price', axis=1)
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

#%%
from tkinter import *
window = Tk()
window.geometry('1920x1080')
window.configure(background="#36688D")
window.title("Car Price Predictor")

miFrame = Frame()
miFrame.pack()
miFrame.config(width="1920", heigh=("245"))

photo = PhotoImage(file="pic2.png")
photolabel =Label(miFrame, image=photo)
photolabel.pack()

miFrame2 = Frame()
miFrame2.pack()
miFrame2.config(width="1920", heigh=("830"))

photo2= PhotoImage(file="bg.png")
photolabel =Label(miFrame2, image=photo2)
photolabel.pack()


lbl1 = Label(window,text="Location                                          :",font=("Times ",20),bg="#36688D",fg="WHITE")
lbl1.place(x=100, y=380)
E1=Entry(window,bd=9,width=24,font = ('courier', 12, 'bold'))
E1.place(x=350,y=380)

lbl2 = Label(window,text="Year                           ",font=("Times ",20),bg="#36688D",fg="WHITE")
lbl2.place(x=100, y=430)
E2=Entry(window,bd=9,width=24,font = ('courier', 12, 'bold'))
E2.place(x=350,y=430)

lbl3 = Label(window,text="Kilometers Driven                               ",font=("Times ",20),bg="#36688D",fg="WHITE")
lbl3.place(x=100, y=480)
E3=Entry(window,bd=9,width=24,font = ('courier', 12, 'bold'))
E3.place(x=350,y=480)

lbl4 = Label(window,text="Fuel Type                              ",font=("Times ",20),bg="#36688D",fg="WHITE")
lbl4.place(x=100, y=530)
list1 = ['CNG', 'Diesel', 'Petrol', 'LPG', 'Electric'];
c = StringVar()
E4= OptionMenu(window, c, *list1)
E4.config(width=35, height=1)
c.set('Select Fuel Type')
E4.place(x=350,y=530)

lbl5 = Label(window,text="Transmission Type ",font=("Times ",20),bg="#36688D",fg="WHITE")
lbl5.place(x=100, y=580)
option1 = StringVar()
R1 = Radiobutton(window, text="Manual    ", value="Manual",bg="#36688D",font=("Times 19  bold"),fg="#720017",var=option1)
R2 = Radiobutton(window, text="Automatic ", value="Automatic",bg="#36688D",font=("Times 19 bold" ),fg="#720017",var=option1)
R1.place(x=350,y=580)
R2.place(x=500,y=580)

lbl6 = Label(window,text="Owner Type                        ",font=("Times ",20),bg="#36688D",fg="WHITE")
lbl6.place(x=100, y=630)
list2 = ['First', 'Second', 'Third', 'Fourth & Above'];
c1 = StringVar()
E5= OptionMenu(window, c1, *list2)
E5.config(width=35)
c1.set('Select Owner Type')
E5.place(x=350,y=630)

lbl7 = Label(window,text="Mileage                       ",font=("Times ",20),bg="#36688D",fg="WHITE")
lbl7.place(x=100, y=680)
E6=Entry(window,bd=9,width=24,font = ('courier', 12, 'bold'))
E6.place(x=350,y=680)

lbl8 = Label(window,text="Engine (CC)                                  ",font=("Times ",20),bg="#36688D",fg="WHITE")
lbl8.place(x=100, y=730)
E7=Entry(window,bd=9,width=24,font = ('courier', 12, 'bold'))
E7.place(x=350,y=730)

lbl9 = Label(window,text="""Power (BHP)                   """,font=("Times ",20),bg="#36688D",fg="WHITE")
lbl9.place(x=100, y=780)
E8=Entry(window,bd=9,width=24,font = ('courier', 12, 'bold'))
E8.place(x=350,y=780)

lbl10 = Label(window,text="Seats                      ",font=("Times ",20),bg="#36688D",fg="WHITE")
lbl10.place(x=100, y=830)
E9=Entry(window,bd=9,width=24,font = ('courier', 12, 'bold'))
E9.place(x=350,y=830)

def clicked():

    a1 = E1.get()
    a2 = E2.get()
    a3 = E3.get()
    a8 = E6.get()
    a9 = E7.get()
    a10 = E8.get()
    a11 = E9.get()


    data=[[str(a1),float(a2),float(a3),str(c),str(option1),str(c1),float(a8),float(a9),float(a10),float(a11)]]
    df=pd.DataFrame(data,columns=['Location','Year','Kilometers_Driven','Fuel_Type','Transmission','Owner_Type','Mileage','Engine','Power','Seats'])
    df.iloc[:, 0:1] = labelencoder_X.fit_transform(df.iloc[:, 0:1])
    df.iloc[:, 3:4] = labelencoder_X.fit_transform(df.iloc[:, 3:4])
    df.iloc[:, 4:5] = labelencoder_X.fit_transform(df.iloc[:, 4:5])
    df.iloc[:, 5:6] = labelencoder_X.fit_transform(df.iloc[:, 5:6])


    x_poly = polynomial_features.transform(df)
    y_pred = linreg.predict(x_poly)


    lbl11 = Label(window, text="Predicted Price is " + "\n" + str(y_pred[0]), font=("Times ", 45), bg="#36688D",
                  fg="WHITE")
    lbl11.place(x=970, y=480)

BuTTON = Button(bg="#132226", bd=25, text="       Predict        ", padx=1, pady=1, fg="#F3CD05",
                    font=('courier', 25, 'bold'), command=clicked)
BuTTON.place(x=190, y=910)

window.mainloop()
