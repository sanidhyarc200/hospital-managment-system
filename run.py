import pandas as pd
import os
import matplotlib.pyplot as plt


def searchdoctor():
    Id = int(input("Enter a member id : "))
    bdf = pd.read_csv("C:/Users/shree/Downloads/doctorslist.csv")
    df = bdf.loc[bdf["Id"] == Id]
    if df.empty:
        print("No member found with given name")
    else:
        print("Members details are :")
        print(df)



def deletedoctor():
    Id = float(input("Enter a member id : "))
    bdf = pd.read_csv("C:/Users/shree/Downloads/doctorslist.csv")
    os.chmod("C:/Users/shree/Downloads/doctorslist.csv",0o777)
    bdf = bdf.drop(bdf[bdf["Id"] == Id].index)
    bdf.to_csv("C:/Users/shree/Downloads/doctorslist.csv", index=False)
    print("Member Deleted Successfully")
    print(bdf)


def adddoctor():
    Id = int(input("Enter a doctor id : "))
    Doctor_in_charge  = input("Enter member name : ")
    Salary = int(input("Enter Salary : "))
    Age = int(input("Enter Age : "))
    Specialization = input("Enter Specialization : ")
    DOJ = input("Enter Date of joining : ")
    Mob = int(input("Enter Mobile number : "))

    mdf = pd.read_csv("C:/Users/shree/Downloads/doctorslist.csv")
    n = mdf["Id"].count()
    mdf.at[n] = [Id,Doctor_in_charge,Salary,Age,Specialization,DOJ,Mob]
    mdf.to_csv("C:/Users/shree/Downloads/doctorslist.csv",index = False)
    print("New Member added successfully")
    print(mdf)



def searchpatient():
    s_no = float(input("Enter a member id : "))
    bdf = pd.read_csv(r"C:/Users/shree/Downloads/patientsList.csv")
    df = bdf.loc[bdf["s_no"] == s_no]
    if df.empty:
        print("No member found with given name")
    else:
        print("Members details are :")
        print(df)


def deletepatient():
    s_no = float(input("Enter a member id : "))
    bdf = pd.read_csv(r"C:/Users/shree/Downloads/patientsList.csv")
    bdf = bdf.drop(bdf[bdf["s_no"] == s_no].index)
    bdf.to_csv(r"C:/Users/shree/Downloads/patientsList.csv", index=False)
    print("Member Deleted Successfully")
    print(bdf)

def addpatient():
    s_no = int(input("Enter a patient id : "))
    Name = input("Enter patient name : ")
    Age = int(input("Enter Age : "))
    Disease = input("Enter Disease : ")
    Address = input("Enter Address : ")
    m_no = int(input("Enter Mobile number : "))
    Dr_name = input("Enter Doctor name : ")
    DOA = input("enter date of admission")
    Billing_Amount = int(input("Enter Billing amount : "))

    mdf = pd.read_csv(r"C:/Users/shree/Downloads/patientsList.csv")
    n = mdf["s_no"].count()
    mdf.at[n] = [s_no,Name, Age,Disease,Address,m_no,Dr_name,DOA,Billing_Amount]
    mdf.to_csv(r"C:/Users/shree/Downloads/patientsList.csv", index=False)
    print("New Member added successfully")
    print(mdf)



def searchstaff():
    E_id = float(input("Enter a member id : "))
    bdf = pd.read_csv(r"C:/Users/shree/Downloads/stafflist.csv")
    df = bdf.loc[bdf["E_id"] == E_id]
    if df.empty:
        print("No member found with given name")
    else:
        print("Members details are :")
        print(df)


def deletestaff():
    E_id = float(input("Enter a member id : "))
    bdf = pd.read_csv(r"C:/Users/shree/Downloads/stafflist.csv")
    bdf = bdf.drop(bdf[bdf["E_id"] == E_id].index)
    bdf.to_csv(r"C:/Users/shree/Downloads/stafflist.csv", index=False)
    print("Member Deleted Successfully")
    print(bdf)



def addstaff():
    E_id = int(input("Enter a Employee id : "))
    Em_name = input("Enter member name : ")
    Em_salary = int(input("Enter Salary : "))
    Em_doj = input("Enter Date of joining : ")
    Age = int(input("Enter Age : "))
    Job = input("Enter Job : ")
    Mob = int(input("Enter Mobile number : "))

    mdf = pd.read_csv(r"C:/Users/shree/Downloads/stafflist.csv")
    n = mdf["E_id"].count()
    mdf.at[n] = [E_id,Em_name,Em_salary,Em_doj,Job,Age, Mob]
    mdf.to_csv(r"C:/Users/shree/Downloads/stafflist.csv", index=False)
    print("New Member added successfully")
    print(mdf)



def Showchart():
    print("Press 1 - salary of doctor ")
    print("Press 2 - patients amount of billing")
    ch = int(input("Enter your choice : "))
    if ch == 1:
        df = pd.read_csv("C:/Users/shree/Downloads/doctorslist.csv")
        #df["DOA"] = df["DOA"].astype('datetime64[ns]')
        df = df[["Doctor_in_charge", "Salary"]]
        df.plot("Doctor_in_charge", "Salary", kind='bar')
        plt.xlabel('Doctor_in_charge------->')
        plt.ylabel('DOA------->')
        plt.show()

    if ch == 2:
        df = pd.read_csv(r"C:/Users/shree/Downloads/PatientsList.csv")
        df["Billing_Amount"] = df["Billing_Amount"].astype(float)
        df = df[["Name","Billing_Amount" ]]
        df.plot(kind='bar', color="red")
        plt.show()


def searchmenu():
    print("-------------------------------------------------------")
    print("           Hospital management system                  ")
    print("-------------------------------------------------------")
    print("press 1 - Search a doctor")
    print("press 2 - Delete a doctor")
    print("press 3 - Add a doctor")
    print("press 4 - Search a patient information")
    print("press 5 - Delete a patient")
    print("press 6 - Add a patient")
    print("press 7 - Search a staff member")
    print("press 8 - Delete a staff member")
    print("press 9 - Add a staff member")
    print("press 10 - View a chart")
    print("press 11 - To exit")
    choice = int(input("Enter your choice : "))
    return choice
#if login():
while True:
    ch = searchmenu()
    if ch == 1:
        searchdoctor()
    elif ch == 2:
        deletedoctor()
    elif ch == 3:
        adddoctor()
    elif ch == 4:
        searchpatient()
    elif ch == 5:
        deletepatient()
    elif ch == 6:
        addpatient()
    elif ch == 7:
        searchstaff()
    elif ch == 8:
        deletestaff()
    elif ch == 9:
        addstaff()
    elif ch == 10:
        Showchart()
    elif ch == 11:
        break
    else:
        print("Invalid option selected")

print("Thankyou for visiting our system")
