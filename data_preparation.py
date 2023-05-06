import pandas as pd
import numpy as np
import re

# код Саши)
df = pd.read_csv('Data/PhonesPriceInKenya_v2.csv')
df['Display (inch)'] = np.nan
df['Display resolution'] = np.nan
df['Camera'] = np.nan
df['Operational system'] = np.nan
df['Storage (GB)'] = np.nan
df['RAM (GB)'] = np.nan
df['Battery (mAh)'] = np.nan
df['Battery type'] = np.nan
for num, i in df.iterrows():
    specs = i['Specs'].split(',')
    if len(specs) == 8:
        i['Display (inch)'] = ''.join(filter(str.isdigit, specs[0]))
        i['Display resolution'] = specs[1].replace(' pixels', '')
        i['Camera'] = ''.join(filter(str.isdigit, specs[2]))
        i['Operational system'] = specs[3].replace('OS:', '')
        i['Storage (GB)'] = ''.join(filter(str.isdigit, specs[4]))
        i['RAM (GB)'] = ''.join(filter(str.isdigit, specs[5]))
        i['Battery (mAh)'] = ''.join(filter(str.isdigit, specs[6]))
        i['Battery type'] = specs[7]
        df.loc[num] = i
    elif specs[4] == ' One UI':
        i['Display (inch)'] = ''.join(filter(str.isdigit, specs[0])) 
        i['Display resolution'] = specs[1].replace(' pixels', '')
        i['Camera'] = ''.join(filter(str.isdigit, specs[2]))
        i['Operational system'] = specs[3].replace('OS:', '')
        i['Storage (GB)'] = ''.join(filter(str.isdigit, specs[4] + specs[5]))
        i['RAM (GB)'] = ''.join(filter(str.isdigit,specs[6])) 
        i['Battery (mAh)'] = ''.join(filter(str.isdigit,specs[7])) 
        i['Battery type'] = ''.join(filter(str.isdigit,specs[8])) 
        df.loc[num] = i
    elif specs[2] == 'Front Camera:TripleOS:Android 9.0 Pie' or specs[2] =='Front Camera:VGAOS:Android 6.0 Marshmallow':
        i['Display (inch)'] = ''.join(filter(str.isdigit,specs[0])) 
        i['Display resolution'] = specs[1].replace(' pixels', '')
        i['Camera'] = ''.join(filter(str.isdigit, specs[2].split('Android')[0]))
        i['Operational system'] = 'Android' + specs[2].split('Android')[1].replace('OS:', '')
        i['Storage (GB)'] = ''.join(filter(str.isdigit, specs[3]))
        i['RAM (GB)'] = ''.join(filter(str.isdigit, specs[4])) 
        i['Battery (mAh)'] = ''.join(filter(str.isdigit, specs[5])) 
        i['Battery type'] = ''.join(filter(str.isdigit, specs[6])) 
        df.loc[num] = i
    elif specs[3].find('+') == 1:
        i['Display (inch)'] = ''.join(filter(str.isdigit, specs[0])) 
        i['Display resolution'] = specs[1].replace(' pixels', '')
        i['Camera'] = ''.join(filter(str.isdigit, specs[2] + specs[3])) 
        i['Operational system'] = specs[4].replace('OS:', '')
        i['Storage (GB)'] = ''.join(filter(str.isdigit, specs[5])) 
        i['RAM (GB)'] = ''.join(filter(str.isdigit, specs[6])) 
        i['Battery (mAh)'] = ''.join(filter(str.isdigit, specs[7])) 
        i['Battery type'] = ''.join(filter(str.isdigit, specs[8])) 
        df.loc[num] = i
    elif specs[6] == 'Battery:-':
        i['Display (inch)'] = ''.join(filter(str.isdigit, specs[0])) 
        i['Display resolution'] = specs[1].replace(' pixels', '')
        i['Camera'] = ''.join(filter(str.isdigit, specs[1] + specs[2])) 
        i['Operational system'] = specs[3].replace('OS:', '')
        i['Storage (GB)'] = ''.join(filter(str.isdigit, specs[4])) 
        i['RAM (GB)'] = ''.join(filter(str.isdigit, specs[5])) 
        i['Battery (mAh)'] = np.nan
        i['Battery type'] = np.nan
        df.loc[num] = i
    elif specs[2] == 'Front Camera:NoOS:-' or specs[2] == 'Front Camera:VGAOS:Android 5.1 Lollipop' or specs[2] == 'Front Camera:NoOS:KaiOS:':
        i['Display (inch)'] = ''.join(filter(str.isdigit, specs[0])) 
        i['Display resolution'] = specs[1].replace(' pixels', '')
        i['Camera'] = ''.join(filter(str.isdigit, specs[2].split(':')[1]))
        i['Operational system'] = specs[2].split(':')[2].replace('OS:', '')
        i['Storage (GB)'] = ''.join(filter(str.isdigit, specs[5]))
        i['RAM (GB)'] = ''.join(filter(str.isdigit, specs[6]))
        i['Battery (mAh)'] = np.nan
        i['Battery type'] = np.nan
        df.loc[num] = i
    elif len(specs) == 7 and specs[-1] == ' Li-Ion':

        i['Display (inch)'] = ''.join(filter(str.isdigit, specs[0]))
        i['Display resolution'] = specs[1].replace(' pixels', '')
        i['Camera'] = ''.join(filter(str.isdigit, specs[2]))
        i['Operational system'] = np.nan
        i['Storage (GB)'] = ''.join(filter(str.isdigit, specs[3]))
        i['RAM (GB)'] = ''.join(filter(str.isdigit, specs[4]))
        i['Battery (mAh)'] = ''.join(filter(str.isdigit, specs[5]))
        i['Battery type'] = ''.join(filter(str.isdigit, specs[6]))
        df.loc[num] = i
    elif len(specs) > 9:
        print(df[df['Specs'] == i['Specs']].index)
    elif len(specs) == 9:
        i['Display (inch)'] = ''.join(filter(str.isdigit, specs[0])) 
        i['Display resolution'] = specs[1].replace(' pixels', '')
        i['Camera'] = ''.join(filter(str.isdigit, specs[2]))
        string = specs[3] + specs[4]
        i['Operational system'] = string.replace('OS:', '')
        i['Storage (GB)'] = ''.join(filter(str.isdigit, specs[5])) 
        i['RAM (GB)'] = ''.join(filter(str.isdigit, specs[6])) 
        i['Battery (mAh)'] = ''.join(filter(str.isdigit, specs[7]))
        i['Battery type'] = ''.join(filter(str.isdigit, specs[8])) 
        df.loc[num] = i
    elif specs[-1] == ' Li-Ion' or specs[-1] == ' Li-Po':
        i['Display (inch)'] = ''.join(filter(str.isdigit, specs[0]))
        i['Display resolution'] = specs[1].replace(' pixels', '')
        i['Camera'] = ''.join(filter(str.isdigit, specs[2]))
        i['Operational system'] = np.nan
        i['Storage (GB)'] = ''.join(filter(str.isdigit, specs[3]))
        i['RAM (GB)'] = ''.join(filter(str.isdigit, specs[4]))
        i['Battery (mAh)'] = ''.join(filter(str.isdigit, specs[5]))
        i['Battery type'] = ''.join(filter(str.isdigit, specs[6]))
        df.loc[num] = i
    elif len(specs) == 7:
        i['Display (inch)'] = ''.join(filter(str.isdigit, specs[0]))
        i['Display resolution'] = specs[1].replace(' pixels', '')
        i['Camera'] = ''.join(filter(str.isdigit, specs[2]))
        i['Operational system'] = specs[3].replace('OS:', '')
        i['Storage (GB)'] = ''.join(filter(str.isdigit, specs[4]))
        i['RAM (GB)'] = ''.join(filter(str.isdigit, specs[5]))
        i['Battery (mAh)'] = ''.join(filter(str.isdigit, specs[6]))
        i['Battery type'] = np.nan
        df.loc[num] = i

    else:
        print(specs)
        print(len(specs))


