import random
import statistics as st
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd 

df = pd.read_csv("data.csv")
hList = df["Height(Inches)"].tolist()

mean=st.mean(hList)
median=st.median(hList)
mode=st.mode(hList)
std=st.stdev(hList)
print("Mean of data : {}".format(mean))
print("Median of data : {}".format(median))
print("Mode of data : {}".format(mode))
print("Standard Deviation of data : {}\n".format(std))


first_std_start , first_std_end= mean-std , mean+std
second_std_start , second_std_end= mean-(2*std) , mean+(2*std)
third_std_start , third_std_end= mean-(3*std) , mean+(3*std)

fig=ff.create_distplot([hList] , ["Height List"] , show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN of data" ))
fig.add_trace(go.Scatter(x=[first_std_start, first_std_start], y=[0, 0.17], mode="lines", name="First STD start" ))
fig.add_trace(go.Scatter(x=[first_std_end, first_std_end], y=[0, 0.17], mode="lines", name="First STD end" ))
fig.add_trace(go.Scatter(x=[second_std_start, second_std_start], y=[0, 0.17], mode="lines", name="Second STD start" ))
fig.add_trace(go.Scatter(x=[second_std_end, second_std_end], y=[0, 0.17], mode="lines", name="Second STD end" ))
fig.add_trace(go.Scatter(x=[third_std_start, third_std_start], y=[0, 0.17], mode="lines", name="Third STD start" ))
fig.add_trace(go.Scatter(x=[third_std_end, third_std_end], y=[0, 0.17], mode="lines", name="Third STD end" ))
fig.show()

data_within_std1=[result for result in hList if result>first_std_start and result<first_std_end]
data_within_std2=[result for result in hList if result>second_std_start and result<second_std_end]
data_within_std3=[result for result in hList if result>third_std_start and result<third_std_end]

print("{} % of data lies within first std".format(len(data_within_std1)*100.0/len(hList)))

print("{} % of data lies within second std".format(len(data_within_std2)*100.0/len(hList)))

print("{} % of data lies within third std".format(len(data_within_std3)*100.0/len(hList)))
