import argparse
import pandas as pd
import re
import os

dataset = []
tickers = []
def run_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', help="Input datafile used for backtester")
    parser.add_argument('--start-time', help="Set the start time for data input")
    parser.add_argument('--end-time', help="Set the end time for data input")
    parser.add_argument('--current-dir', help="Select all csv files in current directory")
    args = parser.parse_args()
    if(args.file is not None and args.current_dir is None):
        try:
            data = pd.read_csv(args.file)
            data.set_index(['timestamp'], inplace=True)
            data = data.iloc[::-1]
            # Check to see if start and end time specified
            if args.start_time in data.index:
                if args.end_time in data.index:
                    data = data.loc[args.end_time:args.start_time]
                    dataset.append(data)
                else:
                    print("No end time specified")
                    indexes = data.index.get_values()
                    data = data.loc[indexes[0]:args.start_time]
                    dataset.append(data)
            else:
                dataset.append(data)
            # m = re.search("(?<=_)([A-Z]*)(?=.csv)", str(args.file))
            m = str(args.file)
            print(m)
            tickers.append(m.group(0))
        except:
            print("File could not be found or opened")

    elif(args.file is None and args.current_dir is not None):
       for file in os.listdir("./"):
           print(file)
           if file.endswith(".csv"):
               try:
                    temp = pd.read_csv(file)
                    temp = temp.iloc[::-1]
                    temp.set_index(['timestamp'], inplace=True)
               except:
                    print(file + " could not be processed")
                   # Check to see if start and end time specified
               if args.start_time in temp.index:
                   if args.end_time in temp.index:
                        temp = temp.loc[args.end_time:args.start_time]
                   else:
                        print("No end time specified")
                        indexes = temp.index.get_values()
                        temp = temp.loc[indexes[0]:args.start_time]

               dataset.append(temp)
               m = re.search("(?<=_)([A-Z]*)(?=.csv)", str(file))
               tickers.append(m.group(0))
        

                   
def get_data():
    market_data = dict()
    count = 0
    for ticker in tickers:
        market_data[ticker] = dataset[count]
        count += 1
    return market_data 
