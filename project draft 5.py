### Preparing the dataset regarding the Household travel tendency
## Data acquired site from and interactive website: https://www.bts.gov/statistical-products/surveys/
## vehicle-miles-traveled-and-vehicle-trips-state
## Variables need to be addressed: 1. Average Mileage 2. Average trip counts 3.Average Mleage per trips

# importing the library
import pandas as pd
import us
pd.set_option('display.max_columns',None)
# reading the datafile.xlsx regarding the EV cost
Household_travel_tendency1=pd.read_excel("C:\\Users\ishma\Desktop\Courseworks\msisprogramming\Project work\datasets\\nhts2009transferabilityvtvmtbystate(1).xlsx")
print(Household_travel_tendency1)
# omitting unnecessary columns and rows
Household_travel_tendency1 = Household_travel_tendency1.drop([0,1,2,3,55], axis=0)
print(Household_travel_tendency1)
Household_travel_tendency1.rename(columns={"Vehicle miles traveled and vehicle trips by State":"State",
                                           "Unnamed: 1":"Mean urban mileage", "Unnamed: 2":"Mean suburban mileage",
                                           "Unnamed: 3":"Mean rural mileage", "Unnamed: 4":"Mean urban trips",
                                           "Unnamed: 5":"Mean suburban trips", "Unnamed: 6":"Mean rural trips"},
                                  inplace=True)
print(Household_travel_tendency1)
#averaging the mileage and trip counts
Household_travel_tendency1['Average Mileage'] = (Household_travel_tendency1[['Mean urban mileage',
                                                                            'Mean suburban mileage', 'Mean rural mileage']].
                                                 mean(axis=1))
Household_travel_tendency1['Average trip counts'] = (Household_travel_tendency1[['Mean urban trips',
                                                                            'Mean suburban trips', 'Mean rural trips']].
                                                 mean(axis=1))
Household_travel_tendency1['Average Mileage per trips'] = (Household_travel_tendency1['Average Mileage']/
                                                           Household_travel_tendency1['Average trip counts'])

print(Household_travel_tendency1)
# dropping unnecessary columns
Cols_to_drop= ["Mean urban mileage", "Mean suburban mileage", "Mean rural mileage", "Mean urban trips",
               "Mean suburban trips", "Mean rural trips"]
Household_travel_tendency1 = Household_travel_tendency1.drop(Cols_to_drop, axis=1)
print(Household_travel_tendency1)
print("=======")
# abbreviating the state names
def abbreviate_state(row):
    state_name = row["State"]
    try:
        return us.states.lookup(state_name).abbr
    except AttributeError:
        return state_name
State_code_mapping={"District Of Columbia":'DC'}
Household_travel_tendency1['State'] = Household_travel_tendency1['State'].replace(State_code_mapping)
Household_travel_tendency1["State"]= Household_travel_tendency1.apply(abbreviate_state, axis=1)
print(Household_travel_tendency1)

# Saving this dataset as a new CSV
Household_travel_tendency1.to_csv("C:\\Users\ishma\Desktop\Courseworks\msisprogramming\Project work\Household_travel_tendency.csv",index=False)