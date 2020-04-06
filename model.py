from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn import metrics, preprocessing
from createCSV import finalize_csv
import pandas as pd
import numpy as np
import sys, csv

from mlxtend.feature_selection import ExhaustiveFeatureSelector as EFS

scaler = MinMaxScaler()

cols = ['DATE', 'HOME', 'VISITOR', 'VISITOR_PTS', 'HOME_PTS', 'WINNER', 'HOME_GAME', 'AWAY GAME']

df_2018 = pd.read_csv("season_2018.csv")
df_2019 = pd.read_csv("season_2019.csv")
df_2020 = pd.read_csv("season_2020.csv")
#df_2020 = pd.read_csv(finalize_csv('season_2020.csv', 2020))
df = pd.concat([df_2018, df_2019], ignore_index=True)

columns = ['HOME_NRtg', 'HOME_DRB%', 'HOME_SRS', 'VISITOR_NRtg', 'HOME_B2B', 'VISITOR_B2B', 
    'VISITOR_DRB%', 'VISITOR_SRS', 'HOME_ORtg', 'HOME_DRtg', 'VISITOR_ORtg', 'VISITOR_DRtg',
    'VISITOR_MOV', 'HOME_MOV', 'HOME_PACE', 'VISITOR_PACE']
df[columns] = scaler.fit_transform(df[columns])
df_2020[columns] = scaler.fit_transform(df_2020[columns])

X = df.drop(columns=cols)
y = df['WINNER']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=24)

def SVMModel(print_bool):
    # Best Results (as of 3/3/2020 @ 2:20PM)
    #   - kernel : linear
    #   - Test Accuracy : 73.8%
    #   - K-Fold : 67.5% (+/- 3.63%)
    #   - F1 Score : 79.75%
    clf = SVC(kernel='rbf', probability=True, break_ties=True)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    if print_bool:
        scores = cross_val_score(clf, X, y, cv=10)

        sys.stderr.write("[K-FOLD ACCURACY] " + str(scores.mean()) + " (+/- " + str(scores.std()) + ")\n")
        sys.stderr.write("[ACCURACY] " + str(metrics.accuracy_score(y_test, y_pred)) + "\n")
        sys.stderr.write("[F1 SCORE] " + str(metrics.f1_score(y_pred, y_test)) + "\n")
        sys.stderr.flush()
    predict_results = df_2020.drop(columns=cols)
    predict_results = predict_results.drop(["('VISITOR_WIN_PROB',)","('HOME_WIN_PROB',)"], axis=1)
    return clf.predict_proba(predict_results)


average = SVMModel(True)
average = pd.DataFrame(average, columns=[['VISITOR_WIN_PROB', 'HOME_WIN_PROB']])
sys.stderr.write("[PROGRESS] 1/50 runs completed.\n")
sys.stderr.flush()

for n in range(0, 49):
    nth_run = SVMModel(False)
    nth_run = pd.DataFrame(nth_run, columns=[['VISITOR_WIN_PROB', 'HOME_WIN_PROB']])
    average = average.add(nth_run).div(2)
    if (n+2) % 5 == 0:
        sys.stderr.write("[PROGRESS] " + str(n+2) + "/50 runs completed.\n")
        sys.stderr.flush()

df_2020 = pd.concat([df_2020, average], axis=1, sort=True)
total_cols = len(df_2020.columns)
df_2020.to_csv('season_2020.csv', index=False)
print("[COMPLETE] CSV file update completed!")

from nba_games.models import Game

CSV_PATH = 'season_2020.csv'

with open(CSV_PATH, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar=';')
    for row in reader:
        if not row[0] == "DATE":
            if row[2] == '':
                try:
                    # Updates games that have not been played yet.
                    game = Game.objects.get(date=row[0], visitor_team=row[1], home_team=row[3])
                    game.visitor_probability = round(float(row[total_cols-2]) * 100, 2)
                    game.home_probability = round(float(row[total_cols-1]) * 100, 2)
                    game.save()
                except Game.DoesNotExist:
                    Game.objects.create(date=row[0], visitor_team=row[1], home_team=row[3], visitor_probability=round(float(row[total_cols-2]) * 100, 2), home_probability=round(float(row[total_cols-1]) * 100, 2))
                except:
                    print("[ERROR] Unexpected error occured when attempting to update database.")
            else:
                try:
                    # Updates the scores of games that have been played (from yesterday)
                    game = Game.objects.get(date=row[0], visitor_team=row[1], home_team=row[3])
                    if (game.home_score == ''):
                        game.home_score = int(float(row[4]))
                        game.visitor_score = int(float(row[2]))
                        game.save()
                except Game.DoesNotExist:
                    Game.objects.create(date=row[0], visitor_team=row[1], visitor_score=int(float(row[2])), home_team=row[3], home_score=int(float(row[4])),
                                visitor_probability=round(float(row[total_cols-2]) * 100, 2), home_probability=round(float(row[total_cols-1]) * 100, 2))
                except:
                    print("[ERROR] Unexpected error occured when attempting to update database.")