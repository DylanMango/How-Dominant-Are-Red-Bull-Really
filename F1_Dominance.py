import pandas as pd
from pandas import DataFrame as df
import numpy as np
import statistics as s

#------------ Import Data ------------#
#Race Data 
RB_races_raw = pd.read_csv("C:\\Users\\Dylan\\Desktop\\F1 Dominance\\RawData\\2023_race_results_raw.csv")
FERRARI_races_raw = pd.read_csv("C:\\Users\\Dylan\\Desktop\\F1 Dominance\\RawData\\2002_race_results_raw.csv")
MERC_races_raw = pd.read_csv("C:\\Users\\Dylan\\Desktop\\F1 Dominance\\RawData\\2015_race_results_raw.csv")
MCL_races_raw = pd.read_csv("C:\\Users\\Dylan\\Desktop\\F1 Dominance\\RawData\\1988_race_results_raw.csv")

#Quali Data
RB_quali_raw = pd.read_csv("C:\\Users\\Dylan\\Desktop\\F1 Dominance\\RawData\\2023_quali_results_raw.csv")
FERRARI_quali_raw = pd.read_csv("C:\\Users\\Dylan\\Desktop\\F1 Dominance\\RawData\\2002_quali_results_raw.csv")
MERC_quali_raw = pd.read_csv("C:\\Users\\Dylan\\Desktop\\F1 Dominance\\RawData\\2015_quali_results_raw.csv")
MCL_quali_raw = pd.read_csv("C:\\Users\\Dylan\\Desktop\\F1 Dominance\\RawData\\1988_quali_results_raw.csv")

#------------ Clean Data ------------#
#------ Race Data ------
RB_races = RB_races_raw
#We can remove the "+" & "s" to make the "Time" column purely numeric
RB_races["Time"] = RB_races["Time"].str.replace("+", "",regex=True).str.replace("s","",regex=True)
#Make the "Time" column purely numeric, replacing any DNF with 0
RB_races["Time"] = pd.to_numeric(RB_races["Time"], errors = "coerce")
RB_races["Time"] = RB_races["Time"].fillna(0)
#Make sure the "Pos" column data is stored as integers
RB_races["Pos"] = RB_races["Pos"].astype(str)
#------ Quali Data ------
RB_quali = RB_quali_raw
#Clean data by removing non-numeric characters
#We can remove the "1:" or "2:" at the beginning as we only care about the difference between 1st and 2nd/3rd, and there are no tracks where this will flip from 2:0x.xxx to 1:59.xxx
RB_quali["Time"] = RB_quali["Time"].str.replace("1:", "",regex=True).str.replace("2:", "",regex=True)
#Make the "Time" column purely numeric, replacing any DNF with 0
RB_quali["Time"] = pd.to_numeric(RB_quali["Time"], errors = "coerce")
RB_quali["Time"] = RB_quali["Time"].fillna(0)
#Make sure the "Pos" column data is stored as integers
RB_quali["Pos"] = RB_quali["Pos"].astype(str)

#All the same steps as above
#------ Race Data ------
FERRARI_races = FERRARI_races_raw
FERRARI_races["Time"] = FERRARI_races["Time"].str.replace("+", "",regex=True).str.replace("s","",regex=True)
FERRARI_races["Time"] = pd.to_numeric(FERRARI_races["Time"], errors = "coerce")
FERRARI_races["Time"] = FERRARI_races["Time"].fillna(0)
FERRARI_races["Pos"] = FERRARI_races["Pos"].astype(str)
#------ Quali Data ------
FERRARI_quali = FERRARI_quali_raw
FERRARI_quali["Time"] = FERRARI_quali["Time"].astype(str)
FERRARI_quali["Time"] = FERRARI_quali["Time"].str.replace("1:", "",regex=True).str.replace("2:","",regex=True)
FERRARI_quali["Time"] = pd.to_numeric(FERRARI_quali["Time"], errors = "coerce")
FERRARI_quali["Time"] = FERRARI_quali["Time"].fillna(0)
FERRARI_quali["Pos"] = FERRARI_quali["Pos"].astype(str)

#All the same steps as above
#------ Race Data ------
MERC_races = MERC_races_raw
MERC_races["Time"] = MERC_races["Time"].str.replace("+", "",regex=True).str.replace("s","",regex=True)
MERC_races["Time"] = pd.to_numeric(MERC_races["Time"], errors = "coerce")
MERC_races["Time"] = MERC_races["Time"].fillna(0)
MERC_races["Pos"] = MERC_races["Pos"].astype(str)

