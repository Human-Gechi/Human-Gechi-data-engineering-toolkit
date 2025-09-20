import pandas as pd # Library for data manipulation

def load_data(path): #Loading function
    """Load data from various file formats"""
    if path.endswith('.csv'):
        return pd.read_csv(path)
    elif path.endswith('.json'):
        #For Loop for several json formats
        orientations = ["records", "values", "split", "columns"]
        for orient in orientations:
            try:
                return pd.read_json(path, orient=orient)
            except ValueError: # Raising ValueError if there exist any orientaion format asides the above listed
                continue
        raise ValueError("Could not read JSON file with any orientation")
    elif path.endswith('.xlsx'):
        return pd.read_excel(path)
    elif path.endswith('.parquet'):
        return pd.read_parquet(path)
    else:
        raise ValueError("Unsupported file format")

def remove_duplicates_and_save(data): #Function for duplicates removal
    """Remove duplicates and save back to file"""
    before = len(data) #Length of DataFrame before duplicates were deleted
    clean_data = data.drop_duplicates(keep='first', ignore_index=True)
    after = len(clean_data) #Length of DataFrame before duplicates were deleted
    print(f"Removed {before - after} duplicate rows.") #Printing number of dremoved duplicated columns

    if data.empty:
        print("Warning: Dataframe is empty after removing duplicates")
    elif data.duplicated().sum()==0:
        print("Dataframe has no duplicate values")

    return clean_data.head()

def convert_data_types(data): #Function to convert data types
    """ Converting data types adn save back to file"""
    data.info()
    try:
        columns=input("Enter the column name you wish to convert the data type: ")
        dtype = input("Enter dtype: ")
        data[columns] = data[columns].astype(dtype, errors="ignore")
    except KeyError:
        print("Enter a valid column name and dtype")