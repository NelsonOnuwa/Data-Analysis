Data Analysis

Data Analysis is the 

               Analysis of the dataset- Accident Level Data, Wales(AccLvlData-2020-2022) using Python libraries


import plotly.express as px

import pandas as pd

from pandas import DataFrame


                  Data from the CSV file with name "AccLvlData-2020" can be read using:

pd.read_csv("C:\\Users\\User\\OneDrive\\Documents\\PGD-DP\\PGD DP RESUBMISSION\\AccLvlData-2020.csv")

pd.read_csv("C:\\Users\\User\\OneDrive\\Documents\\PGD-DP\\PGD DP RESUBMISSION\\AccLvlData-2021.csv")

pd.read_csv("C:\\Users\\User\\OneDrive\\Documents\\PGD-DP\\PGD DP RESUBMISSION\\AccLvlData-2022.csv")


                                    Assigning....




AccLvlData2020 = pd.read_csv("C:\\Users\\User\\OneDrive\\Documents\\PGD-DP\\PGD DP RESUBMISSION\\AccLvlData-2020.csv")
AccLvlData2020 


AccLvlData2021 = pd.read_csv("C:\\Users\\User\\OneDrive\\Documents\\PGD-DP\\PGD DP RESUBMISSION\\AccLvlData-2021.csv")
AccLvlData2021


AccLvlData2022 = pd.read_csv("C:\\Users\\User\\OneDrive\\Documents\\PGD-DP\\PGD DP RESUBMISSION\\AccLvlData-2022.csv")
AccLvlData2022 







                       Data Cleaning Steps with Python and Pandas include:

1.Basic exploratory data analysis
 
2.Detect and remove missing data
 
3.Drop unnecessary columns and rows
 
4.Detect outliers

5.Inconsistent data

6.Irrelevant features
 
 







                       Step 1: 
 
 Exploratory data analysis:
     
 It shows the data types, shape and size, missing values, sample data.


                 To view the top ten rows of the total columns



AccLvlData2020.head(10)

AccLvlData2021.head(10)

AccLvlData2022.head(10)






                view the bottom ten rows of the total columns



AccLvlData2020.tail(10)

AccLvlData2021.tail(10)

AccLvlData2022.tail(10)








                    view a number of random sample of the dataset



AccLvlData2020.sample(10)

AccLvlData2021.sample(10)

AccLvlData2022.sample(10)






                 Determine the total number of rows and columns 
     
 
 The result is a tuple showing 2864 rows and 49 columns
 
AccLvlData2020.shape

AccLvlData2021.shape

AccLvlData2020.shape







                To list the columns

AccLvlData2020.columns

AccLvlData2021.columns

AccLvlData2022.columns







                      To get the dataframe,columns,data types and memory


AccLvlData2020.info()

AccLvlData2021.info()

AccLvlData2022.info()




AccLvlData2020.info

AccLvlData2021.info

AccLvlData2022.info







                              renaming the object columns

AccLvlData2020.rename(columns = {"Date Of Accident" : "Date_Of_Accident", "Day Of Accident" : "Day_Of_Accident","Local Authority Code" : "Local_Authority_Code"}, inplace = True)
AccLvlData2020.describe (include='object')


AccLvlData2021.rename(columns = {"Date Of Accident" : "Date_Of_Accident", "Day Of Accident" : "Day_Of_Accident","Local Authority Code" : "Local_Authority_Code"}, inplace = True)
AccLvlData2021.describe (include='object')



AccLvlData2022.rename(columns = {"Date Of Accident" : "Date_Of_Accident", "Day Of Accident" : "Day_Of_Accident","Local Authority Code" : "Local_Authority_Code"}, inplace = True)
AccLvlData2022.describe (include='object')








#                               Descriptive Analysis

#                    Descriptive Statistics for the numeric series 

# In[33]:


AccLvlData2020.describe()


# In[34]:


AccLvlData2021.describe()


# In[35]:


AccLvlData2022.describe()


# In[ ]:





#                      Descriptive Statistics for the numeric series  per column

# In[36]:


AccLvlData2020.describe().info


# In[37]:


AccLvlData2021.describe().info


# In[38]:


AccLvlData2022.describe().info


# In[ ]:





#                 Descriptive Statistics for the object series 
#     
# 

