# standard imports
import numpy as np
import pandas as pd
# visualization
import seaborn as sns
import matplotlib.pyplot as plt
# model
import cluster
from sklearn.cluster import KMeans


def initial_visuals(df):
    plt.figure(figsize=[15,15])
    plt.subplot(421)
    sns.boxplot(df.fixed_acidity, df.index)
    plt.subplot(422)
    sns.barplot(df.fixed_acidity, df.index)
    plt.subplot(423)
    sns.boxplot(df.volatile_acidity, df.index)
    plt.subplot(424)
    sns.barplot(df.volatile_acidity, df.index)
    plt.subplot(425)
    sns.boxplot(df.citric_acid, df.index)
    plt.subplot(426)
    sns.barplot(df.citric_acid, df.index)
    plt.subplot(427)
    sns.boxplot(df.residual_sugar, df.index)
    plt.subplot(428)
    sns.barplot(df.residual_sugar, df.index)
    plt.tight_layout()
    plt.show()
    plt.figure(figsize=[15,15])
    plt.subplot(421)
    sns.boxplot(df.chlorides, df.index)
    plt.subplot(422)
    sns.barplot(df.chlorides, df.index)
    plt.subplot(423)
    sns.boxplot(df.free_sulfur_dioxide, df.index)
    plt.subplot(424)
    sns.barplot(df.free_sulfur_dioxide, df.index)
    plt.subplot(425)
    sns.boxplot(df.total_sulfur_dioxide, df.index)
    plt.subplot(426)
    sns.barplot(df.total_sulfur_dioxide, df.index)
    plt.subplot(427)
    sns.boxplot(df.density, df.index)
    plt.subplot(428)
    sns.barplot(df.density, df.index)
    plt.tight_layout()
    plt.show()
    plt.figure(figsize=[15,15])
    plt.subplot(421)
    sns.boxplot(df.pH, df.index)
    plt.subplot(422)
    sns.barplot(df.pH, df.index)
    plt.subplot(423)
    sns.boxplot(df.sulphates, df.index)
    plt.subplot(424)
    sns.barplot(df.sulphates, df.index)
    plt.subplot(425)
    sns.boxplot(df.alcohol, df.index)
    plt.subplot(426)
    sns.barplot(df.alcohol, df.index)
    plt.subplot(427)
    sns.boxplot(df.quality, df.index)
    plt.subplot(428)
    sns.barplot(df.quality, df.index)
    plt.tight_layout()
    plt.show()
    plt.figure(figsize=[15,15])
    plt.subplot(421)
    sns.scatterplot(df.fixed_acidity, df.index)
    plt.subplot(422)
    sns.scatterplot(df.volatile_acidity, df.index)
    plt.subplot(423)
    sns.scatterplot(df.citric_acid, df.index)
    plt.subplot(424)
    sns.scatterplot(df.residual_sugar, df.index)
    plt.subplot(425)
    sns.scatterplot(df.chlorides, df.index)
    plt.subplot(426)
    sns.scatterplot(df.free_sulfur_dioxide, df.index)
    plt.subplot(427)
    sns.scatterplot(df.total_sulfur_dioxide, df.index)
    plt.subplot(428)
    sns.scatterplot(df.density, df.index)
    plt.tight_layout()
    plt.show()
    plt.figure(figsize=[15,15])
    plt.subplot(421)
    sns.scatterplot(df.pH, df.index)
    plt.subplot(422)
    sns.scatterplot(df.sulphates, df.index)
    plt.subplot(423)
    sns.scatterplot(df.alcohol, df.index)
    plt.subplot(424)
    sns.scatterplot(df.quality, df.index)
    plt.tight_layout()
    plt.show()

def qual_x_alc(train):
    # quality x alcohol for all wine
    plt.figure(figsize=[10,10])
    plt.subplot(321)
    plt.title('Wine Quality x %Alcohol for All Wines')
    sns.barplot(data=train, x='quality_bins', y='alcohol', palette="rocket")
    plt.subplot(322)
    plt.title('Wine Quality x %Alcohol for All Wines')
    sns.boxplot(data=train, x='quality_bins', y='alcohol', palette="rocket")
    # red wine
    plt.subplot(323)
    plt.title('Wine Quality x %Alcohol for Red Wines')
    sns.barplot(data=train[train['type']=='red'], x='quality_bins', y='alcohol', palette='gist_heat')
    plt.subplot(324)
    plt.title('Wine Quality x %Alcohol for Red Wines')
    sns.boxplot(data=train[train['type']=='red'], x='quality_bins', y='alcohol', palette='gist_heat')
    # white wine
    plt.subplot(325)
    plt.title('Wine Quality x %Alcohol for White Wines')
    sns.barplot(data=train[train['type']=='white'], x='quality_bins', y='alcohol', palette='Wistia')
    plt.subplot(326)
    plt.title('Wine Quality x %Alcohol for White Wines')
    sns.boxplot(data=train[train['type']=='white'], x='quality_bins', y='alcohol', palette='Wistia')
    plt.tight_layout()
    plt.show()

