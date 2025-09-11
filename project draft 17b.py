import plotly.express as px
import pandas as pd

# Load your dataset here (replace 'your_dataset.csv' with your dataset file)
# For this example, using Plotly's built-in dataset
df = pd.read_csv("C:\\Users\HP\OneDrive\Desktop\Ty  - Fall 2023\Programming\Project proposal\Project presentation document\df43.csv")

# Define the variables
dependent_variable_1= 'Count of EV registration (2022)'
dependent_variable_2= 'Growth_percentage'
dependent_variable_3= 'Probability of having EVs per household'
independent_variables = ['Average trip counts', 'Average Mileage per trips',
                         'Taxes', 'Fuel',
                         'Non EV vs EV difference in Total cost without purchase price',
                         'Non EV vs EV difference in Fuel', 'Non EV vs EV difference in Insurance',
                         'Median Income', 'Percentage', 'EV DC Fast Count Percentage']

# Calculate the correlation matrix
correlation_matrix_1 = df[[dependent_variable_1] + independent_variables].corr()
correlation_matrix_2 = df[[dependent_variable_2] + independent_variables].corr()
correlation_matrix_3 = df[[dependent_variable_3] + independent_variables].corr()
# Create the heatmap
fig_1 = px.imshow(correlation_matrix_1,
                labels=dict(color='Correlation'),
                x=correlation_matrix_1.columns,
                y=correlation_matrix_1.columns,
                title=f'Correlation Heatmap between {dependent_variable_1} and Independent Variables')

fig_2 = px.imshow(correlation_matrix_2,
                labels=dict(color='Correlation'),
                x=correlation_matrix_2.columns,
                y=correlation_matrix_2.columns,
                title=f'Correlation Heatmap between {dependent_variable_2} and Independent Variables')

fig_3 = px.imshow(correlation_matrix_3,
                labels=dict(color='Correlation'),
                x=correlation_matrix_3.columns,
                y=correlation_matrix_3.columns,
                title=f'Correlation Heatmap between {dependent_variable_3} and Independent Variables')

# Show the heatmap
fig_1.show()
fig_2.show()
fig_3.show()