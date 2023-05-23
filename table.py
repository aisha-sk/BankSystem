import mysql.connector as sql
from datetime import date

todaydate = date.today()

conn=sql.connect(host='localhost',user='root',password='aisha585',database='BANK')
if conn.is_connected():
      print("sucessfully connected")
mycursor=conn.cursor()

mn="CREATE TABLE IF NOT EXISTS RECORDS( ACCOUNTNUM  INT(4) primary key,PASSWORD INT(3),NAME VARCHAR(20),CREATEAMT INT default(0),WITHDRAWL INT default(0),BALANCE INT default(0))"
mycursor.execute(mn)


mycursor.execute("CREATE TABLE IF NOT EXISTS TRANSACTIONHISTORY(ACCOUNTNUM INT(4), MONEYTRANSAC NUMERIC(8,2),DATES DATE)")

mycursor.execute("CREATE TABLE IF NOT EXISTS LOANS(ACCOUNTNUM INT(4), LOANTYPE VARCHAR(20), AMOUNT NUMERIC(8,2), DATETAKEN VARCHAR(20), EXPIRY VARCHAR(20), COLLATERAL VARCHAR(20))")


mycursor.execute("create table if not exists emp (EMPNUM INT PRIMARY KEY, EMPNAME VARCHAR(15), ASSIGNATION DATE, POSITION VARCHAR(15),SALARY NUMERIC(8,2), AVAILABILITY VARCHAR(30) DEFAULT 'AVAILABLE')")

mycursor.execute('alter table emp modify ASSIGNATION varchar(20)')
conn.commit()

#MySQL  localhost:33060+ ssl  bank  SQL > ALTER TABLE TRANSACTIONHISTORY ADD FOREIGN KEY(ACCOUNTNUM) REFERENCES RECORDS(ACCOUNTNUM);
#MySQL  localhost:33060+ ssl  bank  SQL > alter table transactionhistory modify dates varchar(20);
#MySQL  localhost:33060+ ssl  bank  SQL > alter table loans add foreign key(accountnum) references records(accountnum);
 