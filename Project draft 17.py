import plotly.express as px
import pandas as pd

# Load your dataset here (replace 'your_dataset.csv' with your dataset file)
# For this example, using Plotly's built-in dataset
df = pd.read_csv("C:\\Users\HP\OneDrive\Desktop\Ty  - Fall 2023\Programming\Project proposal\Project presentation document\df43.csv")

# Define your dependent variable and independent variables
dependent_variable_1 = 'Count of EV registration (2022)'
dependent_variable_2 = 'Growth_percentage'
dependent_variable_3= 'Probability of having EVs per household'
independent_variables = ['Average trip counts', 'Average Mileage per trips',
                    'Taxes', 'Fuel',
                    'Non EV vs EV difference in Total cost without purchase price',
                    'Non EV vs EV difference in Fuel', 'Non EV vs EV difference in Insurance',
                    'Median Income', 'Percentage', 'EV DC Fast Count Percentage']  # Add more independent variables

# Create a heatmap based on US states
fig_1 = px.choropleth(df,  # Pass the DataFrame directly
                    locations='State',  # Assuming 'State' contains state codes or names
                    locationmode='USA-states',
                    color=dependent_variable_1,
                    scope='usa',
                    labels={'color': dependent_variable_1},
                    title=f'Heatmap of {dependent_variable_1} across US States',
                    color_continuous_scale='Viridis')  # Change the color scale if needed

fig_2 = px.choropleth(df,  # Pass the DataFrame directly
                    locations='State',  # Assuming 'State' contains state codes or names
                    locationmode='USA-states',
                    color=dependent_variable_2,
                    scope='usa',
                    labels={'color': dependent_variable_2},
                    title=f'Heatmap of {dependent_variable_2} across US States',
                    color_continuous_scale='Viridis')  # Change the color scale if needed

fig_3= px.choropleth(df,  # Pass the DataFrame directly
                    locations='State',  # Assuming 'State' contains state codes or names
                    locationmode='USA-states',
                    color=dependent_variable_3,
                    scope='usa',
                    labels={'color': dependent_variable_3},
                    title=f'Heatmap of {dependent_variable_3} across US States',
                    color_continuous_scale='Viridis')  # Change the color scale if needed

# Show the heatmap
fig_1.show()
fig_2.show()
fig_3.show()