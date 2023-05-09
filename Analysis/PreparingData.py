import os
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf 
from scipy.stats import t


def encode_and_bind(original_dataframe, feature_to_encode, drop=True, drop_cat=None):
    if drop_cat == None:
        dummies = pd.get_dummies(original_dataframe[[feature_to_encode]], drop_first = drop)
    else:
        dummies = pd.get_dummies(original_dataframe[[feature_to_encode]])
        dummies.drop(columns=feature_to_encode + '_' + drop_cat, inplace=True)
    res = pd.concat([original_dataframe, dummies], axis=1)
    res = res.drop(columns = [feature_to_encode])
    return(res)


os.chdir(os.path.normpath(os.getcwd() + os.sep + os.pardir))
data = pd.read_csv('Data/PhonesDF_years.csv')
data.sample(3)

data = data.loc[(data.price >= np.exp(8.3)) & (data.price < np.exp(12.5)), :].copy(deep=True)

# adding log price and PPI to dataset
data['log_price'] = np.log(data.price)
data['density'] = data.disp_height * data.disp_width / data.disp_diag**2
data = data.drop(columns = ['price', 'specs_score'])

# data = data[data['brand_Hotwav'] != 1]
# data = data.drop(columns = ['brand_Hotwav'])
data = data.set_index('phone_title')
data['Other_oper_syst'] = 0
data['IOS_oper_syst'] = 0

data.loc[data['oper_syst_type'] == 'Other', 'Other_oper_syst'] = 1 # Android - base dummy
data.loc[data['oper_syst_type'] == 'IOS', 'IOS_oper_syst'] = 1 
data = data.drop(columns = ['oper_syst_type', 'likes'])

data = encode_and_bind(data, 'battery_type', drop=False)
data = encode_and_bind(data, 'brand', drop=False)
data = data.rename(columns = {'battery_type_ Li-Po':'battery_type_LiPo', 'battery_type_ Li-Ion':'battery_type_LiIon'})
data = data[data['brand_Hotwav'] != 1]
data = data.drop(columns = ['brand_Hotwav'])

# Dropping outliers
X_columns = data.drop(columns=['log_price', 'IOS_oper_syst', 'oper_syst_vers', 'disp_height', 'disp_width']).columns

ols = smf.ols(f"log_price ~ {' + '.join(map(str, X_columns))}", data=data).fit()

n = data.shape[0]
k = X_columns.shape[0] + 1
t_crit_r = t.ppf(0.975, n - k - 1)
t_crit_l = -t_crit_r
resid_std = ols.outlier_test()['student_resid']
mask = (resid_std < t_crit_r) & (resid_std > t_crit_l)

data = data[mask]

data.to_csv('Data/PhonesDFUndroppedV2.csv', index=True)

data.drop(columns=['brand_Xiaomi', 'battery_type_LiIon']).to_csv('Data/PhonesDF_years_corrected_v2.csv', index=True)