df = df.replace('', np.nan)
df = df.replace('-', np.nan)
df = df.replace(';', '')

df["Display (inch)"] = pd.to_numeric(df["Display (inch)"])
df["Camera"] = pd.to_numeric(df["Camera"])
df["Storage (GB)"] = pd.to_numeric(df["Storage (GB)"])
df["RAM (GB)"] = pd.to_numeric(df["RAM (GB)"])
df["Battery (mAh)"] = pd.to_numeric(df["Battery (mAh)"])
df['Operational system'] = df['Operational system'].astype(str)


disp_row = df['Display (inch)']
for num, i in df.iterrows():
    if i['Display (inch)'] > 100:
        disp_row[num] = i['Display (inch)']/100
    elif i['Display (inch)'] < 100:
        disp_row[num] =  i['Display (inch)']/10
df['Display (inch)'] = disp_row

row_os = df['Operational system']
for num, row in df.iterrows():
    if row['Operational system'].find(';') == 1:
        row_os[num] = row['Operational system'].replace(';', '')
    else:
        row_os[num] = row['Operational system']

# конец кода Саши


# converting prices
def get_price(price_str):
    if type(price_str) != str:
        return np.nan
    elif '.' in price_str:
        return float(price_str)
    elif ',' in price_str:
        return float(price_str.replace(',', ''))


