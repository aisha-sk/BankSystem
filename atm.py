
import mysql.connector as sql

from datetime import date

from captcha.image import ImageCaptcha 

from PIL import Image 

import random

todaydate = str(date.today())

conn=sql.connect(host='localhost',user='root',password='aisha585',database='BANK')
c1=conn.cursor(buffered=True)
print("================================================================================")

print("BANK MANAGEMENT SYSTEM")

print("================================================================================")




while True:
    print('\nWelcome, thank you for visiting us today.\nTo continue, choose an option from the following.')
    print("1.Signup as a user")
    print("2.User Login")
    print("3.Exit")
    print("4.Admin Portal")
    print("5.Employee Portal")
    print("================================================================================")

    op=int(input("Enter your choice (1/2/3/4/5) :"))
    print("================================================================================")

    if op==5:
        print('**** WELCOME TO APEX BANK EMPLOYEE PORTAL ****')
        print('1.NEW EMPLOYEE','\n2.EXISTING EMPLYOYEE','\n3.CHECK EMPLOYEE AVAILABILITY')
        choice=int(input('ENTER 1/2/3:'))
        if choice==1:
            enum=int(input('ENTER ASSIGNED EMPLOYEE ID NUMBER:-')) #to check if ID is already registered
            c1.execute('select * from EMP where EMPNUM={}'.format(enum))
            rec=c1.fetchall() 
            row=c1.rowcount #returns a row if accnum exists
            if row==1:
                print('THIS EMPLOYEE NUMBER ALREADY EXISTS!')
                print('PLEASE LOGIN AS AN EXISTING EMPLOYEE')

            #if it does not exist
            else:
                ename=input('ENTER REGISTERED EMPLOYEE NAME:')
                joining=input('ENTER JOINING DATE:')
                pos=input('ENTER ALOTTED POST:')
                sal=int(input('ENTER SALARY:'))
                c1.execute("insert into EMP (EMPNUM,EMPNAME,ASSIGNATION,POSITION,SALARY) values({},'{}','{}','{}',{})".format(enum,ename,joining,pos,sal))
                conn.commit()
                print('EMPLOYEE DATA SUCCESSFULLY ADDED TO PORTAL')
                
            


        if choice==2:
            ename=input('ENTER YOUR REGISTERED NAME:')
            c1.execute("select * from emp where EMPNAME='{}'".format(ename))
            c1.fetchall()
            record=c1.rowcount
            if record==1:
                print('**** NAME MATCHED ****')
                print('CHOOSE YOUR PREFERRED SERVICE:')
                print('1.CHECK CLIENT LOAN HISTORY','\n2.REQUEST LEAVE','\n3.CHECK MONTHLY PAYROLL','\n4.EXIT FROM PORTAL')
                cf=int(input('enter choice:'))
                if cf==1:
                    acct=int(input('ENTER CLIENT ACCOUNT NUMBER:'))
                    c1.execute("select*from loans where ACCOUNTNUM={}".format(acct))
                    rec=c1.fetchone()
                    conn.commit()
                    print(rec)

                if cf==2:
                    eno=int(input('ENTER EMPLOYEE NUMBER:'))
                    fromdat=input('ENTER LEAVE SANCTION DATE:')
                    enddat=input('ENTER LEAVE END DATE:')
                    c1.execute("update emp set availability='On Leave' where empnum={}".format(eno))
                    print('LEAVE FROM',fromdat,'TO',enddat,'SENT FOR REQUEST')
                    conn.commit()
                    
                    
                
                if cf==3:
                    eno=int(input('ENTER EMPLOYEE NUMBER:'))
                    c1.execute('select * from emp where EMPNUM={}'.format(eno))
                    
                    for i in c1:
                        print('Salary: ',i[4])
                

                if cf==4:
                    print('EMPLOYEE PORTAL CLOSED')

        if choice==3:
            av='available'
            eno=int(input('ENTER EMPLOYEE NUMBER:'))
            c1.execute("select availability from emp where EMPNUM={} and AVAILABILITY='{}'".format(eno,av))
            c1.fetchall()
            data=c1.rowcount
            if data==1:
                print('EMPLOYEE',eno,'IS AVAILABLE')
            else:
                print('EMPLOYEE',eno,'IS NOT AVAILABLE')

    if op==4:
        print ('Please verify that you are not a robot by entering what you see in Captcha Verification Image.')
        image = ImageCaptcha(width = 280, height = 90)
        captcha_text = 'Apex Bank'
        data = image.generate(captcha_text)
        im = Image.open('/Users/aishakhan/Desktop/cs docs/sql/CAPTCHA.png')
        
        im.show() 

        captchainput=str(input('Enter words in Captcha: '))
        if captchainput==captcha_text:
            print('Sucessful!')

            print('''Choose one of the following:
            
            1. View employee records
            2. View specific employee details
            3. View transaction history table
            4. View specific transaction history of user
            5. View User Table
            6. View Specific Records of User
            7. View Loan Table
            8. View Specific Loan
            0. Exit System''')

            
            while True:
                choice=int(input('Enter choice:'))
                if choice==1:
                    c1.execute("select * from emp")
                    for i in c1:
                        print('Employee Number: ',i[0], '  Employee Name: ',i[1], '  Designation: ',i[3])
                    y=input("Do you want to continue? (y/n) -")
                    if y=="y":
                        continue
                    else:
                        print("Thank you")
                        break

                if choice==2:
                    eno=eval(input('Enter employee number:'))
                    c1.execute("select * from emp where empnum={}".format(eno))
                    for i in c1:
                        print('Employee Number: ',i[0], '  Employee Name: ',i[1], '  Designation: ',i[3])
                    y=input("Do you want to continue? (y/n) -")
                    if y=="y":
                        continue
                    else:
                        print("Thank you")
                        break

                if choice==3:
                    
                    c1.execute("select * from transactionhistory")
                    for i in c1:
                        print('Account Number: ',i[0], '  Money Deposited: ',i[1], '  Date: ',i[2])
                    y=input("Do you want to continue? (y/n) -")
                    if y=="y":
                        continue
                    else:
                        print("Thank you")
                        break

                if choice==4:
                    acct=eval(input('Enter the account number: '))
                    c1.execute("select * from transactionhistory where accountnum=%d"%(acct))
                    for i in c1:
                        print('Account Number: ',i[0], '  Money Deposited: ',i[1], '  Date: ',i[2])
                    y=input("Do you want to continue? (y/n) -")
                    if y=="y":
                        continue
                    else:
                        print("Thank you")
                        break

                if choice==5:
                    c1.execute("Select * from records")
                    for i in c1:
                        print('Account Number: ',i[0], '  PASSWORD: ',i[1], ' NAME:',i[2], '  BALANCE:',i[3])
                    y=input("Do you want to continue? (y/n) -")
                    if y=="y":
                        continue
                    else:
                        print("Thank you")
                        break

                if choice==6:
                    acct=eval(input('Enter the account number: '))
                    c1.execute("Select * from records where accountnum=%d"%acct)
                    for i in c1:
                        print('Account Number: ',i[0], '  PASSWORD: ',i[1], ' NAME:',i[2], '  BALANCE:',i[3])
                    y=input("Do you want to continue? (y/n) -")
                    if y=="y":
                        continue
                    else:
                        print("Thank you")
                        break

                if choice==7:
                    c1.execute("Select * from loans")
                    for i in c1:
                        print('Account Number: ',i[0], '  Loan Type:',i[1], ' Amount:',i[2], '  Date Taken: ',i[3],'  Expiry:',i[4], ' Collateral: ',i[5])
                    y=input("Do you want to continue? (y/n) -")
                    if y=="y":
                        continue
                    else:
                        print("Thank you")
                        break

                if choice==8:
                    acct=eval(input('Enter the account number: '))  
                    c1.execute("Select * from loans where accountnum=%d"%acct)
                    for i in c1:
                        print('Account Number: ',i[0], '  Loan Type:',i[1], ' Amount:',i[2], '  Date Taken: ',i[3],'  Expiry:',i[4], ' Collateral: ',i[5])
                    y=input("Do you want to continue? (y/n) -")
                    if y=="y":
                        continue
                    else:
                        print("Thank you")
                        break
                if choice==0:
                    break

                
        else:
            print('Incorrect. Try again.')
            
        
    if op==1:
        c="y"
        while c=="y":
                m=random.randint(1000,9999)
                cb="select * from records where ACCOUNTNUM={}".format(m)
                c1.execute(cb)
                d=c1.fetchall()
                data=c1.rowcount
                if data==1:
                    print("================================================================================")

                    print("This account number already exists:")
                    c=input("Do you want to continue y/n -")
                    print("================================================================================")

                    if c=="y":
                            continue
                    else:
                            print("Thank you.")
                            
                            print("================================================================================")
                    

                else:
                    name=input("Enter name:")
                    passw=int(input("Enter password:"))
                    ab="insert into records(ACCOUNTNUM,PASSWORD,NAME) values({},{},'{}')".format(m,passw,name)
                    print("================================================================================")

                    c1.execute(ab)
                    conn.commit()
                    print("Account has been sucessfully created!")
                    print('Your assigned account number is',m)
                    print("The minimum balance in an account is alloted to be 1000 ")
                    print("================================================================================") 

                    s=int(input("Enter the amount to be deposited : "))
                    print("================================================================================")

                    sr="update records set  CREATEAMT={} where ACCOUNTNUM={}".format(s,m)
                    c1.execute(sr)
                    conn.commit()
                    ef="update records set balance=CREATEAMT-withdrawl where ACCOUNTNUM={}".format(m)
                    c1.execute(ef)
                    conn.commit()
                    print("sucessfully deposited")

                    print("Thank you")
                    print("Visit again")
                    break
    if op==2:
        y="y"
        while y=="y":
                
                acct=int(input("Enter account number:"))
                
                cb="select * from records where ACCOUNTNUM={}".format(acct)
                c1.execute(cb)
                c1.fetchall()
                data=c1.rowcount
                if data==1:
                    pas=int(input("Enter password  :"))
                    print("================================================================================")

                    e="select password from records where ACCOUNTNUM={}".format(acct)
                    c1.execute(e)
                    a=c1.fetchone()
                    d=list(a)
                    if pas==d[0]:
                        
                            print("1.Depositing money")
                            print("2.Withdrawing money")
                            print("3.Transfering money")
                            print("4.Checking balance")
                            
                            print("5.View Transaction History")
                            print("6.View Loan Details (if available)")
                            print("7.Take Loan")
                            print("0.Exit")
                            print("================================================================================")

                            r=int(input("Enter your choice:"))
                            print("================================================================================")

                            if r==1:
                                amt=int(input("Enter the money to be deposited:"))
                                print("================================================================================")

                                sr="update records set CREATEAMT=CREATEAMT+ {} where ACCOUNTNUM={}".format(amt,acct)
                                c1.execute(sr)
                                conn.commit()
                                ef="update records set balance=CREATEAMT-withdrawl where ACCOUNTNUM={}".format(acct)
                                c1.execute(ef)
                                conn.commit()
                                print("sucessfully deposited")
                                
                                cz="insert into TRANSACTIONHISTORY(accountnum,moneytransac) values({},{})".format(acct,amt)
                                c1.execute(cz)
                                conn.commit()
                                cz2="update TRANSACTIONHISTORY set dates='%s' where accountnum=%d"%(todaydate,acct)
                                c1.execute(cz2)
                                conn.commit()
                                
                                t=input("Do you want to continue y/n -")
                                print("================================================================================")

                                if t=="y":
                                        continue
                                else:
                                        print("Thank you")
                                        break

                            if r==2:
                                amt=int(input("Enter the money to withdraw:"))
                                print("================================================================================")

                                ah="select  BALANCE from records where ACCOUNTNUM={}".format(acct)
                                c1.execute(ah)
                                m=c1.fetchone()
                                if amt >m[0]:
                                        print("Your are having less than",amt)
                                        print("Please try again")
                                        print("================================================================================")

                                else:
                                        sr="update records set balance=balance - {}  where ACCOUNTNUM={}".format(amt,acct)
                                        ed="update records set  WITHDRAWL ={}  where ACCOUNTNUM={}".format(amt,acct)
                                        c1.execute(ed)
                                        c1.execute(sr)
                                        conn.commit()
                                        print("Sucessfully updatad")
                                y=input("do you want to continue y/n -")
                                if y=="y":
                                        continue
                                else:
                                        print("Thank you")
                                        break
                            
                            if r==3:
                                act=int(input("Enter the account number where amount is to be deposited:"))

                                print("================================================================================")

                                cb="select * from records where ACCOUNTNUM={}".format(act)
                                c1.execute(cb)
                                c1.fetchall()
                                data=c1.rowcount
                                if data==1:
                                        print(act ,"number exists")
                                        m=int(input("Enter the money to be transferred :"))

                                        print("================================================================================")

                                        ah="select  BALANCE from records where ACCOUNTNUM={}".format(acct)
                                        c1.execute(ah)
                                        c=c1.fetchone()
                                        if m > c[0]:
                                            print("Your account has less than ",m)
                                            print("Please try again.")

                                            print("================================================================================")

                                        else:
                                            av="update records set balance=balance-{} where ACCOUNTNUM={}".format(m,acct)  
                                            cv="update records set balance=balance+{} where ACCOUNTNUM={}".format(m,act)
                                            w="update records set withdrawl=withdrawl+{} where ACCOUNTNUM={}".format(m,acct)
                                            t="update records set  CREATEAMT=CREATEAMT+{} where ACCOUNTNUM={}".format(m,act)
                                            c1.execute(av)
                                            c1.execute(cv)
                                            c1.execute(w)
                                            c1.execute(t)
                                            conn.commit()
                                            print("Sucessfully transfered")
                                        y=input("Do you want to continue? (y/n) -")
                                        if y=="y":
                                            continue
                                        else:
                                            print("Thank you")
                                            break
                            if r==4:
                                ma="select balance from records where ACCOUNTNUM={}".format(acct)
                                c1.execute(ma)
                                k=c1.fetchone()
                                print("Balance in your account=",k)
                                print("================================================================================")

                                y=input("Do you want to continue? (y/n) -")
                                if y=="y":
                                        continue
                                else:
                                        print("Thank you")
                                        break
                            

                            if r==5:
                                acct=eval(input('Enter your account number: '))
                                c1.execute("select * from transactionhistory where accountnum=%d"%(acct))
                                for i in c1:
                                        print('Account Number: ',i[0], '  Money Deposited: ',i[1], '  Date: ',i[2])



                            if r==6:
                            
                                acct=eval(input('Enter the account number: '))  
                                c1.execute("Select * from loans where accountnum=%d"%acct)
                                for i in c1:
                                    print('Account Number: ',i[0], '  Loan Type:',i[1], ' Amount:',i[2], '  Date Taken: ',i[3],'  Expiry:',i[4], ' Collateral: ',i[5])
                                    
                                    t=input("Do you want to continue ? (y/n) -")
                                    print("================================================================================")

                                    if t=="y":
                                            continue
                                else:
                                        print("NO LOAN HISTORY TO DISPLAY")
                                        break

                            if r==7:
                                acct1=int(input('Enter your account number: '))
                                loantype=str(input('Enter loan type:'))
                                amt1=int(input('Enter loan amount:'))
                                col1=str(input('Enter collateral:'))
                                c1.execute("insert into loans values(%d,'%s',%d,'%s','2023-8-1','%s')"%(acct1,loantype,amt1,todaydate,col1))
                                conn.commit()

                                print('\nYour loan expiry date is 2023-8-1\n')

                                

                            if r==0:
                                break
                
                    
                    else:
                            print("Wrong password")
                            print("================================================================================")

                            y=input("do you want to continue ? (y/n)-")
                            if t=="y":
                                        continue
                            else:
                                    print("Thank you")
                                    break
                
                    
                else:
                    print("Your account does not exist.")
                    break

        

    if op==3:
        print("Exiting...")
        break