# Import required libraries

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt

#Load customers data
customersdata = pd.read_csv("/Users/asifa/Desktop/customer_seg/customers-data - customers-data.csv")
