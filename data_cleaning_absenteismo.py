import pandas as pd
raw_csv_data=pd.read_csv("C:/Users/Eduardo/Desktop/Data Science/Udemy BI Analyst/Part 7 - Integration/S47_L364/Absenteeism_data.csv")

df= raw_csv_data.copy()
df

df['Age'].min()

df.drop(['Age'],axis=1)

reason_columns=pd.get_dummies(df['Age'])
reason_columns

# reason_columns['Check']=reason_columns.sum(axis=1)
# reason_columns
# reason_columns['Check'].sum(axis=0)
# reason_col=reason_columns.drop(['Check'], axis=1)
# reason_col

ag1 = reason_columns.loc[:, :30].max(axis=1)
ag2 = reason_columns.loc[:, 31:40].max(axis=1)
ag3 = reason_columns.loc[:, 41:50].max(axis=1)
ag4 = reason_columns.loc[:, 51:].max(axis=1)

df=pd.concat([df,ag1,ag2,ag3,ag4],axis=1)
# df

df.columns.values

column_names=['ID', 'Reason for Absence', 'Date', 'Transportation Expense',
       'Distance to Work', 'Age', 'Daily Work Load Average',
       'Body Mass Index', 'Education', 'Children', 'Pets',
       'Absenteeism Time in Hours', 'Aged 20s', 'Aged 30s', 'Aged 40s', 'Aged 50s']

df.columns=column_names
df

column_names_reordered=['ID', 'Reason for Absence', 'Date', 'Transportation Expense',
       'Distance to Work', 'Age', 'Daily Work Load Average',
       'Body Mass Index', 'Education', 'Children', 'Pets',
        'Aged 20s', 'Aged 30s', 'Aged 40s', 'Aged 50s','Absenteeism Time in Hours']

df=df[column_names_reordered]
df

df_checkpoint=df.copy()
df_checkpoint

df_checkpoint['Date']=pd.to_datetime(df_checkpoint['Date'],format= '%d/%m/%Y')
# df_checkpoint['Date'][2].weekday()

def weekday(date):
    return date.weekday()
df_checkpoint['Weekday']=df_checkpoint['Date'].apply(weekday)
df_checkpoint

list_months= []

for i in range(df_checkpoint.shape[0]):
    list_months.append(df_checkpoint['Date'][i].month)

df_checkpoint['Month']=list_months
df_check2=df_checkpoint
df_check2

df_check2=df_check2.drop(['Date'],axis=1)
df_check2

df_check2.columns.values

names =(['ID', 'Reason for Absence','Aged 20s',
       'Aged 30s', 'Aged 40s', 'Aged 50s', 'Weekday', 'Month', 'Transportation Expense',
       'Distance to Work', 'Age', 'Daily Work Load Average',
       'Body Mass Index', 'Education', 'Children', 'Pets', 'Absenteeism Time in Hours'
       ])

df_check2= df_check2[names]
df_check2
