import random


match_sequence_list = list()
match_count = 1
team1 = None
team2 = None
t1name = None
t2name = None

def draw_matches(group1, group2, group3, group4, group5, group6, group7, group8, group9, group10, group11, group12):
    global match_sequence_list
    match_sequence_list.append(group1[0])
    match_sequence_list.append(group1[1])
    
    match_sequence_list.append(group1[2])
    match_sequence_list.append(group1[3])
    
    match_sequence_list.append(group2[0])
    match_sequence_list.append(group2[1])
    
    match_sequence_list.append(group4[0])
    match_sequence_list.append(group4[1])
    
    match_sequence_list.append(group2[2])
    match_sequence_list.append(group2[3])
    
    match_sequence_list.append(group3[0])
    match_sequence_list.append(group3[1])
    
    match_sequence_list.append(group3[2])
    match_sequence_list.append(group3[3])
    
    match_sequence_list.append(group4[2])
    match_sequence_list.append(group4[3])
    
    match_sequence_list.append(group5[0])
    match_sequence_list.append(group5[1])
    
    match_sequence_list.append(group5[2])
    match_sequence_list.append(group5[3])
    
    match_sequence_list.append(group6[0])
    match_sequence_list.append(group6[1])
    
    match_sequence_list.append(group6[2])
    match_sequence_list.append(group6[3])
    
    match_sequence_list.append(group7[0])
    match_sequence_list.append(group7[1])
    
    match_sequence_list.append(group7[2])
    match_sequence_list.append(group7[3])
    
    match_sequence_list.append(group8[0])
    match_sequence_list.append(group8[1])
    
    match_sequence_list.append(group8[2])
    match_sequence_list.append(group8[3])
    
    match_sequence_list.append(group9[0])
    match_sequence_list.append(group9[1])
    
    match_sequence_list.append(group9[2])
    match_sequence_list.append(group9[3])
    
    match_sequence_list.append(group10[0])
    match_sequence_list.append(group10[1])
    
    match_sequence_list.append(group10[2])
    match_sequence_list.append(group10[3])
    
    match_sequence_list.append(group11[0])
    match_sequence_list.append(group11[1])
    
    match_sequence_list.append(group11[2])
    match_sequence_list.append(group11[3])
    
    match_sequence_list.append(group12[0])
    match_sequence_list.append(group12[1])
    
    match_sequence_list.append(group12[2])
    match_sequence_list.append(group12[3])
    
    match_sequence_list.append(group1[3])
    match_sequence_list.append(group1[1])
    
    match_sequence_list.append(group1[0])
    match_sequence_list.append(group1[2])
    
    match_sequence_list.append(group2[3])
    match_sequence_list.append(group2[1])
    
    match_sequence_list.append(group2[0])
    match_sequence_list.append(group2[2])
    
    match_sequence_list.append(group3[3])
    match_sequence_list.append(group3[1])
    
    match_sequence_list.append(group3[0])
    match_sequence_list.append(group3[2])
    
    match_sequence_list.append(group4[3])
    match_sequence_list.append(group4[1])
    
    match_sequence_list.append(group4[0])
    match_sequence_list.append(group4[2])
    
    match_sequence_list.append(group5[3])
    match_sequence_list.append(group5[1])
    
    match_sequence_list.append(group5[0])
    match_sequence_list.append(group5[2])
    
    match_sequence_list.append(group6[3])
    match_sequence_list.append(group6[1])
    
    match_sequence_list.append(group6[0])
    match_sequence_list.append(group6[2])
    
    match_sequence_list.append(group7[3])
    match_sequence_list.append(group7[1])
    
    match_sequence_list.append(group7[0])
    match_sequence_list.append(group7[2])
    
    match_sequence_list.append(group8[3])
    match_sequence_list.append(group8[1])
    
    match_sequence_list.append(group8[0])
    match_sequence_list.append(group8[2])
    
    match_sequence_list.append(group9[3])
    match_sequence_list.append(group9[1])
    
    match_sequence_list.append(group9[0])
    match_sequence_list.append(group9[2])
    
    match_sequence_list.append(group10[3])
    match_sequence_list.append(group10[1])
    
    match_sequence_list.append(group10[0])
    match_sequence_list.append(group10[2])
    
    match_sequence_list.append(group11[3])
    match_sequence_list.append(group11[1])
    
    match_sequence_list.append(group11[0])
    match_sequence_list.append(group11[2])
    
    match_sequence_list.append(group12[3])
    match_sequence_list.append(group12[1])
    
    match_sequence_list.append(group12[0])
    match_sequence_list.append(group12[2])
    
    match_sequence_list.append(group1[3])
    match_sequence_list.append(group1[0])
    
    match_sequence_list.append(group1[1])
    match_sequence_list.append(group1[2])
    
    match_sequence_list.append(group2[3])
    match_sequence_list.append(group2[0])
    
    match_sequence_list.append(group2[1])
    match_sequence_list.append(group2[2])
    
    match_sequence_list.append(group3[3])
    match_sequence_list.append(group3[0])
    
    match_sequence_list.append(group3[1])
    match_sequence_list.append(group3[2])
    
    match_sequence_list.append(group4[3])
    match_sequence_list.append(group4[0])
    
    match_sequence_list.append(group4[1])
    match_sequence_list.append(group4[2])
    
    match_sequence_list.append(group5[3])
    match_sequence_list.append(group5[0])
    
    match_sequence_list.append(group5[1])
    match_sequence_list.append(group5[2])
    
    match_sequence_list.append(group6[3])
    match_sequence_list.append(group6[0])
    
    match_sequence_list.append(group6[1])
    match_sequence_list.append(group6[2])
    
    match_sequence_list.append(group7[3])
    match_sequence_list.append(group7[0])
    
    match_sequence_list.append(group7[1])
    match_sequence_list.append(group7[2])
    
    match_sequence_list.append(group8[3])
    match_sequence_list.append(group8[0])
    
    match_sequence_list.append(group8[1])
    match_sequence_list.append(group8[2])
    
    match_sequence_list.append(group9[3])
    match_sequence_list.append(group9[0])
    
    match_sequence_list.append(group9[1])
    match_sequence_list.append(group9[2])
    
    match_sequence_list.append(group10[3])
    match_sequence_list.append(group10[0])
    
    match_sequence_list.append(group10[1])
    match_sequence_list.append(group10[2])
    
    match_sequence_list.append(group11[3])
    match_sequence_list.append(group11[0])
    
    match_sequence_list.append(group11[1])
    match_sequence_list.append(group11[2])
    
    match_sequence_list.append(group12[3])
    match_sequence_list.append(group12[0])
    
    match_sequence_list.append(group12[1])
    match_sequence_list.append(group12[2])
    
    ("Group Matches Drawn")
    (match_sequence_list)

