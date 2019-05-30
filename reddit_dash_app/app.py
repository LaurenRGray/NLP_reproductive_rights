# misc imports
import pickle
import pandas as pd
import numpy as np
# dash imports
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State


H_cv = pickle.load(open('H_cv_dataframe_dash.pkl', 'rb'))
print(H_cv.head())

x1_c = H_cv[(H_cv['topics'] == 'contraception') & (H_cv['subreddit'] == 'prochoice')]['compound']
x2_c = H_cv[(H_cv['topics'] == 'contraception') & (H_cv['subreddit'] == 'prolife')]['compound']

x1_s = H_cv[(H_cv['topics'] == 'start_of_life') & (H_cv['subreddit'] == 'prochoice')]['compound']
x2_s = H_cv[(H_cv['topics'] == 'start_of_life') & (H_cv['subreddit'] == 'prolife')]['compound']

x1_b = H_cv[(H_cv['topics'] == 'bodily_autonomy') & (H_cv['subreddit'] == 'prochoice')]['compound']
x2_b = H_cv[(H_cv['topics'] == 'bodily_autonomy') & (H_cv['subreddit'] == 'prolife')]['compound']

x1_o = H_cv[(H_cv['topics'] == 'other') & (H_cv['subreddit'] == 'prochoice')]['compound']
x2_o = H_cv[(H_cv['topics'] == 'other') & (H_cv['subreddit'] == 'prolife')]['compound']

## Dash figures

# Topic = contraception, prochoice vs. prolife sentiment subplots
contraception_sentiment = dcc.Graph(
    id='contraception_pc-v-pl_sentiment',
    figure={
        'data': [
            {
                'x': x1_c,
                'name': 'Prochoice',
                'type': 'histogram'
            },
            {
                'x': x2_c,
                'name': 'Prolife',
                'type': 'histogram'
            }
        ],
        'layout': { 
        	'title': 'Contraception & Sex Education',
        	'xaxis': dict(
		        title='Sentiment',
		        # titlefont=dict(
		        #     family='Arial, sans-serif',
		        #     size=18,
		        #     color='lightgrey'
		        # ),
		        showticklabels=True,
		        tickangle=0,
		        tickfont=dict(
		            family='Old Standard TT, serif',
		            size=14,
		            color='black'
		        ),
		        exponentformat='e',
		        showexponent='all'
	        ),
        	'yaxis': dict(
		        title='Topic Frequency',
		        # titlefont=dict(
		        #     family='Arial, sans-serif',
		        #     size=18,
		        #     color='lightgrey'
		        # ),
		        showticklabels=True,
		        tickangle=0,
		        tickfont=dict(
		            family='Old Standard TT, serif',
		            size=14,
		            color='black'
		        ),
		        exponentformat='e',
		        showexponent='all'
    		)
    	}
    }
)

start_of_life_sentiment = dcc.Graph(
    id='start-of-life_pc-v-pl_sentiment',
    figure={
        'data': [
            {
                'x': x1_s,
                'name': 'Prochoice',
                'type': 'histogram'
            },
            {
                'x': x2_s,
                'name': 'Prolife',
                'type': 'histogram'
            }
        ],
        'layout': { 
        	'title': 'When does life begin?',
        	'xaxis': dict(
		        title='Sentiment',
		        # titlefont=dict(
		        #     family='Arial, sans-serif',
		        #     size=18,
		        #     color='lightgrey'
		        # ),
		        showticklabels=True,
		        tickangle=0,
		        tickfont=dict(
		            family='Old Standard TT, serif',
		            size=14,
		            color='black'
		        ),
		        exponentformat='e',
		        showexponent='all'
	        ),
        	'yaxis': dict(
		        title='Topic Frequency',
		        # titlefont=dict(
		        #     family='Arial, sans-serif',
		        #     size=18,
		        #     color='lightgrey'
		        # ),
		        showticklabels=True,
		        tickangle=0,
		        tickfont=dict(
		            family='Old Standard TT, serif',
		            size=14,
		            color='black'
		        ),
		        exponentformat='e',
		        showexponent='all'
    		)
    	}
    }
)

