from plotly import express as px
import pandas as pd
import altair as alt

def load_data(file_path):
    return pd.read_csv(file_path)

def plot_click_through_rate(data):
    ctr_data = data.groupby('feature')['clicks'].sum().reset_index()
    fig = px.bar(ctr_data, x='feature', y='clicks', title='Click-Through Rate by Feature')
    fig.show()

def plot_heatmap(data):
    heatmap_data = data.groupby(['x_coord', 'y_coord']).size().reset_index(name='counts')
    heatmap = alt.Chart(heatmap_data).mark_rect().encode(
        x='x_coord:O',
        y='y_coord:O',
        color='counts:Q'
    ).properties(
        width=600,
        height=400,
        title='Heatmap of User Clicks'
    )
    heatmap.show()

def plot_scroll_depth(data):
    scroll_data = data.groupby('scroll_depth')['user_id'].count().reset_index()
    line_chart = alt.Chart(scroll_data).mark_line().encode(
        x='scroll_depth:Q',
        y='user_id:Q'
    ).properties(
        title='Scroll Depth Analysis'
    )
    line_chart.show()

def plot_session_duration(data):
    session_data = data.groupby('session_id')['duration'].mean().reset_index()
    fig = px.histogram(session_data, x='duration', title='Session Duration Distribution')
    fig.show()

def plot_conversion_funnel(data):
    funnel_data = data.groupby('step')['user_id'].count().reset_index()
    fig = px.funnel(funnel_data, x='step', y='user_id', title='Conversion Funnel')
    fig.show()