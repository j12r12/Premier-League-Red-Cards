import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

### Functions ### 

def best_fit(x, y):

    """
    Function to manually create a line of best fit or linear regression line for a given dataset. 
    """
    
    xmean = sum(x)/len(x)
    ymean = sum(y)/len(y)
    n = len(x)
    
    numerator = sum([i*j for i,j in zip(x,y)]) - (n * xmean * ymean)
    denominator = sum([i**2 - xmean for i in x])
    
    b = numerator/denominator
    a = ymean - (b * xmean)
    
    yfit = [a+b*xi for xi in x]
    
    return yfit
    

def line_graph(dataset, save_name, title, figsize=[12,8], style="fivethirtyeight"):

    """
    Function to create a standard line graph (including a linear regression line from the best_fit function.
    """
    
    yfit = best_fit([i for i in range(1,11)], dataset)
    
    plt.style.use(style)
    
    fig, ax = plt.subplots(figsize=figsize)
    ax.plot(dataset, label="Red Cards")
    ax.plot(yfit, label="Line of Best Fit")
    ax.set_title(title)
    ax.legend()
    ax.set_ylabel("Red Cards")
    plt.xticks(rotation=45)
    plt.savefig(save_name)
    plt.show()
    
    
def normal_curve(vline_yes=False, z=0, title=""):

    """
    Function to create normal curve plots and add vertical lines showing location of z-value for given observation.
    """
    
    plt.style.use("seaborn-poster")
    
    xrange = np.arange(-10, 10, 0.01)
    yall = norm.pdf(xrange, 0, 1)
    
    fig, ax = plt.subplots(figsize=[12,8])
    
    ax.plot(xrange, yall)
    ax.fill_between(xrange, yall, 0, alpha=0.2, color="b")
    
    y_first = norm.pdf(np.arange(-1,1,0.01), 0, 1)
    y_second_left = norm.pdf(np.arange(-2,-1,0.01),0,1)
    y_second_right = norm.pdf(np.arange(1,2,0.01),0,1)
    y_third_left = norm.pdf(np.arange(-4,-2,0.01),0,1)
    y_third_right = norm.pdf(np.arange(2,4,0.01),0,1)
    ax.fill_between(np.arange(-1,1,0.01), y_first, 0, alpha=0.2, color="b")
    ax.fill_between(np.arange(-2,-1,0.01),y_second_left,0,alpha=0.3,color="g")
    ax.fill_between(np.arange(1,2,0.01),y_second_right,0,alpha=0.3,color="g")
    ax.fill_between(np.arange(-4,-2,0.01),y_third_left,0,alpha=0.3,color="y")
    ax.fill_between(np.arange(2,4,0.01),y_third_right,0,alpha=0.3,color="y")
    
    if vline_yes:
        ax.vlines(z, ymin=0, ymax=norm.sf(abs(z))*1.98, color="r", linestyle="--")
        
        
    plt.xlim([-4,4])
    ax.set_xlabel("# Standard Deviations from the Mean")
    ax.set_title(title)
    plt.savefig(f"{z}.png")
    plt.show()
    
