import os
import csv
import pandas as pd

import src.features.settings as st
import src.features.actions

def processSession1(df, action_file):
    #### Mudar aqui para pegar de tempos em tempos
    # Opens a session file containing raw mouse events and creates a file segmented into actions
    # "CSV file structure: record timestamp, timestamp, button, state, x, y "

    # line counter needed for the n_from and n_to fields
    # rows belonging to a segmented action [n_from, n_to]
    counter = 1
    prevrow = None
    n_from = 2
    n_to = 2

    reader = df.transpose().to_dict().values()
    data = []
    for row in reader:
        counter = counter + 1

        # Skip duplicates
        if prevrow != None and prevrow == row:
            continue
        # Skip equal timestamps
        # if prevrow != None and row['timestamp'] == prevrow['timestamp']:
        #     continue

        item = {
            "x": row['x'],
            "y": row['y'],
            "t": row['timestamp'],
            "button": row['button'],
            "state": row['state']
        }
        # SCROLLs are not actions
        # therefore are ignored
        if row["button"] == 'Scroll':
            if prevrow != None:
                item['x'] = prevrow['x']
                item['y'] = prevrow['y']
            # continue
        if row['button'] == 'Left' and row['state'] == 'Released':
            # n_to = counter
            # print("Left - Released: "+str(n_from)+"-"+str(n_to))
        # if row['state'] == 'Released':
            data.append(item)
            # is it a short sequence?
            if len(data) <= 2:
                # print(str(n_from)+"--"+str(counter ))
                data = []
                n_from = counter
                continue

            # A Drag Drop Action (4) ends here.
            # It can be a compound action: {MM}*DD - several MM actions followed by a DD action
            if prevrow != None and prevrow['state'] == 'Drag':
                # if actions.GLOBAL_DEBUG:
                #     print(str(counter))
                #     print(item)
                n_to =counter
                actions.processDragActions(data, action_file, n_from, n_to)

            # A Point Click Action (3) ends here.
            # It can be a compunded action: {MM}*PC - several MM actions followed by a DD action
            if prevrow != None and prevrow['state'] == 'Pressed':
                # if actions.GLOBAL_DEBUG:
                #     print(str(counter))
                #     print(item)
                n_to = counter
                actions.processPointClickActions(data, action_file, n_from, n_to)

            # It starts a new action
            data = []
            n_from = n_to +1
        else:
            if int(item['x'])<st.X_LIMIT or int(item['y']) <st.Y_LIMIT:
                data.append(item)
        prevrow = row
    n_to = counter
    actions.processPointClickActions(data, action_file,n_from, n_to)
    return


# print CSV header, case SESSION_CUT = 2
def printCsvHeaderAction(feature_file, case):
    print("printCsvHeaderAction")
    feature_file.write("type_of_action,traveled_distance_pixel,elapsed_time,direction_of_movement,");
    feature_file.write("straightness,num_points,sum_of_angles,mean_curv,sd_curv,max_curv,min_curv,mean_omega,sd_omega,max_omega,min_omega,");
    feature_file.write("largest_deviation,dist_end_to_end_line,num_critical_points,")
    feature_file.write("mean_vx,sd_vx,max_vx,min_vx,mean_vy,sd_vy,max_vy,min_vy,mean_v,sd_v,max_v,min_v,mean_a,sd_a,max_a,min_a,mean_jerk,sd_jerk,max_jerk,min_jerk,a_beg_time,class,session,n_from,n_to")
    if case == 'test':
        feature_file.write(", islegal")
    feature_file.write("\n");
    return





