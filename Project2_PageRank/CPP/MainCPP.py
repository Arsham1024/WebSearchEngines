import numpy as np
import pandas as pd

# Clean list for Outlinks
def clean_list(list_):
    list_ = list_.replace(',', '","')
    list_ = list_.replace('[', '["')
    list_ = list_.replace(']', '"]')
    return list_

# Check if outlink has correlation with unique link
def boolean_df(lists_links, unique_links):
    bool_dict = {}
    # Loop through all the tags
    for i, item in enumerate(unique_links):
        # Apply boolean mask that returns a True-False list of whether a tag is in a taglist
        bool_dict[item] = lists_links.apply(lambda x: item in x)

    return pd.DataFrame(bool_dict)

def main():
    # Print options for pandas
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)

    # Read in list.csv
    df = pd.read_csv('Data\list.csv', ).drop_duplicates(subset='Link')
    # Remove link if there are no outlinks
    df = df.loc[df["Outlink"] != '[]']
    # Grab number of rows
    index = df.index
    number_of_rows = len(index)

    # Clean and separate outlinks column
    df["Outlink"] = df["Outlink"].apply(eval)
    df["Outlink"].dtype
    print(clean_list(df))

    # Get all unique links using value
    unique_links = df["Link"].value_counts()

    # Return bool if link points to outlink
    df_bool = pd.DataFrame(boolean_df(df["Outlink"], unique_links.keys()))
    #print(df_bool)

    # corr() correlates links
    df_corr = df_bool.corr()
    #print(df_corr)

    # Change bool to int
    df_int = df_bool.astype(int)
    print(df_int)

    # Get count of outlinks that match with unique links
    df_count = df_int.sum(axis=0)
    print(df_count)

    # Matrix ------------------------------------------------------------------------------------------------------------

    # Divides links based on number of outlinks
    vector = np.array(df_count)
    df_freq_mat = np.dot(1, df_int)
    # Outlinks 1/n
    df_freq_mat = (df_freq_mat / vector[np.newaxis])
    df_freq = pd.DataFrame(df_freq_mat, columns=unique_links.keys(), index=unique_links.keys())
    # print(df_freq)

    # Create vector filled with 1's, divide by vector with number of total unique links
    base_vector = np.full((number_of_rows, 1), 1, dtype=int)
    vector = np.full((number_of_rows, 1), number_of_rows, dtype=int)
    vector = base_vector / vector

    # Multiplies by vector of outlink count, reshapes into column Nx1
    #df_div1 = np.sum(np.dot(df_freq_mat, vector), axis=1).reshape((number_of_rows, 1))
    df_div1 = ((0.15 / number_of_rows) + (1 - 0.15)) * (np.sum(np.dot(df_freq_mat, vector), axis=1).reshape((number_of_rows, 1)))
    print("Iteration 1:")
    print(df_div1)
    print(pd.DataFrame(df_div1))
    #df_div2 = np.sum(np.dot(df_freq_mat, df_div1), axis=1)
    df_div2 = ((0.15 / number_of_rows) + (1 - 0.15)) * (np.sum(np.dot(df_freq_mat, df_div1), axis=1))

    print("Iteration 2:")
    print(pd.DataFrame(df_div2))
    ran_surf1 = df_div2 / ((0.15 / number_of_rows) + (1 - 0.15))
    ran_surf2 = ran_surf1 / ((0.15 / number_of_rows) + (1 - 0.15))

    # Sort matrix
    #df_final = pd.DataFrame(df_div1, unique_links.keys()).stack().sort_values(ascending=False).reset_index()
    df_final = pd.DataFrame(ran_surf2, unique_links.keys()).stack().sort_values(ascending=False).reset_index()
    # Keeps only top 100 links
    #df_final = df_final.head(100)
    print(df_final)
    # Writes dataframe to csv
    df_final.to_csv('Data\listRanked.csv', header=['Link', 'Delete', 'PageRank'])
    # Reopens csv to name index column and remove 'Delete' column
    df_csv = pd.read_csv('Data\listRanked.csv')
    df_csv.drop('Delete', axis=1, inplace=True)
    df_csv.to_csv('Data\listRanked.csv', index=False, header=['Rank', 'Link', 'PageRank'])


    #creating a csv file for the top 100 websites
    df_hundred = pd.DataFrame(ran_surf2, unique_links.keys()).stack().sort_values(ascending=False).reset_index()
    # Keeps only top 100 links
    df_hundred = df_final.head(100)
    #print(df_final)
    # Writes dataframe to csv
    df_hundred.to_csv('Data\list100.csv', header=['Link', 'Delete', 'PageRank'])
    # Reopens csv to name index column and remove 'Delete' column
    df_csv = pd.read_csv('Data\list100.csv')
    df_csv.drop('Delete', axis=1, inplace=True)
    df_csv.to_csv('Data\list100.csv', index=False, header=['Rank', 'Link', 'PageRank'])

main()
