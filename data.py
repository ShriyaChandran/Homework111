import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import statistics
import random

df = pd.read_csv("data.csv")
data = df["reading_time"].tolist()
population_mean = statistics.mean(data)
print("The mean of the population is: " + str(population_mean))
population_stdDev = statistics.stdev(data)
print("The standard deviation of the population is: " + str(population_stdDev))

def rand_set_mean(counter):
    dataset=[]
    for i in range(0, counter):
        random_index= random.randint(0,len(data))
        value=data[random_index]
        dataset.append(value)
    randomMean = statistics.mean(dataset)
    return(randomMean)


def show_fig(mean_list):
    figData = mean_list
    fig = ff.create_distplot([figData],["Reading time"],show_hist = False)
    mean = statistics.mean(mean_list)
    stdDev = statistics.stdev(meanList)
    #this this the new formula learnt in class, to find the difference between stndard devs.
    first_std_start, first_std_end = mean-stdDev, mean+stdDev
    second_std_start, second_std_end = mean-(2*stdDev), mean+(2*stdDev)
    third_std_start, third_std_end = mean-(3*stdDev), mean+(3*stdDev)

    print("std 1: ", first_std_start, first_std_end)
    print("std 2: ", second_std_start, second_std_end)
    print("std 3: ", third_std_start, third_std_end)    

    fig.add_trace(go.Scatter(x=[first_std_start, first_std_start], y=[0,0.7], mode='lines', name="std1Start"))
    fig.add_trace(go.Scatter(x=[first_std_end, first_std_end], y=[0,0.7], mode='lines', name="std1End"))
    fig.add_trace(go.Scatter(x=[second_std_start, second_std_start], y=[0,0.7], mode='lines', name="std2Start"))
    fig.add_trace(go.Scatter(x=[second_std_end, second_std_end], y=[0,0.7], mode='lines', name="std2End"))
    fig.add_trace(go.Scatter(x=[third_std_start, third_std_start], y=[0,0.7], mode='lines', name="std3Start"))
    fig.add_trace(go.Scatter(x=[third_std_end, third_std_end], y=[0,0.7], mode='lines', name="std3End"))

    fig.add_trace(go.Scatter(x=[mean, mean], y=[0,0.7], mode='lines', name="Mean"))
    sampleMean = statistics.mean(data)
    fig.add_trace(go.Scatter(x = [sampleMean,sampleMean],y = [0,0.7]))
    print("Mean is: " + str(mean))
    print("Standard deviation is: " + str(stdDev))

    zTest = (sampleMean - mean)/stdDev
    print("Z Test:",zTest)

    fig.show()

meanList=[]
for i in range(0,100):
    meanSet = rand_set_mean(30)
    meanList.append(meanSet)
show_fig(meanList)