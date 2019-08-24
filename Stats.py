import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class exploratory_analysis():
    def __init__(self,arr):
        self.arr = arr


    def get_mean(self):
        mean1 = np.mean(self.arr)
        return mean1

    def get_median(self):
        median1 = np.median(self.arr)
        return median1

    def getSD(self):
        return np.std(self.arr)

    def getNanSD(self):
        return np.nanstd(self.arr)

    def getNanMean(self):
        return np.nanmean(self.arr)

    def getHistogram(self):
        return np.histogram(self.arr)

    def getQ1(self):
        return np.percentile(self.arr,25)

    def getQ3(self):
        return np.percentile(self.arr,75)

    def getIQR(self):
        q1=np.percentile(self.arr,25)
        q3=np.percentile(self.arr,75)
        iqr=q3-q1
        return iqr

    def get_skewness(self):
        SD1 = self.getSD()
        mean2 = self.get_mean()
        median2 = self.get_median()
        skewness1 = (3*(mean2-median2))/SD1
        if skewness1 == 0:
            return ("Dataset is Normal/Gaussian Distribution as skewness is ",skewness1)
        if skewness1 > 0:
            return ("Dataset is Right Skewed as skewness is ",skewness1)
        if skewness1 < 0:
            return ("Dataset is Left Skewed as skewness is ",skewness1)
        
    def get_outliers(self):
        a_list = []
        per_75 = np.percentile(self.arr,75)
        per_25 = np.percentile(self.arr,25)
        iqr = per_75-per_25
        tot_75 = per_75 + (1.5*iqr)
        tot_25 = per_25 - (1.5*iqr)
        a_list1 = np.array(self.arr).tolist()
        for x in a_list1:
            if x > tot_75:
                a_list.append(x)
            if x < tot_25:
                a_list.append(x)
        return a_list
    
    def visualisation_Distribution(self):
    
        #Histogram of input array
        fig,axes = plt.subplots(nrows=1,ncols=3,figsize=(15,10))


        axes[0].hist(self.arr)
        axes[0].axvline(self.get_mean(), color='r', linestyle='--')
        axes[0].axvline(self.get_median(), color='g', linestyle='-')
        #axes[0].axvline(mode, color='b', linestyle='-')
        axes[0].legend({'Mean':self.get_mean(),'Median':self.get_median()})

        axes[1].boxplot(self.arr)
        sns.distplot(self.arr,ax=axes[2])

 
        plt.show() 

    print("Mean is ",x.get_mean())
    print("Median is ",x.get_median())
    print("GetSD is ",x.getSD())
    print("Q1 is ",x.getQ1())
    print("Q3 is ",x.getQ3())
    print("IQR is ",x.getIQR())
    print("Skewness is",x.get_skewness())
    print("Outliers are",x.get_outliers())
    

class relation():
    def __init__(self,df):
        self.df = df


    def scatterplot(self):
        sns.jointplot(x=self.df[''])

    def barplots(self):
        sns.barplot(x=self.df['Sex'],y=self.df['Survived'],data=self.df)

if __name__ == "__main__":
    df = pd.read_csv("train.csv")
    
    df.dropna(subset=['Age'],inplace=True)
    df['fare_group']=pd.qcut(df['Fare'],10,range(1,11))
    print(df.head())




    x = exploratory_analysis(df['Age'])
    y=relation(df)
    
   


    x.visualistion()
    y.barplots()


