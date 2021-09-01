import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def Fun():
    print("***********WELCOME TO MY PROJECT**********")
    
    print("ENTER any NUMBER FOR, What you like to see?")
    print("#1. Reading complete data with index.")
    print("#2. Reading complete data without index.")
    print("#3. Line Chart")
    print("#4. Bar Chart")
    print("#5. Scatter Chart")
    print("#6. Pie Chart")
    print("#7. Enter a new row.")
    print("#8. For Exit")

#***************************************************************************************

def Read_CSV():
    print("The Data")
    df=pd.read_csv('E:\\Rishi Study\\Projects\IP\\main files\\mobile.csv')
    print(df)

#***************************************************************************************

def No_Index():
    print("Reading the file without index")
    df=pd.read_csv('E:\\Rishi Study\\Projects\IP\\main files\\mobile.csv', index_col=0)
    print(df)

#****************************FOR LINE CHART*********************************************

def line_plot():
    print("    Press 1 to print the data for Price as per Mobile.")
    print("    Press 2 to print the data for Purchase as per Mobile.")
    print("    Press 3 to print the data for Sales as per Mobile.")
    print("    Press 4 to print the data for Returns as per Mobile.")
    print("    Press 5 to print All data.")
    df=pd.read_csv('E:\\Rishi Study\\Projects\IP\\main files\\mobile.csv')
    Mobile=df["Mobile"]
    Price=df["Price"]
    Purchase=df["Purchase"]
    Sales=df["Sales"]
    Returns=df["Returns"]
    plt.xlabel("Mobile")
  
    YC = int(input("Enter the number representing your preferred line chart from the above choices: "))
    
    if YC == 1:
        plt.ylabel("Price")
        plt.title("Mobile wise Prices")
        plt.plot(Mobile, Price, color='b')
        plt.show()
    elif YC == 2:
        plt.ylabel("Purchase")
        plt.title("Mobile Brands Wise Purchase")
        plt.plot(Mobile, Purchase, color='g')
        plt.show()
    elif YC == 3:
        plt.ylabel("Sales")
        plt.title("Mobile Brands Wise Sales")
        plt.plot(Mobile, Sales, color='r')
        plt.show()
    elif YC == 4:
        plt.ylabel("Returns")
        plt.title("Mobile Brands Wise Returns")
        plt.plot(Mobile, Returns, color='c')
        plt.show()
    elif YC == 5:
        plt.ylabel("Number of Mobile")
        plt.plot(Mobile, Price, color='b', label = "Mobile Brands Wise Price")
        plt.plot(Mobile, Purchase, color='g', label = "Mobile Brands Wise Purchase")
        plt.plot(Mobile, Sales, color='r', label = "Mobile Brands Wise Sales")
        plt.plot(Mobile, Returns, color='c', label = "Mobile Brands Wise Returns")
        plt.legend()
        plt.show()
    else:
        print("Enter valid input")
#_________________________________________________________________________________

#******************************FOR BAR GRAPH**************************************

def bar_plot():
    print("    Press 1 to print the data for Price as per Mobile.")
    print("    Press 2 to print the data for Purchase as per Mobile.")
    print("    Press 3 to print the data for Sales as per Mobile.")
    print("    Press 4 to print the data for Returns as per Mobile.")
    print("    Press 5 to print the data in form of stack bar chart")
    print("    Press 6 to print the data in form of multi bar chart")
    df = pd.read_csv('E:\\Rishi Study\\Projects\IP\\main files\\mobile.csv')
    Mobile = df["Mobile"]
    Price = df["Price"]
    Purchase = df["Purchase"]
    Sales = df["Sales"]
    Returns = df["Returns"]
    plt.xlabel("Mobile")

    YC = int(input("Enter the number representing your preferred bar graph from the above choices: "))
    
    if YC == 1:
        plt.ylabel("Price")
        plt.title("Mobile Brands Wise Price")
        plt.bar(Mobile, Price, color='b', width = 0.5)
        plt.show()
    elif YC == 2:
        plt.ylabel("Purchase")
        plt.title("Mobile Brands Wise Purchase")
        plt.bar(Mobile, Purchase, color='g', width = 0.5)
        plt.show()
    elif YC == 3:
        plt.ylabel("Sales")
        plt.title("Mobile Brands Wise Sales")
        plt.bar(Mobile, Sales, color='r', width = 0.5)
        plt.show()
    elif YC == 4:
        plt.ylabel("Returns")
        plt.title("Mobile Brands Wise Returns")
        plt.bar(Mobile, Returns, color='c', width = 0.5)
        plt.show()
    elif YC == 5:
        plt.bar(Mobile, Price, color='b', width = 0.5, label = "Mobile Brands Wise Price")
        plt.bar(Mobile, Purchase, color='g', width = 0.5, label = "Mobile Brands Wise Purchase")
        plt.bar(Mobile, Sales, color='r', width = 0.5, label = "Mobile Brands Wise Sales")
        plt.bar(Mobile, Returns, color='c',width = 0.5, label = "Mobile Brands Wise Returns")
        plt.legend()
        plt.show()
    elif YC == 6:
        D=np.arange(len(Mobile))
        width=0.25
        plt.bar(D,Price, width, color='b', label = "Mobile Brands Wise Price")
        plt.bar(D+0.25, Purchase, width, color='g', label = "Mobile Brands Wise Purchase")
        plt.bar(D+0.50, Sales, width, color='r', label = "Mobile Brands Wise Sales")
        plt.bar(D+0.75, Returns ,width, color='c', label = "Mobile Brands Wise Returns")
        plt.legend()
        plt.show()
    else:
        print("Enter valid input")
#____________________________________________________________________________

#************************FOR SCATTER CHART***********************************
        
