import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('stats (5).csv')

feature_cols = ["exit_velocity_avg","launch_angle_avg","sweet_spot_percent","barrel_batted_rate","solidcontact_percent","flareburner_percent","poorlyweak_percent","hard_hit_percent","z_swing_percent","oz_swing_percent","oz_contact_percent","iz_contact_percent","whiff_percent","hp_to_1b"]
y = "on_base_percent"
#attempts to find correlations between features and y (ex. slg_percent)
for col in feature_cols:
    xpoints = np.array(df[[col]])
    ypoints = np.array(df[[y]])
    plt.scatter(xpoints, ypoints, s=5)
    plt.xlabel(col)
    plt.ylabel(y)
    plt.show()

# observation of correlation

#walk
"""
extremely consistent correlation with:
- oz_swing_percent (1/x for sure)

high correlation with: 

low correlation with:
- z_swing_percent
- barrel_batted_rate
- exit_velocity
- hard_hit_percent
- launch_angle_avg
- solidcontact_percent
- poorlyweak_percent (1/x?)
no correlation with:
- sweet_spot_percent
- flareburner_percent
- oz_contact_percent
- iz_contact_percent
- whiff_percent
- hp_to_1b
"""

#home_run
"""
extremely consistent correlation with:
- barrel_batted_rate

high correlation with:
- exit_velocity_avg
- launch_angle_avg
- solidcontact_percent
- hard_hit_percent
- oz_contact_percent 

low correlation with:
- whiff_percent
- iz_contact_percent
- poorlyweak_percent (1/x graph?)
- flareburner_percent
- sweet_spot_percent
- hp_to_1b

no correlation with:
- z_swing_percent
- oz_swing_percent
"""


#on_base_percent
"""
extremely consistent correlation with:

high correlation with:
- oz_swing_percent
- hard_hit_percent  (x^2)

low correlation with:
- flareburner_percent
- sweet_spot_percent
- exit_velocity_avg
- z_swing_percent
- solidcontact_percent
- barrel_batted_rate
- oz_contact_percent

no correlation with:
- hp_to_1b
- whiff_percent
- iz_contact_percent
- poorlyweak_percent
- launch_angle_avg

"""

#batting_avg
"""
extremely consistent correlation with:
high correlation with:
- flareburner_percent
- oz_contact_percent
- iz_contact_percent
- launch_angle_avg
- whiff_percent
low correlation with:
- hp_to_1b
- sweet_spot_percent
- poorlyweak_percent(1/x)
no correlation with:
- hard_hit_percent
- exit_velocity_avg
- barrel_batted_rate
- solidcontact_percent
- z_swing_percent
- oz_swing percent
"""

#slg_percent
"""
extremely consistent correlation with:
- barrel_batted_rate
- hard_hit_percent
high correlation with:
- exit_velocity_avg
-sweet_spot_percent
-solidcontact_percent
- poorlyweak_percent 
low correlation with:
-whiff_percent
-flareburner_percent
-launch_angle_avg
-oz_contact_percent
-iz_contact_percent
no correlation with:
-z_swing_percent
-oz_swing_percent
-hp_to_1b
"""