#------ Quali Data ------
MERC_quali = MERC_quali_raw
MERC_quali["Time"] = MERC_quali["Time"].str.replace("1:", "",regex=True).str.replace("2:","",regex=True)
MERC_quali["Time"] = pd.to_numeric(MERC_quali["Time"], errors = "coerce")
MERC_quali["Time"] = MERC_quali["Time"].fillna(0)
MERC_quali["Pos"] = MERC_quali["Pos"].astype(str)

#All the same steps as above
#------ Race Data ------
MCL_races = MCL_races_raw
MCL_races["Time"] = MCL_races["Time"].str.replace("+", "",regex=True).str.replace("s","",regex=True)
MCL_races["Time"] = pd.to_numeric(MCL_races["Time"], errors = "coerce")
MCL_races["Time"] = MCL_races["Time"].fillna(0)
MCL_races["Pos"] = MCL_races["Pos"].astype(str)

#------ Quali Data ------
MCL_quali = MCL_quali_raw
MCL_quali["Time"] = MCL_quali["Time"].astype(str)
MCL_quali["Time"] = MCL_quali["Time"].str.replace("1:", "",regex=True).str.replace("2:","",regex=True)
MCL_quali["Time"] = pd.to_numeric(MCL_quali["Time"], errors = "coerce")
MCL_quali["Time"] = MCL_quali["Time"].fillna(0)
MCL_quali["Pos"] = MCL_quali["Pos"].astype(str)

#------------ Save Clean Data ------------#
save_path = "C:\\Users\\Dylan\\Desktop\\F1 Dominance\\CleanData\\"

#------ Race Data ------
RB_races.to_csv(save_path + '2023_race_results_clean.csv', index=False)
FERRARI_races.to_csv(save_path + '2002_race_results_clean.csv', index=False)
MERC_races.to_csv(save_path + '2015_race_results_clean.csv', index=False)
MCL_races.to_csv(save_path + '1988_race_results_clean.csv', index=False)

#------ Quali Data ------
RB_quali.to_csv(save_path + '2023_quali_results_clean.csv', index=False)
FERRARI_quali.to_csv(save_path + '2002_quali_results_clean.csv', index=False)
MERC_quali.to_csv(save_path + '2015_quali_results_clean.csv', index=False)
MCL_quali.to_csv(save_path + '1988_quali_results_clean.csv', index=False)

#------------ View Data ------------#
print("--------- Red Bull 2023 Season ---------")
print(RB_races.head())
print(RB_quali.head(), "\n")

print("--------- Ferrari 2002 Seaspm ---------")
print(FERRARI_races.head())
print(FERRARI_quali.head(), "\n")

print("--------- Mercedes 2015 Season ---------")
print(MERC_races.head())
print(MERC_quali.head(), "\n")

print("--------- McLaren 1988 Season ---------")
print(MCL_races.head())
print(MCL_quali.head(), "\n")
#------------ Defining functions ------------#
def Avg(a):
    s = sum(a)
    l = len(a)
    x = s/l

    return x

def DominantCar(df):
    n = len(df)
    w = []
    for i in range(n-1):
        if df.at[i,"Pos"] == "1":
            c = df.at[i,"Car"]
            w.append(c)

    d = s.mode(w)
    return d

def DominantDriver(df):
    n = len(df)
    w = []
    for i in range(n-1):
        if df.at[i,"Pos"] == "1":
            c = df.at[i,"Driver"]
            w.append(c)

    d = s.mode(w)
    return d

def SecondDriver(df, D, C):
    n = len(df)
    w = []
    for i in range(n-1):
        if df.at[i,"Car"] == C:
            if df.at[i,"Driver"] != D:
                d = df.at[i,"Driver"]
    return d

def TeamWinningMargin(df):
    wm = []
    n = len(df)
    C = DominantCar(df)
    for i in range(n-1):
        if df.at[i,"Pos"] == "1":
            if df.at[i, "Car"] == C:
                if df.at[i,"Car"] != df.at[i+1,"Car"]:
                    d = df.at[i+1,"Time"]
                
                else:
                    d = df.at[i+2,"Time"]
                wm.append(d)
    return wm

def DriverWinningMargin(df, C):
    wm = []
    n = len(df)
    for i in range(n-1):
        if df.at[i,"Pos"] == "1":
            if df.at[i, "Driver"] == C:
                d = df.at[i+1,"Time"]
                wm.append(d)
    return wm

