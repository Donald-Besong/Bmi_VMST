import pytest
import sys
import os
new_wd = os.getcwd() + "/src/"
new_wd2 = os.getcwd() + "/src/donald_besong_bmi_package/"
sys.path.append(new_wd)
sys.path.append(new_wd2)
import donald_besong_bmi_package
from donald_besong_bmi_package import main_argparser, main_program

#*****************begin reading arguments
xparam = main_argparser.xparam
data_source = main_argparser.data_source
nMin = main_argparser.nMin
nMax = main_argparser.nMax
category = main_argparser.category
fullMessage = main_argparser.fullMessage 
nLow_risk = main_argparser.nLow_risk
nVeryHigh_risk = main_argparser.nVeryHigh_risk
file_load_test = main_argparser.file_load_test 
compare_lengths = main_argparser.compare_lengths

A = main_program.A
B = main_program.B
lenA = len(A.pandasDf)
lenB = len(B)
print("here is the whole dataset you requested")
print(A.pandasDf)
print("here is the filtered category")
print(B)
#*****************end reading arguments
def test_file_loaded():
 assert lenA > 0

def test_lenAlenB():
 assert lenB < lenA
 
def test_normal_weight():
 lenB = len(B)
 assert lenB == nLow_risk 

def test_very_severely_obese():
 lenB = len(B)
 assert lenB == nVeryHigh_risk
  
if file_load_test != -1:  
 test_file_loaded()

if compare_lengths != -1:
 test_lenAlenB()
 
if nLow_risk != -1: 
 if category=='normal_weight':
  test_normal_weight()
 else:
  print("nLow_risk is for risk category %s" % category)

if nVeryHigh_risk != -1:
 if category == 'very_severely_obese':
  test_very_severely_obese()
 else:
  print("nVeryHigh_risk is for risk category %s" % category)
  
#python3 tests/first/test_code.py --category=very_severely_obese --nvery_high_risk=0
#python3 tests/first/test_code.py --file_load_test=1 --compare_lengths=1 --category=normal_weight --nlow_risk=2
