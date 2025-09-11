### Preparing the dataset regarding the Household income
## Data download site: https://www.statista.com/statistics/233170/median-household-income-in-the-united-states-by-state/
## Variables need to be addressed: 1. Median Household income

# importing the library
import pandas as pd
import us
pd.set_option('display.max_columns',None)
# reading the datafile.xlsx
Household_income1=pd.read_excel("C:\\Users\HP\OneDrive\Desktop\Ty  - Fall 2023\Programming\Project proposal\Project presentation document\\statistic_id233170_us-median-household-income-2022-by-state(1).xlsx", sheet_name="Data")
print(Household_income1)
# omitting unnecessary columns and rows
Household_income1 = Household_income1.drop([0,1,2,3], axis=0)
Columns_to_drop= [0]
Household_income1 = Household_income1.drop(Household_income1.columns[Columns_to_drop],axis=1)
print(Household_income1)
Household_income1.reset_index(drop=True, inplace=True)
print(Household_income1)
Household_income1.rename(columns={'Unnamed: 1': 'State', 'Unnamed: 2': 'Median Income'}, inplace=True)
print(Household_income1)
# abbreviating the state code
def abbreviate_state(row):
    state_name = row["State"]
    try:
        return us.states.lookup(state_name).abbr
    except AttributeError:
        return state_name
State_code_mapping={"District of Columbia":'DC'}
Household_income1['State'] = Household_income1['State'].replace(State_code_mapping)
Household_income1["State"]= Household_income1.apply(abbreviate_state, axis=1)
print(Household_income1)

# omitting unnecessary rows
Household_income1 = Household_income1.drop([24], axis=0)
print(Household_income1)

# Saving this dataset as a new CSV
Household_income1.to_csv("C:\\Users\HP\OneDrive\Desktop\Ty  - Fall 2023\Programming\Project proposal\Project presentation document\Household_income.csv",index=False)