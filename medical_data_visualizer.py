import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import the data from medical_examination.csv and assign it to the df variable
df = pd.read_csv("./medical_examination.csv")
df.head()
# Add 'overweight' column
BMI = df['weight']/((df['height']/100)**2)
df['overweight'] = (BMI>25).astype(int)
df

df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df["cholesterol"].describe()
df["cholesterol"].unique()
df['gluc'] = (df['gluc'] > 1).astype(int)
df["gluc"].describe()
df["gluc"].unique()

def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc' , 'smoke', 'alco', 'active', 'overweight'])



    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    df_cat = df_cat.rename(columns={'value': 'variable_value'}) #this code is necesary in order to help the catplot to recognize correctly the variables

    

    # Draw the catplot with 'sns.catplot()'

    fig= sns.catplot(x='variable', y='total', hue='variable_value', col='cardio', data=df_cat, kind='bar')

    # Get the figure for the output
    fig = fig.fig
    
    plt.close(fig)

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig

draw_cat_plot()

def draw_heat_map():
    # Clean the data
    df_heat = df.loc[
        (df['ap_lo'] <= df['ap_hi']) & 
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height']<= df['height'].quantile(0.975)) &
        (df['weight']>= df['weight'].quantile(0.025)) &
        (df['weight']<=df['weight'].quantile(0.975))
    ]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 12))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', linewidths=.5, vmax=.3, center=0)
    plt.close(fig)
    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig

draw_heat_map()


    # 16
    fig.savefig('heatmap.png')
    return fig
