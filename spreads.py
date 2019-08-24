import numpy as np 
import pandas as pd

def getSD(nparray):
    return np.std(nparray)

def getMean(nparray):
    return np.mean(nparray)

def getMedian(nparray):
    return np.median(nparray)

def getNanSD(nparray):
    return np.nanstd(nparray)

def getNanMean(nparray):
    return np.nanmean(nparray)

def getHistogram(nparray):
    return np.histogram(nparray)

def getQ1(nparray):
    return np.percentile(nparray,25)

def getQ3(nparray):
    return np.percentile(nparray,75)

def getIQR(nparray):
    q1=np.percentile(nparray,25)
    q3=np.percentile(nparray,75)
    iqr=q3-q1
    return iqr

testlist=[1,3,5,7,9,12,15,18,21]
testnparr = np.array(testlist)
print(getMean(testnparr))
print(getSD(testnparr))
