import random
import statistics as st
import plotly.figure_factory as ff
import plotly.graph_objects as go

dice_result= []
for i in range(0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice_result.append(dice1+dice2)
mean=st.mean(dice_result)
median=st.median(dice_result)
mode=st.mode(dice_result)
std=st.stdev(dice_result)
print("Mean of data : {}".format(mean))
print("Median of data : {}".format(median))
print("Mode of data : {}".format(mode))
print("Standard Deviation of data : {}\n".format(std))

first_std_start , first_std_end= mean-std , mean+std
second_std_start , second_std_end= mean-(2*std) , mean+(2*std)
third_std_start , third_std_end= mean-(3*std) , mean+(3*std)

fig=ff.create_distplot([dice_result] , ["Dice Result"] , show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN of data" ))
fig.add_trace(go.Scatter(x=[first_std_start, first_std_start], y=[0, 0.17], mode="lines", name="First STD start" ))
fig.add_trace(go.Scatter(x=[first_std_end, first_std_end], y=[0, 0.17], mode="lines", name="First STD end" ))
fig.add_trace(go.Scatter(x=[second_std_start, second_std_start], y=[0, 0.17], mode="lines", name="Second STD start" ))
fig.add_trace(go.Scatter(x=[second_std_end, second_std_end], y=[0, 0.17], mode="lines", name="Second STD end" ))
fig.add_trace(go.Scatter(x=[third_std_start, third_std_start], y=[0, 0.17], mode="lines", name="Third STD start" ))
fig.add_trace(go.Scatter(x=[third_std_end, third_std_end], y=[0, 0.17], mode="lines", name="Third STD end" ))
#fig.show()

data_within_std1=[i for result in dice_result if result>first_std_start and result<first_std_end]
data_within_std2=[i for result in dice_result if result>second_std_start and result<second_std_end]
data_within_std3=[i for result in dice_result if result>third_std_start and result<third_std_end]

print("{} % of data lies within first std".format(len(data_within_std1)*100.0/len(dice_result)))

print("{} % of data lies within second std".format(len(data_within_std2)*100.0/len(dice_result)))

print("{} % of data lies within third std".format(len(data_within_std3)*100.0/len(dice_result)))
