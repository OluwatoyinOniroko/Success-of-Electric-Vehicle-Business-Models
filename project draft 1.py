### Preparing the dataset regarding the Electronic vehicle registration
## Data download site: https://afdc.energy.gov/data/10962 and
## https://electrek.co/2022/08/24/current-ev-registrations-in-the-us-how-does-your-state-stack-up/
## Variables need to be addressed: 1. vehicle registration count 2021 statewise 2. vehicle registration count 2022
## statewise 3. Percent of total EV 2022 accross U.S., 4. statewise growth of EVs

# importing the library
import pandas as pd
import us
pd.set_option('display.max_columns',None)
# reading the datafile.xlsx
Electric_vehicle_registration1 = pd.read_excel("C:\\Users\HP\OneDrive\Desktop\Ty  - Fall 2023\Programming\Project proposal\Project presentation document\EV registration 2020 and 2021.xlsx")

print(Electric_vehicle_registration1.head())
# abbreviate the state code and aggregating based on the state code name to yield similar dataset as Charging_
# station_distribution_final
def abbreviate_state(row):
    state_name = row["State"]
    try:
        return us.states.lookup(state_name).abbr
    except AttributeError:
        return state_name
State_code_mapping={"Columbia":'DC'}
Electric_vehicle_registration1['State'] = Electric_vehicle_registration1['State'].replace(State_code_mapping)
Electric_vehicle_registration1["State"]= Electric_vehicle_registration1.apply(abbreviate_state, axis=1)
print(Electric_vehicle_registration1)
Electric_vehicle_registration2= (Electric_vehicle_registration1.groupby("State").
                                 agg({'Count of EV registrations (2021)': 'sum'}))
print(Electric_vehicle_registration2)
# removing the extra row having "TOTAL" values
Electric_vehicle_registration2= Electric_vehicle_registration2.drop('TOTAL', axis=0)
print(Electric_vehicle_registration2)

# reading the 2022 datafile.xlsx
Electric_vehicle_registration3=pd.read_excel("C:\\Users\HP\OneDrive\Desktop\Ty  - Fall 2023\Programming\Project proposal\Project presentation document\\10962-ev-registration-counts-by-state_8-2-23 (1).xlsx")
print(Electric_vehicle_registration3.head())

# omitting unnecessary columns and rows
Electric_vehicle_registration3 = Electric_vehicle_registration3.drop([0, 53], axis=0)
Columns_to_drop= [0,3,4]
Electric_vehicle_registration3 = Electric_vehicle_registration3.drop(Electric_vehicle_registration3.columns[Columns_to_drop],axis=1)
print(Electric_vehicle_registration3)

Electric_vehicle_registration3.columns = Electric_vehicle_registration3.iloc[0]

# Rename the second column
Electric_vehicle_registration3 = Electric_vehicle_registration3.rename(columns={'Unnamed: 2': 'Count of EV registration (2022)'})

# Drop the first row since it's now the column names
Electric_vehicle_registration3 = Electric_vehicle_registration3.drop(Electric_vehicle_registration3.index[0])
print("====")
print(Electric_vehicle_registration3)
State_code_mapping={"District of Columbia":'DC'}
Electric_vehicle_registration3['State'] = Electric_vehicle_registration3['State'].replace(State_code_mapping)
Electric_vehicle_registration3["State"]= Electric_vehicle_registration3.apply(abbreviate_state, axis=1)
print("===")
# Renaming the second column
Electric_vehicle_registration3 = Electric_vehicle_registration3.rename(columns={'Registration Count': 'Count of EV registration (2022)'})
print(Electric_vehicle_registration3)
Electric_vehicle_registration3 = (Electric_vehicle_registration3.groupby("State").
                                 agg({'Count of EV registration (2022)': 'sum'}))

print("==========")

Electric_vehicle_registration4 = pd.merge(
    Electric_vehicle_registration2,
    Electric_vehicle_registration3,
    left_on='State',
    right_on='State',
    how='inner'  # Or other types of joins based on your needs
)
print(Electric_vehicle_registration4)

# Measuring the percentage variables
Electric_vehicle_registration4['EV Percentage (2022)'] = (Electric_vehicle_registration4
                                                          ['Count of EV registration (2022)'] /
                                                          Electric_vehicle_registration4
                                                          ['Count of EV registration (2022)'].sum()) * 100
Electric_vehicle_registration4['Growth_percentage'] = ((Electric_vehicle_registration4
                                                        ['Count of EV registration (2022)'] -
                                                        Electric_vehicle_registration4
                                                        ['Count of EV registrations (2021)']) /
                                                       Electric_vehicle_registration4
                                                       ['Count of EV registrations (2021)']) * 100

Electric_vehicle_registration_final= Electric_vehicle_registration4[['Count of EV registrations (2021)',
                                                                     'Count of EV registration (2022)',
                                                                     'EV Percentage (2022)','Growth_percentage' ]]
print(Electric_vehicle_registration_final)
# Saving this dataset as a new CSV
Electric_vehicle_registration_final.to_csv("C:\\Users\HP\OneDrive\Desktop\Ty  - Fall 2023\Programming\Project proposal\Project presentation document\Electric_vehicle_registration.csv",index=True)