# In[39]:


AccLvlData2020.describe(include='object')


# In[40]:


AccLvlData2021.describe(include='object')


# In[41]:


AccLvlData2022.describe(include='object')


# The method "describe" gets more detailed information about the data values 
# 
# 
# It generates descriptive statistics for:
#     
# 
# 1. Numeric series -  (the count,mean,standard deviation and percentile excluding NaN values)
# 
# 
# 2. Object series  -  (count,unique,top, frequency)
# 
# 
# It analyzes both numeric and object series, as well as DataFrame column sets of mixed data types.

# In[ ]:





#                      Results from OBJECT analysis
# 
# 
# 
# 1. Road type and Road2 have missing values looking at the count figure
# 
# 2. More accidents happened on friday, on single carriageway on 25/11/2020 (2020), 10/11/2021(2021) and 10/04/2022(2022)

# In[ ]:





#                                  Step 2.
#     
# 
#     
#     
# 1. Detect Unique Values
# 
# 2. Detect and remove duplicates
# 
# 

#                               1.  Unique Value   
#     

#              number of unique value in a particular column 

# In[42]:


AccLvlData2020.Date_Of_Accident.nunique()


# In[43]:


AccLvlData2021.Date_Of_Accident.nunique()


# In[44]:


AccLvlData2022.Date_Of_Accident.nunique()


# In[ ]:





# In[45]:


AccLvlData2020.Day_Of_Accident.nunique()


# In[46]:


AccLvlData2021.Day_Of_Accident.nunique()


# In[47]:


AccLvlData2022.Day_Of_Accident.nunique()


# In[ ]:





# In[48]:


AccLvlData2020.Local_Authority_Code.nunique()


# In[49]:


AccLvlData2021.Local_Authority_Code.nunique()


# In[50]:


AccLvlData2022.Local_Authority_Code.nunique()


# In[ ]:





# In[51]:


AccLvlData2020.RoadType.nunique()


# In[52]:


AccLvlData2021.RoadType.nunique()


# In[53]:


AccLvlData2020.RoadType.nunique()


# In[ ]:





# In[54]:


AccLvlData2020.Road.nunique()


# In[55]:


AccLvlData2021.Road.nunique()


# In[56]:


AccLvlData2022.Road.nunique()


# In[ ]:





# In[57]:


AccLvlData2020.Road2.nunique()


# In[58]:


AccLvlData2021.Road2.nunique()


# In[59]:


AccLvlData2022.Road2.nunique()


# In[ ]:





# In[ ]:





#                         list the unique values in a particular column 

# In[60]:


AccLvlData2020.Date_Of_Accident.unique()


# In[61]:


AccLvlData2021.Date_Of_Accident.unique()


# In[62]:


AccLvlData2022.Date_Of_Accident.unique()


# In[ ]:





# In[63]:


AccLvlData2020.Day_Of_Accident.unique()


# In[64]:


AccLvlData2021.Day_Of_Accident.unique()


# In[65]:


AccLvlData2022.Day_Of_Accident.unique()


# In[ ]:





# In[66]:


AccLvlData2020.Local_Authority_Code.unique()


# In[67]:


AccLvlData2021.Local_Authority_Code.unique()


# In[68]:


AccLvlData2022.Local_Authority_Code.unique()


# In[ ]:





# In[69]:


AccLvlData2020.RoadType.unique()


# In[70]:


AccLvlData2021.RoadType.unique()


# In[71]:


AccLvlData2022.RoadType.unique()


# In[ ]:





# In[72]:


AccLvlData2020.Road.unique()


# In[73]:


AccLvlData2021.Road.unique()


# In[74]:


AccLvlData2022.Road.unique()


# In[ ]:





# In[75]:


AccLvlData2020.Road2.unique()


# In[76]:


AccLvlData2021.Road2.unique()


# In[77]:


AccLvlData2022.Road2.unique()


# In[ ]:





#                       Unique values and their frequency(count) for a particular column

# In[78]:


AccLvlData2020.Date_Of_Accident.value_counts(dropna=False)


# In[79]:


AccLvlData2021.Date_Of_Accident.value_counts(dropna=False)


# In[80]:


AccLvlData2022.Date_Of_Accident.value_counts(dropna=False)


# In[ ]:





# In[81]:


AccLvlData2020.Day_Of_Accident.value_counts(dropna=False)


# In[82]:


AccLvlData2021.Day_Of_Accident.value_counts(dropna=False)


# In[83]:


AccLvlData2022.Day_Of_Accident.value_counts(dropna=False)


# In[ ]:





# In[84]:


AccLvlData2020.Local_Authority_Code.value_counts(dropna=False)


# In[85]:


AccLvlData2021.Local_Authority_Code.value_counts(dropna=False)


# In[86]:


AccLvlData2022.Local_Authority_Code.value_counts(dropna=False)


# In[ ]:





# In[87]:


AccLvlData2020.RoadType.value_counts(dropna=False)


# In[88]:


AccLvlData2021.RoadType.value_counts(dropna=False)


# In[89]:


AccLvlData2022.RoadType.value_counts(dropna=False)


# In[ ]:





# In[90]:


AccLvlData2020.Road.value_counts(dropna=False)


# In[91]:


AccLvlData2021.Road.value_counts(dropna=False)


# In[92]:


AccLvlData2022.Road.value_counts(dropna=False)


# In[ ]:





# In[93]:


AccLvlData2020.Road2.value_counts(dropna=False)


# In[94]:


AccLvlData2021.Road2.value_counts(dropna=False)


# In[95]:


AccLvlData2022.Road2.value_counts(dropna=False)


# In[ ]:





# In[96]:


Road2 has missing values


# In[ ]:





#                                 2. Duplicates
#     
# 
# The method duplicated() is used to detect duplicate values 
#     
# 

# In[97]:


AccLvlData2020.duplicated()


# In[98]:


AccLvlData2021.duplicated()


# In[99]:


AccLvlData2022.duplicated()


# In[ ]:





# In[ ]:





#                 find duplicates and keep only the last record

# In[100]:


AccLvlData2020.duplicated(keep = False)


# In[101]:


AccLvlData2021.duplicated(keep = False)


# In[102]:


AccLvlData2022.duplicated(keep = False)


# In[ ]:





#                     get index of all detected duplication

# In[103]:


AccLvlData2020[AccLvlData2020.duplicated(keep = "last")].index


# In[104]:


AccLvlData2021[AccLvlData2021.duplicated(keep = "last")].index


# In[105]:


AccLvlData2022[AccLvlData2022.duplicated(keep = "last")].index


# In[ ]:





#                     drop duplicates from columns

# In[106]:


AccLvlData2020.drop_duplicates(subset = ["Road2"])


# In[107]:


AccLvlData2021.drop_duplicates(subset = ["Road2"])


# In[108]:


AccLvlData2022.drop_duplicates(subset = ["Road2"])


# In[ ]:





# In[109]:


AccLvlData2020.shape


# In[110]:


AccLvlData2021.shape


# In[111]:


AccLvlData2022.shape


# In[ ]:





# In[ ]:





# In[112]:


AccLvlData2020.drop_duplicates(subset = ["Road"])


# In[113]:


AccLvlData2021.drop_duplicates(subset = ["Road"])


# In[114]:


AccLvlData2022.drop_duplicates(subset = ["Road"])


# In[ ]:





# In[115]:


AccLvlData2020.shape


# In[116]:


AccLvlData2021.shape


# In[117]:


AccLvlData2022.shape


# In[ ]:





#                            Step 3
#     
# 
#     
#     
# Detect Outliers using:
#     
#     
#     1. describe
#     2. boxplot
#  
# 
# 
# 
# Remove Outliers using:
#    
# 
#       1. quantiles
#       2. standard deviation
# 

# In[ ]:





#                        Detect outliers in columns using describe

# In[118]:


AccLvlData2020["Road"].describe()


# In[119]:


AccLvlData2021["Road"].describe()


# In[120]:


AccLvlData2022["Road"].describe()


# In[ ]:





# In[121]:


AccLvlData2020["Road2"].describe()


# In[122]:


AccLvlData2021["Road2"].describe()


# In[123]:


AccLvlData2022["Road2"].describe()


# In[ ]:





# In[ ]:





# In[124]:


AccLvlData2020["Total Casualties"].describe()


# In[125]:


AccLvlData2021["Total Casualties"].describe()


# In[126]:


AccLvlData2022["Total Casualties"].describe()


