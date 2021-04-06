import pandas as pd
import numpy as np
import math
import csv

# get mean of certain pose from trainning set
def pose_mean(pose, col):
    df = pd.read_csv("train.csv", header=None)
    df = df.replace(9999, np.nan)
    gb = df.groupby(0)
    data = gb.get_group(pose)
    mu = round(data[col].mean(), 10)
    #print(mu)
    return mu

# get stdev of certain pose from trainning set
def pose_stdv(pose, col):
    df = pd.read_csv("train.csv", header=None)
    df = df.replace(9999, np.nan)
    gb = df.groupby(0)
    data = gb.get_group(pose)
    sig = round(data[col].std(), 10)
    #print(sig)
    return sig

# get all types of poses so that when compare diff prob can easily find
def all_pose():
    df = pd.read_csv("test.csv", header=None)
    pose_list = []
    for i in df[0]:
        if i not in pose_list:
            pose_list.append(i)
        else:
            continue
    #print(pose_list)
    return pose_list

# the prior prob of inputed pose
def prior(pose):
    df = pd.read_csv("train.csv", header=None)
    posedict = {}
    for i in df[0]:
        if i not in posedict:
            posedict[i] = 1
        else:
            posedict[i] += 1
    prob = round(posedict[pose] / len(df[0]), 10)
    #print(prob)
    return prob


# calculate the total prob that a certain pose has
def prob(pose, xbar, col):
    mu = pose_mean(pose, col)
    sig = pose_stdv(pose, col)
    down = 1 / (sig * math.sqrt(2 * math.pi))
    up = math.exp(-0.5 * ((xbar - mu) / sig) ** 2)
    norm = down * up
    p = round(norm, 10)
    #print(p)
    return p

def pred():
    df = pd.read_csv("test.csv", header=None)
    df2 = df.copy()
    del df2[0]
    tot_num = len(df2)
    keylist = []
    for row in range(0, tot_num):
        print(row)
        tot_prob = 0
        compdict = {}
        for col in df2:
            xbar = df2.iloc[row][col]
            if xbar == 9999:
                continue
            for pose in all_pose():
                if pose not in compdict:
                    compdict[pose] = prior(pose) * prob(pose, xbar, col)

                else:
                    compdict[pose] *= prob(pose, xbar, col)

        if compdict:
            keymax = max(compdict, key=compdict.get)
            keylist.append(keymax)
            print(keymax)

        else:
            keylist.append('NoData')
            print('NO DATA AVAILABLE')

    listFile = open('pred.csv', 'a', newline='')
    writer = csv.writer(listFile)
    for item in keylist:
        writer.writerow([item])

#return true pos
def evaluation():
    df1 = pd.read_csv("test.csv", header=None)
    df2 = pd.read_csv("pred.csv", header=None)
    same = 0
    count = 0
    for i in df2[0]:
        if i != "NoData":
            count += 1
    for i in df1[0] == df2[0]:
        if i == True:
            same += 1
    print(same / count)

def __main__():
    #pose_mean('bridge', 1)
    #pose_stdv('bridge', 1)
    #prior('childs')
    #prob('bridge', 0)
    #pred()
    evaluation()
__main__()