# SESSIONCUT = 2
# one action --> one feature vector
def printSession2(userid, feature_file, label, sessionid, case):
    action_file = open(st.ACTION_FILENAME, "r")
    reader = csv.DictReader(action_file)
    for row in reader:
        # print( row )
        feature_file.write( row["type_of_action"])
        feature_file.write(",")
        feature_file.write(row["traveled_distance_pixel"])
        feature_file.write(",")
        feature_file.write(row["elapsed_time"])
        feature_file.write(",")
        feature_file.write(row["direction_of_movement"])
        feature_file.write(",")
        feature_file.write(row["straightness"])
        feature_file.write(",")
        feature_file.write(row["num_points"])
        feature_file.write(",")
        feature_file.write(row["sum_of_angles"])
        feature_file.write(",")

        feature_file.write(row["mean_curv"])
        feature_file.write(",")
        feature_file.write(row["sd_curv"])
        feature_file.write(",")
        feature_file.write(row["max_curv"])
        feature_file.write(",")
        feature_file.write(row["min_curv"])
        feature_file.write(",")

        feature_file.write(row["mean_omega"])
        feature_file.write(",")
        feature_file.write(row["sd_omega"])
        feature_file.write(",")
        feature_file.write(row["max_omega"])
        feature_file.write(",")
        feature_file.write(row["min_omega"])
        feature_file.write(",")

        feature_file.write(row["largest_deviation"])
        feature_file.write(",")
        feature_file.write(row["dist_end_to_end_line"])
        feature_file.write(",")
        feature_file.write(row["num_critical_points"])
        feature_file.write(",")

        feature_file.write(row["mean_vx"])
        feature_file.write(",")
        feature_file.write(row["sd_vx"])
        feature_file.write(",")
        feature_file.write(row["max_vx"])
        feature_file.write(",")
        feature_file.write(row["min_vx"])
        feature_file.write(",")

        feature_file.write(row["mean_vy"])
        feature_file.write(",")
        feature_file.write(row["sd_vy"])
        feature_file.write(",")
        feature_file.write(row["max_vy"])
        feature_file.write(",")
        feature_file.write(row["min_vy"])
        feature_file.write(",")

        feature_file.write(row["mean_v"])
        feature_file.write(",")
        feature_file.write(row["sd_v"])
        feature_file.write(",")
        feature_file.write(row["max_v"])
        feature_file.write(",")
        feature_file.write(row["min_v"])
        feature_file.write(",")

        feature_file.write(row["mean_a"])
        feature_file.write(",")
        feature_file.write(row["sd_a"])
        feature_file.write(",")
        feature_file.write(row["max_a"])
        feature_file.write(",")
        feature_file.write(row["min_a"])
        feature_file.write(",")

        feature_file.write(row["mean_jerk"])
        feature_file.write(",")
        feature_file.write(row["sd_jerk"])
        feature_file.write(",")
        feature_file.write(row["max_jerk"])
        feature_file.write(",")
        feature_file.write(row["min_jerk"])
        feature_file.write(",")

        feature_file.write(row["a_beg_time"])
        feature_file.write(",")

        feature_file.write(userid + "," + sessionid+",")
        feature_file.write(row["n_from"])
        feature_file.write(",")
        feature_file.write(row["n_to"])

        if case == "test":
            feature_file.write("," + str(label))
        feature_file.write("\n")
    action_file.close()
    return

# public part of the test files
def process_public_labels():
    dlabels={}
    input_file  = open(st.BASE_FOLDER + '/' + st.PUBLIC_LABELS, "r")
    reader = csv.DictReader(input_file)
    for row in reader:
        fname = row['filename']
        is_illegal = row['is_illegal']
        sessionid = str(fname[8:len(fname)])
        dlabels[sessionid] = 1-int(is_illegal)
    input_file.close()
    return dlabels


# input: case {'training','test'}
# output: output/balabit_featutes_training.csv OR output/balabit_featutes_test.csv
def process_files(df):
    #filename = 'session_0041905381'
    #filename = 'mouse_data_test.csv'

    action_file = open(st.ACTION_FILENAME, "w")
    action_file.write(st.ACTION_CSV_HEADER)

    processSession1(df, action_file)

    action_file.close()
    df2 = pd.read_csv(st.ACTION_FILENAME)
    return df2

'''
if __name__ == '__main__':
    st.FILENAME = input('Insira o nome do arquivo a ser processado: ')
    st.ACTION_FILENAME = input('Insira o nome do arquivo de SAÍDA: ')
    st.SESSION_CUT = 2
    print("***Computing training features")
    st.CASE = 'training'
    process_files()
'''