def TeamWinPercentage(df):
    w = []
    n = len(df)
    C = DominantCar(df)
    for i in range(n-1):
        if df.at[i,"Pos"] == "1":
            if df.at[i,"Car"] == C:
                w.append(1)
            else:
                w.append(0)
    return w

def DriverWinPercentage(df, C):
    w = []
    n = len(df)
    for i in range(n-1):
        if df.at[i,"Pos"] == "1":
            if df.at[i,"Driver"] == C:
                w.append(1)
            else:
                w.append(0)
    return w

def TeamPodiumPercentage(df):
    p = []
    n = len(df)
    C = DominantCar(df)
    for i in range(n-1):
        if df.at[i,"Pos"] == "1":
            if df.at[i,"Car"] == C:
                p.append(1)
            else:
                if df.at[i+1,"Car"] == C:
                    p.append(1)
                else:
                    if df.at[i+2,"Car"] == C:
                        p.append(1)
                    else:
                        p.append(0)
    return p

def DriverPodiumPercentage(df, C):
    p = []
    n = len(df)
    for i in range(n-1):
        if df.at[i,"Pos"] == "1":
            if df.at[i,"Driver"] == C:
                p.append(1)
            else:
                if df.at[i+1,"Driver"] == C:
                    p.append(1)
                else:
                    if df.at[i+2,"Driver"] == C:
                        p.append(1)
                    else:
                        p.append(0)
    return p

def OneTwoPercentage(df):
    ot = []
    n = len(df)
    C = DominantCar(df)
    for i in range(n-1):
        if df.at[i,"Pos"] == "1":
            if df.at[i,"Car"] and df.at[i+1,"Car"] == C:
                ot.append(1)
            else:
                ot.append(0)
    return ot 

def TeamQualiGap(df):
    qg = []
    n = len(df)
    C = DominantCar(df)
    for i in range(n-2):
        if df.at[i,"Pos"] == "1":
            if df.at[i, "Car"] == C:
                if df.at[i,"Car"] != df.at[i+1,"Car"]:
                    d = df.at[i+1,"Time"] - df.at[i,"Time"]
                else:
                    d = df.at[i+2,"Time"] - df.at[i,"Time"]
                qg.append(d)
            else: 
                qg.append(0)
    return qg

def DriverQualiGap(df,C):
    qg = []
    n = len(df)
    for i in range(n-2):
        if df.at[i,"Pos"] == "1":
            if df.at[i, "Driver"] == C:
                d = df.at[i+1,"Time"] - df.at[i,"Time"]
                qg.append(d)
            else:
                qg.append(0)
    return qg

#------------ Check Dominant Team & Driver ------------#
RB = DominantCar(RB_races)
RB_1 = DominantDriver(RB_races)
RB_1_q = DominantDriver(RB_quali)
RB_2 = SecondDriver(RB_races,RB_1,RB)

FERRARI = DominantCar(FERRARI_races)
FERRARI_1 = DominantDriver(FERRARI_races)
FERRARI_1_q = DominantDriver(FERRARI_quali)
FERRARI_2 = SecondDriver(FERRARI_races,FERRARI_1,FERRARI)
\
MERC = DominantCar(MERC_races)
MERC_1 = DominantDriver(MERC_races)
MERC_1_q = DominantDriver(MERC_quali)
MERC_2 = SecondDriver(MERC_races,MERC_1,MERC)

MCL = DominantCar(MCL_races)
MCL_1 = DominantDriver(MCL_races)
MCL_1_q = DominantDriver(MCL_quali)
MCL_2 = SecondDriver(MCL_races,MCL_1,MCL)

#------------ Calculations ------------ #
#Winning Margin
RB_wm = round(Avg(TeamWinningMargin(RB_races)),2)
VER_wm = round(Avg(DriverWinningMargin(RB_races,RB_1)),2)
PER_wm = round(Avg(DriverWinningMargin(RB_races,RB_2)),2)

FERRARI_wm = round(Avg(TeamWinningMargin(FERRARI_races)),2)
MSC_wm = round(Avg(DriverWinningMargin(FERRARI_races,FERRARI_1)),2)
BAR_wm = round(Avg(DriverWinningMargin(FERRARI_races,FERRARI_2)),2)

MERC_wm = round(Avg(TeamWinningMargin(MERC_races)),2)
HAM_wm = round(Avg(DriverWinningMargin(MERC_races,MERC_1)),2)
ROS_wm = round(Avg(DriverWinningMargin(MERC_races,MERC_2)),2)

