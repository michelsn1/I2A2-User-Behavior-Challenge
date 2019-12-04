import os
import csv
import pandas as pd
import src.features.settings as st
import src.features.actions as actions

def processSession1(df, action_file,time_limit):
    #### Mudar aqui para pegar de tempos em tempos
    # Opens a session file containing raw mouse events and creates a file segmented into actions
    # "CSV file structure: record timestamp, timestamp, button, state, x, y "

    # line counter needed for the n_from and n_to fields
    # rows belonging to a segmented action [n_from, n_to]
    counter = 1
    prevrow = None
    n_from = 2
    n_to = 2
    time = 0
    #reader = df.transpose().to_dict().values()
    data = []
    target = df.loc[0,'target']
    for index, row in df.iterrows():
        item = {
        "x": row['x'],
        "y": row['y'],
        "t": row['timestamp'],
        }
        n_to =counter
        data.append(item)

        if item['t']-time >= time_limit:
            n_to = counter
            actions.processPointClickActions(pd.DataFrame(data),target, action_file, n_from, n_to)
            # It starts a new action
            data = []
            n_from = n_to +1
            time=item['t']

    prevrow = row
    n_to = counter
    return


def process_files(df,subject,time_limit=0.3,train_notebook=True):

    if train_notebook:
        filename = '.'+st.ACTION_FILENAME+'_'+subject+'.csv'
    else:
        filename = st.ACTION_FILENAME+'_'+subject+'.csv'
        
    action_file = open(filename, "w")
    action_file.write(st.ACTION_CSV_HEADER)

    processSession1(df, action_file,time_limit)

    action_file.close()
    df2 = pd.read_csv(filename)
    return df2
