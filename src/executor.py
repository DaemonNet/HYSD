#################################################################################################################
# Author: Alexander Diedrich
# Initial Date: 05.05.2022
# Updated: 27.03.2024
# Description: Main file to run experiments. All generated files will be written into folder "output".
# Each step generates its own files, which are plaintext and can be inspected. This file performs correlation
# and Granger Causality analysis, and executes diagnosis on simulated (random observations are set to faulty)
# and real fault data (taken from the input process data). 
# NOTE: COMPS.csv must be filled out. Unused Granger and Correlation files can be commented out. 
# All files in "output" folder are generated automatically
#################################################################################################################

import random


#Diagnosis

from manualDiagEval import ManualExecution
from diagExecution import *


if __name__ == '__main__': 
    random.seed(1337)
    logfile = open("output/diag.log", "w")
    
    #Run Reiter's HS-tree diagnsosi algorithm on simulated observations.
    diag = diagExecution()
    logfile.write("Reiter \n")
    diag.runDiagnosisReiter_simulatedObs(logfile)


    logfile.flush() #Save what we got so far

    #An execution script for using real observations, as these are very customized

    manExe = ManualExecution(logfile, outpath ="output\\")
    
    
    print("----------------------------------------Granger MODELS------------------------------------------------")
    print("ONE TANK")
    logfile.write("ONE TANK\n")
    manExe.tanks("ONETANK","output\\GrangerOneTankOnePump.txt","..\\data\\tanks\\S1_OneTankOnePump\\*.csv", "..\\data\\tanks\\S1_OneTankOnePump\\COMPS.csv", startIndex=50)
    print("THREE TANK")
    logfile.write("THREE TANK\n")
    manExe.tanks("THREETANK","output\\GrangerThreeTanksTwoPumps.txt","..\\data\\tanks\\S2_ThreeTanksTwoPumps\\*.csv", "..\\data\\tanks\\S2_ThreeTanksTwoPumps\\COMPS.csv", startIndex=50)
    print("FOUR TANK")
    logfile.write("FOUR TANK\n")
    manExe.tanks("FOURTANK","output\\GrangerFourTanksEightValves.txt", "..\\data\\tanks\\S3_FourTanksEightValves\\*.csv", "..\\data\\tanks\\S3_FourTanksEightValves\\COMPS.csv", startIndex=50)
    print("One Tank Filling")
    logfile.write("One Tank Filling\n")
    manExe.tanks("FILLING","output\\GrangerOneTankFillingSystem.txt","..\\data\\tanks\\S4_OneTankFillingSystem\\*.csv", "..\\data\\tanks\\S4_OneTankFillingSystem\\COMPS.csv", startIndex=50)
    print("DS1")
    logfile.write("DS1\n")
    manExe.tanks("DS1","output\\Grangerds1.txt","..\\data\\ds1\\*.csv", "..\\data\\ds1\\COMPS.csv", startIndex=1000)
    print("DS2")
    logfile.write("DS2\n")
    manExe.tanks("DS2","output\\Grangerds2.txt","..\\data\\ds2\\*.csv", "..\\data\\ds2\\COMPS.csv", startIndex=1000)
    print("DS3")
    logfile.write("DS3\n")
    manExe.tanks("DS3","output\\Grangerds3.txt", "..\\data\\ds3\\*.csv", "..\\data\\ds3\\COMPS.csv", startIndex=1000)
    print("DS4")
    logfile.write("DS4\n")
    manExe.tanks("DS4","output\\Grangerds4.txt", "..\\data\\ds4\\*.csv", "..\\data\\ds4\\COMPS.csv", startIndex=1000)

    
    #logfile.write("TE\n")
    manExe.TE(prefix="TE",modelPath="output\\GrangerTennesseeEastman.txt", dataPath="../data/1_Tests/", startIndex=100)

    #Add-On functionality

    
    logfile.close()