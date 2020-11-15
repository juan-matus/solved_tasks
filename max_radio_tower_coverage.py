#Here i use greedy algorithm

states = {
        'wyoming': 0,
        'colorado': 0,
        'connecticut': 0,
        'alabama': 0,
        'alaska': 0,
        'washington': 0,
        'massachusetts': 0,
        'seattle': 0,
        'losAngeles': 0,
        'kalifornia': 0,
        }

radioTowers = {
        'a':{'washington':40, 'alabama':30, 'connecticut':50},
        'b':{'seattle':50, 'losAngeles':60, 'connecticut':70},
        'c':{'massachusetts':30, 'alaska':70, 'colorado':70},
        'd':{'seattle':50, 'kalifornia':60, 'wyoming':70}
        }

finalTowers = []

while 0 in states.values():

    unreachedStates = [state for state,value in states.items() if value == 0]

    coverageOfTowers = {}
    
    for tower in radioTowers:
    
        coverageOfTowers[tower] = 0
        
        for state,reached in radioTowers[tower].items():
            if state in unreachedStates:
                coverageOfTowers[tower] += reached
    
    #tower with max covearge
    maxtower = ''.join([k for k,v in coverageOfTowers.items() if v == max(coverageOfTowers.values())][:1])
    
    for state, reached in radioTowers[maxtower].items():
        states[state] += reached
    
    finalTowers.append(maxtower)
    
    del radioTowers[maxtower]

print(states,'\n', finalTowers)