def draw_knockout_32(group1, group2, group3, group4, group5, group6, group7, group8, group9, group10, group11, group12, third_place_teams):
    global match_sequence_list
    ("Third Placed Teams")
    (third_place_teams)
    
    #M1
    match_sequence_list.append(group1[1])
    match_sequence_list.append(group2[1])
    #M2
    match_sequence_list.append(group3[0])
    match_sequence_list.append(group6[1])
    #M3
    match_sequence_list.append(group6[0])
    match_sequence_list.append(group3[1])
    #M4
    match_sequence_list.append(group5[1])
    match_sequence_list.append(group9[1])
    #M5
    match_sequence_list.append(group5[0])
    temp_hold = random.choice(third_place_teams)
    match_sequence_list.append(temp_hold)
    third_place_teams.remove(temp_hold)
    #M6
    match_sequence_list.append(group1[0])
    temp_hold = random.choice(third_place_teams)
    match_sequence_list.append(temp_hold)
    third_place_teams.remove(temp_hold)
    #M7
    match_sequence_list.append(group9[0])
    temp_hold = random.choice(third_place_teams)
    match_sequence_list.append(temp_hold)
    third_place_teams.remove(temp_hold)
    #M8
    match_sequence_list.append(group12[0])
    temp_hold = random.choice(third_place_teams)
    match_sequence_list.append(temp_hold)
    third_place_teams.remove(temp_hold)
    #M9
    match_sequence_list.append(group4[0])
    temp_hold = random.choice(third_place_teams)
    match_sequence_list.append(temp_hold)
    third_place_teams.remove(temp_hold)
    #M10
    match_sequence_list.append(group2[0])
    temp_hold = random.choice(third_place_teams)
    match_sequence_list.append(temp_hold)
    third_place_teams.remove(temp_hold)
    #M11
    match_sequence_list.append(group7[0])
    temp_hold = random.choice(third_place_teams)
    match_sequence_list.append(temp_hold)
    third_place_teams.remove(temp_hold)
    #M12
    match_sequence_list.append(group10[0])
    match_sequence_list.append(group8[1])
    #M13
    match_sequence_list.append(group11[1])
    match_sequence_list.append(group12[1])
    #M14
    match_sequence_list.append(group4[1])
    match_sequence_list.append(group7[1])
    #M15
    match_sequence_list.append(group8[0])
    match_sequence_list.append(group10[1])
    #M16
    match_sequence_list.append(group11[0])
    temp_hold = random.choice(third_place_teams)
    match_sequence_list.append(temp_hold)
    third_place_teams.remove(temp_hold)
    
    ("Round of 32 Matches Drawn")
    (match_sequence_list)
    
    ("ERRORS IF YES---------")
    (third_place_teams)  

