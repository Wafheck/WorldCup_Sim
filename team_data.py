import country_data

country_forgoals_dict = {}
country_againstgoals_dict = {}
country_appearances_dict = {}
curr_rank_dict = {}
avg_rank_dict = {}

for country in country_data.world:
    country_forgoals_dict[country] = list()
    country_againstgoals_dict[country] = list()
    country_appearances_dict[country] = list()
    curr_rank_dict[country] = list()
    avg_rank_dict[country] = list()


def podium_stats(team1, team2, team3):
    global rank1, rank2, rank3, curr_rank_dict, latest_againstgoals_team1, latest_againstgoals_team2, latest_againstgoals_team3, latest_forgoals_team1, latest_forgoals_team2, latest_forgoals_team3
    country_forgoals_dict[team1].sort(key=lambda x: x[1])
    country_forgoals_dict[team2].sort(key=lambda x: x[1])
    country_forgoals_dict[team3].sort(key=lambda x: x[1])
    
    country_againstgoals_dict[team1].sort(key=lambda x: x[1])
    country_againstgoals_dict[team2].sort(key=lambda x: x[1])
    country_againstgoals_dict[team3].sort(key=lambda x: x[1])

    latest_forgoals_team1 = country_forgoals_dict[team1][-1][0]
    latest_forgoals_team2 = country_forgoals_dict[team2][-1][0]
    latest_forgoals_team3 = country_forgoals_dict[team3][-1][0]
    
    latest_againstgoals_team1 = country_againstgoals_dict[team1][-1][0]
    latest_againstgoals_team2 = country_againstgoals_dict[team2][-1][0]
    latest_againstgoals_team3 = country_againstgoals_dict[team3][-1][0]
    
    rank1 = curr_rank_dict[team1][-1][0]
    rank2 = curr_rank_dict[team2][-1][0]
    rank3 = curr_rank_dict[team3][-1][0]

        
    