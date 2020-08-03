# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file is stored in the variable path

#Code starts here

# Data Loading 
data = pd.read_csv(path, sep=",", delimiter=None)
print(data.columns)
data.rename(columns = {'Total':'Total_Medals'}, inplace=True)
print(data.columns)
data.head(10)

# Summer or Winter
data['Better_Event'] = np.where(data['Total_Summer']>data['Total_Winter'], 'Summer', 'Winter')
data['Better_Event'] =np.where(data['Total_Summer'] == data['Total_Winter'],'Both',data['Better_Event'])
better_event = data['Better_Event'].value_counts()
print(better_event)
better_event = 'Summer'

# Top 10
tc = {'Country_Name':data['Country_Name'], 'Total_Summer':data['Total_Summer'], 'Total_Winter':data['Total_Winter'], 'Total_Medals':data['Total_Medals']}
top_countries = pd.DataFrame(tc)
#print(len(top_countries))
top_countries.drop(top_countries.tail(1).index, inplace=True)
#print(len(top_countries)
def top_ten(df_name,col_name):
    #country_list = []
    #cl = df_name.nlargest(10, col_name)
    if col_name is 'Total_Summer':
        top_10_summer = []
        cl = df_name.nlargest(10, col_name)
        top_10_summer = list(cl['Country_Name'])
        #print('summer')
        return top_10_summer
    elif col_name is 'Total_Winter':
        top_10_winter = []
        cll = df_name.nlargest(10, col_name)
        top_10_winter = list(cll['Country_Name'])
        #print('winter')
        return top_10_winter
    elif col_name is 'Total_Medals':
        top_10 = []
        clll = df_name.nlargest(10, col_name)
        top_10 = list(clll['Country_Name'])
        #print('top 10')
        return top_10
    else:
        print('None')
    #country_list = list(cl['Country_Name'])    i
    #eturn country_list
top_10_summer = top_ten(top_countries,'Total_Summer')
top_10_winter = top_ten(top_countries,'Total_Winter')
top_10 = top_ten(top_countries,'Total_Medals')
print(top_10_summer)
print(top_10_winter)
print(top_10)
common = []
for i in top_10_summer:
    if i in top_10_winter and top_10:
        common.append(i)
print(common)

# Plotting top 10

summer_df = data[data['Country_Name'].isin(top_10_summer)]
print(summer_df)
winter_df = data[data['Country_Name'].isin(top_10_winter)]
print(winter_df)
top_df = data[data['Country_Name'].isin(top_10)]
print(top_df)
#summer_df['Total_Summer'].plot(kind='bar')
summer_df['Total_Winter'].plot(kind='bar')
summer_df['Total_Summer'].plot(kind='bar')
plt.show()
#['China', 'France', 'Germany', 'East Germany', 'Great Britain', 'Italy', 'Russia', 'Soviet Union', 'Sweden', 'United States']
# Top Performing Countries
#print(summer_df.columns)
summer_df['Golden_Ratio'] = summer_df['Gold_Summer'] / summer_df['Total_Summer']
print(summer_df)
summer_max_ratio = summer_df['Golden_Ratio'].max()
print(summer_max_ratio)

#summer_country_gold = summer_df['Golden_Ratio'].idxmax(summer_df['Country_Name'])
summer_country_gold = summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']
print(summer_country_gold)

winter_df['Golden_Ratio'] = winter_df['Gold_Winter'] / winter_df['Total_Winter']
#print(winter_df)
winter_max_ratio = winter_df['Golden_Ratio'].max()
print(winter_max_ratio)
winter_country_gold = winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']
print(winter_country_gold)

top_df['Golden_Ratio'] = top_df['Gold_Total'] / top_df['Total_Medals']
#print(top_df)
top_max_ratio = top_df['Golden_Ratio'].max()
print(top_max_ratio)
top_country_gold = top_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']
#print(top_country_gold)

# Best in the world 
data_1 = data[:-1]
#data_1['Total_Points'] = df.groupby(['Gold_Total', 'Silver_Total', 'Bronze_Total'])
data_1['Total_Points'] = (data_1['Gold_Total'] * 3) + (data_1['Silver_Total'] * 2) + (data_1['Bronze_Total'] * 1)
print(data_1.head(2))
most_points = max(data_1['Total_Points'])
print(most_points)
best_country = data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']
print(best_country)
best = data[data['Country_Name'] == best_country]
#print(best)
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
print(best.head(2))
# Plotting the best
best.plot(kind='bar', stacked=True)
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)


