#!/usr/bin/env python
# coding: utf-8

# Exploratory data analysis
# 
# This activity is to examine data provided and prepare it for analysis.
# 
# The structure of this activity is designed to emulate the proposals likely to be assigned in my career as a data professional. This dataset was sourced from Coursera.
# 
# The purpose of this project is to conduct exploratory data analysis on a provided dataset. Your mission is to continue the investigation you began in C2 and perform further EDA on this data with the aim of learning more about the variables.
# 
# The goal is to clean dataset, structure and create a visualization.

# In[14]:


#importing all relevant libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


#load data
trip = pd.read_csv(r"C:\Users\naaod\OneDrive\Desktop\Coursera\2017_Yellow_Taxi_Trip_Data.csv")

#Previewing the first five rows
trip.head(5)


# In[5]:


#Identify the total number of rows and columns
trip.shape


# In[6]:


#Get more details about our dataset
trip.info()


# In[9]:


#checking to confirm that there is no missing data
trip.isna().shape


# In[10]:


trip.describe()


# From the preview above,
# tpep_pickup_datetime and tpep_dropoff_datetime dtypes are objects so we will convert to datetime.
# 
# passenger_count deals with the number of rides so we can find the average number, etc.
# RatecodeID and store_and_fwd_flag will not be needed in our analysis so we can drop them.
# 
# 
# Also,
# 
# Per preview, a bar chart, box plot and scatter plot will be most helpful in understanding this data.
# A box plot will be helpful to determine outliers and where the bulk of the data points reside in terms of trip_distance, duration, and total_amount.
# 
# A scatter plot will be helpful to visualize the trends and patters and outliers of critical variables, such as trip_distance and total_amount.
# 
# A bar chart will help determine average number of trips per month, weekday, weekend, etc.

# In[12]:


# Convert data columns to datetime
trip['tpep_pickup_datetime']=pd.to_datetime(trip['tpep_pickup_datetime'])
trip['tpep_dropoff_datetime']=pd.to_datetime(trip['tpep_dropoff_datetime'])

#Previewing info.
trip.info()


# In[16]:


# Create box plot of trip_distance
plt.figure(figsize=(7,2))
plt.title('trip_distance')
sns.boxplot(data=None, x=trip['trip_distance'], fliersize=1);


# In[17]:


# Create histogram of trip_distance
plt.figure(figsize=(10,5))
sns.histplot(trip['trip_distance'], bins=range(0,26,1))
plt.title('Trip distance histogram');


# In[19]:


# Create box plot of total_amount
plt.figure(figsize=(7,2))
plt.title('total_amount')
sns.boxplot(x=trip['total_amount'], fliersize=1);


# In[21]:


# Create histogram of total_amount
plt.figure(figsize=(12,6))
ax = sns.histplot(trip['total_amount'], bins=range(-10,101,5))
ax.set_xticks(range(-10,101,5))
ax.set_xticklabels(range(-10,101,5))
plt.title('Total amount histogram');


# In[22]:


# Create box plot of tip_amount
plt.figure(figsize=(7,2))
plt.title('tip_amount')
sns.boxplot(x=trip['tip_amount'], fliersize=1);


# In[23]:


# Create histogram of tip_amount
plt.figure(figsize=(12,6))
ax = sns.histplot(trip['tip_amount'], bins=range(0,21,1))
ax.set_xticks(range(0,21,2))
ax.set_xticklabels(range(0,21,2))
plt.title('Tip amount histogram');


# In[24]:


# Create histogram of tip_amount by vendor
plt.figure(figsize=(12,7))
ax = sns.histplot(data=trip, x='tip_amount', bins=range(0,21,1), 
                  hue='VendorID', 
                  multiple='stack',
                  palette='pastel')
ax.set_xticks(range(0,21,1))
ax.set_xticklabels(range(0,21,1))
plt.title('Tip amount by vendor histogram');


# From the histogram above, it seems like vendor 2 has slightly higher share of the rides, and this proportion is approximately maintained for all tip amounts.

# In[25]:


# Create histogram of tip_amount by vendor for tips > $10 
tips_over_ten = trip[trip['tip_amount'] > 10]
plt.figure(figsize=(12,7))
ax = sns.histplot(data=tips_over_ten, x='tip_amount', bins=range(10,21,1), 
                  hue='VendorID', 
                  multiple='stack',
                  palette='pastel')
ax.set_xticks(range(10,21,1))
ax.set_xticklabels(range(10,21,1))
plt.title('Tip amount by vendor histogram');


# In[27]:


#Let's find the unique values in the passenger_counts column
trip[['passenger_count']].value_counts()