MCL_wm = round(Avg(TeamWinningMargin(MCL_races)),2)
SEN_wm = round(Avg(DriverWinningMargin(MCL_races,MCL_2)),2)
PRO_wm = round(Avg(DriverWinningMargin(MCL_races,MCL_2)),2)

#Qualifying Gap
RB_qg = round(Avg(TeamQualiGap(RB_quali)),2)
VER_qg = round(Avg(DriverQualiGap(RB_quali,RB_1_q)),2)

FERRARI_qg = round(Avg(TeamQualiGap(FERRARI_quali)),2)
MSC_qg = round(Avg(DriverQualiGap(FERRARI_quali,FERRARI_1_q)),2)

MERC_qg = round(Avg(TeamQualiGap(MERC_quali)),2)
HAM_qg = round(Avg(DriverQualiGap(MERC_quali,MERC_1_q)),2)

MCL_qg = round(Avg(TeamQualiGap(MCL_quali)),2)
SEN_qg = round(Avg(DriverQualiGap(MCL_quali,MCL_1_q)),2)

#Win Percentage
RB_wp = round(100 * Avg(TeamWinPercentage(RB_races)),2)
VER_wp = round(100 * Avg(DriverWinPercentage(RB_races,RB_1)),2)
PER_wp = round(100 * Avg(DriverWinPercentage(RB_races,RB_2)),2)

FERRARI_wp = round(100 * Avg(TeamWinPercentage(FERRARI_races)),2)
MSC_wp = round(100 * Avg(DriverWinPercentage(FERRARI_races,FERRARI_1)),2)
BAR_wp = round(100 * Avg(DriverWinPercentage(FERRARI_races,FERRARI_2)),2)

MERC_wp = round(100 * Avg(TeamWinPercentage(MERC_races)),2)
HAM_wp = round(100 * Avg(DriverWinPercentage(MERC_races,MERC_1)),2)
ROS_wp = round(100 * Avg(DriverWinPercentage(MERC_races,MERC_2)),2)

MCL_wp = round(100 * Avg(TeamWinPercentage(MCL_races)),2)
SEN_wp = round(100 * Avg(DriverWinPercentage(MCL_races,MCL_1)),2)
PRO_wp = round(100 * Avg(DriverWinPercentage(MCL_races,MCL_2)),2)

#Podium Percentage
RB_pp = round(100 * Avg(TeamPodiumPercentage(RB_races)),2)
VER_pp = round(100 * Avg(DriverPodiumPercentage(RB_races,RB_1)),2)
PER_pp = round(100 * Avg(DriverPodiumPercentage(RB_races,RB_2)),2)

FERRARI_pp = round(100 * Avg(TeamPodiumPercentage(FERRARI_races)),2)
MSC_pp = round(100 * Avg(DriverPodiumPercentage(FERRARI_races,FERRARI_1)),2)
BAR_pp = round(100 * Avg(DriverPodiumPercentage(FERRARI_races,FERRARI_2)),2)

MERC_pp = round(100 * Avg(TeamPodiumPercentage(MERC_races)),2)
HAM_pp = round(100 * Avg(DriverPodiumPercentage(MERC_races,MERC_1)),2)
ROS_pp = round(100 * Avg(DriverPodiumPercentage(MERC_races,MERC_2)),2)

MCL_pp = round(100 * Avg(TeamPodiumPercentage(MCL_races)),2)
SEN_pp = round(100 * Avg(DriverPodiumPercentage(MCL_races,MCL_1)),2)
PRO_pp = round(100 * Avg(DriverPodiumPercentage(MCL_races,MCL_2)),2)

#One-Two Percentage
RB_ot = round(100 * Avg(OneTwoPercentage(RB_races)),2)
FERRARI_ot = round(100 * Avg(OneTwoPercentage(FERRARI_races)),2)
MERC_ot = round(100 * Avg(OneTwoPercentage(MERC_races)),2)
MCL_ot = round(100 * Avg(OneTwoPercentage(MCL_races)),2)

#------------ Printing ------------
print("-------- Red Bull Racing --------")
print("RedBull Average-Winning-Margin: " + str(RB_wm) + " Seconds")
print("RedBull Average-Qualifying-Gap: " + str(RB_qg) + " Seconds")
print("RedBull Win-Percentage: " + str(RB_wp) + "%")
print("RedBull Podium-Percentage: " + str(RB_pp) + "%")
print("RedBull One-Two-Percentage: " + str(RB_ot) + "%")
print("VER Average-Winning-Margin: " + str(VER_wm) + " Seconds")
print("VER Average-Qualifying-Gap: " + str(VER_qg) + " Seconds")
print("VER Win-Percentage: " + str(VER_wp) + "%")
print("VER Podium-Percentage: " + str(VER_pp) + "%\n")


