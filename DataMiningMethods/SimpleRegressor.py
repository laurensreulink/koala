import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import make_scorer
from sklearn.metrics import accuracy_score
from sklearn.linear_model import Lasso
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
from math import sqrt

#PREPROCESSING

keys = ['X','Events']
values = []
metadata = dict(zip(keys, values))

def runPreprocessing(dictinput, filename):
    dataset = filename
    origdata = pd.read_csv(dataset, sep=';')
    label_selection_continuous = dictinput['Label']  # USER INPUT
    training_type = 0  # or R USER INPUT
    uid = dictinput['UID']
    event = dictinput['Event']
    timestamp = dictinput['Timestamp']
    attributes_categorical = dictinput['Cat']  # USER INPUT
    attributes_continuous = dictinput['Con'] #USER INPUT
    labels_continuous = origdata[label_selection_continuous]
    labels_to_keep = [uid,event,timestamp]
    labels_to_keep.extend(attributes_categorical)
    labels_to_keep.extend(attributes_continuous)
    labels_to_keep.append(label_selection_continuous)
    data = origdata[labels_to_keep]
    events = list(data[event].unique())
    events.sort()
    transsys = create_ts_dict(data, uid, event, events)
    print('Transition System Created')

    t = 28

    data = createMilestones(data, uid, timestamp, label_selection_continuous, labels_continuous, t)
    # infolist = milestoneInfo(data)

    min = 0  # USER INPUT
    max = 6  # USER INPUT

    dfa = createAttributeDataFrame(data, min, max, uid, event, timestamp)
    dfa = removeDuplicates(dfa)
    dfa = removeAttributes(dfa, uid, label_selection_continuous)

    features = getFeatures(data, uid, event)
    df = count_events(data, min, max, uid, event, features)
    dictinput['Events'] = df.columns.values

    df_merged = pd.merge(df, dfa, on='TraceID')
    df_merged = pd.get_dummies(df_merged, columns=attributes_categorical)

    traceid = df['TraceID']
    df_merged.drop(labels=['TraceID'], axis=1, inplace=True)
    df_merged.insert(0, 'TraceID', traceid)
    droplist = ['Max Milestone']
    droplist.append(label_selection_continuous)
    df_merged = df_merged.drop(columns=droplist)
    return df_merged, dictinput, transsys

def createMilestones(data,uid,timestamp,label,labels_categorical, t):
    cids = data[uid].unique()

    for id in cids:
        min = data.loc[data[uid]==id, timestamp].min(axis=0)
        data.loc[data[uid]==id, 'FirstEventTime'] = min
    for id in cids:
        max = data.loc[data[uid]==id, timestamp].max(axis=0)
        data.loc[data[uid]==id, 'LastEventTime'] = max

    data['EventDateTime'] = pd.to_datetime(data['EventDateTime'])
    data['FirstEventTime'] = pd.to_datetime(data['FirstEventTime'])
    data['LastEventTime'] = pd.to_datetime(data['LastEventTime'])
    data['Prefix Time Elapsed'] = data[timestamp] - data['FirstEventTime']
    data['Prefix Time Elapsed'] = data['Prefix Time Elapsed'].dt.total_seconds()
    data['Milestone'] = data['Prefix Time Elapsed'].apply(lambda x: x/(t*86400))
    data['Milestone'] = np.floor(data['Milestone'])
    for id in cids:
        maxm = data.loc[data[uid] == id, 'Milestone'].max(axis=0)
        data.loc[data[uid] == id, 'Max Milestone'] = maxm
    data['Prefix Time Elapsed'] = data['Prefix Time Elapsed'].apply(lambda x: x/(86400))
    data['Label'] = labels_categorical

    return data

def milestoneInfo(data): #OUTPUT USER?
    max_milestone = data['Milestone'].max()
    mean_milestone = data['Milestone'].mean()
    median_milestone = data['Milestone'].median()
    # print('The maximum milestone in the trace is ' + str(max_milestone) + '.')
    # print('The mean milestone in the trace is ' + str(mean_milestone) + '.')
    # print('The median milestone in the trace is ' + str(median_milestone) + '.')
    infolist = []
    infolist.append(max_milestone)
    infolist.append(mean_milestone)
    infolist.append(median_milestone)
    return infolist

