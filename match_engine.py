### Football match engine

#Test Database
import random
import main

goal_shout = ("GOOOAAALLL!!! ", "OH! WHAT A BANGER!! ", "GOAL! ", "WHAT A STRIKE! ", "INCREDIBLE! ")
missed_shout = ("'s missed the chance to score.", "'s shot is deflected. Unlucky!", " shoots, What a miss!", "'s missed it!")
chance_shout = (" has a shot on goal.", " has a chance to score!", " can capitalize on a mistake.", " can score here.", " can finish it here.")

matchprompt_list = list()
curr_score_list = list()
curr_time_list = list()

chance_range = range(15, 25)
ratingnoise = list(range(-10,11))
timeperiod = list(range(0, 11))
timechoice = list(range(1, 91))
extratimechoice = list(range(90, 121))
xgrange = list(range(5, 12))
timepicked = list()
percent = list(range(0, 100))
possesion_range = list(range(30, 70))
t1score = 0
t2score = 0
attack_factor = 0.36
defense_factor = 0.34
t1coeff = 0
t2coeff = 0
xg1 = 0
xg2 = 0
possesion1 = 0
possesion2 = 0
t1shots = 0
t2shots = 0

def clear_prompt():
    global matchprompt_list, curr_score_list, curr_time_list
    matchprompt_list.clear()
    curr_score_list.clear()
    curr_time_list.clear()

def set_factors(att, dfe):
    global attack_factor, defense_factor
    attack_factor = att/100
    defense_factor = dfe/100
    ("Attack Factor: " + str(attack_factor))
    ("Defense Factor: " + str(defense_factor))

def sim_match(team1rating, team2rating, key):
    global t1rating, t2rating, t1attck, t2attck, t1def, t2def, t1score, t2score, team1chances, team2chances, chance_range, max_timeperiod, attack_factor, defense_factor
    global t1coeff, t2coeff, xg1, xg2, possesion1, possesion2, t1shots, t2shots, matchprompt_list, curr_score_list, curr_time_list
    matchprompt_list.clear()
    curr_score_list.clear()
    curr_time_list.clear()
    max_chance = random.choice(chance_range)
    ("Total Chance: " + str(max_chance))
    t1rating = team1rating
    t2rating = team2rating
    t1attck = t1rating * attack_factor
    t2attck = t2rating * attack_factor
    t1def = t1rating * defense_factor
    t2def = t2rating * defense_factor
    noise1 = random.choice(ratingnoise)
    noise2 = random.choice(ratingnoise)

    ("Team 1 rating: " + str(t1rating))
    ("Team 2 rating: " + str(t2rating))

    t1rating += noise1
    t2rating += noise2
    ("Team 1 rating[with noise]: " + str(t1rating))
    ("Team 2 rating[with noise]: " + str(t2rating))

    t1score = 0
    t2score = 0
    advcoeff = 0
    t1coeff = 0
    t2coeff = 0
    xg1 = 0
    xg2 = 0
    possesion1 = 0
    possesion2 = 0
    t1shots = 0
    t2shots = 0
    
    possesion1 = random.choice(possesion_range)
    possesion2 = 100 - possesion1

    if t1rating >= t2rating:
        diff = abs(t1rating - t2rating)
        advcoeff = float((t2rating - (diff*1.5))/(t1rating + t2rating))
        t1coeff = 1 - advcoeff
        t2coeff = advcoeff
        ("team 1 coefficient: " + str(t1coeff))
        ("team 2 coefficient: " + str(t2coeff))
    
    elif t2rating > t1rating:
        diff = abs(t1rating - t2rating)
        advcoeff = float((t1rating - (diff*1.5))/(t1rating + t2rating))
        t1coeff = advcoeff
        t2coeff = 1 - advcoeff
        ("team 1 coefficient: " + str(t1coeff))
        ("team 2 coefficient: " + str(t2coeff))
    
    team1chances = int(round(t1coeff * max_chance))
    team2chances = int(round(t2coeff * max_chance))
    max_timeperiod = int(team1chances) + int(team2chances)
    ("Team 1 chances: " + str(team1chances))
    ("Team 2 chances: " + str(team2chances))
    (max_timeperiod)
    team1chances = list(range(1, team1chances + 1))
    team2chances = list(range(1, team2chances + 1))
    sim_match2(key)

