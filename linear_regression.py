#it is obvious that it is impossible to earn more than 60% with simple linear model.
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np


df = pd.read_csv('stats (5).csv')
#feature_cols = ["exit_velocity_avg","launch_angle_avg","sweet_spot_percent","barrel_batted_rate","solidcontact_percent","flareburner_percent","poorlyweak_percent","hard_hit_percent","z_swing_percent","oz_swing_percent","oz_contact_percent","iz_contact_percent","whiff_percent","hp_to_1b"]

#X = df.loc[:,"exit_velocity_avg":"hp_to_1b"]
X = df[["exit_velocity_avg","launch_angle_avg", "sweet_spot_percent", "barrel_batted_rate","solidcontact_percent","flareburner_percent","poorlyweak_percent", "hard_hit_percent","z_swing_percent","oz_swing_percent","oz_contact_percent","iz_contact_percent", "whiff_percent"]]

#X = df[["exit_velocity_avg","launch_angle_avg", "barrel_batted_rate", "flareburner_percent","poorlyweak_percent","z_swing_percent","oz_swing_percent","oz_contact_percent","iz_contact_percent", "whiff_percent"]]
# multi target regression.
# targets: "home_run","walk","batting_avg","slg_percent","on_base_percent"


#savant xBA score: 0.267
#prediction score: 0.483

#savant xOBP score: 0.723
#prediction score: 0.513

#savant xSLG score: 0.660
#prediction score: 0.586
y = df["slg_percent"]
savant = df["xslg"]
l_reg = linear_model.LinearRegression()
print("savant score ", r2_score(savant, y))
score = 0
for i in range(1000):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = l_reg.fit(X_train, y_train)

    predictions = model.predict(X_test)
    score += l_reg.score(X_test,y_test)
    #print("Prediction Score ", score)

print(score/1000)

"""
yy = y_test.to_numpy()
for i in range(len(yy)):
    #xx = X_test.iloc[i]
    print(predictions[i],  yy[i])
"""







