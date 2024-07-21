import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

data= pd.read_csv("ipl_2022.csv")
data.head()

figure = px.bar(data, x=data['match_winner'],
               title= 'Number Of Matches Won In IPL 2022')
figure.show()

data["won_by"]= data["won_by"].map({"Wickets":"Chasing",
                                   "Runs": "Defending"})
won_by= data["won_by"].value_counts()
label= won_by.index
counts= won_by.values
colors= ['gold','lightgreen']

fig= go.Figure(data= [go.Pie(labels= label, values= counts)])
fig.update_layout(title_text= 'Number of matches won by defending or chasing')
fig.update_traces(hoverinfo= 'label + percent', textinfo= 'value',
                 textfont_size= 30,
                 marker= dict(colors= colors,
                             line=dict(color= 'black', width= 3)))
fig.show()

toss=data['toss_decision'].value_counts()
label=toss.index
counts=toss.values
print(toss)
print(label)
print(counts)

toss= data["toss_decision"].value_counts()
label= toss.index
counts= toss.values
colors= ['blue', 'yellow']

fig= go.Figure(data= [go.Pie(labels= label, values= counts)])
fig.update_layout(title_text= 'Toss Decision')
fig.update_traces(hoverinfo= 'label + percent', textinfo= 'value',
                 textfont_size= 30,
                 marker= dict(colors= colors,
                             line=dict(color= 'black', width= 2)))
fig.show()

figure= px.bar(data, x=data['top_scorer'],
              title= 'Top Scores in IPL 2022')
figure.show()

figure= px.bar(data, x=data['top_scorer'],
               y= data['highscore'],
               color= data['highscore'],
              title= 'Top Scores in IPL 2022')
figure.show()

figure= px.bar(data, x=data['player_of_the_match'],
              title= 'Most Player Of The Match Awards')
figure.show()

figure= px.bar(data, x=data['best_bowling'],
              title= 'Best Bowler in IPL 2022')
figure.show()

fig = go.Figure()
fig.add_trace(go.Bar(
    x=data["venue"],
    y=data["first_ings_wkts"],
    name='First Inning Wickets',
    marker_color='red'
))
fig.add_trace(go.Bar(
    x=data["venue"],
    y=data["second_ings_wkts"],
    name= 'Second Inning Wickets',
    marker_color='green'
))
fig.update_layout(barmode='group', xaxis_tickangle=-45)
fig.show()

