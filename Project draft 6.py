### Preparing the master datasheet

# importing the library
import pandas as pd
import us
pd.set_option('display.max_columns',None)

# reading all the processed dataframes
Household_travel_tendency=pd.read_csv("C:\\Users\ishma\Desktop\Courseworks\msisprogramming\Project "
                                      "work\Household_travel_tendency.csv")
print(Household_travel_tendency)
print("=====")
Cost_of_EV_vs_NonEV=pd.read_csv("C:\\Users\ishma\Desktop\Courseworks\msisprogramming\Project "
                                      "work\Cost_of_EV_vs_NonEV.csv")
print(Cost_of_EV_vs_NonEV)
print("=====")
Household_income=pd.read_csv("C:\\Users\ishma\Desktop\Courseworks\msisprogramming\Project "
                                      "work\Household_income.csv")
print(Household_income)
print("=====")
Households=pd.read_csv("C:\\Users\ishma\Desktop\Courseworks\msisprogramming\Project "
                                      "work\Households.csv")
print(Households)
print("=====")
Electric_vehicle_registration=pd.read_csv("C:\\Users\ishma\Desktop\Courseworks\msisprogramming\Project "
                                      "work\Electric_vehicle_registration.csv")
print(Electric_vehicle_registration)
print("=====")
Charging_station_distribution=pd.read_csv("C:\\Users\ishma\Desktop\Courseworks\msisprogramming\Project "
                                      "work\Charging_station_distribution.csv")
print(Charging_station_distribution)
print("=====")

# merging the datasets on state column to yield the master sheet
Electric_vehicle_statewise_parametric_attributes = pd.merge(Household_travel_tendency, Cost_of_EV_vs_NonEV, on='State', how='inner') \
    .merge(Household_income, on='State', how='inner') \
    .merge(Households, left_on='State', right_on='state', how='inner') \
    .merge(Electric_vehicle_registration, on='State', how='inner') \
    .merge(Charging_station_distribution, on='State', how='inner') \
    .drop('state',axis=1)
print(Electric_vehicle_statewise_parametric_attributes)

# Saving this master sheet as a new CSV
Electric_vehicle_statewise_parametric_attributes.to_csv("C:\\Users\ishma\Desktop\Courseworks\msis"
                                                        "programming\Project work\Electric_vehicle_statewise_"
                                                        "parametric_attributes.csv",index=False)
