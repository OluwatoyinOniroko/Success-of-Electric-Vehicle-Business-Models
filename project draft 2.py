### Preparing the dataset regarding the household
## Data download site: https://worldpopulationreview.com/state-rankings/households-by-state
## Variables need to be addressed: 1. Number of households per state

# importing the library
import pandas as pd
import us
pd.set_option('display.max_columns',None)
# reading the datafile.xlsx
Household1=pd.read_csv("C:\\Users\HP\OneDrive\Desktop\Ty  - Fall 2023\Programming\Project proposal\Project presentation document\\households-by-state-2023.csv")
print(Household1.head())
# abbreviating the state code
def abbreviate_state(row):
    state_name = row["state"]
    try:
        return us.states.lookup(state_name).abbr
    except AttributeError:
        return state_name
State_code_mapping={"District of Columbia":'DC'}
Household1['state'] = Household1['state'].replace(State_code_mapping)
Household1["state"]= Household1.apply(abbreviate_state, axis=1)
print(Household1)
# omitting unnecessary columns and rows
Household1 = Household1.drop([51], axis=0)
Columns_to_drop= [0,2,3,4,5,6,7,8,9,10]
Household1 = Household1.drop(Household1.columns[Columns_to_drop],axis=1)
print(Household1)
#converting the "TotalHouseholds values into integer
Household1['TotalHouseholds']=Household1['TotalHouseholds'].astype(int)
print(Household1)
# Saving this dataset as a new CSV
Household1.to_csv("C:\\Users\HP\OneDrive\Desktop\Ty  - Fall 2023\Programming\Project proposal\Project presentation document\Households.csv",index=False)