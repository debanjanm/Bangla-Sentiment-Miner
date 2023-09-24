import os
import pandas as pd
from sklearn.model_selection import train_test_split
from config import DATA_BASE_PATH


def numerals_normalize(df):
    for i in range(len(df)):
        words = df["Data"][i].split()
        st = ""
        for word in words:
            if st != "":
                st += " "
            if (
                word[0] >= "0"
                and word[0] <= "9"
                and word[-1] >= "0"
                and word[-1] <= "9"
            ):
                st += "CC"
            else:
                st += word
        df["Data"][i] = st

    return df


df_train = pd.read_csv(os.path.join(DATA_BASE_PATH, "Train.csv"))
df_train = numerals_normalize(df_train)

df_val = pd.read_csv(os.path.join(DATA_BASE_PATH, "Val.csv"))
df_val = numerals_normalize(df_val)

df_test = pd.read_csv(os.path.join(DATA_BASE_PATH, "Test.csv"))
df_test = numerals_normalize(df_test)


df_train.to_csv(os.path.join(DATA_BASE_PATH, "Final_Train.csv"), index=False)
df_val.to_csv(os.path.join(DATA_BASE_PATH, "Final_Val.csv"), index=False)
df_test.to_csv(os.path.join(DATA_BASE_PATH, "Final_Test.csv"), index=False)