def scatter_chart():
    print("    Press 1 to print the data for Price as per Mobile.")
    print("    Press 2 to print the data for Purchase as per Mobile.")
    print("    Press 3 to print the data for Sales as per Mobile.")
    print("    Press 4 to print the data for Returns as per Mobile.")
    print("    Press 5 to print the data in form of stack scatter chart")
    print("    Press 6 to print the data in form of multi scatter chart")

    df=pd.read_csv('E:\\Rishi Study\\Projects\IP\\main files\\mobile.csv')
    Mobile = df["Mobile"]
    Price = df["Price"]
    Purchase = df["Purchase"]
    Sales = df["Sales"]
    Returns = df["Returns"]

    YC = int(input("Enter the number representing your preferred scatter graph from the above choices: "))

    if YC == 1:
        plt.ylabel("Price")
        plt.title("Mobile Brands Wise Price")
        plt.scatter(Mobile, Price, color='b')
        plt.show()
    elif YC == 2:
        plt.ylabel("Purchase")
        plt.title("Mobile Brands Wise Purchase")
        plt.scatter(Mobile, Purchase, color='g')
        plt.show()
    elif YC == 3:
        plt.ylabel("Sales")
        plt.title("Mobile Brands Wise Sales")
        plt.scatter(Mobile, Sales, color='r')
        plt.show()
    elif YC == 4:
        plt.ylabel("Returns")
        plt.title("Mobile Brands Wise Returns")
        plt.scatter(Mobile, Returns, color='c')
        plt.show()
    elif YC == 5:
        plt.scatter(Mobile, Price, color='b', label = "Mobile Brands Wise Price")
        plt.scatter(Mobile, Purchase, color='g', label = "Mobile Brands Wise Purchase")
        plt.scatter(Mobile, Sales, color='r', label = "Mobile Brands Wise Sales")
        plt.scatter(Mobile, Returns, color='c', label = "Mobile Brands Wise Returns")
        plt.legend()
        plt.show()
    elif YC == 6:
        D=np.arange(len(Mobile))
        width=0.25
        plt.scatter(D,Price, width, color='b', label = "Mobile Brands Wise Price")
        plt.scatter(D+0.25, Purchase, width, color='g', label = "Mobile Brands Wise Purchase")
        plt.scatter(D+0.50, Sales, width, color='r', label = "Mobile Brands Wise Sales")
        plt.scatter(D+0.75, Returns ,width, color='c', label = "Mobile Brands Wise Returns")
        plt.legend()
        plt.show()
    else:
        print("Enter valid input")
#____________________________________________________________________________________

#************************************FOR PIE CHART***********************************

def pie_chart():

    print("    Press 1 to print the data for Price as per Mobile.")
    print("    Press 2 to print the data for Purchase as per Mobile.")
    print("    Press 3 to print the data for Sales as per Mobile.")
    print("    Press 4 to print the data for Returns as per Mobile.")

    df=pd.read_csv('E:\\Rishi Study\\Projects\IP\\main files\\mobile.csv')
    Mobile = df["Mobile"]
    Price = df["Price"]
    Purchase = df["Purchase"]
    Sales = df["Sales"]
    Returns = df["Returns"]

    YC = int(input("Enter the number representing your preferred scatter graph from the above choices: "))

    if YC == 1:
        plt.title("Mobile Brands Wise Price")
        plt.pie(Price, labels=Mobile, autopct="%5.2f%%")
        plt.show()
    elif YC == 2:
        plt.title("Mobile Brands Wise Purchase")
        plt.pie(Purchase, labels=Mobile, autopct="%5.2f%%")
        plt.show()
    elif YC == 3:
        plt.title("Mobile Brands Wise Sales")
        plt.pie(Sales, labels=Mobile, autopct="%5.2f%%")
        plt.show()
    elif YC == 4:
        plt.title("Mobile Brands Wise Returns")
        plt.pie(Returns, labels=Mobile, autopct="%5.2f%%")
        plt.show()
    else:
        print("Enter valid input")
#_________________________________________________________________________

#**********************ADD DATA*******************************************

def add_csv():
    df=pd.read_csv('E:\\Rishi Study\\Projects\IP\\main files\\mobile.csv')
    a = str(input('Enter Mobile Name: '))
    b = int(input('Enter Price of Mobile: '))
    c = int(input('Enter no. of Mobile Purchase: '))
    d = int(input('Enter no. of Mobile Sold: '))
    e = int(input('Enter no. of Mobile Returned: '))
    df =df.append({'Mobile':a,'Price':b,'Purchase':c,'Sales':d,'Returns':e,},ignore_index=True)
    df.to_csv('E:\\Rishi Study\\Projects\IP\\main files\\mobile.csv')
    print('Your record is added')

#**************************************************************************
#**************************************************************************
    
Fun()
YC = int(input("Enter Your Choice: "))

while YC == 1 or 2 or 3 or 4 or 5 or 6:

    if YC == 1:
        Read_CSV()
        break
    elif YC == 2:
        No_Index()
        break
    elif YC == 3:
        line_plot()
        break
    elif YC == 4:
        bar_plot()
        break
    elif YC == 5:
        scatter_chart()
        break
    elif YC == 6:
        pie_chart()
        break
    elif YC == 7:
        add_csv()
        add=str(input("Do You Want to Add Another Row (Y/N): "))
        if add=='Y':
            add_csv()
            break
        elif add=='y':
            add_csv()
            break
        elif add=='N':
            print("OKAY! Your row successfully added")
            break
        elif add=='n':
            print("OKAY! Your row successfully added")
            break
        else:
            print("Invalid Char Inputed...")
            break
    elif YC == 8:
        print("Thank You for using...")
        break
    else:
        print("Enter valid input")
        break