def sim_match2(key):
    global  t1score, t2score, timechoice, timepicked, timeperiod, max_timeperiod
    ratingnoise = list(range(-10,11))
    (max_timeperiod)
    timeperiod = list(range(0, int(max_timeperiod)))
    (timeperiod)
    timechoice = list(range(1, 91))
    timepicked = list()
    percent = list(range(1, 101))
    t1score = 0
    t2score = 0
    t1score = 0
    t2score = 0
    for i in timeperiod:
        chosentime = random.choice(timechoice)
        timechoice.remove(chosentime)
        timepicked.append(chosentime)
        timepicked.sort()
        (timepicked)
    sim_match3(key)

def team1attempt(team1name, team2name):
    global time, t1score, t1attck, t2def, t1shots, xg1, xgrange, percent, matchprompt_list, curr_score_list, curr_time_list
    chancerate = random.choice(range(-5,6))
    composerate = random.choice(range(-5,6))
    t1_adjusted_attack = t1attck + chancerate
    t2_adjusted_defense =  t2def + composerate
    diff = ((t1_adjusted_attack - t2_adjusted_defense)/1000)
    t1shots += 1
    xg1 += ((random.choice(xgrange))/100)*(t1score+1)
    xg1 = round(xg1, 2) 
    scrcoeff = max(0, min(1, 0.0 + diff))
    scorechance = round(scrcoeff * 100)
    yesgoal = random.choice(percent)
    (scorechance)
    (yesgoal)
    if yesgoal <= scorechance:
        t1score += 1
        matchprompt = (str(random.choice(goal_shout)) + str(team1name) + " scores!")
        curr_score = (str(t1score) + " - " + str(t2score))
        curr_time = (str(time) + "\'")
        matchprompt_list.append(matchprompt)
        curr_score_list.append(curr_score)
        curr_time_list.append(curr_time)
    else:
        matchprompt = (str(team1name) + str(random.choice(missed_shout)))
        curr_score = (str(t1score) + " - " + str(t2score))
        curr_time = (str(time) + "\'")
        matchprompt_list.append(matchprompt)
        curr_score_list.append(curr_score)
        curr_time_list.append(curr_time)
        
def team2attempt(team1name, team2name):
    global time, t2score, t2attck, t1def, t2shots, xg2, xgrange, percent, matchprompt_list, curr_score_list, curr_time_list
    chancerate = random.choice(range(-5,6))
    composerate = random.choice(range(-5,6))
    t2_adjusted_attack = t2attck + chancerate
    t1_adjusted_defense =  t1def + composerate
    diff = ((t2_adjusted_attack - t1_adjusted_defense)/ 1000)
    t2shots += 1
    xg2 += ((random.choice(xgrange))/100)*(t2score+1)
    xg2 = round(xg2, 2) 
    scrcoeff = max(0, min(1, 0.0 + diff))
    scorechance = round(scrcoeff * 100)
    yesgoal = random.choice(percent)
    (scorechance)
    (yesgoal)
    if yesgoal <= scorechance:
        t2score += 1
        matchprompt = (str(random.choice(goal_shout)) + str(team2name) + " scores!")
        curr_score = (str(t1score) + " - " + str(t2score))
        curr_time = (str(time) + "\'")
        matchprompt_list.append(matchprompt)
        curr_score_list.append(curr_score)
        curr_time_list.append(curr_time)
    else:
        matchprompt = (str(team2name) + " missed a chance to score!")
        curr_score = (str(t1score) + " - " + str(t2score))
        curr_time = (str(time) + "\'")
        matchprompt_list.append(matchprompt)
        curr_score_list.append(curr_score)
        curr_time_list.append(curr_time)
        