def createAttributeDataFrame(data, min, max,uid, event_column, timestamp):
    atts = ['FirstEventTime','LastEventTime','Prefix Time Elapsed']
    event = [event_column]
    droplist = atts + event
    dfaf = data
    dfaf = dfaf.drop(columns=droplist)
    dfaf.to_csv('Test DFAF.csv')

    min_milestone = min
    max_milestone = max

    frames_a = []

    dfa_list_milestones = []
    dfa_milestones = []
    for m in range(min_milestone, max_milestone):
        dfa_milestones.append(m)
        dfa_list_milestones.append('dfm_' + str(m))
    dict_dfa = dict(zip(dfa_milestones, dfa_list_milestones))

    for m in range(0, max_milestone):
        dfsa = dfaf.loc[dfaf['Milestone'] <= m]  # split on milestone value
        dfsa = dfsa.loc[dfsa['Max Milestone']>= m]
        dfsa = dfsa.reset_index(drop=True)
        mcids = dfsa[uid].unique()
        for i in range(0, len(mcids)):
            new_id = str(mcids[i]) + '-' + str(m)
            dfsa.loc[dfsa[uid] == mcids[i], 'TraceID'] = new_id
            max = dfsa.loc[dfsa[uid] == mcids[i], timestamp].max(axis=0)
            dfsa.loc[dfsa[uid] == mcids[i], 'LastEventTimeMilestone'] = max

        dict_dfa[m] = dfsa
        frames_a.append(dict_dfa[m])
        print('Milestone ' + str(m) + ' done!')

    dfa = pd.concat(frames_a, ignore_index=True)
    dfa = dfa.loc[dfa[timestamp] == dfa['LastEventTimeMilestone']]

    return dfa

def removeDuplicates(dfa):
    dfa_sorted = dfa.TraceID.value_counts()
    dfa_multiples = dfa_sorted[dfa_sorted > 1]
    multiples = dfa_multiples.index.values
    multiples.tolist()

    dfa_error = dfa[dfa['TraceID'].isin(multiples)]
    dfa_error
    error_index = dfa_error.index.tolist()
    index_dfa = dfa.index.tolist()
    keep_index = set(index_dfa) - set(error_index)
    keep_index = sorted(list(keep_index))
    dfa = dfa.loc[keep_index, :]
    return dfa

def removeAttributes(dfa, uid, label_selection_continuous):
    id = [uid]
    standard_atts = ['EventDateTime', 'LastEventTimeMilestone', 'Milestone', label_selection_continuous]
    list = id+standard_atts
    dfa = dfa.drop(columns=list)
    return dfa

def getFeatures(data, uid, event):
    events = list(data[event].unique())
    events.sort()
    cid = [uid]
    milestones = ['Milestone']
    features = cid + events + milestones
    return features

def count_events(data, min, max, uid, event, features):
    df_list_milestones = []
    min_milestone=min
    max_milestone=max
    milestones_a = []
    frames = []
    for m in range(min_milestone, max_milestone):
        milestones_a.append(m)
        df_list_milestones.append('dfm_' + str(m))
    dict_df = dict(zip(milestones_a, df_list_milestones))

    for m in range(0, max_milestone):
        dfs = data.loc[data['Milestone'] <= m]  # split on milestone value
        dfs = dfs.loc[dfs['Max Milestone'] >=m]
        dfs = dfs.reset_index(drop=True)
        mcids = dfs[uid].unique()
        dfm = pd.DataFrame(0, index=np.arange(len(mcids)), columns=features)
        for i in range(0, len(mcids)):
            new_id = str(mcids[i]) + '-' + str(m)
            dfm.loc[i, uid] = mcids[i]
            dfm.loc[i, 'TraceID'] = new_id
            dfm.loc[i, 'Milestone'] = m
        print('loop 1 done!')
        for i in mcids:
            rows = dfs.loc[dfs[uid] == i]
            activities = rows[event].unique()
            for a in activities:
                total = len(rows.loc[rows[event] == a])
                dfm.loc[dfm[uid] == i, a] = total
        print('loop 2 done!')
        dict_df[m] = dfm
        frames.append(dict_df[m])
        print('Milestone ' + str(m) + ' done!')

    df = pd.concat(frames, ignore_index=True)

    return df

#CLASSIFIER

def runAlgorithm(dictinput, dataset, focus):
    uid = dictinput['UID']

    use_lasso = True
    lasso_scalers = [True, [None, StandardScaler(), MinMaxScaler()]]
    lasso_alpha = [True, [0.001, 0.01, 0.1, 1, 10, 100]]
    use_rf = True
    rf_max_features = [True, [1, 3, 5]]
    rf_n_estimators = [True, [100]]
    use_gb = True
    gb_scalers = [True, [None, StandardScaler(), MinMaxScaler()]]
    gb_n_estimators = [True, [100]]
    gb_learning_rate = [True, [0.001, 0.01, 0.1, 1, 10, 100]]

    data = dataset
    data = data.drop(columns=[uid, 'TraceID'])
    y = data['Label']
    X = data.drop(columns=['Label'])
    columns = X.columns.values
    dictinput['X'] = columns

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, stratify=y)
    param_grid = create_grid(use_lasso, lasso_scalers, lasso_alpha, use_rf, rf_max_features, rf_n_estimators, use_gb, gb_scalers, gb_n_estimators, gb_learning_rate)
    grid = define_grid(X_train, y_train, param_grid, focus)
    df = table(create_result_table(grid))
    finished = True
    model = grid.best_estimator_
    return finished, model, dictinput, df

