import pandas as pd

hotel_df = pd.read_csv('D:\Varun Athithiya\DE_ROADMAP_2025\data_engineer_2025\python\pandas\sample_dataset.csv', 
                sep="\t", 
                on_bad_lines="skip", 
                parse_dates=True, 
                infer_datetime_format=True,
                float_precision="high")


date_pattern = '^[0-9]{1,2}-[a-zA-Z]{1,9}-[0-9]{1,4}$'

hotel_df.columns = hotel_df.columns.str.lower()
hotel_df = hotel_df[hotel_df['date'].str.contains(date_pattern, regex=True, na=False)]

hotel_df['date'] = pd.to_datetime(hotel_df['date'], dayfirst=True)

hotel_df['year'] = hotel_df['date'].dt.year
hotel_df['month'] = hotel_df['date'].dt.month
hotel_df['day'] = hotel_df['date'].dt.day
hotel_df['month_name'] = hotel_df['date'].dt.month_name()
hotel_df['day_name'] = hotel_df['date'].dt.day_name()

print(hotel_df.head())