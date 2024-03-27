#################################################################################################################
# Author: Alexander Diedrich
# Date: 05.05.2022
# Description: File containing functions to write the generated rules from correlation and from Granger into
# a result file.
#################################################################################################################
def correlationTupleToRules(edges, measurementCols, filename):
    preRules = dict()
    for tp in edges:
        one = tp[0]
        two = tp[1]

        if one in measurementCols:

            if one not in preRules.keys():
                if two not in measurementCols:
                    preRules[one] = [two]
            else:
                if two not in measurementCols:
                    preRules[one].append(two)

    print("preRules: ", preRules)

    file = open(filename, "w")
    for k,v in preRules.items():
        outstr = v[0]
        for predicate in v[1:]:
            outstr+= " AND " + predicate
        outstr += " IMPLIES "
        outstr += k
        file.write(outstr+"\n")
    file.close()

def grangerMatrixToRules(data, COMPONENTS, filename,tau=0.01,  outlist = [], writeFile = True):
    data[data<tau] = 0
    data[data>=tau] = 1
    if writeFile:
        fileRules = open(filename, "w")
    for i in range(0,data.shape[0]):
        outstr=""
        label=str(data.iloc[i,:].name).split("_")[0]
        if label not in COMPONENTS:
            for j in range(0,data.shape[1]):
                if data.iloc[i,j] > 0:
                    name = str(data.columns[j])
                    name = name.replace("_x","")
                    if name in COMPONENTS:
                        if outstr=="":
                            outstr=name
                        else:
                            outstr += " AND " + name
            if outstr!="":
                outstr += " IMPLIES "
                outstr += label
                outlist.append(outstr)
    outlist=list(set(outlist))  

    if writeFile:
        for item in outlist:
            fileRules.write(item+"\n")
        fileRules.close()
    return outlist

def writeFile(filename, outlist):
    outlist=list(set(outlist))  
    fileRules = open(filename, "w")
    for item in outlist:
            fileRules.write(item+"\n")
    fileRules.close()


def ruleCorrector(OBScol, outlist):
    outlist_new = []
    elemsPerSignal = dict()
    print(OBScol)
    for elem in outlist:
        elems = elem.split(" IMPLIES ")
        for signal in OBScol:
            #print("looking for: ", signal)
            if elems[1] in signal:
                if signal in elemsPerSignal:
                    elemsPerSignal[signal].append(elems[0])
                else:
                    elemsPerSignal[signal] = [elems[0]]
             
    for k,v in elemsPerSignal.items():
        string = ""
        for elem in v:
            if string == "":
                string = elem
            else:
                string+= " AND " + elem
        outlist_new.append(string + " IMPLIES " + k)
    return outlist_new
