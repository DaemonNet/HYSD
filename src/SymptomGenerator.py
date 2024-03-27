#################################################################################################################
# Author: Alexander Diedrich
# Date: 05.05.2022
# Description: Generates fake symptoms. True means a fault exists.
#################################################################################################################
import numpy as np
from Parser import replacer

class SymptomGenerator():

    def getFakeSymptoms(self, rules, probability=0.5, returnStringKeys=False):
        allSymptoms = {}

        if hasattr(rules, 'values'):  # dict-like
            for v in rules.values():
                allSymptoms[v.implicant] = False
        else:  # list-like
             for rule in rules:  # dict-like
                allSymptoms[rule.implicant] = False
        
        # set symtoms to True with given probability
        samples = np.random.binomial(1, probability, size=len(allSymptoms))
        indices, = np.where(samples)

        keys = tuple(allSymptoms.keys())
        for i in indices:
            allSymptoms[keys[i]] = True

        if returnStringKeys:
            return self.convertToStringKeys(allSymptoms)
        return allSymptoms

    def writeQuantumObservations(self, values_dict, rulesfile, outfile):

        f = open(rulesfile, "r")
        alllines = f.readlines()

        out = []

        for k,v in values_dict.items():
            for line in alllines:
                line = replacer(line)
                k = str(k)
                new_v = None
                if v == True:
                    new_v= " F "
                else:
                    new_v= " T "
                if k in line:
                    newline = line.replace(k,new_v)
                    out.append(newline)
                    break
            
        f.close()
        f = open("output/"+outfile, "w")
        for line in out:
            f.writelines(line)
        f.close()


    def convertToStringKeys(self, symptom_dict):
        newdict = dict()
        for k,v in symptom_dict.items():
            newdict[str(k)] = v
        return newdict

    def getNoSymptoms(self, rules):
        allSymptoms = dict()
        for v in rules.values():
            allSymptoms[v.implicant] = False

        return allSymptoms