def draw_knockout_16(winners_knockout):
    global match_sequence_list
    (winners_knockout)
    ("-----------------------------MATCHES DRAWN--------------------------------") 
    #M1
    team1picked = random.choice(winners_knockout)
    match_sequence_list.append(team1picked)
    winners_knockout.remove(team1picked)
    team2picked = random.choice(winners_knockout)
    match_sequence_list.append(team2picked)
    winners_knockout.remove(team2picked)
   
    #M2
    team1picked = random.choice(winners_knockout)
    match_sequence_list.append(team1picked)
    winners_knockout.remove(team1picked)
    team2picked = random.choice(winners_knockout)
    match_sequence_list.append(team2picked)
    winners_knockout.remove(team2picked)
    
    #M3
    team1picked = random.choice(winners_knockout)
    match_sequence_list.append(team1picked)
    winners_knockout.remove(team1picked)
    team2picked = random.choice(winners_knockout)
    match_sequence_list.append(team2picked)
    winners_knockout.remove(team2picked)
    
    #M4
    team1picked = random.choice(winners_knockout)
    match_sequence_list.append(team1picked)
    winners_knockout.remove(team1picked)
    team2picked = random.choice(winners_knockout)
    match_sequence_list.append(team2picked)
    winners_knockout.remove(team2picked)
    
    #M5
    team1picked = random.choice(winners_knockout)
    match_sequence_list.append(team1picked)
    winners_knockout.remove(team1picked)
    team2picked = random.choice(winners_knockout)
    match_sequence_list.append(team2picked)
    winners_knockout.remove(team2picked)
    
    #M6
    team1picked = random.choice(winners_knockout)
    match_sequence_list.append(team1picked)
    winners_knockout.remove(team1picked)
    team2picked = random.choice(winners_knockout)
    match_sequence_list.append(team2picked)
    winners_knockout.remove(team2picked)
    
    #M7
    team1picked = random.choice(winners_knockout)
    match_sequence_list.append(team1picked)
    winners_knockout.remove(team1picked)
    team2picked = random.choice(winners_knockout)
    match_sequence_list.append(team2picked)
    winners_knockout.remove(team2picked)
    
    #M8
    team1picked = random.choice(winners_knockout)
    match_sequence_list.append(team1picked)
    winners_knockout.remove(team1picked)
    team2picked = random.choice(winners_knockout)
    match_sequence_list.append(team2picked)
    winners_knockout.remove(team2picked)
    ("-----------------------------MATCHES DRAWN--------------------------------") 
    (match_sequence_list)

def draw_knockout_8(winners_knockout):
    #M1
    team1picked = random.choice(winners_knockout)
    match_sequence_list.append(team1picked)
    winners_knockout.remove(team1picked)
    team2picked = random.choice(winners_knockout)
    match_sequence_list.append(team2picked)
    winners_knockout.remove(team2picked)
    
    #M2
    team1picked = random.choice(winners_knockout)
    match_sequence_list.append(team1picked)
    winners_knockout.remove(team1picked)
    team2picked = random.choice(winners_knockout)
    match_sequence_list.append(team2picked)
    winners_knockout.remove(team2picked)
    
    #M3
    team1picked = random.choice(winners_knockout)
    match_sequence_list.append(team1picked)
    winners_knockout.remove(team1picked)
    team2picked = random.choice(winners_knockout)
    match_sequence_list.append(team2picked)
    winners_knockout.remove(team2picked)

    #M4
    team1picked = random.choice(winners_knockout)
    match_sequence_list.append(team1picked)
    winners_knockout.remove(team1picked)
    team2picked = random.choice(winners_knockout)
    match_sequence_list.append(team2picked)
    winners_knockout.remove(team2picked)
        
def draw_knockout_4(winners_knockout): 
    #M1
    team1picked = random.choice(winners_knockout)
    match_sequence_list.append(team1picked)
    winners_knockout.remove(team1picked)
    team2picked = random.choice(winners_knockout)
    match_sequence_list.append(team2picked)
    winners_knockout.remove(team2picked)
    
    #M2
    team1picked = random.choice(winners_knockout)
    match_sequence_list.append(team1picked)
    winners_knockout.remove(team1picked)
    team2picked = random.choice(winners_knockout)
    match_sequence_list.append(team2picked)
    winners_knockout.remove(team2picked)
    
def draw_finals(winners_knockout, losers_knockout):
    #M1
    team1picked = random.choice(losers_knockout)
    match_sequence_list.append(team1picked)
    losers_knockout.remove(team1picked)
    team2picked = random.choice(losers_knockout)
    match_sequence_list.append(team2picked)
    losers_knockout.remove(team2picked)
    
    #M2
    team1picked = random.choice(winners_knockout)
    match_sequence_list.append(team1picked)
    winners_knockout.remove(team1picked)
    team2picked = random.choice(winners_knockout)
    match_sequence_list.append(team2picked)
    winners_knockout.remove(team2picked)


def parse_data():
        global match_count, team1, team2, t1name, t2name, tr1, tr2
        team1 = match_sequence_list.pop(0)
        team2 = match_sequence_list.pop(0)
        t1name = str(team1[0]).upper() 
        t2name = str(team2[0]).upper()
        tr1 = team1[1]  
        tr2 = team2[1]
        diff = abs(tr1 - tr2)
        (f"MATCH ({match_count}): {t1name} vs {t2name} | TR Difference: {diff}")
        match_count += 1  
