import argparse
from FileFormat import FileFormat
import pandas as pd
import os
from scipy import stats
import numpy as np

def diff_custom(x):
    vals = [get_fps(x[n],x[n+1]) for n in range(x.shape[0]-1)]
    ret = [0]
    ret = vals + ret
    return(ret)

def get_fps(t1, t2):
    return 1 / (t2 -t1).total_seconds()
    
def analyze(data_dir):
    suffix = '.json'
    fs = [x.rstrip(suffix) for x in os.listdir(data_dir) 
        if x.endswith(suffix)]
    fs.sort()
    
    data = {}
    for f in fs:
        ff = FileFormat.from_string(f)
        if ff.time not in data:
            data[ff.time] = 0
        data[ff.time] += 1
    
    df = pd.DataFrame(data.items(), columns=['time', 'num_faces'])
    fps = df[['time']].apply(diff_custom, axis=0)
    df['fps'] = fps

    df['norm_fps'] = df['fps'] * df['num_faces']

    # remove outliers
    df = df[(np.abs(stats.zscore(df['norm_fps'])) < 3)]

    # save plots
    ax = df.plot(x='time', y='fps')
    fig = ax.get_figure()
    fig.savefig('fps.jpg')

    ax = df.plot(x='time', y='norm_fps')
    fig = ax.get_figure()
    fig.savefig('norm_fps.jpg')
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=str, default='data')
    args = parser.parse_args()

    analyze(args.data)
    