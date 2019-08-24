def get_mean(list_1):
    mean1 = np.mean(list_1)
    return (print ("Mean of the dataset is: ",mean1))

def get_median(list_1):
    median1 = np.median(list_1)
    return (print ("Median of the dataset is: ",median1))

def get_skewness(list_1):
    SD1 = getSD(list_1)
    mean2 = get_mean(list_1)
    median2 = get_median(list_1)
    skewness1 = (3*mean2*median2)/SD1
    if skewness1 == 0:
        return ("Dataset is Normal/Gaussian Distribution as skewness is ",skewness1)
    if skewness1 > 0:
        return ("Dataset is Left Skewed as skewness is ",skewness1)
    if skewness1 < 0:
        return ("Dataset is Right Skewed as skewness is ",skewness1)