def qual_x_rs(train):
    plt.figure(figsize=[10,10])
    plt.subplot(321)
    plt.title('Residual Sugar x Quality for All Wine')
    sns.barplot(data=train, x='quality_bins', y='residual_sugar', palette="rocket")
    plt.subplot(322)
    plt.title('Residual Sugar x Quality for All Wine')
    sns.boxplot(data=train, x='quality_bins', y='residual_sugar', palette="rocket")
    # red wine
    plt.subplot(323)
    plt.title('Residual Sugar x Quality for Red Wine')
    sns.barplot(data=train[train['type']=='red'], x='quality_bins', y='residual_sugar', palette="rocket")
    plt.subplot(324)
    plt.title('Residual Sugar x Quality for Red Wine')
    sns.boxplot(data=train[train['type']=='red'], x='quality_bins', y='residual_sugar', palette="rocket")
    # white wine
    plt.subplot(325)
    plt.title('Residual Sugar x Quality for White Wine')
    sns.barplot(data=train[train['type']=='white'], x='quality_bins', y='residual_sugar', palette="rocket")
    plt.subplot(326)
    plt.title('Residual Sugar x Quality for White Wine')
    sns.boxplot(data=train[train['type']=='white'], x='quality_bins', y='residual_sugar', palette="rocket")
    plt.tight_layout()
    plt.show()
    # identify residual sugar range
    print(f' Min Residual Sugar Value: {train.residual_sugar.min()}')
    print(f' Max Residual Sugar Value: {train.residual_sugar.max()}')

def qual_x_rs_wo_outliers(train):
    # after outliers
    plt.figure(figsize=[10,10])
    plt.subplot(321)
    plt.title('Residual Sugar x Quality for All Wine \nw/o Outliers')
    sns.barplot(data=train, x='quality_bins', y='residual_sugar', palette="rocket")
    plt.subplot(322)
    plt.title('Residual Sugar x Quality for All Wine \nw/o Outliers')
    sns.boxplot(data=train, x='quality_bins', y='residual_sugar', palette="rocket")
    # red wine
    plt.subplot(323)
    plt.title('Residual Sugar x Quality for Red Wine \nw/o Outliers')
    sns.barplot(data=train[train['type']=='red'], x='quality_bins', y='residual_sugar', palette="rocket")
    plt.subplot(324)
    plt.title('Residual Sugar x Quality for Red Wine \nw/o Outliers')
    sns.boxplot(data=train[train['type']=='red'], x='quality_bins', y='residual_sugar', palette="rocket")
    # white wine
    plt.subplot(325)
    plt.title('Residual Sugar x Quality for White Wine \nw/o Outliers')
    sns.barplot(data=train[train['type']=='white'], x='quality_bins', y='residual_sugar', palette="rocket")
    plt.subplot(326)
    plt.title('Residual Sugar x Quality for White Wine \nw/o Outliers')
    sns.boxplot(data=train[train['type']=='white'], x='quality_bins', y='residual_sugar', palette="rocket")
    plt.tight_layout()
    plt.show()

def fsd_x_ph(train):
    plt.figure(figsize=[10,10])
    plt.subplot(321)
    plt.title('Free Sulfur Dioxide Distribution Values')
    train.free_sulfur_dioxide.hist(color='lightsalmon', alpha = 0.7)
    plt.subplot(321)
    train[train['type']== 'white'].free_sulfur_dioxide.hist(color='rosybrown', alpha = 0.7)
    plt.subplot(321)
    train[train['type']== 'red'].free_sulfur_dioxide.hist(color='maroon', alpha = 0.9)
    plt.subplot(322)
    plt.title('pH Distribution Values')
    train.pH.hist(color='lightsalmon', alpha = 0.7)
    plt.subplot(322)
    train[train['type']== 'white'].pH.hist(color='rosybrown', alpha = 0.7)
    plt.subplot(322)
    train[train['type']== 'red'].pH.hist(color='maroon', alpha = 0.9)
    plt.subplot(323)
    plt.title('Free Sulfer Dioxide x Wine Quality Distribution Values')
    sns.boxplot(data=train, x='quality_bins', y='free_sulfur_dioxide', palette='rocket')
    plt.subplot(324)
    plt.title('pH x Wine Quality Distributions Values')
    sns.boxplot(data=train, x='quality_bins', y='pH', palette='rocket')
    plt.subplot(325)
    plt.title('Free Sulfer Dioxide x pH')
    sns.scatterplot(data=train, x='pH', y='free_sulfur_dioxide', color='chocolate')
    plt.tight_layout()
    plt.show()
    # min and max values for free sulfur dioxide and pH
    print(f'Free Sulfur Dioxide Min Value: {train.free_sulfur_dioxide.min()}')
    print(f'Free Sulfur Dioxide Max Value: {train.free_sulfur_dioxide.max()}')
    print('-'*50)
    print(f'pH Min Value: {train.pH.min()}')
    print(f'pH Max Value: {train.pH.max()}')
    
