### Preparing the dataset regarding the Total costs of ownership
## Data acquired site from and interactive website: https://www.self.inc/info/electric-cars-vs-gas-cars-cost/#maintenance-cost
## Variables need to be addressed: 1. EV Total cost without purchase price, 2. EV Total cost with purchase price,
## 3. EV associated Taxes, 4. EV associated Fuel cost, 5.EV associated insurance cost
## 6. Non-EV Total cost without purchase price, 7. Non-EV Total cost with purchase price,
## 8. Non-EV associated Taxes, 9. Non-EV associated Fuel cost, 10.Non-EV associated insurance cost,
# 11. Non EV vs EV difference in Total cost without purchase price, 12.Non EV vs EV difference
# in Total cost with purchase price 13. Non EV vs EV difference in Taxes 14. Non EV vs EV difference in Fuel
# 15. Non EV vs EV difference in Insurance

# importing the library
import pandas as pd
import us
pd.set_option('display.max_columns',None)
# reading the datafile.xlsx regarding the EV cost
Total_cost_of_ownership_EV1=pd.read_excel("C:\\Users\ishma\Desktop\Courseworks\msisprogramming\Project work\datasets\Total cost of ownership for msis proposal.xlsx", sheet_name="EV")
print(Total_cost_of_ownership_EV1)
# after analyzing the dataset modifying the dataset by mergeing and dropiing unnecessary rows and columns
df1= Total_cost_of_ownership_EV1.iloc[0:50, 0:2]
print(df1)
df2= Total_cost_of_ownership_EV1.iloc[0:50, 2:4]
print(df2)
df3= Total_cost_of_ownership_EV1.iloc[0:50, 4:6]
print(df3)
df4= Total_cost_of_ownership_EV1.iloc[0:50, 6:8]
print(df4)
df5= Total_cost_of_ownership_EV1.iloc[0:50, 8:10]
print(df5)
merged_df1 = pd.merge(df1, df2, left_on='State', right_on='State.1', how='inner')
print(merged_df1)
merged_df2= pd.merge(merged_df1, df3, left_on='State', right_on='State.2', how='inner')
print(merged_df2)
merged_df3= pd.merge(merged_df2, df4, left_on='State', right_on='State.3', how='inner')
print(merged_df3)
merged_df4= pd.merge(merged_df3, df5, left_on='State', right_on='State.4', how='inner')
print(merged_df4)
cols_to_drop=["State.1","State.2","State.3","State.4"]
merged_df_EV=merged_df4.drop(columns=cols_to_drop,axis=1)
print(merged_df_EV)

# reading the datafile.xlsx regarding the EV cost
Total_cost_of_ownership_Non_EV1=pd.read_excel("C:\\Users\ishma\Desktop\Courseworks\msisprogramming\Project work\datasets\Total cost of ownership for msis proposal.xlsx", sheet_name="Non EV")
print(Total_cost_of_ownership_Non_EV1)
# after analyzing the dataset modifying the dataset by mergeing and dropiing unnecessary rows and columns
df11= Total_cost_of_ownership_Non_EV1.iloc[0:50, 0:2]
print(df11)
df21= Total_cost_of_ownership_Non_EV1.iloc[0:50, 2:4]
print(df21)
df31= Total_cost_of_ownership_Non_EV1.iloc[0:50, 4:6]
print(df31)
df41= Total_cost_of_ownership_Non_EV1.iloc[0:50, 6:8]
print(df41)
df51= Total_cost_of_ownership_Non_EV1.iloc[0:50, 8:10]
print(df51)
merged_df11 = pd.merge(df11, df21, left_on='State', right_on='State.1', how='inner')
print(merged_df11)
merged_df21= pd.merge(merged_df11, df31, left_on='State', right_on='State.2', how='inner')
print(merged_df21)
merged_df31= pd.merge(merged_df21, df41, left_on='State', right_on='State.3', how='inner')
print(merged_df31)
merged_df41= pd.merge(merged_df31, df51, left_on='State', right_on='State.4', how='inner')
print(merged_df41)
cols_to_drop=["State.1","State.2","State.3","State.4"]
merged_df_Non_EV=merged_df41.drop(columns=cols_to_drop,axis=1)
print(merged_df_Non_EV)
# merging the EV and non_EV datasets
merged= pd.merge(merged_df_EV, merged_df_Non_EV, on="State")
print(merged)
# yielding different prameters having the diffrence of corresponding values between EV and Non_EVs
merged["Non EV vs EV difference in Total cost without purchase price"]= (merged["Total cost of Non EV "
                                                                                "without purchase price"]-
                                                                         merged ["Total Cost without purchase "
                                                                                 "price of EV"])
merged["Non EV vs EV difference in Total cost with purchase price"]= (merged["Total cost of Non EV "
                                                                                "with purchase price"]-
                                                                         merged ["Total Cost with purchase "
                                                                                 "price of EV"])
merged["Non EV vs EV difference in Taxes"]= (merged["Non-EV Taxes"]- merged ["Taxes"])
merged["Non EV vs EV difference in Fuel"]= (merged["Non-EV Fuel"]- merged["Fuel"])
merged["Non EV vs EV difference in Insurance"]= (merged["Non_EV Insurance"]-merged ["Insurance"])
print("====")
print(merged)
# abbreviating the state code
def abbreviate_state(row):
    state_name = row["State"]
    try:
        return us.states.lookup(state_name).abbr
    except AttributeError:
        return state_name
State_code_mapping={"District of Columbia":'DC'}
merged['State'] = merged['State'].replace(State_code_mapping)
merged["State"]= merged.apply(abbreviate_state, axis=1)
print(merged)
# Saving this dataset as a new CSV
merged.to_csv("C:\\Users\ishma\Desktop\Courseworks\msisprogramming\Project work\Cost_of_EV_vs_NonEV.csv",index=False)