# converting specs score
def get_score(score_str):
    if type(score_str) != str:
        return score_str
    else:
        return int(score_str.replace('%', ''))


# converting display resolution
def get_disp_w(res_str):
    if type(res_str) != str:
        return res_str
    else:
        width, _ = map(int, res_str.split(' x '))
        return width

def get_disp_h(res_str):
    if type(res_str) != str:
        return res_str
    else:
        _, height = map(int, res_str.split(' x '))
        return height

# parsing operational system
def get_opersyst(oper_syst_str):
    if type(oper_syst_str) != str:
        return np.nan
    else:
        new_str = oper_syst_str.replace(';', '').strip().lower()
        words = new_str.split()
        if 'android' in new_str:
            return 'Android'
        elif 'i' in words:
            return 'IOS'
        elif 'duali' in words:
            return 'Duali'
        elif 'blackberry' in words:
            return 'BlackBerry'
        elif 'kai' in new_str:
            return 'KaiOS'
        elif 'dual' in words:
            return 'Dual'
        else:
            return np.nan

# parsing version of operational system
def get_operversion(oper_syst_str):
    if type(oper_syst_str) != str or oper_syst_str == 'nan':
        return np.nan
    else:
        new_str = oper_syst_str.replace(';', '').strip().lower()
        words = new_str.split()
        syst_names = ['i', 'android', 'duali', 'blackberry', 'kai', 'dual']
        num_str = None
        for syst_name in syst_names:
            for word in words:
                if syst_name in word:
                    if syst_name == 'i' and word != 'i':
                        continue
                    idx_syst = words.index(word) + 1
                    if idx_syst < len(words):
                        num_str = words[words.index(word) + 1]
        if num_str == None:
            return np.nan
        reg = re.compile('[0-9.]+')
        num = reg.findall(num_str)
        if len(num) == 0:
            return np.nan
        return num[0].split('.')[0]

# converting
df['Price(Kshs)'] = df['Price(Kshs)'].apply(get_price)

df['Specs Score'] = df['Specs Score'].apply(get_score)

df['disp_height'] = df['Display resolution'].apply(get_disp_h)
df['disp_width'] = df['Display resolution'].apply(get_disp_w)

df['oper_syst_type'] = df['Operational system'].apply(get_opersyst)
df['oper_syst_vers'] = df['Operational system'].apply(get_operversion)
df.oper_syst_type.replace({'Duali': 'IOS', 'BlackBerry': 'Other'}, inplace=True)

# dropping columns we do not need
df.drop(columns=['Display resolution', 'Operational system', 'Specs'], inplace=True)

# renaming columns
df.rename(columns={'Phone Title': 'phone_title', 'Price(Kshs)': 'price',
            'Specs Score': 'specs_score', 'Display (inch)': 'disp_diag',
               'Storage (GB)': 'storage', 'RAM (GB)': 'ram', 'Battery (mAh)': 'battery_capacity',
                   'Battery type': 'battery_type'}, inplace=True)
df.columns = [item.lower() for item in df.columns]

# dropping missing values
df.dropna(inplace=True)

# saving dataset
df.to_csv('data/PhonesDF.csv', encoding='utf-8', index=False)
            
    