def fsd_x_ph_wo_fsd_outlier(train):
    # after the free sulfur dioxide outlier has been removed
    plt.figure(figsize=[15,15])
    plt.subplot(421)
    plt.title('Free Sulfur Dioxide Distibution Values \nw/o High FSD Val')
    train.free_sulfur_dioxide.hist(color='lightsalmon', alpha = 0.7)
    plt.subplot(421)
    train[train['type']== 'white'].free_sulfur_dioxide.hist(color='rosybrown', alpha = 0.7)
    plt.subplot(421)
    train[train['type']== 'red'].free_sulfur_dioxide.hist(color='maroon', alpha = 0.9)
    plt.subplot(422)
    plt.title('pH Distribution Values \nw/o High FSD Val')
    train.pH.hist(color='lightsalmon', alpha = 0.7)
    plt.subplot(422)
    train[train['type']== 'white'].pH.hist(color='rosybrown', alpha = 0.7)
    plt.subplot(422)
    train[train['type']== 'red'].pH.hist(color='maroon', alpha = 0.9)
    plt.subplot(423)
    plt.title('Free Sulfer Dioxide x Wine Quality Distribution Values \nw/o High FSD Val')
    sns.boxplot(data=train, x='quality_bins', y='free_sulfur_dioxide', palette='rocket')
    plt.subplot(424)
    plt.title('pH x Wine Quality Distributions Values \nw/o High FSD Val')
    sns.boxplot(data=train, x='quality_bins', y='pH', palette='rocket')
    plt.subplot(425)
    plt.title('Free Sulfer Dioxide x pH \nw/o High FSD Val')
    sns.scatterplot(data=train, x='pH', y='free_sulfur_dioxide', hue='quality_bins', palette='rocket')
    plt.subplot(426)
    plt.title('Free Sulfur Dioxide x pH \nw/o High FSD Val')
    sns.scatterplot(data=train, x='pH', y='free_sulfur_dioxide', hue='type', palette='rocket')
    plt.subplot(427)
    plt.title('Free Sulfer Dioxide x pH \nw/o High FSD Val')
    sns.scatterplot(data=train, x='pH', y='free_sulfur_dioxide', color='chocolate')
    plt.tight_layout()
    plt.show()
    # min and max values for free sulfur dioxide and pH
    print(f'Free Sulfur Dioxide Min Value: {train.free_sulfur_dioxide.min()}')
    print(f'Free Sulfur Dioxide Max Value: {train.free_sulfur_dioxide.max()}')
    print('-'*50)
    print(f'pH Min Value: {train.pH.min()}')
    print(f'pH Max Value: {train.pH.max()}')
       
def fsd_x_ph_wo_outliers(train):
    # after removing outliers
    plt.figure(figsize=[15,15])
    plt.subplot(421)
    plt.title('Free Sulfur Dioxide Distibution Values \nw/o Outliers')
    train.free_sulfur_dioxide.hist(color='lightsalmon', alpha = 0.7)
    plt.subplot(421)
    train[train['type']== 'white'].free_sulfur_dioxide.hist(color='rosybrown', alpha = 0.7)
    plt.subplot(421)
    train[train['type']== 'red'].free_sulfur_dioxide.hist(color='maroon', alpha = 0.9)
    plt.subplot(422)
    plt.title('pH Distribution Values \nw/o Outliers')
    train.pH.hist(color='lightsalmon', alpha = 0.7)
    plt.subplot(422)
    train[train['type']== 'white'].pH.hist(color='rosybrown', alpha = 0.7)
    plt.subplot(422)
    train[train['type']== 'red'].pH.hist(color='maroon', alpha = 0.9)
    plt.subplot(423)
    plt.title('Free Sulfer Dioxide x Wine Quality Distribution Values \nw/o Outliers')
    sns.boxplot(data=train, x='quality_bins', y='free_sulfur_dioxide', palette='rocket')
    plt.subplot(424)
    plt.title('pH x Wine Quality Distributions Values \nw/o Outliers')
    sns.boxplot(data=train, x='quality_bins', y='pH', palette='rocket')
    plt.subplot(425)
    plt.title('Free Sulfer Dioxide x pH \nw/o Outliers')
    sns.scatterplot(data=train, x='pH', y='free_sulfur_dioxide', hue='quality_bins', palette='rocket')
    plt.subplot(426)
    plt.title('Free Sulfur Dioxide x pH \nw/o Outliers')
    sns.scatterplot(data=train, x='pH', y='free_sulfur_dioxide', hue='type', palette='rocket')
    plt.subplot(427)
    plt.title('Free Sulfer Dioxide x pH \nw/o Outliers')
    sns.scatterplot(data=train, x='pH', y='free_sulfur_dioxide', color='chocolate')
    sns.relplot(data=train, x='pH', y='free_sulfur_dioxide', col='quality_bins', hue='type', palette='rocket')
    sns.relplot(data=train, x='pH', y='free_sulfur_dioxide', col='type', hue='quality_bins', palette='rocket')
    plt.tight_layout()
    plt.show()
    # min and max values for free sulfur dioxide and pH
    print(f'Free Sulfur Dioxide Min Value: {train.free_sulfur_dioxide.min()}')
    print(f'Free Sulfur Dioxide Max Value: {train.free_sulfur_dioxide.max()}')
    print('-'*50)
    print(f'pH Min Value: {train.pH.min()}')
    print(f'pH Max Value: {train.pH.max()}')
     
