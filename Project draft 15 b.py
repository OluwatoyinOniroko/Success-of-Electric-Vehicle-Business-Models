import pandas as pd
import statsmodels.api as sm

df4 = pd.read_csv("C:\\Users\ishma\Desktop\Courseworks\msisprogramming\Project work\df43.csv")
print(df4.head())

selected_columns = ['Average trip counts', 'Average Mileage per trips',
                    'Taxes', 'Fuel',
                    'Non EV vs EV difference in Total cost without purchase price',
                    'Non EV vs EV difference in Fuel', 'Non EV vs EV difference in Insurance',
                    'Median Income', 'Percentage', 'EV DC Fast Count Percentage']

# Create X using only the selected columns and define y as the target variable
X = df4[selected_columns]
y = df4['Count of EV registration (2022)']
y1 = df4['Growth_percentage']
y2 = df4['Probability of having EVs per household']

# Define a function for backward elimination
def backward_elimination(X, y):
    cols = list(X.columns)
    pmax = 1
    while pmax > 0.05:  # Set significance level
        p_values = []
        X_ols = sm.add_constant(X)
        model = sm.OLS(y, X_ols).fit()
        p_values = pd.Series(model.pvalues.values[1:], index=cols)  # Exclude the constant
        pmax = max(p_values)
        if pmax > 0.05:
            exclude = p_values.idxmax()
            X = X.drop(exclude, axis=1)
            cols.remove(exclude)
    print(model.summary())
    return X

# Apply backward elimination for each target variable
print("===== Count of EV registration (2022) =====")
X_updated_1 = backward_elimination(X, y)

print("\n===== Growth_percentage =====")
X_updated_2 = backward_elimination(X, y1)

print("\n===== Probability of having EVs per household =====")
X_updated_3 = backward_elimination(X, y2)