bodily_autonomy_sentiment = dcc.Graph(
    id='bodily_autonomy_pc-v-pl_sentiment',
    figure={
        'data': [
            {
                'x': x1_b,
                'name': 'Prochoice',
                'type': 'histogram'
            },
            {
                'x': x2_b,
                'name': 'Prolife',
                'type': 'histogram'
            }
        ],
        'layout': { 
        	'title': 'Bodily Autonomy of the mother and fetus',
        	'xaxis': dict(
		        title='Sentiment',
		        # titlefont=dict(
		        #     family='Arial, sans-serif',
		        #     size=18,
		        #     color='lightgrey'
		        # ),
		        showticklabels=True,
		        tickangle=0,
		        tickfont=dict(
		            family='Old Standard TT, serif',
		            size=14,
		            color='black'
		        ),
		        exponentformat='e',
		        showexponent='all'
	        ),
        	'yaxis': dict(
		        title='Topic Frequency',
		        # titlefont=dict(
		        #     family='Arial, sans-serif',
		        #     size=18,
		        #     color='lightgrey'
		        # ),
		        showticklabels=True,
		        tickangle=0,
		        tickfont=dict(
		            family='Old Standard TT, serif',
		            size=14,
		            color='black'
		        ),
		        exponentformat='e',
		        showexponent='all'
    		)
    	}
    }
)

other_sentiment = dcc.Graph(
    id='other_pc-v-pl_sentiment',
    figure={
        'data': [
            {
                'x': x1_o,
                'name': 'Prochoice',
                'type': 'histogram'
            },
            {
                'x': x2_o,
                'name': 'Prolife',
                'type': 'histogram'
            }
        ],
        'layout': { 
        	'title': 'All remaining unclassified comments',
        	'xaxis': dict(
		        title='Sentiment',
		        # titlefont=dict(
		        #     family='Arial, sans-serif',
		        #     size=18,
		        #     color='lightgrey'
		        # ),
		        showticklabels=True,
		        tickangle=0,
		        tickfont=dict(
		            family='Old Standard TT, serif',
		            size=14,
		            color='black'
		        ),
		        exponentformat='e',
		        showexponent='all'
	        ),
        	'yaxis': dict(
		        title='Topic Frequency',
		        # titlefont=dict(
		        #     family='Arial, sans-serif',
		        #     size=18,
		        #     color='lightgrey'
		        # ),
		        showticklabels=True,
		        tickangle=0,
		        tickfont=dict(
		            family='Old Standard TT, serif',
		            size=14,
		            color='black'
		        ),
		        exponentformat='e',
		        showexponent='all'
    		)
    	}
    }
)


# pc_v_pl_comment_count = dcc.Graph(
#     id='pc_v_pl_comment_count',
#     figure={
#         'data': [
#             {'y': H_cv.groupby(['subreddit'])['clean_comment'].count(), 
#             'type': 'bar', 
#             'name': 'SF'},
#         ],
#         'layout': {
#             'title': 'Quantity of comments in prochoice and prolife subreddit forums'
#         }
#     }
# )


# comment_dist_per_topic = dcc.Graph(
#     id='comment_dist_per_topic',
#     figure={
#         'data': [
#             {'y': H_cv.topics.value_counts(), 
#             'type': 'bar', 
#             'name': 'SF'},
#         ],
#         'layout': {
#             'title': 'Quantity of comments within each discussion'
#         }
#     }
# )


# pc_v_pl_topic_sentiment_count = dcc.Graph(
#     id='pc_v_pl_topic_sentiment_count',
#     figure={
#         'data': [
#             {'y': H_cv.groupby(['topics','sentiment'])['sentiment'].count(), 
#             'type': 'bar', 
#             'name': 'SF'},
#         ],
#         'layout': {
#             'title': 'Quantity of comments in prochoice and prolife subreddit forums'
#         }
#     }
# )

# sentiment_value_counts = dcc.Graph(
#     id='sentiment_value_counts',
#     figure={
#         'data': [
#             {'y': H_cv.groupby(['topics','sentiment'])['sentiment'].count(), 
#             'type': 'bar', 
#             'name': 'SF'},
#         ],
#         'layout': {
#             'title': 'Quantity of comments within each sentiment category'
#         }
#     }
# )


# Dash app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='NLP & Sentiment Analysis of Reproductive Rights Conversations on Reddit'),

    html.Div(children='''A comparison of sentiment in discussions surrounding three key topics within prochoice and prolife subreddit forums:'''), 
    contraception_sentiment, start_of_life_sentiment, bodily_autonomy_sentiment, other_sentiment])

if __name__ == '__main__':
    app.run_server(debug=True)