# For the passenger_count column, we notice that the most record of the rides were single occupancy. 
# Also, there are 33 rides with an occupancy count of zero, which doesn't make sense. If zero, then how come 33 rides were recorded?
# Although there were still almost 700 rides (i.e 693) with as many as six passengers. These would likely be dropped unless a reasonable explanation can be found for them.

# In[32]:


# Calculate average tips by passenger_count
average_tips_by_passenger_count = trip.groupby(['passenger_count']).mean()[['tip_amount']]
average_tips_by_passenger_count


# In[33]:


# Create bar plot for average tips by passenger count
data = average_tips_by_passenger_count.tail(-1)
pal = sns.color_palette("Greens_d", len(data))
rank = data['tip_amount'].argsort().argsort()
plt.figure(figsize=(12,7))
ax = sns.barplot(x=data.index,
            y=data['tip_amount'],
            palette=np.array(pal[::-1])[rank])
ax.axhline(trip['tip_amount'].mean(), ls='--', color='red', label='global mean')
ax.legend()
plt.title('Mean tip amount by passenger count', fontsize=16);


# The average tip amount varies very little by passenger count. Although it does drop noticeably for four-passenger rides, it's expected that there would be a higher degree of fluctuation because rides with four passengers were the least plentiful in the dataset (aside from rides with zero passengers).

# In[35]:


#Let's now see the total rides by months or days. We will have to derive our months and days from the datetime columns.

# Create a month column
trip['month'] = trip['tpep_pickup_datetime'].dt.month_name()
# Create a day column
trip['day'] = trip['tpep_pickup_datetime'].dt.day_name()


# In[41]:


# Get total number of rides for each month
monthly_rides = trip['month'].value_counts()
monthly_rides


# In[42]:


#As we can all see, the months are arranged in a wrong order. So, let's try and reorder them.
# Reorder the monthly ride list so months go in order
month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
         'August', 'September', 'October', 'November', 'December']

monthly_rides = monthly_rides.reindex(index=month_order)
monthly_rides


# In[44]:


#I prefer using this graphical interface for my bar plots.
# Create a bar plot of total rides per month
plt.figure(figsize=(12,7))
ax = sns.barplot(x=monthly_rides.index, y=monthly_rides)
ax.set_xticklabels(month_order)
plt.title('Ride count by month', fontsize=16);


# From the above, we can conclude that monthly rides are fairly consistent, with notable dips in the summer months of July, August, and September, and also in February.
# 
# Now, let's see what the days record will also give us.

# In[45]:


daily_rides = trip['day'].value_counts()
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
daily_rides = daily_rides.reindex(index=day_order)
daily_rides


# In[46]:


# Create bar plot for ride count by day
plt.figure(figsize=(12,7))
ax = sns.barplot(x=daily_rides.index, y=daily_rides)
ax.set_xticklabels(day_order)
ax.set_ylabel('Count')
plt.title('Ride count by day', fontsize=16);


# Seems like, Wednesday through Friday had the highest number of daily rides, while Saturday, Sunday and Monday had the least.
# 
# Does it mean that most rides were used to commute to work or school? Well, if so, then how come Monday recorded least? I guess we cannot make this conclusion then.
# 
# However, we can clearly see the days with the highest records from our data.

# In[47]:


#What about total amount by day?
# Repeat the process, this time for total revenue by day
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
total_amount_day = trip.groupby('day').sum()[['total_amount']]
total_amount_day = total_amount_day.reindex(index=day_order)
total_amount_day


# In[48]:


#Let's plot on a bar chart to see.
# Create bar plot of total revenue by day
plt.figure(figsize=(12,7))
ax = sns.barplot(x=total_amount_day.index, y=total_amount_day['total_amount'])
ax.set_xticklabels(day_order)
ax.set_ylabel('Revenue (USD)')
plt.title('Total revenue by day', fontsize=16);


# Thursday had the highest gross revenue of all days, and Sunday and Monday had the least.

# In[49]:


#How about we check the total revenue by month since we know for the days. 

#Seems like we checked for rides by month and must have skipped monthly revenue
total_amount_month = trip.groupby('month').sum()[['total_amount']]
total_amount_month = total_amount_month.reindex(index=month_order)
total_amount_month


# In[50]:


# Create a bar plot of total revenue by month
plt.figure(figsize=(12,7))
ax = sns.barplot(x=total_amount_month.index, y=total_amount_month['total_amount'])
plt.title('Total revenue by month', fontsize=16);


# Monthly revenue generally follows the pattern of monthly rides, with noticeable dips in the summer months of July, August, and September, and also one in February.
