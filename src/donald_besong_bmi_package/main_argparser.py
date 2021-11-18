import argparse
import sys
import os
#import pathlib
#file_dir = pathlib.Path('__file__').parent.absolute()
#print(file_dir)
#new_wd = os.path.abspath(os.curdir)
new_wd = os.getcwd()

def mainParsArgs(arg):
    parser = argparse.ArgumentParser(description="testing...")
    parser.add_argument('--xparam', help='this is just a test', default=10)
    parser.add_argument('--json_source', help='data source', default=new_wd + '/src/donald_besong_bmi_package/data/data.json')
    parser.add_argument('--nmin', help='starting row', default=0)
    parser.add_argument('--nmax', help='ending row', default=5)
    parser.add_argument('--category', help='category/health risk level', default='normal_weight')
    parser.add_argument('--full_message', help='print dataframe', default=0)
    parser.add_argument('--nvery_high_risk', help='very high risk value', default=-1)
    parser.add_argument('--nlow_risk', help='low risk value', default=-1)
    parser.add_argument('--file_load_test', help='test if file is loaded', default=-1)
    parser.add_argument('--compare_lengths', help='compare lengths of filtered and whole', default=-1)
    return parser.parse_args(arg)

my_args = mainParsArgs(sys.argv[1:])
#*****************begin reading arguments
data_source = my_args.json_source
nMin = int(my_args.nmin)
nMax = int(my_args.nmax)
category = my_args.category
fullMessage = int(my_args.full_message)
nVeryHigh_risk = int(my_args.nvery_high_risk)
nLow_risk = int(my_args.nlow_risk) 
xparam = int(my_args.xparam)
file_load_test = int(my_args.file_load_test) 
compare_lengths = int(my_args.compare_lengths)   
#*****************end reading arguments
