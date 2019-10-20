def same_rows_number(df1,df2):
    return df1.shape[0]==df2.shape[0]

def duplicated(df,column):
    duplicateRowsDF = df[df.duplicated([column])]
    if duplicateRowsDF.shape[0]==0:
        return True
    else:
        print("Duplicate Rows based on a single column are:", duplicateRowsDF, sep='\n')
        return False

def isna_test(df):
    return not df.isnull().values.any()
