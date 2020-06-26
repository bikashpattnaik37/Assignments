import pandas as pd
import pyodbc


data = pd.read_csv (r'C:\Users\Ron\Desktop\Test\TimeStamp.csv')   
df = pd.DataFrame(data, columns= ['Result Time','Granularity Period','Object Name','Cell ID',' CallAttemps'])


conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=RON\SQLEXPRESS;'
                      'Database=TestDB;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()


cursor.execute('CREATE TABLE people_info (Result Time DATE TIME), Granularity Period nvarchar(50),Object Name  varchar),(Cell ID int),(CallAttemps int)')

for row in df.itertuples():
    cursor.execute('''
                INSERT INTO TestDB.dbo.people_info (Result Time,Granularity Period ,Object Name,CallAttemps )
                VALUES (?,?,?)
                ''',
                row.Result_Time, 
                row.Granularity_Period,
                row.Object_Name
                row.CallAttemps
                )
conn.commit()