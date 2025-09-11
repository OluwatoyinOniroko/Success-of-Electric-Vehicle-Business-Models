import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant

# Loading the dataset
df = pd.read_csv(
    "C:\\Users\ishma\Desktop\Courseworks\msisprogramming\Project work\Electric_vehicle_statewise_parametric_attributes_2.csv")
print(df.head())

# Select only the columns used as independent variables
independent_cols = ['Average Mileage', 'Average trip counts', 'Average Mileage per trips',
                    'Total Cost without purchase price of EV',
                    'Total Cost with purchase price of EV', 'Taxes', 'Fuel', 'Insurance',
                    'Non EV vs EV difference in Total cost without purchase price',
                    'Non EV vs EV difference in Total cost with purchase price', 'Non EV vs EV difference in Taxes',
                    'Non EV vs EV difference in Fuel', 'Non EV vs EV difference in Insurance', 'Median Income',
                    'Total Count',
                    'Percentage', 'EV Level1 EVSE Percentage', 'EV Level2 EVSE Percentage',
                    'EV DC Fast Count Percentage']
X = df[independent_cols]

# Iteratively drop features with the highest VIF until reaching 10 least VIF features
while len(independent_cols) > 10:
    # Add a constant to the independent variables matrix (required for VIF calculation)
    X_with_const = add_constant(X)

    # Calculate VIF for each variable, excluding 'const'
    vif_data = pd.DataFrame()
    vif_data["Features"] = X_with_const.columns
    vif_data["VIF"] = [variance_inflation_factor(X_with_const.values, i) for i in range(X_with_const.shape[1])]

    # Remove 'const' from the list of features
    vif_data = vif_data[vif_data["Features"] != "const"]

    # Get the feature with the highest VIF value
    max_vif_feature = vif_data.loc[vif_data['VIF'].idxmax()]['Features']

    # Drop the feature with the highest VIF value
    X = X.drop(columns=max_vif_feature)
    independent_cols.remove(max_vif_feature)
    print(f"Dropped: {max_vif_feature}")

# Print the 10 least VIF features
print(f"\nRemaining Features with 10 Least VIF Values:")
print(vif_data.nsmallest(10, 'VIF'))

