import pandas as pd
import datetime
import matplotlib.pyplot as plt 
import seaborn as sns 
import plotly.express as px
import numpy as np
import plotly.graph_objects as go
import streamlit as st
import plotly.figure_factory as ff
import requests

url = http://ergast.com/api/f1/driverStandings/1


response = requests.request("GET", url = url)

