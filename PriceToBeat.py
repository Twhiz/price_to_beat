"""
Twhiz PriceToBeat Algorithm
Created on Wednesday 30 May 2018
@author: Alexander Bechtel (email@alexanderbechtel.com)
"""


#%% Import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#%% Load data from API
flight_data_raw = pd.read_csv('flight_data.csv')
flight_data_raw['business'] = pd.DataFrame([1,0,1,0,1,0,1,1,1,0,0,0,1,0,1,0,0,0,1,1,1,1]) #manually add column for class




#%% Drop outliers


#%% Filter data according to travel policy
def filter_flight(flight_data_raw,business = 0, airline == None):
    if airline == None:
        return(flight_data_raw[flight_data_raw.business==business])
        else:
            flight_data_raw[flight_data_raw.airline==airline]


flight_data_filtered = filter_flight(flight_data_raw,business=0)


#%% PriceToBeat
def ptb_flight(flight_data):
    return(np.mean(flight_data.prices))
    

ptb_flight(flight_data_filtered)



#%% Summary statistics
flight_mean = np.mean(flight_data.prices) 
flight_median = np.median(flight_data.prices)
flight_std = np.std(flight_data.prices)
flight_min = np.min(flight_data.prices)
flight_max = np.max(flight_data.prices)
flight_obs = len(flight_data)


#%% Clean data
flight_data = flight_data.loc[flight_data.duration<=np.median(flight_data.duration)*2,:]