def create_grid(use_lasso, lasso_scalers, lasso_alpha, use_rf, rf_max_features, rf_n_estimators, use_gb, gb_scalers, gb_n_estimators, gb_learning_rate):
    param_grid = []
    if use_lasso == True:
        lasso = dict()
        lasso['regressor'] = [Lasso()]
        lasso['preprocessing']=[None]
        if lasso_scalers[0]==True:
            lasso['preprocessing']=lasso_scalers[1]
        if lasso_alpha[0]==True:
            lasso['regressor__alpha']= lasso_alpha[1]
    if use_rf==True:
        rf = dict()
        rf['regressor']=[RandomForestRegressor()]
        rf['preprocessing']=[None]
        if rf_max_features[0]==True:
            rf['regressor__max_features']=rf_max_features[1]
        if rf_n_estimators[0]==True:
            rf['regressor__n_estimators']=rf_n_estimators[1]
    if use_gb==True:
        gb = dict()
        gb['regressor'] = [GradientBoostingRegressor()]
        gb['preprocessing']=[None] 
        if gb_scalers[0]==True:
            gb['preprocessing'] = gb_scalers[1]
        if gb_n_estimators[0]==True:
            gb['regressor__n_estimators'] = gb_n_estimators[1]
        if gb_learning_rate[0]==True:
            gb['regressor__learning_rate'] = gb_learning_rate[1]
    if use_lasso==True and use_gb==True and use_rf==True:
        param_grid=[lasso, gb, svc]
    if use_lasso==True and use_gb==True and use_rf==False:
        param_grid=[lasso, gb]
    if use_lasso==True and use_gb==False and use_rf==True:
        param_grid=[lasso, rf]
    if use_lasso==False and use_gb==True and use_rf==True:
        param_grid=[gb, rf]
    if use_lasso==True and use_gb==False and use_rf==False:
        param_grid=[lasso]
    if use_lasso==False and use_gb==True and use_rf==False:
        param_grid=[gb]
    if use_lasso==False and use_gb == False and use_rf == True:
        param_grid=[rf]
    print('ParamGrid Defined!')
    return param_grid

def define_grid(X_train, y_train,param_grid,focus):
    scorer = {'R2': 'r2','Variance':'explained_variance','RMSE': 'mean_squared_error'}
    pipe = Pipeline([('preprocessing', StandardScaler()), ('regressor', Lasso())])
    grid = GridSearchCV(pipe, param_grid, cv=3, scoring=scorer, refit=focus, n_jobs=-1)
    grid.fit(X_train, y_train)
    return grid

def create_result_table(grid):
    df = grid.cv_results_
    return df

def get_best_params(grid):
    params = grid.best_params_
    return params

def table(df):
    table = pd.DataFrame()
    table.loc[:,'Estimator'] = df['param_regressor']
    table.loc[:,'Preprocessing'] = df['param_preprocessing']
    table.loc[:,'Mean R2 Test Score']  = df['mean_test_R2']
    table.loc[:,'Mean Variance Test Score']  = df['mean_test_Explained Variance']
    table.loc[:,'Mean RMSE Test Score']  = df['mean_test_MSE']
    table['Mean RMSE Test Score'] = np.sqrt(abs(table['Mean RMSE Test Score']))
    table.loc[:,'Parameters'] = df['params']
    table = table.sort_values(['Mean R2 Test Score'], ascending=False)
    table = table.reset_index(drop=True)
    table.index = table.index + 1
    table.index.name = 'Rank'
    return table

def create_ts_dict(data, uid, event, events):
    prefixtable = dict()
    cids = list(data[uid].unique())
    for id in cids:
        ds = data.loc[data[uid] == id]
        trace = list(ds[event])
        for i in range(0, len(trace)):
            key = pd.DataFrame(0, index=np.arange(1), columns=events)
            prefix = trace[:i + 1]
            for i in range(0, len(prefix)):
                element = prefix[i]
                key.loc[0, element] += 1
            final_list = list(key.iloc[0].values)
            key_value = tuple(final_list)
            if key_value not in [*prefixtable]:
                value = dict()
                value['None'] = 1
                prefixtable[key_value] = value
                next_prefix = trace[:i + 2]
                if next_prefix != prefix:
                    element = next_prefix[-1]
                    value = dict()
                    value[element] = 1
                    prefixtable[key_value] = value
            else:
                value = prefixtable[key_value]
                next_prefix = trace[:i + 2]
                if next_prefix != prefix:
                    element = next_prefix[-1]
                    if element in [*value]:
                        value[element] += 1
                    if element not in [*value]:
                        value[element] = 1
                else:
                    if 'None' in [*value]:
                        value['None'] += 1
                    else:
                        value['None'] = 1
                prefixtable[key_value] = value

    return prefixtable