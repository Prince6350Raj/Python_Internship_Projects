import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

ev_data = pd.read_csv('electric_vehicle.csv')
print(ev_data.head())

ev_data.isnull().sum()

ev_data = ev_data.dropna()
ev_data.info()

sns.set_style("whitegrid")

plt.figure(figsize = (12,6))
ev_adoption_by_year = ev_data['Model Year'].value_counts().sort_index()
sns.barplot(x = ev_adoption_by_year.index, y = ev_adoption_by_year.values, palette = 'viridis')
plt.title('Ev Adoption Over Time')
plt.xlabel('Model Year')
plt.ylabel('Number of Vehicles Registered')
plt.xticks(rotation = 45)
plt.tight_layout()
plt.show()

ev_county_distribution = ev_data['County'].value_counts()
top_counties = ev_county_distribution.head(3).index
top_counties_data = ev_data[ev_data['County'].isin(top_counties)]

ev_city_distribution_top_counties = top_counties_data.groupby(['County', 'City']).size().sort_values(ascending = False).reset_index(name = 'Number of Vehicles')

top_cities = ev_city_distribution_top_counties.head(10)

plt.figure(figsize = (12,8))
sns.barplot(x = 'Number of Vehicles', y = 'City', hue = 'County', data = top_cities, palette = "magma")
plt.title('Top Cities in Top Counties by Ev Registration')
plt.xlabel('Number of Vehicles Registered')
plt.ylabel('City')
plt.legend(title = 'County')
plt.tight_layout()
plt.show()

#analyzing the distribution of electric vehicle types
ev_type_distribution = ev_data['Electric Vehicle Type'].value_counts()

plt.figure(figsize = (10, 6))
sns.barplot(x = ev_type_distribution.values, y = ev_type_distribution.index, palette = "rocket")
plt.title('Distribution of Electric Vehicle Types')
plt.xlabel('Number of Vehicles Registered')
plt.ylabel('Electric Vehicle Type')
plt.tight_layout()
plt.show()

ev_make_distribution = ev_data['Make'].value_counts().head(10) #limting to top 10 for clarity

plt.figure(figsize = (12, 6))
sns.barplot(x = ev_make_distribution.values, y = ev_make_distribution.index, palette = "cubehelix")
plt.title('Top 10 Popular EV Makes')
plt.xlabel('Number of Vehicles Registered')
plt.ylabel('Make')
plt.tight_layout()
plt.show()

# Select the top 3 manufacturers based on the number of vehicles registered
top_3_makes = ev_make_distribution.head(3).index

# Filtering the dataset for these top manufacturers
top_makes_data = ev_data[ev_data['Make'].isin(top_3_makes)]

# Analyzing the popularity of EV models within these top manufacturers
ev_model_distribution_top_makes = top_makes_data.groupby(['Make', 'Model']).size().sort_values(ascending=False).reset_index(name='Number of Vehicles')

# Visualizing the top 10 models across these manufacturers
top_models = ev_model_distribution_top_makes.head(10)

# Plotting
plt.figure(figsize=(12, 8))
sns.barplot(x='Number of Vehicles', y='Model', hue='Make', data=top_models, palette="viridis")
plt.title('Top Models in Top 3 Makes by EV Registrations')
plt.xlabel('Number of Vehicles Registered')
plt.ylabel('Model')
plt.legend(title='Make', loc = 'center right')
plt.tight_layout()
plt.show()

# Analyzing the distribution of electric range

plt.figure(figsize=(12, 6))
sns.histplot(ev_data['Electric Range'], bins= 30, kde= True, color= 'royalblue') #kde= kernel density estimate
plt.title('Distribution of Electric Vehicle Ranges')
plt.xlabel('Electric Range (miles)')
plt.ylabel("Number of Vehicles")
plt.axvline(ev_data["Electric Range"].mean(), color='red',linestyle='--',
           label= f'Mean Range : {ev_data["Electric Range"].mean():2f} miles')
plt.legend()
plt.show()

# calculating the average electric range by modrl year

average_range_by_year= ev_data.groupby('Model Year')['Electric Range'].mean().reset_index()

plt.figure(figsize=(12, 8))
sns.lineplot(x='Model Year', y='Electric Range', data= average_range_by_year, marker= 'o', color= 'green')
plt.title('Average Electric Range By Model Year')
plt.xlabel('Model Year')
plt.ylabel('Average Electric Range (miles)')
plt.grid(True)
plt.show()

