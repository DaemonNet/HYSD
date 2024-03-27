#################################################################################################################
# Author: Alexander Diedrich
# Date: 05.05.2022
# Description: Generates fault hypothesis which can be used with Reiter's HS-tree. 
# Conflicts are generated if obs are faulty. We are parsing sympy expressions.
#################################################################################################################

class HypothesesGenerator():

    def generateConflicts2(self, rules, obs):
        conflictSets = []
        for ob,val in obs.items():
            #print(ob, val)
            if not val: #fault
                for rule in rules:
                    if rule.implicant in ob:
                        conflictSets.append(set(rule.predicates))
        return conflictSets


    def generateLegacy(self, rules, obs):
        conflictSets = []
        for ob,val in obs.items():
            if val: #fault
                for rule in rules:
                    for imp in rule.implicant.free_symbols: #there is only one item here. So we break
                        if str(ob).startswith(str(imp)):
                            conflictSets.append(rule.predicates.free_symbols)
                            break
        return conflictSets

        
