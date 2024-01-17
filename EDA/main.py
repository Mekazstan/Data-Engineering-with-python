import pandas as pd

df=pd.read_csv('scooters.csv')

print(df.columns)
# print(df.head(5))

# Dropping a column     NB: inplace=True  ensures it modifies the original dataset
# df.drop(columns=['Start Community Area Number', 'End Community Area Number'], inplace=True)

# Dropping a row
# df.drop(index=[275], inplace=True)


# ------------- Dealing with null values -------------

# # Displaying null counts for all columns
# print(df.isnull().sum())

# # Checking for null values in a specific column
# print(df['Start Community Area Number'][(df['Start Community Area Number'].isnull())])

# # Dropping the null columns
# df.dropna(subset=['start_location_name'],inplace=True)        # NB: Parameters to be passed (axis, how, thresh, subset, inplace)

# # Filling null columns with values
# df.fillna(value='00:00:00',axis='columns')

# # Filling null columns with values continued
# startstop=df[(df['Start Community Area Name'].isnull())&(df['End Community Area Name'].isnull())]
# value={'Start Community Area Name':'Start St.','End Community Area Name':'Stop St.'}
# startstop.fillna(value=value, inplace=True)
# print(startstop[['Start Community Area Name','End Community Area Name']])



# ------------- FIltering -------------

# # Filtering by value
# may=df[(df['Vendor']=='bird')]
# print(may)

# # Counting values in a column
# print(df['Vendor'].value_counts())




# ------------- Creating and modifying columns -------------

# # Changing column casing
# df.columns=[x.lower() for x in df.columns] 
# df.columns=[x.upper() for x in df.columns]
# print(df.columns)

# # Renaming columnn 
# df.rename(columns={'Start Community Area Number':'start_area_name'},inplace=True)
# df.rename(columns={'Start Community Area Number':'start_area_name','End Community Area Name':'end_area_name'},inplace=True)
# print(df.columns)

# # Changing the casing of values in a column
# df['Vendor']=df['Vendor'].str.upper()
# df['Vendor']=df['Vendor'].str.lower()

# # Creating a new column and assigning values to each row of the column
# for i,r in df.head().iterrows():
#     if r['Vendor']=='bird':
#         df.at[i,'new_column']='Vendor is bird'
#     else:
#         df.at[i,'new_column']='Not bird vendor'
# print(df[['Vendor','new_column']].head())

# # More efficient way of iterating
# # Create a new column and set default value to 'not a bird'
# df['new_column'] = 'Not bird vendor'
# df.loc[df['Vendor'] == 'bird', 'new_column'] = 'Vendor is bird'
# print(df[['Vendor', 'new_column']])


# # Creating column by spilting a column
# started_ad=df[['Trip ID','Start Time']].head()
# new=started_ad['Start Time'].str.split(expand=True)
# print(new.head())
# started_ad['date']=new[0]
# started_ad['time']=new[1]
# print(started_ad.head())




# ------------- Converting to datetime -------------

# df['Start Time']=pd.to_datetime(df['Start Time'],format='%m/%d/%Y %H:%M')
# when = '2019-05-23'
# print(df[(df['Start Time']>when)])


# ------------- Geocoding the location -------------
# new=pd.DataFrame(df['start_location_name'].value_counts().head())
# new.reset_index(inplace=True)
# new.columns=['address','count']
# new



# ------------- Joining Dataframes -------------
# joined=new.join(other=geo,how='left',lsuffix='_new',rsuffix='_geo')
# joined[['street_new','street_geo','x','y']]
                #OR
# merged=pd.merge(new,geo,on='street')
# merged.columns