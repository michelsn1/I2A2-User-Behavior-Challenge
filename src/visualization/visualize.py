import seaborn as sns
import matplotlib.pyplot as plt



def two_d_density_plot(df,column1='x',column2='y'):
    sns.jointplot(df[column1], df[column2],kind='kde')
    sns.jointplot(df[d'subje'][column1], df[column2],kind='kde')
    plt.show()
