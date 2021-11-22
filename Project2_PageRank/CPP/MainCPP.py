import numpy as np
import pandas as pd

def clean_list(list_):
    list_ = list_.replace(',', '","')
    list_ = list_.replace('[', '["')
    list_ = list_.replace(']', '"]')
    return list_

def boolean_df(lists_links, unique_links):
    bool_dict = {}
    # Loop through all the tags
    for i, item in enumerate(unique_links):
        # Apply boolean mask that returns a True-False list of whether a tag is in a taglist
        bool_dict[item] = lists_links.apply(lambda x: item in x)

    return pd.DataFrame(bool_dict)

def main():
    # Print options for panda
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)

    #Read in list.csv
    df = pd.read_csv('Data\listTest.csv')

    df["Outlink"] = df["Outlink"].apply(eval)
    df["Outlink"].dtype
    #Clean outlinks column
    clean_list(df)

    #Get all unique links using value
    unique_links = df["Link"].value_counts()
    #print(unique_links)

    #Return bool if link points to outlink
    df_bool = pd.DataFrame(boolean_df(df["Outlink"], unique_links.keys()))
    print(df_bool)

    #corr() correlates links
    df_corr = df_bool.corr()
    # print(fruits_corr)

    #Change bool to int
    df_int = df_bool.astype(int)

    #Numpy dot matrix
    # n = 1
    # df_freq_mat = np.dot(1 / n, df_int)
    # df_freq = pd.DataFrame(df_freq_mat, columns=unique_links.keys(), index=unique_links.keys())
    # print(df_freq)

    #Count of Links n
    vector = np.array(df["Count"])
    df_freq_mat = np.dot(1 , df_int)
    # Links 1/n
    df_freq_mat = (df_freq_mat / vector[np.newaxis])
    df_freq = pd.DataFrame(df_freq_mat, columns=unique_links.keys(), index=unique_links.keys())
    # print(df_freq)

    #Matrix multiplication
    b = np.array([1/3, 1/3, 1/3]).reshape(3,1)
    #Mulitplies by vector of outlink count, reshapes into column Nx1
    df_div = np.sum(np.dot(df_freq_mat, b), axis=1).reshape((3,1))
    print("Iteration 1:")
    #print(df_div1)
    print(pd.DataFrame(df_div))
    df_div2 = np.sum(np.dot(df_freq_mat, df_div), axis=1)
    print("Iteration 2:")
    print(pd.DataFrame(df_div2))

    #Sort matrix
    df_final = pd.DataFrame(df_div2, unique_links.keys()).stack().sort_values().reset_index()
    #Keeps only top 100 links
    df_final =  df_final.head(100)
    #print(df_final)
    #Writes dataframe to csv
    df_final.to_csv('Data\listRanked.csv', header=['Link', 'Delete', 'PageRank'])
    #Reopens csv to name index column and remove 'Delete' column
    df_csv = pd.read_csv('Data\listRanked.csv')
    df_csv.drop('Delete', axis=1, inplace=True)
    df_csv.to_csv('Data\listRanked.csv', index=False, header=['Rank', 'Link', 'PageRank'])


main()
