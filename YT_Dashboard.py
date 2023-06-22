#import libraries
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
from datetime import datetime


#load in data


#build dashboard
sidebar = st.sidebar.selectbox(
    'Aggregate or Individual Video',
    ('Aggregate Metrics', 'Individual Video Analysis')
)

if sidebar == 'Aggregate Metrics':
    st.write('Mihali data')

    st.metric(label="Temperature", value="70F", delta="-1.2F")

if sidebar == 'Individual Video Analysis':
    video_select = st.selectbox(
        'Pick a video:',
        ('video 1', 'video 2')
    )
