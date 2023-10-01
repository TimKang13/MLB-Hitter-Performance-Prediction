from sklearn import linear_model
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import warnings


df = pd.read_csv('stats (5).csv')

X = df[["exit_velocity_avg","launch_angle_avg", "sweet_spot_percent", "barrel_batted_rate","solidcontact_percent","flareburner_percent","poorlyweak_percent", "hard_hit_percent","z_swing_percent","oz_swing_percent","oz_contact_percent","iz_contact_percent", "whiff_percent"]]
y = df["on_base_percent"]
savant = df["xslg"]
#savant xAVG score: 0.267
#prediction score: 0.480

#savant xSLG score: 0.723
#prediction score: 0.503  

#savant xSLG score: 0.660
#prediction score: 0.583

lasso = Lasso(alpha=0.001)
warnings.filterwarnings('ignore')

print("savant score ", r2_score(savant, y))
    
score = 0
for i in range(1000):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = lasso.fit(X_train, y_train)
    predictions = model.predict(X_test)
    score += lasso.score(X_test,y_test)
    #print("Prediction Score ", score)

print(score/1000)

coefficients = pd.DataFrame({'Features': X_train.columns, 'Coefficients': lasso.coef_})
print(coefficients)


"""
yy = y_test.to_numpy()
for i in range(len(yy)):
    #xx = X_test.iloc[i]
    print(predictions[i],  yy[i])
"""