def sim_match3(key):
    import match_sequence
    team1name = match_sequence.t1name
    team2name = match_sequence.t2name
    for i in timepicked:
        global team1chances, team2chances, time, timeperiod, extratimechoice, max_timeperiod, t1coeff, t2coeff, t1score, t2score, matchprompt_list, curr_score_list, curr_time_list
        time = i
        teampicker = random.choice([1, 2])
        (teampicker)
        if teampicker == 1:
            if len(team1chances) > 0:
                team1chances.remove(random.choice(team1chances))
                matchprompt = (str(team1name) + str(random.choice(chance_shout)))
                curr_score = (str(t1score) + " - " + str(t2score))
                curr_time = (str(time) + "\'")
                matchprompt_list.append(matchprompt)
                curr_score_list.append(curr_score)
                curr_time_list.append("")
                team1attempt(team1name, team2name)
            else:
                team2chances.remove(random.choice(team2chances))
                matchprompt = (str(team2name) + str(random.choice(chance_shout)))
                curr_score = (str(t1score) + " - " + str(t2score))
                curr_time = (str(time) + "\'")
                matchprompt_list.append(matchprompt)
                curr_score_list.append(curr_score)
                curr_time_list.append("")
                team2attempt(team1name, team2name)
        else:
            if len(team2chances) > 0:
                team2chances.remove(random.choice(team2chances))
                matchprompt = (str(team2name) + str(random.choice(chance_shout)))
                curr_score = (str(t1score) + " - " + str(t2score))
                curr_time = (str(time) + "\'")  
                matchprompt_list.append(matchprompt)
                curr_score_list.append(curr_score)
                curr_time_list.append("")
                team2attempt(team1name, team2name)
            else:
                team1chances.remove(random.choice(team1chances))
                matchprompt = (str(team1name) + str(random.choice(chance_shout)))
                curr_score = (str(t1score) + " - " + str(t2score))
                curr_time = (str(time) + "\'")
                matchprompt_list.append(matchprompt)
                curr_score_list.append(curr_score)
                curr_time_list.append("")
                team1attempt(team1name, team2name)
                
    
    if key == 0:
        ("Match Over")
        main.sim_result(t1score, t2score)
    elif key == 1:
        extratimechoice = list(range(90, 121))
        if t1score == t2score:
            extratime_chances = int(round(max_timeperiod/5, 0))
            team1extchances = extratime_chances*t1coeff
            team2extchances = extratime_chances*t2coeff
            max_period_et = int(team2extchances) + int(team1extchances)
            team1extchances = list(range(1, int(team1extchances) + 1))
            team2extchances = list(range(1, int(team2extchances) + 1))
            extratime_period = list(range(0, int(max_period_et)))
            extratimepicked = list()
            for i in extratime_period:
                pickedtime = random.choice(extratimechoice)
                extratimepicked.append(pickedtime)
                extratimechoice.remove(pickedtime)
                extratimepicked.sort()
            ("EXTRA TIME STARTS")
            for i in extratimepicked:
                time = i
                teampicker = random.choice([1, 2])
                (teampicker)
                if teampicker == 1:
                    if len(team1extchances) > 0:
                        team1extchances.remove(random.choice(team1extchances))
                        matchprompt = (str(team1name) + str(random.choice(chance_shout)))
                        curr_score = (str(t1score) + " - " + str(t2score))
                        curr_time = (str(time) + "\'")
                        matchprompt_list.append(matchprompt)
                        curr_score_list.append(curr_score)
                        curr_time_list.append("")
                        team1attempt(team1name, team2name)
                    else:
                        team2extchances.remove(random.choice(team2extchances))
                        matchprompt = (str(team2name) + str(random.choice(chance_shout)))
                        curr_score = (str(t1score) + " - " + str(t2score))
                        curr_time = (str(time) + "\'")
                        matchprompt_list.append(matchprompt)
                        curr_score_list.append(curr_score)
                        curr_time_list.append("")
                        team2attempt(team1name, team2name)
                else:
                    if len(team2extchances) > 0:
                        team2extchances.remove(random.choice(team2extchances))
                        matchprompt = (str(team2name) + str(random.choice(chance_shout)))
                        curr_score = (str(t1score) + " - " + str(t2score))
                        curr_time = (str(time) + "\'")
                        matchprompt_list.append(matchprompt)
                        curr_score_list.append(curr_score)
                        curr_time_list.append("")
                        team2attempt(team1name, team2name)
                    else:
                        team1extchances.remove(random.choice(team1extchances))
                        matchprompt = (str(team1name) + str(random.choice(chance_shout)))
                        curr_score = (str(t1score) + " - " + str(t2score))
                        curr_time = (str(time) + "\'")
                        matchprompt_list.append(matchprompt)
                        curr_score_list.append(curr_score)
                        curr_time_list.append("")
                        team1attempt(team1name, team2name)
        if t1score == t2score:
            yespen = 1
            teampicker = random.choice([1, 2])
            if teampicker == 1:
                main.knockresult(t1score+1, t2score, yespen)
            else:
                main.knockresult(t1score, t2score+1, yespen)
        else:
            yespen = 0
            main.knockresult(t1score, t2score, yespen)

                