# In[ ]:





# In[ ]:





# In[127]:


AccLvlData2020["SpeedLimit"].describe()


# In[128]:


AccLvlData2021["SpeedLimit"].describe()


# In[129]:


AccLvlData2022["SpeedLimit"].describe()


# In[ ]:





# In[130]:


AccLvlData2020["Fatal"].describe()


# In[131]:


AccLvlData2021["Fatal"].describe()


# In[132]:


AccLvlData2022["Fatal"].describe()


# In[ ]:





# In[133]:


AccLvlData2020["Serious"].describe()


# In[134]:


AccLvlData2021["Serious"].describe()


# In[135]:


AccLvlData2022["Serious"].describe()


# In[ ]:





# In[ ]:





# In[136]:


AccLvlData2020["Slight"].describe()


# In[137]:


AccLvlData2021["Slight"].describe()


# In[138]:


AccLvlData2022["Slight"].describe()


# In[ ]:





# In[139]:


AccLvlData2020["Older Drivers"].describe()


# In[140]:


AccLvlData2021["Older Drivers"].describe()


# In[141]:


AccLvlData2022["Older Drivers"].describe()


# In[ ]:





# In[142]:


AccLvlData2020["Young Drivers"].describe()


# In[143]:


AccLvlData2021["Young Drivers"].describe()


# In[144]:


AccLvlData2022["Young Drivers"].describe()


# In[ ]:





# In[ ]:





#                      Step 4
#     
#     
# 1. Detect wrong data    
# 
# 2. Detect errors
# 
# 3. Detect typos 
# 
# 4. Detect  misspelling 
# 
# 5. Detect wrong format
# 
# 6. Fix error
# 
# 7. Replace data

#                        Detect wrong data
#     
# 1. empty spaces
# 
# 2. non-numeric rows
# 
# 3. special symbol
# 
# 4. count values 
# 
# 5. datatypes

#                      Empty spaces

#     
#     Detect empty spaces

# In[145]:


import numpy as np


# In[146]:


np.where(AccLvlData2020["Road2"]== "")


# In[147]:


np.where(AccLvlData2021["Road2"]== "")


# In[148]:


np.where(AccLvlData2022["Road2"]== "")


# In[ ]:





# In[149]:


np.where(AccLvlData2020["Road"]== "")


# In[150]:


np.where(AccLvlData2021["Road"]== "")


# In[151]:


np.where(AccLvlData2022["Road"]== "")


# In[ ]:





# In[152]:


np.where(AccLvlData2020["AccidentReference"]== "")


# In[153]:


np.where(AccLvlData2021["AccidentReference"]== "")


# In[154]:


np.where(AccLvlData2022["AccidentReference"]== "")


# In[ ]:





#                     Datatypes                   
#     
#     determine the datatypes of the columns in the DataFrame

# In[155]:


AccLvlData2020.dtypes


# In[156]:


AccLvlData2021.dtypes


# In[157]:


AccLvlData2022.dtypes


#                     count values in a column 

# In[158]:


AccLvlData2020[AccLvlData2020.columns[6]].value_counts().head(10)


# In[159]:


AccLvlData2021[AccLvlData2020.columns[6]].value_counts().head(10)


# In[160]:


AccLvlData2022[AccLvlData2020.columns[6]].value_counts().head(10)


# In[ ]:





#                      detect similar values using difflib:

# In[161]:


import difflib


# In[162]:


difflib.get_close_matches('Friday', ['Friday ', 'Thursday', 'Tuesday', 'Monday ',"Saturday","Wednesday","Sunday"], n=1, cutoff=0.7)


# In[ ]:





#                         Step 5
#     
#     
# 
# Drop columns
#                         
# Drop row
# 
# Drop index
# 
# Drop conditions
# 

#                     Drop single column

# In[163]:


AccLvlData2020.drop(["Year"],axis = 1,inplace= True)

AccLvlData2020


# In[164]:


AccLvlData2021.drop(["Year"],axis = 1,inplace= True)

AccLvlData2021


# In[165]:


AccLvlData2022.drop(["Year"],axis = 1,inplace= True)

AccLvlData2022


# In[ ]:





#                        Drop multiple column

# In[166]:


