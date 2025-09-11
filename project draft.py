### Preparing the dataset regarding the Charging Station Distribution
## Data download site: https://www.kaggle.com/datasets/prasertk/electric-vehicle-charging-stations-in-usa
## Variables need to be addressed: 1. Total count of charging stations per state, 2. Count of EV level 1 charging
## stations, 3. Count of EV level 2 charging stations, 4. Count of EV DC charging stations, 5.Percentage of EV charging
## station distribution accorss the U.S., 6. Percentage of EV level 1 charging
## stations statewise, 7. Percentage of EV level 2 charging stations statewise, 8. Percentage of EV DC charging
## stations Statewise.

# importing the library
import pandas as pd
pd.set_option('display.max_columns',None)
# reading the datafile.csv
Charging_station_distribution=pd.read_csv("C:\\Users\HP\OneDrive\Desktop\Ty  - Fall 2023\Programming\Project proposal\Project presentation document\\ev_stations_v1.csv",dtype={6:str,20:str})
print(Charging_station_distribution.head())
# after analyzing the dataset we approached slicing the datafile based on columns: "State","EV Level1 EVSE Num",
# "EV Level2 EVSE Num", "EV DC Fast Count", "Access Code"
Charging_station_distribution2= Charging_station_distribution [["State","EV Level1 EVSE Num", "EV Level2 EVSE Num",
                                                                "EV DC Fast Count"]]
print(Charging_station_distribution2.head(10))
# From the yielded dataset imputing the missing values with 0 and converting all the decimal to integer type
Charging_station_distribution2['EV Level1 EVSE Num'] = (Charging_station_distribution2['EV Level1 EVSE Num'].fillna(0).
                                                        astype(int))
Charging_station_distribution2['EV Level2 EVSE Num'] = (Charging_station_distribution2['EV Level2 EVSE Num'].fillna(0).
                                                        astype(int))
Charging_station_distribution2['EV DC Fast Count'] = (Charging_station_distribution2['EV DC Fast Count'].fillna(0).
                                                      astype(int))
print(Charging_station_distribution2.head(10))
# replacing the non zero values in the above mentioned columns with 1 with identify them as facility providing the
# specific charging advantage
Charging_station_distribution2.loc[Charging_station_distribution2['EV Level1 EVSE Num'] != 0, 'EV Level1 EVSE Num'] = 1
Charging_station_distribution2.loc[Charging_station_distribution2['EV Level2 EVSE Num'] != 0, 'EV Level2 EVSE Num'] = 1
Charging_station_distribution2.loc[Charging_station_distribution2['EV DC Fast Count'] != 0, 'EV DC Fast Count'] = 1
print(Charging_station_distribution2.head(10))
# Grouping by 'State' and 'Access Code' while aggregating counts of each coulmn "EV Level1 EVSE Num",
# "EV Level2 EVSE Num","EV DC Fast Count"; ON and PR state code has been omitted as "PR" (Puerto Rico) is not a
# U.S. state; it is a U.S. territory. "ON" refers to a Canadian province and is not part of the United States.
filtered_data = Charging_station_distribution2[~Charging_station_distribution2['State'].isin(['ON', 'PR'])]
Charging_station_distribution3 = filtered_data.groupby(['State']).agg({
    'EV Level1 EVSE Num': lambda x: (x == 1).sum(),
    'EV Level2 EVSE Num': lambda x: (x == 1).sum(),
    'EV DC Fast Count': lambda x: (x == 1).sum()
})
print(Charging_station_distribution3)
# Now based on the number of 'EV Level1 EVSE Num','EV Level2 EVSE Num', and 'EV DC Fast Count'; 'Total Count',
# 'Percentage', 'EV Level1 EVSE Percentage', 'EV Level2 EVSE Percentage', 'EV DC Fast Count Percentage' were measured.
# Here to mention that "Percentage" considers the U.S. distribution of charging stations, while
# 'EV Level1 EVSE Percentage', 'EV Level2 EVSE Percentage', and 'EV DC Fast Count Percentage' considers statewise
# distribution
Charging_station_distribution3["Total Count"]= Charging_station_distribution3.sum(axis=1)
Charging_station_distribution3['Percentage'] = (Charging_station_distribution3['Total Count'] /
                                                Charging_station_distribution3['Total Count'].sum()) * 100
Charging_station_distribution3['EV Level1 EVSE Percentage'] = (Charging_station_distribution3['EV Level1 EVSE Num'] /
                                                               Charging_station_distribution3['Total Count']) * 100
Charging_station_distribution3['EV Level2 EVSE Percentage'] = (Charging_station_distribution3['EV Level2 EVSE Num'] /
                                                               Charging_station_distribution3['Total Count']) * 100
Charging_station_distribution3['EV DC Fast Count Percentage'] = (Charging_station_distribution3['EV DC Fast Count'] /
                                                               Charging_station_distribution3['Total Count']) * 100
Charging_station_distribution_final= Charging_station_distribution3[['EV Level1 EVSE Num','EV Level2 EVSE Num','EV DC Fast Count','Total Count',
                                      'Percentage', 'EV Level1 EVSE Percentage', 'EV Level2 EVSE Percentage',
                                      'EV DC Fast Count Percentage' ]]
print(Charging_station_distribution_final)
# Saving this dataset as a new CSV
Charging_station_distribution_final.to_csv("C:\\Users\ishma\Desktop\Courseworks\msisprogramming\Project work\Charging_station_distribution.csv",index=True)
