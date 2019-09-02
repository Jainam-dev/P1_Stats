import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import itertools

class bivariate_analysis():
    def __init__(self,df):
        self.df=df

    def quant_categ(self):
        self.categorical = []
        self.quantitative = []
        self.quantitative_nonobject=[]
        for i in self.df.columns:
            if self.df[i].nunique()<5:
                self.categorical.append(i)
            elif self.df[i].dtype!='object':
                self.quantitative_nonobject.append(i)
            else:
                self.quantitative.append(i)
    
    def bivariate_visualisation(self):
        self.quant_categ()
        self.c=list(itertools.combinations(self.quantitative_nonobject,2))
        
        fig=plt.figure(figsize=(15,15))


        for num,i in enumerate(self.c):
    
            plt.subplot(len(self.c)/2,len(self.c)/2,num+1)
            plt.scatter(self.df[i[0]], self.df[i[1]])
            plt.title(i)

        plt.tight_layout()
        plt.show() 

        self.cq= [self.categorical] + [self.quantitative_nonobject] 
        self.cq= list(itertools.product(*self.cq))  
        fig=plt.figure(figsize=(15,15))            
        for num,i in enumerate(self.cq):
            plt.subplot(len(self.cq)/4,len(self.cq)/5,num+1)
            sns.barplot(x=df[i[0]],y=df[i[1]],data=df)
            #plt.title(i)
        fig.tight_layout()
        plt.show()
            

            



    







class univariate_analysis():
    def __init__(self,df):
        self.df = df

    def quant_categ(self):
        self.categorical = []
        self.quantitative = []

        for i in self.df.columns:
            if self.df[i].nunique()<5:
                self.categorical.append(i)
            else:
                self.quantitative.append(i)

    def get_mean(self,arr):
        mean1 = np.mean(arr)
        return mean1

    def get_median(self,arr):
        median1 = np.median(arr)
        return median1

    def getSD(self,arr):
        return np.std(arr)


    def getQ1(self,arr):
        return np.percentile(arr,25)

    def getQ3(self,arr):
        return np.percentile(arr,75)

    def getIQR(self,arr):
        q1=np.percentile(arr,25)
        q3=np.percentile(arr,75)
        iqr=q3-q1
        return iqr
    
    def get_skewness(self,arr):
        SD1 = self.getSD(arr)
        mean2 = self.get_mean(arr)
        median2 = self.get_median(arr)
        skewness1 = (3*(mean2-median2))/SD1
        if skewness1 == 0:
            return ("Dataset is Normal/Gaussian Distribution as skewness is ",skewness1)
        if skewness1 > 0:
            return ("Dataset is Right Skewed as skewness is ",skewness1)
        if skewness1 < 0:
            return ("Dataset is Left Skewed as skewness is ",skewness1)
    
    def quants_stats(self):
        self.quant_categ()
        for num,i in enumerate(self.quantitative):
            if self.df[i].dtype!='object':
                self.df[i].dropna(inplace=True)
                print("Mean of " + i + " is:", np.mean(self.df[i]))
                print("Median of " + i + " is:",np.median(self.df[i]))
                print("Std of " + i + " is:",np.std(self.df[i]))
                print("Q1 of " + i + " is:",np.percentile(self.df[i],25))
                print("Q3 of " + i + " is:",np.percentile(self.df[i],75))
                print("IQR of " + i + " is:",(np.percentile(self.df[i],75)-np.percentile(self.df[i],25)))
                print("Skewness of " + i + " is:",self.get_skewness(df[i]))
            else:
                print(i + " is of object Type")


    def  quantative_visualisation(self):
        self.quants_stats()
        fig=plt.figure(figsize=(20,20))
        for num,i in enumerate(self.quantitative):
            if self.df[i].dtype!='object':
                self.df[i].dropna(inplace=True)
        
                ax=plt.subplot(len(self.quantitative),1,num+1)
                sns.distplot(self.df[i],ax=ax,kde=False,hist=True)
                ax.axvline(self.df[i].mean(), color='r', linestyle='--')
                ax.axvline(self.df[i].median(), color='g', linestyle='-')
                ax.legend({'Mean':self.df[i].mean(),'Median':self.df[i].median()})
                plt.title(i)
        plt.show()

        fig=plt.figure(figsize=(20,20))
        for num,i in enumerate(self.quantitative):
            if self.df[i].dtype!='object':
                self.df[i].dropna(inplace=True)
        
                ax=plt.subplot(len(self.quantitative),1,num+1)
                sns.boxplot(self.df[i],ax=ax)
        
                plt.title(i)
        
        plt.show()

    
    
        fig=plt.figure(figsize=(20,20))
        for num,i in enumerate(self.categorical):
            self.df[i].dropna(inplace=True)
            plt.subplot(len(self.categorical),1,num+1)
            plt.title("Pie Chart for Column: "+i, color = 'purple', fontsize=16)
            plt.pie(self.df[i].value_counts(),labels=df[i].unique(),autopct='%.2f',shadow=True)
            plt.legend()

        plt.tight_layout()    
        plt.show()    









if __name__ == "__main__":
    df=pd.read_csv("test.csv")
    x=univariate_analysis(df)
    x.quantative_visualisation()
    y=bivariate_analysis(df)
    y.bivariate_visualisation()

    