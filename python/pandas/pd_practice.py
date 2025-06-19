import pandas as pd

hotel_df = pd.read_csv('D:\Varun Athithiya\DE_ROADMAP_2025\data_engineer_2025\python\pandas\sample_dataset.csv', 
                sep="\t", 
                on_bad_lines="skip", 
                parse_dates=True, 
                infer_datetime_format=True,
                float_precision="high")
hotel_df = hotel_df.dropna()

def splitTime (df, date_field, component):
    df = df.dropna()
    df[date_field] = pd.to_datetime(df[date_field])
    dt_accessor = getattr(df[date_field].dt, component)
    df[component] = dt_accessor() if callable(dt_accessor) else dt_accessor
    return df

def computeTimeComponents(df, date_field):
    return(
        df
        .pipe(splitTime, date_field, 'year')
        .pipe(splitTime, date_field, 'month')
        .pipe(splitTime, date_field, 'day')
        .pipe(splitTime, date_field, 'day_name')
        .pipe(splitTime, date_field, 'month_name')
    )
# print(computeTimeComponents(hotel_df, 'Date'))

# hotel_df = hotel_df.dropna()
# if callable(pd.to_datetime(hotel_df['Date']).dt.year):
#     print(True)
# else:
#     print(False)

# LOC, ILOC, IX 
hotel_df_1 = hotel_df.copy().head(10)
# hotel_df_1 = hotel_df.drop(columns=['Date'], axis=1)
hotel_df_1['Room number'] = hotel_df_1['Room number'].astype('int')
# print(type(hotel_df_1.loc[0:22, 'Company':'Person Name']))
# print(type(hotel_df_1['Company']))
# print(hotel_df_1)
# print(hotel_df.columns)
# print(hotel_df_1.iloc[0:10, 0:3])
print(hotel_df_1.iloc[:,:])


# hotel_df.columns = hotel_df.columns.str.lower()
# hote_df.columns = hotel_df.columns.apply(lambda x: x.lower())

# filtering the dataset based on a regex pattern for date
# hotel_df = hotel_df[hotel_df['date'].str.contains('^[0-9]{1,2}-[a-zA-Z]{1,9}-[0-9]{1,4}$', regex=True, na=False)]

# converting the field to datetime
# hotel_df['date'] = pd.to_datetime(hotel_df['date'], dayfirst=True)
# hotel_df['date'] = hotel_df['date'].dt.tz_localize('UTC')

# extracting date components from the date field
# hotel_df['year'] = hotel_df['date'].dt.year
# hotel_df['month'] = hotel_df['date'].dt.month
# hotel_df['day'] = hotel_df['date'].dt.day
# hotel_df['month_name'] = hotel_df['date'].dt.month_name()
# hotel_df['day_name'] = hotel_df['date'].dt.day_name()
# hotel_df['timestamp'] = hotel_df['date'].apply(lambda x: x.timestamp())
# hotel_df['first_name'] = hotel_df['person name'].apply(lambda x: x.split(' ')[0])
# hotel_df['last_name'] = hotel_df['person name'].apply(lambda x: x.split(' ')[1])

# print(hotel_df)
# hotel_df['first_name'] = hotel_df['first_name'].apply(lambda x: x.lower())
# hotel_df['last_name'] = hotel_df['last_name'].apply(lambda x: x.lower())

# print(type(hotel_df.columns))
# print(type(hotel_df['date']))
# print(type(hotel_df['first_name']))
# print(hotel_df)
