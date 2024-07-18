import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

data1= pd.read_csv("transformed_data.csv")
data2= pd.read_csv("raw_data.csv")
print(data1)

data1.head()

data2.head()

data1["COUNTRY"].value_counts()

data1['COUNTRY'].value_counts().mode()

code = data1['CODE'].unique().tolist()
country= data1['COUNTRY'].unique().tolist()
hdi = []
tc = []
td = []
sti = []
population = data1['POP'].unique().tolist()
gdp= []

for i in country:
    hdi.append((data1.loc[data1['COUNTRY']== i, 'HDI']).sum()/294)
    tc.append((data2.loc[data2['location']== i, 'total_cases']).sum())
    td.append((data2.loc[data2['location']== i, 'total_deaths']).sum())
    sti.append((data1.loc[data1['COUNTRY']== i, 'STI']).sum()/294)
    population.append((data2.loc[data2['location']== i, 'population']).sum())

aggregated_data = pd.DataFrame(list(zip(code,country,hdi,tc,td,sti,population)),
                               columns= ['Country Code', 'Country', 'HDI',
                                        'Total Cases', 'Total Deaths', 'Strigency Index', 'Population'])
print(aggregated_data.head())

data= aggregated_data.sort_values(by=['Total Cases'], ascending= False)
data.head()

data = data.head(10)
print(data)

data['GDP Before Covid'] = [6529.53,8897.49,2100.75,1149.65,7027.61,9946.03,
                            29564.74,6001.40,6424.98,42354.41]

data['GDP During Covid']= [63543.58,6796.84,1900.71,10126.72,6126.87,8346.70,
                           27057.16,5090.72,5332.77,40284.64]

print(data)

figure= px.bar(data, y='Total Cases', x='Country',
              title= 'Countries with Highest Covid Cases')
figure.show()

figure= px.bar(data, y='Total Deaths', x='Country',
              title= 'Countries with Highest Deaths')
figure.show()

fig = go.Figure()
fig.add_trace(go.Bar(
    x=data["Country"],
    y=data["Total Cases"],
    name='Total Cases',
    marker_color='indianred'
))
fig.add_trace(go.Bar(
    x=data["Country"],
    y=data["Total Deaths"],
    name='Total Deaths',
    marker_color='blue'
))
fig.update_layout(barmode='group', xaxis_tickangle=-45)
fig.show()

cases= data['Total Cases'].sum()
decreased= data['Total Deaths'].sum()

labels= ['Total Cases', 'Total Deaths']
values= [cases,decreased]

fig= px.pie(data, values=values, names=labels,
           title= 'Percentage of Total Cases and Deaths', hole=0.5)
fig.show()

death_rate= (data["Total Deaths"].sum()/data["Total Cases"].sum()*100)
print("Death Rate= ",death_rate)

fig= px.bar(data, x='Country', y= 'Total Cases',
           hover_data= ['Population', 'Total Deaths'],
           color= 'Strigency Index',height= 400,
           title= 'Strigency Index during Covid-19')
fig.show()

fig= px.bar(data, x='Country', y= 'Total Cases',
           hover_data= ['Population', 'Total Deaths'],
           color= 'GDP Before Covid',height= 400,
           title= 'GDP Per Capita Before Covid-19')
fig.show()

fig= px.bar(data, x='Country', y= 'Total Cases',
           hover_data= ['Population', 'Total Deaths'],
           color= 'GDP During Covid',height= 400,
           title= 'GDP Per Capita During Covid-19')
fig.show()

fig= go.Figure()
fig.add_trace(go.Bar(
    x= data['Country'],
    y= data['GDP Before Covid'],
    name= 'GDP Per Capita Before Covid-19',
    marker_color= 'indianred'
))
fig.add_trace(go.Bar(
    x= data['Country'],
    y= data['GDP During Covid'],
    name= 'GDP Per Capita During Covid-19',
    marker_color= 'lightsalmon'
))
fig.update_layout(barmode= 'group', xaxis_tickangle= -45)
fig.show()

fig= px.bar(data, x='Country', y= 'Total Cases',
           hover_data= ['Population', 'Total Deaths'],
           color= 'HDI',height= 400,
           title= 'Human Development Index During Covid-19')
fig.show()