print("Ferrari Average-Winning-Margin: " + str(FERRARI_wm) + " Seconds")
print("Ferrari Average-Qualifying-Gap: " + str(FERRARI_qg) + " Seconds")
print("Ferrari Win-Percentage: " + str(FERRARI_wp) + "%")
print("Ferrari Podium-Percentage: " + str(FERRARI_pp) + "%")
print("Ferrari One-Two-Percentage: " + str(FERRARI_ot) + "%")
print("MSC Average-Winning-Margin: " + str(MSC_wm) + " Seconds")
print("MSC Average-Qualifying-Gap: " + str(MSC_qg) + " Seconds")
print("MSC Win-Percentage: " + str(MSC_wp) + "%")
print("MSC Podium-Percentage: " + str(MSC_pp) + "%\n")

print("Mercedes Average-Winning-Margin: " + str(MERC_wm) + " Seconds")
print("Mercedes Average-Qualifying-Gap: " + str(MERC_qg) + " Seconds")
print("Mercedes Win-Percentage: " + str(MERC_wp) + "%")
print("Mercedes Podium-Percentage: " + str(MERC_pp) + "%")
print("Mercedes One-Two-Percentage: " + str(MERC_ot) + "%")
print("HAM Average-Winning-Margin: " + str(HAM_wm) + " Seconds")
print("HAM Average-Qualifying-Gap: " + str(HAM_qg) + " Seconds")
print("HAM Win-Percentage: " + str(HAM_wp) + "%")
print("HAM Podium-Percentage: " + str(HAM_pp) + "%\n")

print("McLaren Average-Winning-Margin: " + str(MCL_wm) + " Seconds")
print("McLaren Average-Qualifying-Gap: " + str(MCL_qg) + " Seconds")
print("McLaren Win-Percentage: " + str(MCL_wp) + "%")
print("McLaren Podium-Percentage: " + str(MCL_pp) + "%")
print("McLaren One-Two-Percentage: " + str(MCL_ot) + "%")
print("SEN Average-Winning-Margin: " + str(SEN_wm) + " Seconds")
print("SEN Average-Qualifying-Gap: " + str(SEN_qg) + " Seconds")
print("SEN Win-Percentage: " + str(SEN_wp) + "%")
print("SEN Podium-Percentage: " + str(SEN_pp) + "%\n")

with open("F1_Stats.csv", "w") as file:
    print("Team, Avg Winning Margin, Avg Quali Gap, Win %, Podium %, 1-2 %, Driver #1, Avg Winning Margin, Avg Quali Gap, Win %, Podium %, Driver 2, Win %, Podium %", file=file)
    print("Red Bull," + str(RB_wm) + "," + str(RB_qg) + "," + str(RB_wp) + "," + str(RB_pp) + "," + str(RB_ot) + "," + "VER" + "," + str(VER_wm) + "," + str(VER_qg) + "," + str(VER_wp) + "," + str(VER_pp) + "," + "PER" + "," + str(PER_wp) + "," + str(PER_pp), file=file)
    print("Ferrari," + str(FERRARI_wm) + "," + str(FERRARI_qg) + "," + str(FERRARI_wp) + "," + str(FERRARI_pp) + "," + str(FERRARI_ot) + "," + "MSC" + "," + str(MSC_wm) + "," + str(MSC_qg) + "," + str(MSC_wp) + "," + str(MSC_pp) + "," + "BAR" + "," + str(BAR_wp) + "," + str(BAR_pp), file=file)
    print("Mercedes," + str(MERC_wm) + "," + str(MERC_qg) + "," + str(MERC_wp) + "," + str(MERC_pp) + "," + str(MERC_ot) + "," + "HAM" + "," + str(HAM_wm) + "," + str(HAM_qg) + "," + str(HAM_wp) + "," + str(HAM_pp) + "," + "ROS" + "," + str(ROS_wp) + "," + str(ROS_pp), file=file)
    print("McLaren," + str(MCL_wm) + "," + str(MCL_qg) + "," + str(MCL_wp) + "," + str(MCL_pp) + "," + str(MCL_ot) + "," + "SEN" + "," + str(SEN_wm) + "," + str(SEN_qg) + "," + str(SEN_wp) + "," + str(SEN_pp) + "," + "PRO" + "," + str(PRO_wp) + "," + str(PRO_pp), file=file)
