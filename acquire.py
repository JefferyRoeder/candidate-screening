import psycopg2
import env
import pandas as pd


def addresses():
    #creates connection with Postgresql DB
    connection = psycopg2.connect(user='jefferyroeder',
                              password=env.password,
                              host="127.0.0.1",
                              port="5432",
                              database="jefferyroeder")
    #creates cursor for DB
    cursor = connection.cursor()

    #selects entire table 'addresses'
    table = ''' SELECT * FROM addresses'''

    #executes query and creates dataframe
    cursor.execute(table)
    rows = cursor.fetchall()
    df = pd.DataFrame(rows)
    df.columns = ['address','city','state','zipcode','email','first_name','last_name']
    return df