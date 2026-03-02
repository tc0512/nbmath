import statistics
import math
def mean(data: list):
    if len(data)==0:
        raise statistics.StatisticsError("mean requires at least one data point")
    return sum(data)/len(data)
def SS(data: list):
    if len(data)==0:
        raise statistics.StatisticsError("sum of deviation square requires at least one data point")
    average = mean(data)
    ss = 0
    for i in data:
        ss+=(i-average)**2
    return ss
def var(data: list):
    if len(data)==0:
        raise statistics.StatisticsError("variance requires at least one data point")
    elif len(data)==1:
        return 0
    return SS(data)/len(data)
def std(data: list):
    if len(data)==0:
        raise statistics.StatisticsError("standard deviation requires at least one data point")
    elif len(data)==1:
        return 0
    return math.sqrt(var(data))
def data_range(data: list):
    if len(data)<2:
        raise statistics.StatisticsError("range requires at least two data points")
    return max(data)-min(data)
def percentile(data: list, p: int):
    if len(data)==0:
        raise statistics.StatisticsError("percentile requires at least one data point")
    elif len(data)==1:
        return data[0]
    data.sort()
    pos = len(data)*p/100
    if int(pos)==pos:
        index1 = int(pos-1)
        index2 = int(pos)
        return (data[index1]+data[index2])/2
    else:
        index = int(pos)
        return data[index]
def mode(data):
    freq = {}
    for x in data:
        freq[x] = freq.get(x, 0) + 1
    max_freq = max(freq.values())
    return [k for k, v in freq.items() if v == max_freq]
