<div id="top"></div>
<!--
*** Thanks for checking out my project
*** Dr Donald O. Besong
-->


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="http://github.com/Donald-Besong/BMI_Calculations">
    <img src="src/data/images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Donald's cake shelf</h3>

  <p align="center">
    project_description
    <br />
    <a href="http://github.com/Donald-Besong/BMI_Calculations"><strong>Explore the docs »</strong></a>
  </p>
</div>



<!-- GETTING STARTED -->
## Getting Started

Instructions


1. Clone the repository

2a. virtualenv -p python3 vmst_env3

2b. virtualenv -p python3 vmst_env3
   . vmst_env3/bin/activate

3. Instal python packages using pip.requirements.txt in your python3
environment   
4. Make sure that in your command line, you are in the root folder, which contains
   requirements.txt, and all the code. 

5. Run a command the following command, changing the argument values:
python3 main_program.py --json_source=<full path to json file> --nmin=1 --nmax=4 --category=normal_weight --full_message=1
Here are the arguments to run the code:
  json_source: This should be thevfull path to json file. The default is 
     /src/donald_besong_bmi_package/data/data.json, relative to the root. 
     However, you can provide the full path to any json file in any location
  nmin: This is the row number from which you want to load the data. Default is 0
  nmax: This is the row number up to which you want to load the data. Default is 5
        This is because your json dataset might be too large. The code is optimising
        the reading of your json dataset with ijson.
  category:  This is the filter you require in the exercise.
             The value should be one of the following:
              under_weight, 
              normal_weight, 
              over_weight, 
              moderately_obese, 
              severely_obese, 
              very_severely_obese 
     
  full_message: This tells the program to either print a full message 
              regarding your filtered results, or only print the number
              of people in that category
            
    
TESTING Only:
Run this command
 python3 tests/first/test_code.py --file_load_test=1 --compare_lengths=1 --category=normal_weight --nlow_risk=2
  json_source: This uses the default, so do not enter this parameter when testing.
            The above default file used for testing. If you would like to do the testing
            for other data, replace this folder with same name.
  file_load_test: This is to tell the test to check if your json file has been loaded (trivial)
  compare_lengths: This is to tell the test to assert that the filtered data is s
            shorter than the entire data 
  category: same as above
  nlow_risk: This is the expected value for the number of people in --category=normal_weight
  nvery_high_risk: This is the expected value for the number of people in --category=very_severely_obese
  
  ***Note***
  Manually do calculations on the test json file (default), find out values for
  nlow_risk and nvery_high_risk. Those are the expected values you should use
  in the test command. You must also use them in conjuction with
  the appropriate category 
     
     
    

Note: I am assuming your environment is python3 from virtualenv -p in bullet point 3
5. Please note that your json dataset might be too large. The code is optimising
the reading of your json dataset with ijson. Further, it will select a range 
of rows you specify by:
 nmin is the row from which you want to view the data/or perform calculations
 nmax is the row up to which you need the filter, as nmin
 category is should be under_weight, normal_weight, over_weight, moderately_obese, severely_obese, or very_severely_obese 
 i.e. category is the filter you require in the exercise