def rw_fsd_x_ph(train):
    # graphs for red and white wine individually
    plt.figure(figsize=[15,10])
    plt.subplot(121)
    plt.title('FSD x pH \n for Red Wine')
    sns.scatterplot(data=train[train['type'] == 'red'], x='pH', y='free_sulfur_dioxide', hue='quality_bins', palette='rocket')
    plt.subplot(122)
    plt.title('FSD x pH \n for White Wine')
    sns.scatterplot(data=train[train['type'] == 'white'], x='pH', y='free_sulfur_dioxide', hue='quality_bins', palette='rocket')
    plt.tight_layout()
    rel = sns.relplot(data=train[train['type'] == 'red'], x='pH', y='free_sulfur_dioxide', col='quality_bins', hue='quality_bins', palette='rocket')
    rel.fig.suptitle('FSD x pH relplot for Red Wine')
    plt.tight_layout()
    rel1 = sns.relplot(data=train[train['type'] == 'white'], x='pH', y='free_sulfur_dioxide', col='quality_bins', hue='quality_bins', palette='rocket')
    rel1.fig.suptitle('FSD x pH relplot for White Wine')
    plt.tight_layout()
    plt.show()
    
    
def cluster_vis(df):
    plt.figure(figsize=[10,5])
    plt.subplot(121)
    plt.title('Clustered % Alcohol x Wine Quality')
    sns.scatterplot(data=df, x='quality', y='alcohol', hue='cluster', palette='rocket')
    plt.subplot(122)
    plt.title('Clustered % Alcohol x Wine Quality')
    sns.barplot(data=df, x='quality', y='alcohol', hue='cluster', palette='rocket')
    plt.tight_layout()
    plt.show()
    
def centroid_cluster(df):
    kmean = KMeans(n_clusters=3)
    kmean.fit(df[['quality', 'alcohol']])
    df['cluster'] = kmean.labels_
    centroids = pd.DataFrame(kmean.cluster_centers_, columns=['quality', 'alcohol'])
    colors = ['palevioletred', 'lightsalmon', 'maroon']
    plt.figure(figsize=(14, 9))
    for i, (cluster, subset) in enumerate(df.groupby('cluster')):
        plt.scatter(subset['quality'], subset['alcohol'], label='cluster ' + str(cluster), alpha=.6, c=colors[i])
    centroids.plot.scatter(y='alcohol', x='quality', c='black', marker='x', s=700, ax=plt.gca(), label='centroid')
    plt.legend()
    plt.title('Unscaled Clusters and Cluster Centroids \nfor % Alcohol x Wine Quality')
    plt.xlabel('Wine Quality')
    plt.ylabel('% Alcohol')
    plt.show()
    
def inertia_change(df):
    with plt.style.context('seaborn-whitegrid'):
        plt.figure(figsize=(9, 6))
    pd.Series({k: KMeans(k).fit(df).inertia_ for k in range(2, 12)}).plot(marker='x')
    plt.xticks(range(2, 12))
    plt.xlabel('k')
    plt.ylabel('inertia')
    plt.title('Change in inertia as k increases')
    colors = ['palevioletred', 'lightsalmon', 'maroon', 'thistle', 'peru']
    # create a figure with subplots for each value of k
    fig, axs = plt.subplots(2, 2, figsize=(13, 13), sharex=True, sharey=True)
    # iterate over the subplots and create a scatter plot for each value of k
    for ax, k in zip(axs.ravel(), range(2, 6)):
        clusters = KMeans(k).fit(df).predict(df)
        ax.scatter(df.quality, df.alcohol, c=[colors[c] for c in clusters])
        ax.set(title='k = {}'.format(k), xlabel='quality', ylabel='alcohol')
    fig.suptitle('Variation in k Cluster for\n % Alcohol x Wine Quality', fontsize=20)
    plt.show()