AccLvlData2020.drop(["Northing",
                     "Longitude",
                     "Latitude",
                     "TrunkRoadStatus",
                     "Pedestrians",
                     "Quarter"
                    ],axis = 1,inplace= True)

AccLvlData2020


# In[167]:


AccLvlData2021.drop(["Northing",
                     "Longitude",
                     "Latitude",
                     "TrunkRoadStatus",
                     "Pedestrians",
                     "Quarter"
                    ],axis = 1,inplace= True)

AccLvlData2021


# In[168]:


AccLvlData2022.drop(["Northing",
                     "Longitude",
                     "Latitude",
                     "TrunkRoadStatus",
                     "Pedestrians",
                     "Quarter"
                    ],axis = 1,inplace= True)

AccLvlData2022


# In[ ]:





#                        Drop columns with Not a Number (NAN) values

# In[169]:


AccLvlData2020.shape


# In[170]:


AccLvlData2021.shape


# In[171]:


AccLvlData2022.shape


# In[ ]:





# In[172]:


AccLvlData2020.info()


# In[173]:


AccLvlData2021.info()


# In[174]:


AccLvlData2022.info()


# In[ ]:





# In[175]:


AccLvlData2020.dropna(axis=1, how="any")


# In[176]:


AccLvlData2021.dropna(axis=1, how="any")


# In[177]:


AccLvlData2022.dropna(axis=1, how="any")


# In[ ]:





# In[178]:


AccLvlData2020.dropna(axis=1, how="any").info()


# In[179]:


AccLvlData2021.dropna(axis=1, how="any").info()


# In[180]:


AccLvlData2022.dropna(axis=1, how="any").info()


# In[ ]:





# RoadType and Road2 in 2020 has Not a Number (NAN) values
# 
# 
# Road2 in 2020 has Not a Number (NAN) values
# 
# 
# Road2 in 2020 has Not a Number (NAN) values

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





#                                      QUESTION 2

# Presentation of the Analysis results of the dataset- Accident Level Data,Wales(AccLvlData-2020) in the form of graphs/charts using Plotly

# Plotly is a library for making interactive graphs with python.
# It is based on the famous d3.js javascript library.

# In[181]:


import plotly.express as px
import plotly.graph_objects as go

AccLvlData2020 = pd.read_csv("C:\\Users\\User\\OneDrive\\Documents\\PGD-DP\\PGD DP RESUBMISSION\\AccLvlData-2020.csv")

AccLvlData2020.describe()


# In[182]:


import plotly.express as px
import plotly.graph_objects as go

AccLvlData2021 = pd.read_csv("C:\\Users\\User\\OneDrive\\Documents\\PGD-DP\\PGD DP RESUBMISSION\\AccLvlData-2021.csv")

AccLvlData2021.describe()


# In[183]:


import plotly.express as px
import plotly.graph_objects as go

AccLvlData2022 = pd.read_csv("C:\\Users\\User\\OneDrive\\Documents\\PGD-DP\\PGD DP RESUBMISSION\\AccLvlData-2022.csv")

AccLvlData2022.describe()


# In[ ]:





# In[184]:


AccLvlData2020.drop([
"Year","Quarter","PoliceForce","Easting","Time Of Accident","Ridden horses",
"Pedal cycles","Motorcycles","Agricultural vehicles",
"Northing","Longitude","Latitude","TrunkRoadStatus",
"Trams or light rail vehicles","Other vehicles","Motorcyle Fatal",
"Pedestrians","Road","Road2","Total Vehicles","Buses_ coaches or minibuses","Motorcyle Serious",
"Light vans or goods vehicles","Taxis or private hire vehicles"],axis = 1,inplace= True)

AccLvlData2020.describe()


# In[185]:


AccLvlData2021.drop([
"Year","Quarter","PoliceForce","Easting","Time Of Accident","Ridden horses",
"Pedal cycles","Motorcycles","Agricultural vehicles",
"Northing","Longitude","Latitude","TrunkRoadStatus",
"Trams or light rail vehicles","Other vehicles","Motorcyle Fatal",
"Pedestrians","Road","Road2","Total Vehicles","Buses_ coaches or minibuses","Motorcyle Serious",
"Light vans or goods vehicles","Taxis or private hire vehicles"],axis = 1,inplace= True)

AccLvlData2021.describe()


# In[186]:


AccLvlData2022.drop([
"Year","Quarter","PoliceForce","Easting","Time Of Accident","Ridden horses",
"Pedal cycles","Motorcycles","Agricultural vehicles",
"Northing","Longitude","Latitude","TrunkRoadStatus",
"Trams or light rail vehicles","Other vehicles","Motorcyle Fatal",
"Pedestrians","Road","Road2","Total Vehicles","Buses_ coaches or minibuses","Motorcyle Serious",
"Light vans or goods vehicles","Taxis or private hire vehicles"],axis = 1,inplace= True)

AccLvlData2022.describe()


# In[ ]:





# In[187]:


AccLvlData2022 = pd.read_csv("C:\\Users\\User\\OneDrive\\Documents\\PGD-DP\\PGD DP RESUBMISSION\\AccLvlData-2022.csv")

AccLvlData2022.describe()


# In[194]:


fig = px.bar(AccLvlData2020.describe(),
             x ="SpeedLimit" ,
          
             y="Total Casualties",
             text = "SpeedLimit",
             title = " SpeedLimit vs Total Casualties ",
             hover_data=["Fatal","Slight","Serious",
                        "Young Fatal","Young Serious",
                         "Older Drivers","Young Drivers",
                         "Cars"
                        ],
          
              pattern_shape="Age Of Casualty 0-15",
              pattern_shape_sequence=[".", "x", "+"],
              barmode="group"
            
              )


fig.show()





# In[189]:


fig = px.bar(AccLvlData2021.describe(),
             x ="SpeedLimit" ,
          
             y="Total Casualties",
             text = "SpeedLimit",
             title = " SpeedLimit vs Total Casualties ",
             hover_data=["Fatal","Slight","Serious",
                        "Young Fatal","Young Serious",
                         "Older Drivers","Young Drivers",
                         "Cars"
                        ],
          
              pattern_shape="Age Of Casualty 0-15",
              pattern_shape_sequence=[".", "x", "+"],
              barmode="group"
            
              )


fig.show()


# In[190]:


fig = px.bar(AccLvlData2022.describe(),
             x ="SpeedLimit" ,
          
             y="Total Casualties",
             text = "SpeedLimit",
             title = " SpeedLimit vs Total Casualties ",
             hover_data=["Fatal","Slight","Serious",
                        "Young Fatal","Young Serious",
                         "Older Drivers","Young Drivers",
                         "Cars"
                        ],
          
              pattern_shape="Age Of Casualty 0-15",
              pattern_shape_sequence=[".", "x", "+"],
              barmode="group"
            
              )


fig.show()


# In[ ]:





# In[191]:


fig = px.bar(AccLvlData2020.describe(),
             x ="SpeedLimit" , 
          
             y="Total Casualties",
             text = "SpeedLimit",
             title = " SpeedLimit vs Total Casualties ",
             hover_data=["Fatal","Slight","Serious",
                        "Young Fatal","Young Serious",
                         "Older Drivers","Young Drivers",
                         "Cars"
                        ],
          
              pattern_shape="Age Of Casualty 70+",
              pattern_shape_sequence=[".", "x", "+"],
              barmode="group"
            
              )



fig.show()









# In[192]:


fig = px.bar(AccLvlData2021.describe(),
             x ="SpeedLimit" , 
          
             y="Total Casualties",
             text = "SpeedLimit",
             title = " SpeedLimit vs Total Casualties ",
             hover_data=["Fatal","Slight","Serious",
                        "Young Fatal","Young Serious",
                         "Older Drivers","Young Drivers",
                         "Cars"
                        ],
          
              pattern_shape="Age Of Casualty 70+",
              pattern_shape_sequence=[".", "x", "+"],
              barmode="group"
            
              )



fig.show()


# In[193]:


fig = px.bar(AccLvlData2022.describe(),
             x ="SpeedLimit" , 
          
             y="Total Casualties",
             text = "SpeedLimit",
             title = " SpeedLimit vs Total Casualties ",
             hover_data=["Fatal","Slight","Serious",
                        "Young Fatal","Young Serious",
                         "Older Drivers","Young Drivers",
                         "Cars"
                        ],
          
              pattern_shape="Age Of Casualty 70+",
              pattern_shape_sequence=[".", "x", "+"],
              barmode="group"
            
              )



fig.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




