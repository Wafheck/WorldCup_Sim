import country_data
import webbrowser
import time
import random
import pygame
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sys
sys.setrecursionlimit(150000)

### INITIALIZE COUNTRY DATA ###
asia = country_data.asian_countries
africa = country_data.african_countries
europe = country_data.european_countries
north_america = country_data.northamerican_countries
oceania = country_data.oceanian_countries
south_america = country_data.southamerican_countries
sorted_asia = sorted(asia.items(), key=lambda item: item[1], reverse=True)
sorted_africa = sorted(africa.items(), key=lambda item: item[1], reverse=True)
sorted_europe = sorted(europe.items(), key=lambda item: item[1], reverse=True)
sorted_north_america = sorted(north_america.items(), key=lambda item: item[1], reverse=True)
sorted_oceania = sorted(oceania.items(), key=lambda item: item[1], reverse=True)
sorted_south_america = sorted(south_america.items(), key=lambda item: item[1], reverse=True)
world = {**asia, **africa, **europe, **north_america, **oceania, **south_america}
ordered_world = sorted(world.items(), key=lambda item: item[1], reverse=True)
sorted_teams_top = "\n".join([f"{rank+1}. {team} [{rating}]" for rank, (team, rating) in enumerate(ordered_world[:40])])
goal_diff = {team: 0 for team in world}
wins_no = {team: 0 for team in world}
draws_no = {team: 0 for team in world}
losses_no = {team: 0 for team in world}
points_no = {team: 0 for team in world}
played_no = {team: 0 for team in world}
forgoals = {team: 0 for team in world}
againstgoals = {team: 0 for team in world}
appearances = {team: 0 for team in world}
rank = {team: 0 for team in world}
ecycle = 0

### INITIALIZE TKINTER ###
root = Tk()
root.title("World Cup Simulator")
root.geometry("1920x1080")
root.attributes("-fullscreen", True)
icon = PhotoImage(file="misc/world_cup.png")
root.iconphoto(False, icon)
root.configure(bg='black')
icon = PhotoImage(file="icon.png")
root.iconphoto(False, icon)
### INITIALIZE BACKGROUND ###
left_canvas = Canvas(root, bg='red', highlightthickness=0)
right_canvas = Canvas(root, bg='blue', highlightthickness=0)
center_canvas = Canvas(root, bg='black', highlightthickness=0)
left_canvas.pack(side=LEFT, fill=BOTH, expand=FALSE)
right_canvas.pack(side=RIGHT, fill=BOTH, expand=FALSE)
center_canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)

### INITIALIZE IMAGES ###
win_cup = Image.open("misc/world_cup.png")
win_cup = win_cup.resize((80, 152), Image.LANCZOS)
win_cup = ImageTk.PhotoImage(win_cup)
win_cup_label = Label(root, image=win_cup, bg='black')

silver_medal = Image.open("misc/world_cup_silver.png")
silver_medal = silver_medal.resize((80, 78), Image.LANCZOS)
silver_medal = ImageTk.PhotoImage(silver_medal)
silver_medal_label = Label(root, image=silver_medal, bg='black')

bronze_medal = Image.open("misc/world_cup_bronze.png")
bronze_medal = bronze_medal.resize((80, 78), Image.LANCZOS)
bronze_medal = ImageTk.PhotoImage(bronze_medal)
bronze_medal_label = Label(root, image=bronze_medal, bg='black')

winner_label = Label(root, image='')
silver_label = Label(root, image='')
bronze_label = Label(root, image='')

team1_flag_label = Label(root, image='')
team2_flag_label = Label(root, image='')
### INITIALIZE MISC ###
team_growth_by = range(-100, 100)
year = 2022
cycle_count = 0
draw_count = 0
group_count = 12
sim_cycle = 0
match_count = 0
gsim_count = 0
esim_toggle = 0
esim_count = 0
sorted_qualified_teams = list()
pot1 = list()
pot2 = list()
pot3 = list()
pot4 = list()
team1rating = 0
team2rating = 0
menu_state = 0
best_third_teams = list()
key = 0
winners_knockout = list()
losers_knockout = list()
stage_name = "Intermediary Stage"
sim_speed = 0.01
#region listgroup
group1 = list()
group2 = list()
group3 = list()
group4 = list()
group5 = list()
group6 = list()
group7 = list()
group8 = list()
group9 = list()
group10 = list()
group11 = list()
group12 = list()
#endregion
groups = [group1, group2, group3, group4, group5, group6, group7, group8, group9, group10, group11, group12]
### INITIALIZE FUNCTIONS ###

pygame.init()
pygame.mixer.music.load("background.wav")
pygame.mixer.music.play(-1)
button_sound = pygame.mixer.Sound("click.mp3")

def on_closing():
    if messagebox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()

root.bind("<Escape>", lambda e: on_closing())     

def click_sound():
    button_sound.play()

def callback(url):
    webbrowser.open_new(url)

def initialize():
    global menu_state
    hide_elements()
    click_sound()
    topteams_label.place(relx=0.5, rely=0.05, anchor=N)
    progress_button.place(relx=0.60, rely=0.9, anchor=CENTER)
    intro_credits.place(relx=0.9, rely=0.9, anchor=CENTER)
    stage_label.place(relx=0.6, rely=0.01, anchor=CENTER)
    year_label.place(relx=0.4, rely=0.01, anchor=CENTER)
    eternal_sim_button.place(relx=0.95, rely=0.95, anchor=NE)
    root.config(menu=menubar)
    menu_state = 1
    
def about():
    hide_elements()
    click_sound()
    about_label.place(relx=0.5, rely=0.2, anchor=CENTER)
    back_button.place(relx=0.5, rely=0.5, anchor=CENTER)
    intro_credits.place(relx=0.9, rely=0.9, anchor=CENTER)

def settings():
    hide_elements()
    click_sound()
    back_button.place(relx=0.62, rely=0.9, anchor=CENTER)
    attack_factor_slider.place(relx=0.5, rely=0.1, anchor=CENTER)
    defense_factor_slider.place(relx=0.5, rely=0.2, anchor=CENTER)
    attack_factor_label.place(relx=0.5, rely=0.05, anchor=CENTER)
    defense_factor_label.place(relx=0.5, rely=0.15, anchor=CENTER)
    sim_speed_slider.place(relx=0.5, rely=0.3, anchor=CENTER)
    sim_speed_label.place(relx=0.5, rely=0.25, anchor=CENTER)
    set_factor_button.place(relx=0.5, rely=0.5, anchor=CENTER)

def set_factors():
    click_sound()
    import match_engine
    global af, df, sim_speed
    af = attack_factor_slider.get()
    df = defense_factor_slider.get()
    sim_speed = int(sim_speed_slider.get())
    sim_speed = sim_speed/1000
    match_engine.set_factors(af, df)

def back_menu():
    click_sound()
    global menu_state
    hide_elements()
    if menu_state == 0:
        show_title()
    elif menu_state == 1:
        initialize()
    elif menu_state == 2:
        draw_pots()
    elif menu_state == 3:
        draw_groups_init()
    elif menu_state == 4:
        sim_state()

def show_title():
    hide_elements()
    global menu_state
    intro_title.place(relx=0.5, rely=0.15, anchor=CENTER)
    intro_credits.configure(font=("Trebuchet MS", 10))
    intro_credits.place(relx=0.9, rely=0.9, anchor=CENTER)
    init_button.place(relx=0.5, rely=0.4, anchor=CENTER)
    about_button.place(relx=0.5, rely=0.5, anchor=CENTER)
    settings_button.place(relx=0.5, rely=0.6, anchor=CENTER)
    menu_state = 0

def fade_out(stuff, fontsize):
    stuff.configure(font=("Trebuchet MS", fontsize))
    root.update()
    while fontsize > 0:
        time.sleep(0.10)
        fontsize -= 1
        stuff.configure(font=("Trebuchet MS", fontsize))
        root.update()
        if fontsize == 1:
            stuff.forget()
            show_title()
            break

def hide_elements():
    global winner_label, silver_label, bronze_label
    sim_gstage_button.place_forget()
    intro_title.place_forget()
    intro_credits.place_forget()
    init_button.place_forget()
    about_button.place_forget()
    settings_button.place_forget()
    back_button.place_forget()
    about_label.place_forget()
    year_label.place_forget()
    progress_button.place_forget()
    topteams_label.place_forget()
    qualified_teams_label1.place_forget()
    qualified_teams_label2.place_forget()
    pot_button.place_forget()
    pot1_display.place_forget()
    pot2_display.place_forget()
    pot3_display.place_forget()
    pot4_display.place_forget()
    draw_init_button.place_forget()
    sim_button.place_forget()
    t1name.place_forget()
    t2name.place_forget()
    draw_button.place_forget()
    group1_display.place_forget()
    group2_display.place_forget()
    group3_display.place_forget()
    group4_display.place_forget()
    group5_display.place_forget()
    group6_display.place_forget()
    group7_display.place_forget()
    group8_display.place_forget()
    group9_display.place_forget()
    group10_display.place_forget()
    group11_display.place_forget()
    group12_display.place_forget()
    attack_factor_slider.place_forget()
    defense_factor_slider.place_forget()
    attack_factor_label.place_forget()
    defense_factor_label.place_forget()
    set_factor_button.place_forget()
    team1goal_display.place_forget()
    team2goal_display.place_forget()
    rank_list1.place_forget()
    rank_list2.place_forget()
    rank_list3.place_forget()
    rank_list4.place_forget()
    rank_list5.place_forget()
    rank_list6.place_forget()
    topteams_label.place_forget()
    draw_knockouts_button.place_forget()
    ko_node_1.place_forget()
    ko_node_2.place_forget()
    ko_node_3.place_forget()
    ko_node_4.place_forget()
    ko_node_5.place_forget()
    ko_node_6.place_forget()
    ko_node_7.place_forget()
    ko_node_8.place_forget()
    ko_node_9.place_forget()
    ko_node_10.place_forget()
    ko_node_11.place_forget()
    ko_node_12.place_forget()
    ko_node_13.place_forget()
    ko_node_14.place_forget()
    ko_node_15.place_forget()
    ko_node_16.place_forget()
    draw_knockouts16_button.place_forget() 
    stage_label.place_forget()   
    ko16_node1.place_forget()
    ko16_node2.place_forget()
    ko16_node3.place_forget()
    ko16_node4.place_forget()
    ko16_node5.place_forget()
    ko16_node6.place_forget()
    ko16_node7.place_forget()
    ko16_node8.place_forget()
    ko8_node1.place_forget()
    ko8_node2.place_forget()
    ko8_node3.place_forget()
    ko8_node4.place_forget()
    ko4_node1.place_forget()
    ko4_node2.place_forget()
    knf_node1.place_forget()
    knf_node0.place_forget()
    draw_knockouts4_button.place_forget()
    draw_knockouts8_button.place_forget()
    draw_finals_button.place_forget()
    win_cup_label.place_forget()
    silver_medal_label.place_forget()
    bronze_medal_label.place_forget()
    winner_label.place_forget()
    silver_label.place_forget()
    bronze_label.place_forget()
    winner_team_label.place_forget()
    silver_team_label.place_forget()
    bronze_team_label.place_forget()
    start_cycle_button.place_forget()
    end_cycle_button.place_forget()
    team1_flag_label.place_forget()
    team2_flag_label.place_forget()
    match_stats.place_forget()
    treev.place_forget()
    verscrlbar.place_forget()
    sim_speed_slider.place_forget()
    sim_speed_label.place_forget()
    podiumstat1_label.place_forget()
    podiumstat2_label.place_forget()
    podiumstat3_label.place_forget()
    match_prompt_label.place_forget()
    
           
def get_qualified_teams():
    click_sound()
    ### AFC=10/12, CAF=10/13, CONCACAF=4/5, CONMEBOL=7/8, OFC=1/2, UEFA=16/20
    global sorted_qualified_teams, sorted_asia, sorted_africa, sorted_europe, sorted_north_america, sorted_oceania, sorted_south_america, appearances
    potential_asia = sorted_asia[:12]
    potential_africa = sorted_africa[:13]
    potential_europe = sorted_europe[:20]
    potential_north_america = sorted_north_america[:5]
    potential_oceania = sorted_oceania[:2]
    potential_south_america = sorted_south_america[:8]
    while len(potential_asia) > 10:
        potential_asia.remove(random.choice(potential_asia))
    while len(potential_africa) > 10:
        potential_africa.remove(random.choice(potential_africa))
    while len(potential_europe) > 16:
        potential_europe.remove(random.choice(potential_europe))
    while len(potential_north_america) > 4:
        potential_north_america.remove(random.choice(potential_north_america))
    while len(potential_oceania) > 1:
        potential_oceania.remove(random.choice(potential_oceania))
    while len(potential_south_america) > 7:
        potential_south_america.remove(random.choice(potential_south_america))
    qualified_teams = potential_asia + potential_africa + potential_europe + potential_north_america + potential_oceania + potential_south_america
    sorted_qualified_teams1 = "\n".join([f"{rank+1}. {team} [{rating}]" for rank, (team, rating) in enumerate 
                                        (sorted(qualified_teams, key=lambda item: item[1], reverse=True)[:24])])
    sorted_qualified_teams2 = "\n".join([f"{rank+25}. {team} [{rating}]" for rank, (team, rating) in enumerate
                                        (sorted(qualified_teams, key=lambda item: item[1], reverse=True)[24:])])
    sorted_qualified_teams = sorted(qualified_teams, key=lambda item: item[1], reverse=True)
    qualified_teams_var1.set(sorted_qualified_teams1)
    qualified_teams_label1.place(relx=0.4, rely=0.3, anchor=N)
    qualified_teams_var2.set(sorted_qualified_teams2)
    qualified_teams_label2.place(relx=0.6, rely=0.3, anchor=N)
    for country in qualified_teams:
        appearances[country[0]] += 1
    pot_button.place(relx=0.62, rely=0.9, anchor=CENTER)
    eternal_sim_callback()

def show_rankings():
    click_sound()
    hide_elements()
    year_label.place(relx=0.4, rely=0.01, anchor=CENTER)
    back_button.place(relx=0.62, rely=0.9, anchor=CENTER)
    top40 = "\n".join([f"{rank+1}. {team} [{rating}]" for rank, (team, rating) in enumerate(ordered_world[:40])])
    next40 = "\n".join([f"{rank+41}. {team} [{rating}]" for rank, (team, rating) in enumerate(ordered_world[40:80])])
    next40_80 = "\n".join([f"{rank+81}. {team} [{rating}]" for rank, (team, rating) in enumerate(ordered_world[80:120])])
    next80_120 = "\n".join([f"{rank+121}. {team} [{rating}]" for rank, (team, rating) in enumerate(ordered_world[120:160])])
    next120_160 = "\n".join([f"{rank+161}. {team} [{rating}]" for rank, (team, rating) in enumerate(ordered_world[160:200])])
    next160_200 = "\n".join([f"{rank+201}. {team} [{rating}]" for rank, (team, rating) in enumerate(ordered_world[200:205])])
    rank_list1_var.set(top40)
    rank_list2_var.set(next40)
    rank_list3_var.set(next40_80)
    rank_list4_var.set(next80_120)
    rank_list5_var.set(next120_160)
    rank_list6_var.set(next160_200)
    rank_list1.place(relx=0.01, rely=0.09, anchor=NW)
    rank_list2.place(relx=0.22, rely=0.09, anchor=N)
    rank_list3.place(relx=0.40, rely=0.09, anchor=N)
    rank_list4.place(relx=0.58, rely=0.09, anchor=N)
    rank_list5.place(relx=0.76, rely=0.09, anchor=N)
    rank_list6.place(relx=0.995, rely=0.09, anchor=NE)

def team_growth():
    sim_button.place_forget()
    sim_gstage_button.place_forget()
    topteams_label.place(relx=0.5, rely=0.05, anchor=N)
    intro_credits.place(relx=0.9, rely=0.9, anchor=CENTER)
    stage_label.place(relx=0.6, rely=0.01, anchor=CENTER)
    year_label.place(relx=0.4, rely=0.01, anchor=CENTER)
    progress_button.place(relx=0.60, rely=0.9, anchor=CENTER)
    click_sound()
    global cycle_count, year, world, ordered_world, sorted_teams_top, asia, europe, africa, north_america, oceania, south_america
    global esim_toggle, sorted_africa, sorted_asia, sorted_europe, sorted_north_america, sorted_oceania, sorted_south_america, rank
    if cycle_count == 1:
        global esim_count
        progress_button.place_forget()
        topteams_label.place_forget()
        esim_count = 1
        get_qualified_teams()
    elif cycle_count == 0:
        year += 4
        year_var.set(year)
        for team, rating in asia.items():
            new_rating = rating + random.choice(team_growth_by)
            asia[team] = max(1000, min(2500, new_rating))
        for team, rating in africa.items():
            new_rating = rating + random.choice(team_growth_by)
            africa[team] = max(1000, min(2500, new_rating))
        for team, rating in europe.items():
            new_rating = rating + random.choice(team_growth_by)
            europe[team] = max(1000, min(2500, new_rating))
        for team, rating in north_america.items():
            new_rating = rating + random.choice(team_growth_by)
            north_america[team] = max(1000, min(2500, new_rating))
        for team, rating in oceania.items():
            new_rating = rating + random.choice(team_growth_by)
            oceania[team] = max(1000, min(2500, new_rating))
        for team, rating in south_america.items():
            new_rating = rating + random.choice(team_growth_by)
            south_america[team] = max(1000, min(2500, new_rating))
        world  = {**asia, **africa, **europe, **north_america, **oceania, **south_america}
        ordered_world = sorted(world.items(), key=lambda item: item[1], reverse=True)
        for pos, (team, _) in enumerate(ordered_world):
            rank[team] = pos + 1
        sorted_teams_top = "\n".join([f"{rank+1}. {team} [{rating}]" for rank, (team, rating) in enumerate(ordered_world[:40])])
        sorted_asia = sorted(asia.items(), key=lambda item: item[1], reverse=True)
        sorted_africa = sorted(africa.items(), key=lambda item: item[1], reverse=True)
        sorted_europe = sorted(europe.items(), key=lambda item: item[1], reverse=True)
        sorted_north_america = sorted(north_america.items(), key=lambda item: item[1], reverse=True)
        sorted_oceania = sorted(oceania.items(), key=lambda item: item[1], reverse=True)
        sorted_south_america = sorted(south_america.items(), key=lambda item: item[1], reverse=True)
        progress_button_var.set("View Qualified Teams")
        cycle_count = 1
        topteams_var.set(sorted_teams_top)
        
def draw_pots():
    global pot1, pot2, pot3, pot4, menu_state
    hide_elements()
    click_sound()
    year_label.place(relx=0.4, rely=0.01, anchor=CENTER)
    stage_label.place(relx=0.6, rely=0.01, anchor=CENTER)
    pot1_display.place(relx=0.12, rely=0.22, anchor=CENTER)
    pot2_display.place(relx=0.12, rely=0.78, anchor=CENTER)
    pot3_display.place(relx=0.88, rely=0.22, anchor=CENTER)
    pot4_display.place(relx=0.88, rely=0.78, anchor=CENTER)
    pot1 = list(sorted_qualified_teams[:12])
    for teams in sorted_qualified_teams[:12]:
        pot1_display.insert("", "end", values=(sorted_qualified_teams.index(teams)+1, teams[0]))
    pot2 = list(sorted_qualified_teams[12:24])
    for teams in sorted_qualified_teams[12:24]:
        pot2_display.insert("", "end", values=(sorted_qualified_teams.index(teams)-11, teams[0]))
    pot3 = list(sorted_qualified_teams[24:36])
    for teams in sorted_qualified_teams[24:36]:
        pot3_display.insert("", "end", values=(sorted_qualified_teams.index(teams)-23, teams[0]))
    pot4 = list(sorted_qualified_teams[36:48])
    for teams in sorted_qualified_teams[36:48]:
        pot4_display.insert("", "end", values=(sorted_qualified_teams.index(teams)-35, teams[0]))
    draw_init_button.place(relx=0.62, rely=0.9, anchor=CENTER)
    menu_state = 2
    global esim_count
    esim_count = 2
    eternal_sim_callback()
    
def draw_groups_init():
    global menu_state
    hide_elements()
    click_sound()
    year_label.place(relx=0.4, rely=0.01, anchor=CENTER)
    stage_label.place(relx=0.6, rely=0.01, anchor=CENTER)
    group1_display.place(relx=0.01, rely=0.07, anchor=NW)
    group2_display.place(relx=0.01, rely=0.22, anchor=NW)
    group3_display.place(relx=0.01, rely=0.37, anchor=NW)
    group4_display.place(relx=0.01, rely=0.52, anchor=NW)
    group5_display.place(relx=0.01, rely=0.67, anchor=NW)
    group6_display.place(relx=0.01, rely=0.82, anchor=NW)
    group7_display.place(relx=0.99, rely=0.07, anchor=NE)
    group8_display.place(relx=0.99, rely=0.22, anchor=NE)
    group9_display.place(relx=0.99, rely=0.37, anchor=NE)
    group10_display.place(relx=0.99, rely=0.52, anchor=NE)
    group11_display.place(relx=0.99, rely=0.67, anchor=NE)
    group12_display.place(relx=0.99, rely=0.82, anchor=NE)
    pot1_display.place(relx=0.38, rely=0.22, anchor=CENTER)
    pot2_display.place(relx=0.38, rely=0.78, anchor=CENTER)
    pot3_display.place(relx=0.62, rely=0.22, anchor=CENTER)
    pot4_display.place(relx=0.62, rely=0.78, anchor=CENTER)
    draw_button.place(relx=0.5, rely=0.5, anchor=CENTER)
    menu_state = 3
    global esim_count
    esim_count = 3
    eternal_sim_callback()

def draw_groups():
    import match_sequence
    click_sound()
    global key, stage_name, match_count, pot1, pot2, pot3, pot4, draw_count, menu_state, group, group1, group2, group3, group4, group5, group6, group7, group8, group9, group10, group11, group12
    local_hold = ""
    stage_name = "Group Stage"
    stage_var.set(stage_name)
    if draw_count == 0:
        for i in pot1_display.get_children():
            pot1_display.delete(i)
        for group in groups:
            local_hold = random.choice(pot1)
            group.append(local_hold)
            pot1.remove(local_hold)
        #region push_to_treeview
        group1_display.insert("", "end", values=(1, group1[0][0], 0, 0, 0, 0, 0, 0), tags="qualify")
        group1_display.tag_configure('qualify', background='lightgreen')
        group2_display.insert("", "end", values=(1, group2[0][0], 0, 0, 0, 0, 0, 0), tags="qualify")
        group2_display.tag_configure('qualify', background='lightgreen')
        group3_display.insert("", "end", values=(1, group3[0][0], 0, 0, 0, 0, 0, 0), tags="qualify")
        group3_display.tag_configure('qualify', background='lightgreen')
        group4_display.insert("", "end", values=(1, group4[0][0], 0, 0, 0, 0, 0, 0), tags="qualify")
        group4_display.tag_configure('qualify', background='lightgreen')
        group5_display.insert("", "end", values=(1, group5[0][0], 0, 0, 0, 0, 0, 0), tags="qualify")
        group5_display.tag_configure('qualify', background='lightgreen')
        group6_display.insert("", "end", values=(1, group6[0][0], 0, 0, 0, 0, 0, 0), tags="qualify")
        group6_display.tag_configure('qualify', background='lightgreen')
        group7_display.insert("", "end", values=(1, group7[0][0], 0, 0, 0, 0, 0, 0), tags="qualify")
        group7_display.tag_configure('qualify', background='lightgreen')
        group8_display.insert("", "end", values=(1, group8[0][0], 0, 0, 0, 0, 0, 0), tags="qualify")
        group8_display.tag_configure('qualify', background='lightgreen')
        group9_display.insert("", "end", values=(1, group9[0][0], 0, 0, 0, 0, 0, 0), tags="qualify")
        group9_display.tag_configure('qualify', background='lightgreen')
        group10_display.insert("", "end", values=(1, group10[0][0], 0, 0, 0, 0, 0, 0), tags="qualify")
        group10_display.tag_configure('qualify', background='lightgreen')
        group11_display.insert("", "end", values=(1, group11[0][0], 0, 0, 0, 0, 0, 0), tags="qualify")
        group11_display.tag_configure('qualify', background='lightgreen')
        group12_display.insert("", "end", values=(1, group12[0][0], 0, 0, 0, 0, 0, 0), tags="qualify")
        group12_display.tag_configure('qualify', background='lightgreen')
        #endregion
        draw_count += 1
        eternal_sim_callback()
    elif draw_count == 1:
        for i in pot2_display.get_children():
            pot2_display.delete(i)
        for group in groups:
            local_hold = random.choice(pot2)
            group.append(local_hold)
            pot2.remove(local_hold)
        #region push_to_treeview
        group1_display.insert("", "end", values=(2, group1[1][0], 0, 0, 0, 0, 0, 0), tags="qualify")
        group2_display.insert("", "end", values=(2, group2[1][0], 0, 0, 0, 0, 0, 0), tags="qualify")
        group3_display.insert("", "end", values=(2, group3[1][0], 0, 0, 0, 0, 0, 0), tags="qualify")
        group4_display.insert("", "end", values=(2, group4[1][0], 0, 0, 0, 0, 0, 0), tags="qualify")
        group5_display.insert("", "end", values=(2, group5[1][0], 0, 0, 0, 0, 0, 0), tags="qualify")
        group6_display.insert("", "end", values=(2, group6[1][0], 0, 0, 0, 0, 0, 0), tags="qualify")
        group7_display.insert("", "end", values=(2, group7[1][0], 0, 0, 0, 0, 0, 0), tags="qualify")
        group8_display.insert("", "end", values=(2, group8[1][0], 0, 0, 0, 0, 0, 0), tags="qualify")
        group9_display.insert("", "end", values=(2, group9[1][0], 0, 0, 0, 0, 0, 0), tags="qualify")
        group10_display.insert("", "end", values=(2, group10[1][0], 0, 0, 0, 0, 0, 0), tags="qualify")
        group11_display.insert("", "end", values=(2, group11[1][0], 0, 0, 0, 0, 0, 0), tags="qualify")
        group12_display.insert("", "end", values=(2, group12[1][0], 0, 0, 0, 0, 0, 0), tags="qualify")
        #endregion
        draw_count += 1
        eternal_sim_callback()
    elif draw_count == 2:
        for i in pot3_display.get_children():
            pot3_display.delete(i)
        for group in groups:
            local_hold = random.choice(pot3)
            group.append(local_hold)
            pot3.remove(local_hold)
        #region push_to_treeview
        group1_display.insert("", "end", values=(3, group1[2][0], 0, 0, 0, 0, 0, 0), tags="maybe")
        group1_display.tag_configure('maybe', background='khaki')
        group2_display.insert("", "end", values=(3, group2[2][0], 0, 0, 0, 0, 0, 0), tags="maybe")
        group2_display.tag_configure('maybe', background='khaki')
        group3_display.insert("", "end", values=(3, group3[2][0], 0, 0, 0, 0, 0, 0), tags="maybe")
        group3_display.tag_configure('maybe', background='khaki')
        group4_display.insert("", "end", values=(3, group4[2][0], 0, 0, 0, 0, 0, 0), tags="maybe")
        group4_display.tag_configure('maybe', background='khaki')
        group5_display.insert("", "end", values=(3, group5[2][0], 0, 0, 0, 0, 0, 0), tags="maybe")
        group5_display.tag_configure('maybe', background='khaki')
        group6_display.insert("", "end", values=(3, group6[2][0], 0, 0, 0, 0, 0, 0), tags="maybe")
        group6_display.tag_configure('maybe', background='khaki')
        group7_display.insert("", "end", values=(3, group7[2][0], 0, 0, 0, 0, 0, 0), tags="maybe")
        group7_display.tag_configure('maybe', background='khaki')
        group8_display.insert("", "end", values=(3, group8[2][0], 0, 0, 0, 0, 0, 0), tags="maybe")
        group8_display.tag_configure('maybe', background='khaki')
        group9_display.insert("", "end", values=(3, group9[2][0], 0, 0, 0, 0, 0, 0), tags="maybe")
        group9_display.tag_configure('maybe', background='khaki')
        group10_display.insert("", "end", values=(3, group10[2][0], 0, 0, 0, 0, 0, 0), tags="maybe")
        group10_display.tag_configure('maybe', background='khaki')
        group11_display.insert("", "end", values=(3, group11[2][0], 0, 0, 0, 0, 0, 0), tags="maybe")
        group11_display.tag_configure('maybe', background='khaki')
        group12_display.insert("", "end", values=(3, group12[2][0], 0, 0, 0, 0, 0, 0), tags="maybe")
        group12_display.tag_configure('maybe', background='khaki')
        #endregion
        draw_count += 1
        eternal_sim_callback()
    elif draw_count == 3:
        for i in pot4_display.get_children():
            pot4_display.delete(i)
        for group in groups:
            local_hold = random.choice(pot4)
            group.append(local_hold)
            pot4.remove(local_hold)
        #region push_to_treeview
        group1_display.insert("", "end", values=(4, group1[3][0], 0, 0, 0, 0, 0, 0))
        group2_display.insert("", "end", values=(4, group2[3][0], 0, 0, 0, 0, 0, 0))
        group3_display.insert("", "end", values=(4, group3[3][0], 0, 0, 0, 0, 0, 0))
        group4_display.insert("", "end", values=(4, group4[3][0], 0, 0, 0, 0, 0, 0))
        group5_display.insert("", "end", values=(4, group5[3][0], 0, 0, 0, 0, 0, 0))
        group6_display.insert("", "end", values=(4, group6[3][0], 0, 0, 0, 0, 0, 0))
        group7_display.insert("", "end", values=(4, group7[3][0], 0, 0, 0, 0, 0, 0))
        group8_display.insert("", "end", values=(4, group8[3][0], 0, 0, 0, 0, 0, 0))
        group9_display.insert("", "end", values=(4, group9[3][0], 0, 0, 0, 0, 0, 0))
        group10_display.insert("", "end", values=(4, group10[3][0], 0, 0, 0, 0, 0, 0))
        group11_display.insert("", "end", values=(4, group11[3][0], 0, 0, 0, 0, 0, 0))
        group12_display.insert("", "end", values=(4, group12[3][0], 0, 0, 0, 0, 0, 0))
        #endregion
        draw_button.place_forget()
        pot1_display.place_forget()
        pot2_display.place_forget()
        pot3_display.place_forget()
        pot4_display.place_forget()
        draw_count = 0
        (group1[0])
        match_sequence.draw_matches(group1, group2, group3, group4, group5, group6, group7, group8, group9, group10, group11, group12)
    
    key = 0
    match_count = 1
    sim_setup()
    menu_state = 4 

def sim_setup():
    click_sound()
    import match_sequence
    sim_button.place(relx=0.62, rely=0.9, anchor=CENTER)
    sim_gstage_button.place(relx=0.62, rely=0.95, anchor=N)
    global team1rating, team2rating, match_count, team1_flag_label, team2_flag_label
    match_sequence.parse_data()
    match_stats.place_forget()
    treev.place_forget()
    verscrlbar.place_forget()
    t1name_var.set(match_sequence.t1name)
    t2name_var.set(match_sequence.t2name)
    team1rating = int(match_sequence.tr1)
    team2rating = int(match_sequence.tr2)
    (f"Team 1: {match_sequence.t1name} [{match_sequence.tr1}]")
    (f"Team 2: {match_sequence.t2name} [{match_sequence.tr2}]")
    (team1rating)
    (team2rating)
    team1_flag = Image.open(f"flags/{match_sequence.t1name}.png")
    team1_flag = team1_flag.resize((250, 125), Image.LANCZOS)
    team1_flag = ImageTk.PhotoImage(team1_flag)
    team2_flag = Image.open(f"flags/{match_sequence.t2name}.png")
    team2_flag = team2_flag.resize((250, 125), Image.LANCZOS)
    team2_flag = ImageTk.PhotoImage(team2_flag)
    team1_flag_label.configure(image=team1_flag, bg='black')
    team2_flag_label.configure(image=team2_flag, bg='black')
    team1_flag_label.image = team1_flag
    team2_flag_label.image = team2_flag
    match_stats.heading("team1", text=match_sequence.t1name)
    match_stats.heading("team2", text=match_sequence.t2name)
    t1name.place(relx=0.35, rely=0.45, anchor=CENTER)
    team1_flag_label.place(relx=0.35, rely=0.25, anchor=CENTER)
    t2name.place(relx=0.65, rely=0.45, anchor=CENTER)
    team2_flag_label.place(relx=0.65, rely=0.25, anchor=CENTER)
    global esim_count
    esim_count = 4
    eternal_sim_callback()

def sim_state():
    global sim_cycle, match_count, stage_name
    if sim_cycle == 0:
        if stage_name == "Group Stage":
            t1name.place(relx=0.35, rely=0.45, anchor=CENTER)
            t2name.place(relx=0.65, rely=0.45, anchor=CENTER)
            group1_display.place(relx=0.01, rely=0.07, anchor=NW)
            group2_display.place(relx=0.01, rely=0.22, anchor=NW)
            group3_display.place(relx=0.01, rely=0.37, anchor=NW)
            group4_display.place(relx=0.01, rely=0.52, anchor=NW)
            group5_display.place(relx=0.01, rely=0.67, anchor=NW)
            group6_display.place(relx=0.01, rely=0.82, anchor=NW)
            group7_display.place(relx=0.99, rely=0.07, anchor=NE)
            group8_display.place(relx=0.99, rely=0.22, anchor=NE)
            group9_display.place(relx=0.99, rely=0.37, anchor=NE)
            group10_display.place(relx=0.99, rely=0.52, anchor=NE)
            group11_display.place(relx=0.99, rely=0.67, anchor=NE)
            group12_display.place(relx=0.99, rely=0.82, anchor=NE)
            sim_button.place(relx=0.62, rely=0.9, anchor=CENTER)
        elif stage_name == "Round of 32":
            t1name.place(relx=0.35, rely=0.45, anchor=CENTER)
            t2name.place(relx=0.65, rely=0.45, anchor=CENTER)
            ko_node_1.place(relx=0.005, rely=0.05, anchor=W)
            ko_node_3.place(relx=0.005, rely=0.178, anchor=W)
            ko_node_5.place(relx=0.005, rely=0.306, anchor=W)
            ko_node_7.place(relx=0.005, rely=0.434, anchor=W)
            ko_node_9.place(relx=0.005, rely=0.562, anchor=W)
            ko_node_11.place(relx=0.005, rely=0.69, anchor=W)
            ko_node_13.place(relx=0.005, rely=0.818, anchor=W)
            ko_node_15.place(relx=0.005, rely=0.95, anchor=W)
            ko_node_2.place(relx=0.995, rely=0.05, anchor=E)
            ko_node_4.place(relx=0.995, rely=0.178, anchor=E)
            ko_node_6.place(relx=0.995, rely=0.306, anchor=E)
            ko_node_8.place(relx=0.995, rely=0.434, anchor=E)
            ko_node_10.place(relx=0.995, rely=0.562, anchor=E)
            ko_node_12.place(relx=0.995, rely=0.69, anchor=E)
            ko_node_14.place(relx=0.995, rely=0.818, anchor=E)
            ko_node_16.place(relx=0.995, rely=0.95, anchor=E)
        elif stage_name == "Round of 16":
            t1name.place(relx=0.35, rely=0.45, anchor=CENTER)
            t2name.place(relx=0.65, rely=0.45, anchor=CENTER)
            ko16_node1.place(relx=0.005, rely=0.05, anchor=W)
            ko16_node3.place(relx=0.005, rely=0.36, anchor=W)
            ko16_node5.place(relx=0.005, rely=0.67, anchor=W)
            ko16_node7.place(relx=0.005, rely=0.95, anchor=W)
            ko16_node2.place(relx=0.995, rely=0.05, anchor=E)
            ko16_node4.place(relx=0.995, rely=0.36, anchor=E)
            ko16_node6.place(relx=0.995, rely=0.67, anchor=E)
            ko16_node8.place(relx=0.995, rely=0.95, anchor=E)
        elif stage_name == "Quarterfinals":
            t1name.place(relx=0.35, rely=0.45, anchor=CENTER)
            t2name.place(relx=0.65, rely=0.45, anchor=CENTER)
            ko8_node1.place(relx=0.005, rely=0.05, anchor=W)
            ko8_node3.place(relx=0.005, rely=0.36, anchor=W)
            ko8_node2.place(relx=0.995, rely=0.05, anchor=E)
            ko8_node4.place(relx=0.995, rely=0.36, anchor=E)
        elif stage_name == "Semifinals":
            t1name.place(relx=0.35, rely=0.45, anchor=CENTER)
            t2name.place(relx=0.65, rely=0.45, anchor=CENTER)
            ko4_node1.place(relx=0.005, rely=0.05, anchor=W)
            ko4_node2.place(relx=0.995, rely=0.05, anchor=E)
        elif stage_name == "Final":
            t1name.place(relx=0.35, rely=0.45, anchor=CENTER)
            t2name.place(relx=0.65, rely=0.45, anchor=CENTER)
            knf_node0.place(relx=0.005, rely=0.05, anchor=W)
            knf_node1.place(relx=0.995, rely=0.05, anchor=E)
            
    elif sim_cycle == 1:
        if stage_name == "Group Stage":
            t1name.place(relx=0.35, rely=0.45, anchor=CENTER)
            t2name.place(relx=0.65, rely=0.45, anchor=CENTER)
            group1_display.place(relx=0.01, rely=0.07, anchor=NW)
            group2_display.place(relx=0.01, rely=0.22, anchor=NW)
            group3_display.place(relx=0.01, rely=0.37, anchor=NW)
            group4_display.place(relx=0.01, rely=0.52, anchor=NW)
            group5_display.place(relx=0.01, rely=0.67, anchor=NW)
            group6_display.place(relx=0.01, rely=0.82, anchor=NW)
            group7_display.place(relx=0.99, rely=0.07, anchor=NE)
            group8_display.place(relx=0.99, rely=0.22, anchor=NE)
            group9_display.place(relx=0.99, rely=0.37, anchor=NE)
            group10_display.place(relx=0.99, rely=0.52, anchor=NE)
            group11_display.place(relx=0.99, rely=0.67, anchor=NE)
            group12_display.place(relx=0.99, rely=0.82, anchor=NE)
            sim_button.place(relx=0.62, rely=0.9, anchor=CENTER)
            team1goal_display.place(relx=0.35, rely=0.55, anchor=CENTER)
            team2goal_display.place(relx=0.65, rely=0.55, anchor=CENTER)
        elif stage_name == "Round of 32":
            t1name.place(relx=0.35, rely=0.45, anchor=CENTER)
            t2name.place(relx=0.65, rely=0.45, anchor=CENTER)
            ko_node_1.place(relx=0.005, rely=0.05, anchor=W)
            ko_node_3.place(relx=0.005, rely=0.178, anchor=W)
            ko_node_5.place(relx=0.005, rely=0.306, anchor=W)
            ko_node_7.place(relx=0.005, rely=0.434, anchor=W)
            ko_node_9.place(relx=0.005, rely=0.562, anchor=W)
            ko_node_11.place(relx=0.005, rely=0.69, anchor=W)
            ko_node_13.place(relx=0.005, rely=0.818, anchor=W)
            ko_node_15.place(relx=0.005, rely=0.95, anchor=W)
            ko_node_2.place(relx=0.995, rely=0.05, anchor=E)
            ko_node_4.place(relx=0.995, rely=0.178, anchor=E)
            ko_node_6.place(relx=0.995, rely=0.306, anchor=E)
            ko_node_8.place(relx=0.995, rely=0.434, anchor=E)
            ko_node_10.place(relx=0.995, rely=0.562, anchor=E)
            ko_node_12.place(relx=0.995, rely=0.69, anchor=E)
            ko_node_14.place(relx=0.995, rely=0.818, anchor=E)
            ko_node_16.place(relx=0.995, rely=0.95, anchor=E)
            team1goal_display.place(relx=0.35, rely=0.55, anchor=CENTER)
            team2goal_display.place(relx=0.65, rely=0.55, anchor=CENTER)
        elif stage_name == "Round of 16":
            t1name.place(relx=0.35, rely=0.45, anchor=CENTER)
            t2name.place(relx=0.65, rely=0.45, anchor=CENTER)
            ko16_node1.place(relx=0.005, rely=0.05, anchor=W)
            ko16_node3.place(relx=0.005, rely=0.36, anchor=W)
            ko16_node5.place(relx=0.005, rely=0.67, anchor=W)
            ko16_node7.place(relx=0.005, rely=0.95, anchor=W)
            ko16_node2.place(relx=0.995, rely=0.05, anchor=E)
            ko16_node4.place(relx=0.995, rely=0.36, anchor=E)
            ko16_node6.place(relx=0.995, rely=0.67, anchor=E)
            ko16_node8.place(relx=0.995, rely=0.95, anchor=E)
            team1goal_display.place(relx=0.35, rely=0.55, anchor=CENTER)
            team2goal_display.place(relx=0.65, rely=0.55, anchor=CENTER)
        elif stage_name == "Quarterfinals":
            t1name.place(relx=0.35, rely=0.45, anchor=CENTER)
            t2name.place(relx=0.65, rely=0.45, anchor=CENTER)
            ko8_node1.place(relx=0.005, rely=0.205, anchor=W)
            ko8_node3.place(relx=0.005, rely=0.795, anchor=W)
            ko8_node2.place(relx=0.995, rely=0.205, anchor=E)
            ko8_node4.place(relx=0.995, rely=0.795, anchor=E)
            team1goal_display.place(relx=0.35, rely=0.55, anchor=CENTER)
            team2goal_display.place(relx=0.65, rely=0.55, anchor=CENTER)
        elif stage_name == "Semifinals":
            t1name.place(relx=0.35, rely=0.45, anchor=CENTER)
            t2name.place(relx=0.65, rely=0.45, anchor=CENTER)
            ko4_node1.place(relx=0.005, rely=0.5, anchor=W)
            ko4_node2.place(relx=0.995, rely=0.5, anchor=E)
            team1goal_display.place(relx=0.35, rely=0.55, anchor=CENTER)
            team2goal_display.place(relx=0.65, rely=0.55, anchor=CENTER)
        elif stage_name == "Final":
            t1name.place(relx=0.35, rely=0.45, anchor=CENTER)
            t2name.place(relx=0.65, rely=0.45, anchor=CENTER)
            knf_node0.place(relx=0.005, rely=0.5, anchor=W)
            knf_node1.place(relx=0.995, rely=0.5, anchor=E)
            team1goal_display.place(relx=0.35, rely=0.55, anchor=CENTER) 
            team2goal_display.place(relx=0.65, rely=0.55, anchor=CENTER)
            
            
            
def simulate():
    import match_sequence
    root.update()
    global key, sim_cycle, team1rating, team2rating, menu_state, match_count, gsim_count, team1_flag_label, team2_flag_label, year
    global esim_count
    menu_state = 4
    ("--------------------------------------------")
    (match_count)
    if match_count == 73:
        sim_button.place_forget()
        sim_button_var.set("Simulate")
        sim_cycle = 0
        gsim_count = 0
        draw_knockouts_button.place(relx=0.62, rely=0.9, anchor=CENTER)
        key = 1
        esim_count = 5
        get_best_third_teams()
        eternal_sim_callback()
    elif match_count == 90:
        sim_button.place_forget()
        sim_button_var.set("Simulate")
        sim_cycle = 0
        gsim_count = 0
        draw_knockouts16_button.place(relx=0.62, rely=0.9, anchor=CENTER)
        key = 1
        esim_count = 6
        eternal_sim_callback()
    elif match_count == 99:
        sim_button.place_forget()
        sim_button_var.set("Simulate")
        sim_cycle = 0
        gsim_count = 0
        draw_knockouts8_button.place(relx=0.62, rely=0.9, anchor=CENTER)
        key = 1
        esim_count = 7
        eternal_sim_callback()
    elif match_count == 104:
        sim_button.place_forget()
        sim_button_var.set("Simulate")
        sim_cycle = 0
        gsim_count = 0
        draw_knockouts4_button.place(relx=0.62, rely=0.9, anchor=CENTER)
        key = 1
        esim_count = 8
        eternal_sim_callback()
    elif match_count == 107:
        sim_button.place_forget()
        sim_button_var.set("Simulate")
        sim_cycle = 0
        gsim_count = 0
        draw_finals_button.place(relx=0.62, rely=0.9, anchor=CENTER)
        key = 1
        esim_count = 9
        eternal_sim_callback()
    elif match_count == 110:
        sim_button.place_forget()
        sim_button_var.set("Simulate")
        sim_cycle = 0
        gsim_count = 0
        end_cycle_button_var.set("End " + str(year) + " World Cup!")
        end_cycle_button.place(relx=0.62, rely=0.9, anchor=CENTER)
        esim_count = 10
        eternal_sim_callback()
    elif sim_cycle == 0:
        import match_engine
        sim_cycle = 1
        match_count += 1
        sim_button_var.set("Next Match")
        menu_state = 4
        for i in match_stats.get_children():
            match_stats.delete(i)
        for i in treev.get_children():
            treev.delete(i)
        match_engine.clear_prompt()
        match_engine.sim_match(team1rating, team2rating, key)
    elif sim_cycle == 1:
        (match_count)
        match_sequence.parse_data()
        team1goal_display.place_forget()
        team2goal_display.place_forget()
        match_stats.place_forget()
        treev.place_forget()
        verscrlbar.place_forget()
        match_prompt_label.place_forget()
        for i in match_stats.get_children():
            match_stats.delete(i)
        for i in treev.get_children():
            treev.delete(i)
        t1name_var.set(match_sequence.t1name)
        t2name_var.set(match_sequence.t2name)
        team1rating = int(match_sequence.tr1)
        team2rating = int(match_sequence.tr2)
        team1_flag = Image.open(f"flags/{match_sequence.t1name}.png")
        team1_flag = team1_flag.resize((250, 125), Image.LANCZOS)
        team1_flag = ImageTk.PhotoImage(team1_flag)
        team2_flag = Image.open(f"flags/{match_sequence.t2name}.png")
        team2_flag = team2_flag.resize((250, 125), Image.LANCZOS)
        team2_flag = ImageTk.PhotoImage(team2_flag)
        team1_flag_label.configure(image=team1_flag, bg='black')
        team2_flag_label.configure(image=team2_flag, bg='black')
        team1_flag_label.image = team1_flag
        team2_flag_label.image = team2_flag
        match_stats.heading("team1", text=match_sequence.t1name)
        match_stats.heading("team2", text=match_sequence.t2name)
        sim_cycle = 0
        sim_button_var.set("Simulate")
        global esim_toggle
        if esim_toggle == 1:
            eternal_sim_callback()
        elif gsim_count == 1:
            sim_gstage_verify()

def sim_result(team1score, team2score):
    click_sound()
    root.update()
    import match_sequence
    import match_engine
    match_stats.place(relx=0.63, rely=0.7, anchor=CENTER)
    treev.place(relx = 0.36, rely = 0.8, anchor = CENTER)
    verscrlbar.place(relx=0.4727, rely=0.8, anchor = CENTER, relheight=0.379)
    match_stats.insert("", "end", values=(team1score,"Goals Scored", team2score))
    match_stats.insert("", "end", values=(match_engine.t1shots, "Shots Taken", match_engine.t2shots))
    match_stats.insert("", "end", values=(match_engine.xg1, "xG (Predicted)", match_engine.xg2))
    match_stats.insert("", "end", values=(match_engine.possesion1, "possession", match_engine.possesion2))
    for i, j, k in zip(match_engine.curr_time_list, match_engine.matchprompt_list, match_engine.curr_score_list):
        treev.insert("", "end", values=(i, j, k), tags=('time' if i != "" else 'chance'))
    treev.tag_configure('time', background='lightgreen')
    treev.tag_configure('chance', background='lightblue')
    match_prompt_label.place(relx=0.62, rely=0.85, anchor=CENTER)
    team1goal_display_var.set(team1score)
    team2goal_display_var.set(team2score)
    team1goal_display.place(relx=0.35, rely=0.55, anchor=CENTER)
    team2goal_display.place(relx=0.65, rely=0.55, anchor=CENTER)
    global goal_diff, wins_no, draws_no, losses_no, points_no, played_no
    team1score = int(team1score)
    team2score = int(team2score)
    if team1score > team2score:
        wins_no[match_sequence.t1name] += 1
        losses_no[match_sequence.t2name] += 1
        points_no[match_sequence.t1name] += 3
        match_prompt_var.set(str(match_sequence.t1name) + " BEATS " + str(match_sequence.t2name) + "  " + str(team1score) + " - " + str(team2score))
    elif team1score < team2score:
        wins_no[match_sequence.t2name] += 1
        losses_no[match_sequence.t1name] += 1
        points_no[match_sequence.t2name] += 3
        match_prompt_var.set(str(match_sequence.t2name) + " BEATS " + str(match_sequence.t1name) + "  " + str(team2score) + " - " + str(team1score))
    else:
        draws_no[match_sequence.t1name] += 1
        draws_no[match_sequence.t2name] += 1
        points_no[match_sequence.t1name] += 1
        points_no[match_sequence.t2name] += 1
        match_prompt_var.set(str(match_sequence.t1name) + " DRAWS " + str(match_sequence.t2name) + "  " + str(team1score) + " - " + str(team2score))
        

    played_no[match_sequence.t1name] += 1
    played_no[match_sequence.t2name] += 1
    forgoals[match_sequence.t1name] += team1score
    forgoals[match_sequence.t2name] += team2score
    againstgoals[match_sequence.t2name] += team1score
    againstgoals[match_sequence.t1name] += team2score
    goal_diff[match_sequence.t1name] += (team1score - team2score)
    goal_diff[match_sequence.t2name] += (team2score - team1score)

    for group in groups:
        group.sort(key=lambda team: (points_no[team[0]], goal_diff[team[0]]), reverse=True)

    for i, group in enumerate(groups):
        for item in group_display[i].get_children():
            group_display[i].delete(item)
        for pos, team in enumerate(group):
            tag = "qualify" if group.index(team) < 2 else "maybe" if group.index(team) == 2 else ""
            group_display[i].insert("", "end", values=(pos + 1, team[0], played_no[team[0]], wins_no[team[0]], draws_no[team[0]], losses_no[team[0]], goal_diff[team[0]], points_no[team[0]]), tags=(tag,))
    root.update()
    global esim_toggle
    if esim_toggle == 1:
        eternal_sim_callback()
    elif gsim_count == 1:
        sim_gstage_verify()

def get_best_third_teams():
    import match_sequence
    global best_third_teams
    best_third_teams = []
    for group in groups:
        best_third_teams.append(group[2])
    best_third_teams.sort(key=lambda team: (points_no[team[0]], goal_diff[team[0]]), reverse=True)
    best_third_teams = best_third_teams[:8]
    for group in groups:
        for item in group_display[groups.index(group)].get_children():
            team_name = group_display[groups.index(group)].item(item, "values")[1]
            if any(team[0] == team_name for team in best_third_teams):
                group_display[groups.index(group)].item(item, tags="best_third")
                group_display[groups.index(group)].tag_configure('best_third', background='lightgreen')
    match_sequence.draw_knockout_32(group1, group2, group3, group4, group5, group6, group7, group8, group9, group10, group11, group12, best_third_teams)

def init_knockouts():
    import match_sequence
    import match_engine
    match_engine.clear_prompt()
    global match_count, stage_name
    
    stage_name = "Round of 32"
    stage_var.set(stage_name)
    temp_match_sequence = match_sequence.match_sequence_list
    
    (temp_match_sequence)
    hide_elements()
    year_label.place(relx=0.4, rely=0.01, anchor=CENTER)
    stage_label.place(relx=0.6, rely=0.01, anchor=CENTER)
    ko_node_1.place(relx=0.005, rely=0.05, anchor=W)
    ko_node_3.place(relx=0.005, rely=0.178, anchor=W)
    ko_node_5.place(relx=0.005, rely=0.306, anchor=W)
    ko_node_7.place(relx=0.005, rely=0.434, anchor=W)
    ko_node_9.place(relx=0.005, rely=0.562, anchor=W)
    ko_node_11.place(relx=0.005, rely=0.69, anchor=W)
    ko_node_13.place(relx=0.005, rely=0.818, anchor=W)
    ko_node_15.place(relx=0.005, rely=0.95, anchor=W)
    ko_node_2.place(relx=0.995, rely=0.05, anchor=E)
    ko_node_4.place(relx=0.995, rely=0.178, anchor=E)
    ko_node_6.place(relx=0.995, rely=0.306, anchor=E)
    ko_node_8.place(relx=0.995, rely=0.434, anchor=E)
    ko_node_10.place(relx=0.995, rely=0.562, anchor=E)
    ko_node_12.place(relx=0.995, rely=0.69, anchor=E)
    ko_node_14.place(relx=0.995, rely=0.818, anchor=E)
    ko_node_16.place(relx=0.995, rely=0.95, anchor=E)
    local_n = 0
    
    for node in kn1_nodes:
        node.insert("", "end", values=(temp_match_sequence[local_n][0], 0))
        node.insert("", "end", values=(temp_match_sequence[local_n+1][0], 0))
        local_n += 2
    
    match_count = 74
    sim_button.place(relx=0.62, rely=0.9, anchor=CENTER)
    sim_gstage_button.place(relx=0.62, rely=0.95, anchor=N)
    sim_setup()
        
def sim_gstage():
    global gsim_count
    if gsim_count == 0:
        gsim_count = 1
        simulate()
    elif gsim_count == 1:
        gsim_count = 0
        
def sim_gstage_verify():
    global gsim_count, sim_speed
    if gsim_count == 1:
        root.update()
        ("SIM VERIFIED")
        time.sleep(sim_speed)
        simulate()
    else:
        ("SIM NOT VALID")

def knockresult(team1score, team2score, yespen):
    global stage_name
    import match_sequence
    import match_engine
    if stage_name == "Round of 32":
        node_list = kn1_nodes
    elif stage_name == "Round of 16":
        node_list = kn2_nodes
    elif stage_name == "Quarterfinals":
        node_list = kn3_nodes
    elif stage_name == "Semifinals":
        node_list = kn4_nodes
    elif stage_name == "Final":
        node_list = kn5_nodes
    global winners_knockout, losers_knockout
    team1goal_display.place(relx=0.35, rely=0.55, anchor=CENTER)
    team2goal_display.place(relx=0.65, rely=0.55, anchor=CENTER)
    (str(match_sequence.t1name) + " = " + str(team1score)  + " | " + str(match_sequence.t2name) + " = " + str(team2score) + " | Yespen is " + str(yespen))
    match_stats.place(relx=0.63, rely=0.7, anchor=CENTER)
    treev.place(relx = 0.36, rely = 0.8, anchor = CENTER)
    verscrlbar.place(relx=0.4727, rely=0.8, anchor = CENTER, relheight=0.379)
    match_stats.insert("", "end", values=(match_engine.t1shots, "Shots Taken", match_engine.t2shots))
    match_stats.insert("", "end", values=(match_engine.xg1, "xG (Predicted)", match_engine.xg2))
    match_stats.insert("", "end", values=(match_engine.possesion1, "possession", match_engine.possesion2))
    for i, j, k in zip(match_engine.curr_time_list, match_engine.matchprompt_list, match_engine.curr_score_list):
        treev.insert("", "end", values=(i, j, k), tags=('time' if i != "" else 'chance'))
    treev.tag_configure('time', background='lightgreen')
    treev.tag_configure('chance', background='lightblue')
    match_prompt_label.place(relx=0.62, rely=0.85, anchor=CENTER)
    if yespen == 0:
        forgoals[match_sequence.t1name] += team1score
        forgoals[match_sequence.t2name] += team2score
        againstgoals[match_sequence.t2name] += team1score
        againstgoals[match_sequence.t1name] += team2score
        ("No Penalties")
        match_stats.insert("", "end", values=(team1score,"Goals Scored", team2score))
        team1goal_display_var.set(team1score)
        team2goal_display_var.set(team2score)
        if team1score > team2score:
            winners_knockout.append((match_sequence.t1name, int(match_sequence.tr1)))
            losers_knockout.append((match_sequence.t2name, int(match_sequence.tr2)))
            (winners_knockout)
            match_prompt_var.set(str(match_sequence.t1name) + " BEATS " + str(match_sequence.t2name) + "  " + str(team1score) + " - " + str(team2score))
            for node in node_list:
                if match_sequence.t1name in node.item(node.get_children()[0], "values"):
                    node.item(node.get_children()[0], values=(match_sequence.t1name, team1score), tags="winner")
                    node.item(node.get_children()[1], values=(match_sequence.t2name, team2score), tags="loser")
                    node.tag_configure('winner', background='lightgreen')
                    node.tag_configure('loser', background='lightcoral')
                    break
                elif match_sequence.t1name in node.item(node.get_children()[1], "values"):
                    node.item(node.get_children()[1], values=(match_sequence.t1name, team1score), tags="winner")
                    node.item(node.get_children()[0], values=(match_sequence.t2name, team2score), tags="loser")
                    node.tag_configure('winner', background='lightgreen')
                    node.tag_configure('loser', background='lightcoral')
                    break
                
        elif team1score < team2score:
            winners_knockout.append((match_sequence.t2name, int(match_sequence.tr2)))
            losers_knockout.append((match_sequence.t1name, int(match_sequence.tr1)))
            (winners_knockout)
            match_prompt_var.set(str(match_sequence.t2name) + " BEATS " + str(match_sequence.t1name) + "  " + str(team2score) + " - " + str(team1score))
            for node in node_list:
                if match_sequence.t2name in node.item(node.get_children()[0], "values"):
                    node.item(node.get_children()[0], values=(match_sequence.t2name, team2score), tags="winner")
                    node.item(node.get_children()[1], values=(match_sequence.t1name, team1score), tags="loser")
                    node.tag_configure('winner', background='lightgreen')
                    node.tag_configure('loser', background='lightcoral')
                    break
                elif match_sequence.t2name in node.item(node.get_children()[1], "values"):
                    node.item(node.get_children()[1], values=(match_sequence.t2name, team2score), tags="winner")
                    node.item(node.get_children()[0], values=(match_sequence.t1name, team1score), tags="loser")
                    node.tag_configure('winner', background='lightgreen')
                    node.tag_configure('loser', background='lightcoral')
                    break
    
    elif yespen == 1:
        ("Penalties")
        if team1score > team2score:
            ("Team 1 Wins")
            team1score += -1
            forgoals[match_sequence.t1name] += team1score
            forgoals[match_sequence.t2name] += team2score
            againstgoals[match_sequence.t2name] += team1score
            againstgoals[match_sequence.t1name] += team2score
            match_stats.insert("", "end", values=(team1score,"Goals Scored", team2score))
            team1goal_display_var.set(team1score)
            team2goal_display_var.set(team2score)
            winners_knockout.append((match_sequence.t1name, int(match_sequence.tr1)))
            losers_knockout.append((match_sequence.t2name, int(match_sequence.tr2)))
            (winners_knockout)
            match_prompt_var.set(str(match_sequence.t1name) + " BEATS " + str(match_sequence.t2name) + " ON PENALTIES. ENDED  " + str(team1score) + " - " + str(team2score))
            for node in node_list:
                if match_sequence.t1name in node.item(node.get_children()[0], "values"):
                    node.item(node.get_children()[0], values=(match_sequence.t1name, str(team1score)+'p'), tags="winner")
                    node.item(node.get_children()[1], values=(match_sequence.t2name, str(team2score)), tags="loser")
                    node.tag_configure('winner', background='lightgreen')
                    node.tag_configure('loser', background='lightcoral')
                    break
                elif match_sequence.t1name in node.item(node.get_children()[1], "values"):
                    node.item(node.get_children()[1], values=(match_sequence.t1name, str(team1score)+'p'), tags="winner")
                    node.item(node.get_children()[0], values=(match_sequence.t2name, str(team2score)), tags="loser")
                    node.tag_configure('winner', background='lightgreen')
                    node.tag_configure('loser', background='lightcoral')
                    break
        if team2score > team1score:
            ("Team 2 Wins")
            team2score += -1
            forgoals[match_sequence.t1name] += team1score
            forgoals[match_sequence.t2name] += team2score
            againstgoals[match_sequence.t2name] += team1score
            againstgoals[match_sequence.t1name] += team2score
            match_stats.insert("", "end", values=(team1score,"Goals Scored", team2score))
            team1goal_display_var.set(team1score)
            team2goal_display_var.set(team2score)
            winners_knockout.append((match_sequence.t2name, int(match_sequence.tr2)))
            losers_knockout.append((match_sequence.t1name, int(match_sequence.tr1)))
            (winners_knockout)
            match_prompt_var.set(str(match_sequence.t2name) + " BEATS " + str(match_sequence.t1name) + " ON PENALTIES. ENDED  " + str(team2score) + " - " + str(team1score))
            for node in node_list:
                if match_sequence.t2name in node.item(node.get_children()[0], "values"):
                    node.item(node.get_children()[0], values=(match_sequence.t2name, str(team2score)+'p'), tags="winner")
                    node.item(node.get_children()[1], values=(match_sequence.t1name, str(team1score)), tags="loser")
                    node.tag_configure('winner', background='lightgreen')
                    node.tag_configure('loser', background='lightcoral')
                    break
                elif match_sequence.t2name in node.item(node.get_children()[1], "values"):
                    node.item(node.get_children()[1], values=(match_sequence.t2name, str(team2score)+'p'), tags="winner")
                    node.item(node.get_children()[0], values=(match_sequence.t1name, str(team1score)), tags="loser")
                    node.tag_configure('winner', background='lightgreen')
                    node.tag_configure('loser', background='lightcoral')
                    break
    global esim_toggle
    if esim_toggle == 1:
        eternal_sim_callback()
    elif gsim_count == 1:
        sim_gstage_verify()
    

    
def init_knockouts16():
    import match_sequence
    import match_engine
    match_engine.clear_prompt()
    global match_count, stage_name, winners_knockout
    ("delete losers2")
    losers_knockout.clear()
    stage_name = "Round of 16"
    stage_var.set(stage_name)
    match_sequence.draw_knockout_16(winners_knockout)
    temp_match_sequence = match_sequence.match_sequence_list
    (temp_match_sequence)
    hide_elements()
    year_label.place(relx=0.4, rely=0.01, anchor=CENTER)
    stage_label.place(relx=0.6, rely=0.01, anchor=CENTER)
    ko16_node1.place(relx=0.005, rely=0.05, anchor=W)
    ko16_node3.place(relx=0.005, rely=0.36, anchor=W)
    ko16_node5.place(relx=0.005, rely=0.67, anchor=W)
    ko16_node7.place(relx=0.005, rely=0.95, anchor=W)
    ko16_node2.place(relx=0.995, rely=0.05, anchor=E)
    ko16_node4.place(relx=0.995, rely=0.36, anchor=E)
    ko16_node6.place(relx=0.995, rely=0.67, anchor=E)
    ko16_node8.place(relx=0.995, rely=0.95, anchor=E)
    
    ko16_node1.insert("", "end", values=(temp_match_sequence[0][0], 0))
    ko16_node1.insert("", "end", values=(temp_match_sequence[1][0], 0))
    
    ko16_node2.insert("", "end", values=(temp_match_sequence[2][0], 0))
    ko16_node2.insert("", "end", values=(temp_match_sequence[3][0], 0))
    
    ko16_node3.insert("", "end", values=(temp_match_sequence[4][0], 0))
    ko16_node3.insert("", "end", values=(temp_match_sequence[5][0], 0))
    
    ko16_node4.insert("", "end", values=(temp_match_sequence[6][0], 0))
    ko16_node4.insert("", "end", values=(temp_match_sequence[7][0], 0))
    
    ko16_node5.insert("", "end", values=(temp_match_sequence[8][0], 0))
    ko16_node5.insert("", "end", values=(temp_match_sequence[9][0], 0))
    
    ko16_node6.insert("", "end", values=(temp_match_sequence[10][0], 0))
    ko16_node6.insert("", "end", values=(temp_match_sequence[11][0], 0))
    
    ko16_node7.insert("", "end", values=(temp_match_sequence[12][0], 0))
    ko16_node7.insert("", "end", values=(temp_match_sequence[13][0], 0))
    
    ko16_node8.insert("", "end", values=(temp_match_sequence[14][0], 0))
    ko16_node8.insert("", "end", values=(temp_match_sequence[15][0], 0))
    
    match_count = 91
    sim_button.place(relx=0.62, rely=0.9, anchor=CENTER)
    sim_gstage_button.place(relx=0.62, rely=0.95, anchor=N)
    sim_setup()
    
def init_knockouts8():
    hide_elements()
    import match_engine
    match_engine.clear_prompt()
    year_label.place(relx=0.4, rely=0.01, anchor=CENTER)
    stage_label.place(relx=0.6, rely=0.01, anchor=CENTER)
    global stage_name, match_count, winners_knockout, losers_knockout
    stage_name = "Quarterfinals"
    stage_var.set(stage_name)
    import match_sequence
    match_sequence.draw_knockout_8(winners_knockout)
    losers_knockout.clear()
    temp_match_sequence = match_sequence.match_sequence_list
    (temp_match_sequence)
    ko8_node1.place(relx=0.005, rely=0.205, anchor=W)
    ko8_node3.place(relx=0.005, rely=0.795, anchor=W)
    ko8_node2.place(relx=0.995, rely=0.205, anchor=E)
    ko8_node4.place(relx=0.995, rely=0.795, anchor=E)
    
    ko8_node1.insert("", "end", values=(temp_match_sequence[0][0], 0))
    ko8_node1.insert("", "end", values=(temp_match_sequence[1][0], 0))
    
    ko8_node2.insert("", "end", values=(temp_match_sequence[2][0], 0))
    ko8_node2.insert("", "end", values=(temp_match_sequence[3][0], 0))
    
    ko8_node3.insert("", "end", values=(temp_match_sequence[4][0], 0))
    ko8_node3.insert("", "end", values=(temp_match_sequence[5][0], 0))
    
    ko8_node4.insert("", "end", values=(temp_match_sequence[6][0], 0))
    ko8_node4.insert("", "end", values=(temp_match_sequence[7][0], 0))
    
    match_count = 100
    sim_button.place(relx=0.62, rely=0.9, anchor=CENTER)
    sim_gstage_button.place(relx=0.62, rely=0.95, anchor=N)
    sim_setup()
    
def init_knockouts4():
    hide_elements()
    import match_engine
    match_engine.clear_prompt()
    year_label.place(relx=0.4, rely=0.01, anchor=CENTER)
    stage_label.place(relx=0.6, rely=0.01, anchor=CENTER)
    global stage_name, match_count, winners_knockout, losers_knockout
    (winners_knockout)
    (losers_knockout)
    stage_name = "Semifinals"
    stage_var.set(stage_name)
    import match_sequence
    match_sequence.draw_knockout_4(winners_knockout)
    ("delete losers1")
    losers_knockout.clear()
    temp_match_sequence = match_sequence.match_sequence_list
    (temp_match_sequence)
    ko4_node1.place(relx=0.005, rely=0.5, anchor=W)
    ko4_node2.place(relx=0.995, rely=0.5, anchor=E)
    
    ko4_node1.insert("", "end", values=(temp_match_sequence[0][0], 0))
    ko4_node1.insert("", "end", values=(temp_match_sequence[1][0], 0))
    
    ko4_node2.insert("", "end", values=(temp_match_sequence[2][0], 0))
    ko4_node2.insert("", "end", values=(temp_match_sequence[3][0], 0))
    
    match_count = 105
    sim_button.place(relx=0.62, rely=0.9, anchor=CENTER)
    sim_gstage_button.place(relx=0.62, rely=0.95, anchor=N)
    sim_setup()
    
def init_finals():
    hide_elements()
    import match_engine
    match_engine.clear_prompt()
    
    year_label.place(relx=0.4, rely=0.01, anchor=CENTER)
    stage_label.place(relx=0.6, rely=0.01, anchor=CENTER)
    global stage_name, match_count, winners_knockout, losers_knockout
    (winners_knockout)
    (losers_knockout)
    stage_name = "Final"
    stage_var.set(stage_name)
    import match_sequence
    match_sequence.draw_finals(winners_knockout, losers_knockout)
    ("delete losers2")
    losers_knockout.clear()
    temp_match_sequence = match_sequence.match_sequence_list
    (temp_match_sequence)
    
    knf_node0.place(relx=0.005, rely=0.5, anchor=W)
    knf_node0.insert("", "end", values=(temp_match_sequence[0][0], 0))
    knf_node0.insert("", "end", values=(temp_match_sequence[1][0], 0))
    
    knf_node1.place(relx=0.995, rely=0.5, anchor=E)
    knf_node1.insert("", "end", values=(temp_match_sequence[2][0], 0))
    knf_node1.insert("", "end", values=(temp_match_sequence[3][0], 0))
    
    match_count = 108

    sim_setup()

def setup_podium(filename1, filename2, filename3):
    global winner_label, silver_label, bronze_label
    winnerflg = Image.open(filename1)
    winnerflg = winnerflg.resize((200, 100), Image.LANCZOS)
    winnerflg = ImageTk.PhotoImage(winnerflg)
    winner_label = Label(root, image=winnerflg, bg="black")
    winner_label.image = winnerflg
    winner_label.place(relx=0.5, rely=0.2, anchor=CENTER)
    silverflg = Image.open(filename2)
    silverflg = silverflg.resize((200, 100), Image.LANCZOS)
    silverflg = ImageTk.PhotoImage(silverflg)
    silver_label = Label(root, image=silverflg, bg="black")
    silver_label.image = silverflg
    silver_label.place(relx=0.5, rely=0.42, anchor=CENTER)
    bronzeflg = Image.open(filename3)
    bronzeflg = bronzeflg.resize((200, 100), Image.LANCZOS)
    bronzeflg = ImageTk.PhotoImage(bronzeflg)
    bronze_label = Label(root, image=bronzeflg, bg="black")
    bronze_label.image = bronzeflg
    bronze_label.place(relx=0.5, rely=0.6, anchor=CENTER)

def end_cycle():
    global year, winners_knockout, losers_knockout, match_count, stage_name, appearances, rank, forgoals, againstgoals
    import match_sequence
    import team_data
    hide_elements()
    sim_button.place(relx=0.62, rely=0.9, anchor=CENTER)
    sim_gstage_button.place(relx=0.62, rely=0.95, anchor=N)
    sim_button.place_forget()
    sim_gstage_button.place_forget()
    root.update()
    stage_name = "QUALIFIERS"
    for country in world.keys():
        team_data.country_forgoals_dict[country].append((forgoals.get(country), year))
        team_data.country_againstgoals_dict[country].append((againstgoals.get(country), year))
        team_data.country_appearances_dict[country].append((appearances.get(country), year))
        team_data.curr_rank_dict[country].append((rank.get(country), year))
    root.update()
    team1 = winners_knockout[1][0]
    team2 = losers_knockout[1][0]
    team3 = winners_knockout[0][0]
    team_data.podium_stats(team1, team2, team3)
    country_data.getfinalflag(team1, team2, team3)
    podiumstat1_var.set(str(team1) + " Which is ranked " + str(team_data.rank1) + ". scored: " + str(team_data.latest_forgoals_team1) + " goals and conceded: " 
                        + str(team_data.latest_againstgoals_team1) + " goals.")
    podiumstat2_var.set(str(team2) + " Which is ranked " + str(team_data.rank2) + ". scored: " + str(team_data.latest_forgoals_team2) + " goals and conceded: " 
                        + str(team_data.latest_againstgoals_team2) + " goals.")
    podiumstat3_var.set(str(team3) + " Which is ranked " + str(team_data.rank3) + ". scored: " + str(team_data.latest_forgoals_team3) + " goals and conceded: " 
                        + str(team_data.latest_againstgoals_team3) + " goals.")
    winner_team_var.set(team1)
    silver_team_var.set(team2)
    bronze_team_var.set(team3)
    menubar.entryconfig("Settings", state=DISABLED)
    menubar.entryconfig("Misc", state=DISABLED)
    menubar.entryconfig("Current World Rankings", state=DISABLED)
    menubar_misc_items.entryconfig("About", state=DISABLED)
    win_cup_label.place(relx=0.275, rely=0.20, anchor=CENTER)
    winner_team_label.place(relx=0.275, rely=0.27, anchor=CENTER)
    podiumstat1_label.place(relx=0.5, rely=0.32, anchor=CENTER)
    silver_medal_label.place(relx=0.275, rely=0.42, anchor=CENTER)
    silver_team_label.place(relx=0.275, rely=0.47, anchor=CENTER)
    podiumstat2_label.place(relx=0.5, rely=0.52, anchor=CENTER)
    bronze_medal_label.place(relx=0.275, rely=0.6, anchor=CENTER)
    bronze_team_label.place(relx=0.275, rely=0.65, anchor=CENTER)
    podiumstat3_label.place(relx=0.5, rely=0.7, anchor=CENTER)
    start_cycle_button_var.set("Start " + str(year+4) + " World Cup!")
    start_cycle_button.place(relx=0.62, rely=0.9, anchor=CENTER)
    global esim_toggle, esim_count
    root.update()
    if esim_toggle == 1:
        esim_count = 11
        eternal_sim_callback()

def reset():
    hide_elements()
    global year, match_count, winners_knockout, losers_knockout, pot1, pot2, pot3, pot4, group_count, sim_cycle, match_count, gsim_count, cycle_count, draw_count, group_display
    global world, stage_name, menu_state, key, team1rating, team2rating
    global goal_diff, wins_no, draws_no, losses_no, points_no, played_no, esim_count, esim_toggle
    menubar.entryconfig("Settings", state=NORMAL)
    menubar.entryconfig("Misc", state=NORMAL)
    menubar.entryconfig("Current World Rankings", state=NORMAL)
    menubar_misc_items.entryconfig("About", state=NORMAL)
    sim_button.place_forget()
    sim_gstage_button.place_forget()
    winners_knockout.clear()
    losers_knockout.clear()
    pot1.clear()
    pot2.clear()
    pot3.clear()
    pot4.clear()
    match_count = 0
    cycle_count = 0
    draw_count = 0
    group_count = 12
    sim_cycle = 0
    match_count = 0
    gsim_count = 0
    for i in pot1_display.get_children():
            pot1_display.delete(i)
    for i in pot2_display.get_children():
            pot2_display.delete(i)
    for i in pot3_display.get_children():
            pot3_display.delete(i)
    for i in pot4_display.get_children():
            pot4_display.delete(i)
    for group in group_display:
        for i in group.get_children():
            group.delete(i)
    for node in kn1_nodes:
        for i in node.get_children():
            node.delete(i)
    for node in kn2_nodes:
        for i in node.get_children():
            node.delete(i)
    for node in kn3_nodes:
        for i in node.get_children():
            node.delete(i)
    for node in kn4_nodes:
        for i in node.get_children():
            node.delete(i)
    for node in kn5_nodes:
        for i in node.get_children():
            node.delete(i)
    for team in world:
        wins_no[team[0]] = 0
        draws_no[team[0]] = 0
        losses_no[team[0]] = 0
        points_no[team[0]] = 0
        played_no[team[0]] = 0
        goal_diff[team[0]] = 0
        team1rating = 0
        team2rating = 0
        menu_state = 0
        key = 0
    stage_name = "Intermediary Stage"
    goal_diff = {team: 0 for team in world}
    wins_no = {team: 0 for team in world}
    draws_no = {team: 0 for team in world}
    losses_no = {team: 0 for team in world}
    points_no = {team: 0 for team in world}
    played_no = {team: 0 for team in world}
    for group in groups:
        group.clear()
    global esim_toggle, esim_count
    if esim_toggle == 1:
        esim_count = 0
        eternal_sim_callback()
    else:
        progress_button.place(relx=0.60, rely=0.9, anchor=CENTER)
    
def eternal_sim():
    global esim_toggle, esim_count, ecycle
    if esim_toggle == 1:
        esim_toggle = 0
        eternal_sim_button.config(state=NORMAL)
        end_cycle()
        root.update()
    elif esim_toggle == 0:
        esim_toggle = 1
        eternal_sim_button.config(state=DISABLED)
        ecycle = 0
        eternal_sim_callback()

def eternal_sim_callback():
    global esim_count, esim_toggle, ecycle
    if esim_toggle == 1:
        time.sleep(sim_speed)
        if esim_count == 0:
            team_growth()
            root.update()
            team_growth()
            root.update()
        elif esim_count == 1:
            draw_pots()
            root.update()
        elif esim_count == 2:
            draw_groups_init()
            root.update()
        elif esim_count == 3:
            root.update()
            draw_groups()
        elif esim_count == 4:
            simulate()
            root.update()
        elif esim_count == 5:
            init_knockouts()
            root.update()
        elif esim_count == 6:
            init_knockouts16()
            root.update()
        elif esim_count == 7:
            init_knockouts8()
            root.update()
        elif esim_count == 8:
            init_knockouts4()
            root.update()
        elif esim_count == 9:
            init_finals()
            root.update()
        elif esim_count == 10:
            if ecycle == 4:
                root.update()
                ecycle = 0
                esim_toggle = 1
                sim_button.place_forget()
                sim_gstage_button.place_forget()
                eternal_sim()
                return
            else:
                ecycle += 1
                end_cycle()
        elif esim_count == 11:
            root.update()
            reset()
            root.update()
            
    
### INIT LABELS
intro_credits = Label(root, text="Made with Passion by @Wafheck", font=("Trebuchet MS", 100), bg="black", fg="gold", cursor="hand2")
intro_credits.place(relx=0.5, rely=0.5, anchor=CENTER)
intro_credits.bind("<Button-1>", lambda e: callback("https://github.com/Wafheck"))

#region MENUSPACE
intro_title = Label(root, text="World Cup\nSimulator", bg="black", fg="gold", font=("Impact", 60))
init_button = Button(root, padx=65, text="Initialize >>", fg="black", bg="gold", font = ("Impact", 24), command=initialize)
about_button = Button(root, padx=65, text="About >>", fg="black", bg="gold", font = ("Impact", 24), command=about)
settings_button = Button(root, padx=65, text="Settings >>", fg="black", bg="gold", font = ("Impact", 24), command=settings)
back_button = Button(root, padx=65, text="Back", fg="black", bg="gold", font = ("Impact", 24), command=back_menu)
#endregion

#region MENUBAR
menubar = Menu(root)
menubar_settings = Menu(menubar, tearoff=0)
menubar_misc_items = Menu(menubar, tearoff=0)
menubar_misc_items.add_command(label="About", command=about)
menubar.add_command(label="Settings", command=settings)
menubar.add_cascade(label="Misc", menu=menubar_misc_items)
menubar.add_command(label="Current World Rankings", command=show_rankings)
menubar.add_command(label="Quit", command=root.destroy)
#endregion

#region SETTINGS
af = 35
df = 33

attack_factor_slider = Scale(root, variable = af, from_=30, to=40, orient=HORIZONTAL, length=200, bg='black', fg='gold', font=("Verdana", 12))
attack_factor_slider.set(35)
defense_factor_slider = Scale(root, variable = df, from_=30, to=40, orient=HORIZONTAL, length=200, bg='black', fg='gold', font=("Verdana", 12))
defense_factor_slider.set(33)

attack_factor_label = Label(root, text="Attack Factor:", bg="black", fg="gold", font=("Verdana", 12))
defense_factor_label = Label(root, text="Defense Factor:", bg="black", fg="gold", font=("Verdana", 12))

sim_speed_slider = Scale(root, variable = sim_speed, from_=1, to=100, orient=HORIZONTAL, length=200, bg='black', fg='gold', font=("Verdana", 12))
sim_speed_slider.set(10)
sim_speed_label = Label(root, text="Simulation Speed:", bg="black", fg="gold", font=("Verdana", 12))

set_factor_button = Button(root, padx=65, text="Set Factors", fg="black", bg="gold", font=("Impact", 24), command=set_factors)

eternal_sim_button = Button(root, padx=65, text="Eternal Simulation", fg="black", bg="gold", font=("Impact", 8), command=eternal_sim)
#endregion

#region sim_funcs
sim_gstage_button_var = StringVar()
sim_gstage_button_var.set("Skip Group Stage")
sim_gstage_button = Button(root, padx=65, textvariable=sim_gstage_button_var, fg="black", bg="gold", font = ("Impact", 8), command=sim_gstage)
#endregion

#region CURRENT_RANKINGS
rank_list1_var = StringVar()
rank_list2_var = StringVar()
rank_list3_var = StringVar()
rank_list4_var = StringVar()
rank_list5_var = StringVar()
rank_list6_var = StringVar()
rank_list1_var.set("")
rank_list2_var.set("")
rank_list3_var.set("")
rank_list4_var.set("")
rank_list5_var.set("")
rank_list6_var.set("")
rank_list1 = Label(root, textvariable=rank_list1_var, bg="red", fg="White", font=("Verdana", 10))
rank_list2 = Label(root, textvariable=rank_list2_var, bg="black", fg="White", font=("Verdana", 10))
rank_list3 = Label(root, textvariable=rank_list3_var, bg="black", fg="White", font=("Verdana", 10))
rank_list4 = Label(root, textvariable=rank_list4_var, bg="black", fg="White", font=("Verdana", 10))
rank_list5 = Label(root, textvariable=rank_list5_var, bg="black", fg="White", font=("Verdana", 10))
rank_list6 = Label(root, textvariable=rank_list6_var, bg="blue", fg="White", font=("Verdana", 10))
#endregion

about_label = Label(root, text="This is a simple World Cup Simulator made by @Wafheck. The purpose of this project is to simulate\n"
                                "the World Cup tournament and to predict the winner of the tournament. The simulation is based on\n"
                                "the FIFA World Cup 2026 format and the countries that participated in the tournament.\n"
                                "The countries will be divided into their respective continents and will be selected based on strength\n"
                                "to participate in the tournament. The tournament will be simulated until a winner is determined.\n"
                                "country's strenght will evolve or devolve over time based on their growth chances, more stronger teams\n" 
                                "are likely to win.\n", bg="black", fg="gold", font=("Trebuchet MS", 12))

year_var = StringVar()
year_var.set(year)
year_label = Label(root, textvariable=year_var, bg="black", fg="White", font=("Verdana", 16))

stage_var = StringVar()
stage_var.set("Group Stage")
stage_label = Label(root, textvariable=stage_var, bg="black", fg="White", font=("Verdana", 16))

progress_button_var = StringVar()
progress_button_var.set("Progress")
progress_button = Button(root, padx=65, textvariable=progress_button_var, fg="black", bg="gold", font = ("Impact", 24), command=team_growth)

#region ENDSPACE
winner_team_var = StringVar()
winner_team_var.set("")
winner_team_label = Label(root, textvariable=winner_team_var, bg="black", fg="gold", font=("Verdana", 10))
silver_team_var = StringVar()
silver_team_var.set("")
silver_team_label = Label(root, textvariable=silver_team_var, bg="black", fg="silver", font=("Verdana", 10))
bronze_team_var = StringVar()
bronze_team_var.set("")
bronze_team_label = Label(root, textvariable=bronze_team_var, bg="black", fg="brown", font=("Verdana", 10))
#endregion


#region DRAWSPACE
pot_button = Button(root, padx=65, text="Draw Pots", fg="black", bg="gold", font = ("Impact", 24), command=draw_pots)

topteams_var = StringVar()
topteams_var.set(sorted_teams_top)
topteams_label = Label(root, textvariable=topteams_var, bg="black", fg="White", font=("Verdana", 10))

qualified_teams_var1 = StringVar()
qualified_teams_var1.set("")
qualified_teams_label1 = Label(root, textvariable=qualified_teams_var1, bg="black", fg="White", font=("Verdana", 10))
qualified_teams_var2 = StringVar()
qualified_teams_var2.set("")
qualified_teams_label2 = Label(root, textvariable=qualified_teams_var2, bg="black", fg="White", font=("Verdana", 10))

draw_init_button = Button(root, padx=65, text="Draw Groups", fg="black", bg="gold", font = ("Impact", 24), command=draw_groups_init)
draw_button_var = StringVar()
draw_button_var.set("Draw!")
draw_button = Button(root, padx=65, textvariable=draw_button_var, fg="black", bg="gold", font = ("Impact", 24), command=draw_groups)
#endregion

#region SIMSPACE
sim_button_var = StringVar()
sim_button_var.set("Simulate")
sim_button = Button(root, padx=65, textvariable=sim_button_var, fg="black", bg="gold", font = ("Impact", 16), command=simulate)

t1name_var = StringVar()
t1name_var.set("")
t2name_var = StringVar()
t2name_var.set("")
t1name = Label(root, textvariable=t1name_var, bg="black", fg="White", font=("Verdana", 18))
t2name = Label(root, textvariable=t2name_var, bg="black", fg="White", font=("Verdana", 18))

team1goal_display_var = StringVar()
team2goal_display_var = StringVar()
team1goal_display_var.set("")
team2goal_display_var.set("")
team1goal_display = Label(root, textvariable=team1goal_display_var, bg="black", fg="White", font=("Verdana", 18))
team2goal_display = Label(root, textvariable=team2goal_display_var, bg="black", fg="White", font=("Verdana", 18))
#endregion

#region SIMSPACE_KNOCKOUT

draw_knockouts_button = Button(root, padx=65, text="Draw Knockouts", fg="black", bg="gold", font = ("Impact"), command=init_knockouts)
draw_knockouts16_button = Button(root, padx=65, text="Draw Knockouts", fg="black", bg="gold", font = ("Impact"), command=init_knockouts16)
draw_knockouts8_button = Button(root, padx=65, text="Draw Knockouts", fg="black", bg="gold", font = ("Impact"), command=init_knockouts8)
draw_knockouts4_button = Button(root, padx=65, text="Draw Knockouts", fg="black", bg="gold", font = ("Impact"), command=init_knockouts4)
draw_finals_button = Button(root, padx=65, text="Draw Finals", fg="black", bg="gold", font = ("Impact"), command=init_finals)
end_cycle_button_var = StringVar()
end_cycle_button_var.set("End 2026 World Cup")
end_cycle_button = Button(root, padx=65, textvariable = end_cycle_button_var, fg="black", bg="gold", font = ("Impact"), command=end_cycle)
start_cycle_button_var = StringVar()
start_cycle_button_var.set("Start 2030 World Cup")
start_cycle_button = Button(root, pady=50, padx=65, textvariable=start_cycle_button_var, fg="black", bg="gold", font = ("Impact"), command=reset)
#endregion

#region KNOCKOUT_NODES
### ROUND OF 32

ko_node_1 = ttk.Treeview(root, height=2)
ko_node_1['columns'] = ('teams','score')
ko_node_1.column("#0", width=0,  stretch=NO)
ko_node_1.column("teams",anchor=CENTER, width=170)
ko_node_1.column("score",anchor=CENTER,width=40)
ko_node_1.heading("teams",text="Teams [Round of 32]",anchor=CENTER)
ko_node_1.heading("score",text="Score",anchor=CENTER)

ko_node_2 = ttk.Treeview(root, height=2)
ko_node_2['columns'] = ('teams','score')
ko_node_2.column("#0", width=0,  stretch=NO)
ko_node_2.column("teams",anchor=CENTER, width=170)
ko_node_2.column("score",anchor=CENTER,width=40)
ko_node_2.heading("teams",text="Teams [Round of 32]",anchor=CENTER)
ko_node_2.heading("score",text="Score",anchor=CENTER)

ko_node_3 = ttk.Treeview(root, height=2)
ko_node_3['columns'] = ('teams','score')
ko_node_3.column("#0", width=0,  stretch=NO)
ko_node_3.column("teams",anchor=CENTER, width=170)
ko_node_3.column("score",anchor=CENTER,width=40)
ko_node_3.heading("teams",text="Teams [Round of 32]",anchor=CENTER)
ko_node_3.heading("score",text="Score",anchor=CENTER)

ko_node_4 = ttk.Treeview(root, height=2)
ko_node_4['columns'] = ('teams','score')
ko_node_4.column("#0", width=0,  stretch=NO)
ko_node_4.column("teams",anchor=CENTER, width=170)
ko_node_4.column("score",anchor=CENTER,width=40)
ko_node_4.heading("teams",text="Teams [Round of 32]",anchor=CENTER)
ko_node_4.heading("score",text="Score",anchor=CENTER)

ko_node_5 = ttk.Treeview(root, height=2)
ko_node_5['columns'] = ('teams','score')
ko_node_5.column("#0", width=0,  stretch=NO)
ko_node_5.column("teams",anchor=CENTER, width=170)
ko_node_5.column("score",anchor=CENTER,width=40)
ko_node_5.heading("teams",text="Teams [Round of 32]",anchor=CENTER)
ko_node_5.heading("score",text="Score",anchor=CENTER)

ko_node_6 = ttk.Treeview(root, height=2)
ko_node_6['columns'] = ('teams','score')
ko_node_6.column("#0", width=0,  stretch=NO)
ko_node_6.column("teams",anchor=CENTER, width=170)
ko_node_6.column("score",anchor=CENTER,width=40)
ko_node_6.heading("teams",text="Teams [Round of 32]",anchor=CENTER)
ko_node_6.heading("score",text="Score",anchor=CENTER)

ko_node_7 = ttk.Treeview(root, height=2)
ko_node_7['columns'] = ('teams','score')
ko_node_7.column("#0", width=0,  stretch=NO)
ko_node_7.column("teams",anchor=CENTER, width=170)
ko_node_7.column("score",anchor=CENTER,width=40)
ko_node_7.heading("teams",text="Teams [Round of 32]",anchor=CENTER)
ko_node_7.heading("score",text="Score",anchor=CENTER)

ko_node_8 = ttk.Treeview(root, height=2)
ko_node_8['columns'] = ('teams','score')
ko_node_8.column("#0", width=0,  stretch=NO)
ko_node_8.column("teams",anchor=CENTER, width=170)
ko_node_8.column("score",anchor=CENTER,width=40)
ko_node_8.heading("teams",text="Teams [Round of 32]",anchor=CENTER)
ko_node_8.heading("score",text="Score",anchor=CENTER)

ko_node_9 = ttk.Treeview(root, height=2)
ko_node_9['columns'] = ('teams','score')
ko_node_9.column("#0", width=0,  stretch=NO)
ko_node_9.column("teams",anchor=CENTER, width=170)
ko_node_9.column("score",anchor=CENTER,width=40)
ko_node_9.heading("teams",text="Teams [Round of 32]",anchor=CENTER)
ko_node_9.heading("score",text="Score",anchor=CENTER)

ko_node_10 = ttk.Treeview(root, height=2)
ko_node_10['columns'] = ('teams','score')
ko_node_10.column("#0", width=0,  stretch=NO)
ko_node_10.column("teams",anchor=CENTER, width=170)
ko_node_10.column("score",anchor=CENTER,width=40)
ko_node_10.heading("teams",text="Teams [Round of 32]",anchor=CENTER)
ko_node_10.heading("score",text="Score",anchor=CENTER)

ko_node_11 = ttk.Treeview(root, height=2)
ko_node_11['columns'] = ('teams','score')
ko_node_11.column("#0", width=0,  stretch=NO)
ko_node_11.column("teams",anchor=CENTER, width=170)
ko_node_11.column("score",anchor=CENTER,width=40)
ko_node_11.heading("teams",text="Teams [Round of 32]",anchor=CENTER)
ko_node_11.heading("score",text="Score",anchor=CENTER)

ko_node_12 = ttk.Treeview(root, height=2)
ko_node_12['columns'] = ('teams','score')
ko_node_12.column("#0", width=0,  stretch=NO)
ko_node_12.column("teams",anchor=CENTER, width=170)
ko_node_12.column("score",anchor=CENTER,width=40)
ko_node_12.heading("teams",text="Teams [Round of 32]",anchor=CENTER)
ko_node_12.heading("score",text="Score",anchor=CENTER)

ko_node_13 = ttk.Treeview(root, height=2)
ko_node_13['columns'] = ('teams','score')
ko_node_13.column("#0", width=0,  stretch=NO)
ko_node_13.column("teams",anchor=CENTER, width=170)
ko_node_13.column("score",anchor=CENTER,width=40)
ko_node_13.heading("teams",text="Teams [Round of 32]",anchor=CENTER)
ko_node_13.heading("score",text="Score",anchor=CENTER)

ko_node_14 = ttk.Treeview(root, height=2)
ko_node_14['columns'] = ('teams','score')
ko_node_14.column("#0", width=0,  stretch=NO)
ko_node_14.column("teams",anchor=CENTER, width=170)
ko_node_14.column("score",anchor=CENTER,width=40)
ko_node_14.heading("teams",text="Teams [Round of 32]",anchor=CENTER)
ko_node_14.heading("score",text="Score",anchor=CENTER)

ko_node_15 = ttk.Treeview(root, height=2)
ko_node_15['columns'] = ('teams','score')
ko_node_15.column("#0", width=0,  stretch=NO)
ko_node_15.column("teams",anchor=CENTER, width=170)
ko_node_15.column("score",anchor=CENTER,width=40)
ko_node_15.heading("teams",text="Teams [Round of 32]",anchor=CENTER)
ko_node_15.heading("score",text="Score",anchor=CENTER)

ko_node_16 = ttk.Treeview(root, height=2)
ko_node_16['columns'] = ('teams','score')
ko_node_16.column("#0", width=0,  stretch=NO)
ko_node_16.column("teams",anchor=CENTER, width=170)
ko_node_16.column("score",anchor=CENTER,width=40)
ko_node_16.heading("teams",text="Teams [Round of 32]",anchor=CENTER)
ko_node_16.heading("score",text="Score",anchor=CENTER)

kn1_nodes = [ko_node_1, ko_node_2, ko_node_3, ko_node_4, 
             ko_node_5, ko_node_6, ko_node_7, ko_node_8, 
             ko_node_9, ko_node_10, ko_node_11, ko_node_12, 
             ko_node_13, ko_node_14, ko_node_15, ko_node_16]

ko16_node1 = ttk.Treeview(root, height=2)
ko16_node1['columns'] = ('teams','score')
ko16_node1.column("#0", width=0,  stretch=NO)
ko16_node1.column("teams",anchor=CENTER, width=170)
ko16_node1.column("score",anchor=CENTER,width=40)
ko16_node1.heading("teams",text="Teams [Round of 16]",anchor=CENTER)
ko16_node1.heading("score",text="Score",anchor=CENTER)

ko16_node2 = ttk.Treeview(root, height=2)
ko16_node2['columns'] = ('teams','score')
ko16_node2.column("#0", width=0,  stretch=NO)
ko16_node2.column("teams",anchor=CENTER, width=170)
ko16_node2.column("score",anchor=CENTER,width=40)
ko16_node2.heading("teams",text="Teams [Round of 16]",anchor=CENTER)
ko16_node2.heading("score",text="Score",anchor=CENTER)

ko16_node3 = ttk.Treeview(root, height=2)
ko16_node3['columns'] = ('teams','score')
ko16_node3.column("#0", width=0,  stretch=NO)
ko16_node3.column("teams",anchor=CENTER, width=170)
ko16_node3.column("score",anchor=CENTER,width=40)
ko16_node3.heading("teams",text="Teams [Round of 16]",anchor=CENTER)
ko16_node3.heading("score",text="Score",anchor=CENTER)

ko16_node4 = ttk.Treeview(root, height=2)
ko16_node4['columns'] = ('teams','score')
ko16_node4.column("#0", width=0,  stretch=NO)
ko16_node4.column("teams",anchor=CENTER, width=170)
ko16_node4.column("score",anchor=CENTER,width=40)
ko16_node4.heading("teams",text="Teams [Round of 16]",anchor=CENTER)
ko16_node4.heading("score",text="Score",anchor=CENTER)  

ko16_node5 = ttk.Treeview(root, height=2)
ko16_node5['columns'] = ('teams','score')
ko16_node5.column("#0", width=0,  stretch=NO)
ko16_node5.column("teams",anchor=CENTER, width=170)
ko16_node5.column("score",anchor=CENTER,width=40)
ko16_node5.heading("teams",text="Teams [Round of 16]",anchor=CENTER)
ko16_node5.heading("score",text="Score",anchor=CENTER)

ko16_node6 = ttk.Treeview(root, height=2)
ko16_node6['columns'] = ('teams','score')
ko16_node6.column("#0", width=0,  stretch=NO)
ko16_node6.column("teams",anchor=CENTER, width=170)
ko16_node6.column("score",anchor=CENTER,width=40)
ko16_node6.heading("teams",text="Teams [Round of 16]",anchor=CENTER)
ko16_node6.heading("score",text="Score",anchor=CENTER)

ko16_node7 = ttk.Treeview(root, height=2)
ko16_node7['columns'] = ('teams','score')
ko16_node7.column("#0", width=0,  stretch=NO)
ko16_node7.column("teams",anchor=CENTER, width=170)
ko16_node7.column("score",anchor=CENTER,width=40)
ko16_node7.heading("teams",text="Teams [Round of 16]",anchor=CENTER)
ko16_node7.heading("score",text="Score",anchor=CENTER)

ko16_node8 = ttk.Treeview(root, height=2)
ko16_node8['columns'] = ('teams','score')
ko16_node8.column("#0", width=0,  stretch=NO)
ko16_node8.column("teams",anchor=CENTER, width=170)
ko16_node8.column("score",anchor=CENTER,width=40)
ko16_node8.heading("teams",text="Teams [Round of 16]",anchor=CENTER)    
ko16_node8.heading("score",text="Score",anchor=CENTER)

kn2_nodes = [ko16_node1, ko16_node2, ko16_node3, ko16_node4,
             ko16_node5, ko16_node6, ko16_node7, ko16_node8]

ko8_node1 = ttk.Treeview(root, height=2)
ko8_node1['columns'] = ('teams','score')
ko8_node1.column("#0", width=0,  stretch=NO)
ko8_node1.column("teams",anchor=CENTER, width=170)
ko8_node1.column("score",anchor=CENTER,width=40)
ko8_node1.heading("teams",text="Teams [Quarter Finals]",anchor=CENTER)
ko8_node1.heading("score",text="Score",anchor=CENTER)

ko8_node2 = ttk.Treeview(root, height=2)
ko8_node2['columns'] = ('teams','score')
ko8_node2.column("#0", width=0,  stretch=NO)
ko8_node2.column("teams",anchor=CENTER, width=170)
ko8_node2.column("score",anchor=CENTER,width=40)
ko8_node2.heading("teams",text="Teams [Quarter Finals]",anchor=CENTER)
ko8_node2.heading("score",text="Score",anchor=CENTER)

ko8_node3 = ttk.Treeview(root, height=2)
ko8_node3['columns'] = ('teams','score')
ko8_node3.column("#0", width=0,  stretch=NO)
ko8_node3.column("teams",anchor=CENTER, width=170)
ko8_node3.column("score",anchor=CENTER,width=40)
ko8_node3.heading("teams",text="Teams [Quarter Finals]",anchor=CENTER)
ko8_node3.heading("score",text="Score",anchor=CENTER)

ko8_node4 = ttk.Treeview(root, height=2)
ko8_node4['columns'] = ('teams','score')
ko8_node4.column("#0", width=0,  stretch=NO)
ko8_node4.column("teams",anchor=CENTER, width=170)
ko8_node4.column("score",anchor=CENTER,width=40)
ko8_node4.heading("teams",text="Teams [Quarter Finals]",anchor=CENTER)
ko8_node4.heading("score",text="Score",anchor=CENTER)

kn3_nodes = [ko8_node1, ko8_node2, ko8_node3, ko8_node4]

ko4_node1 = ttk.Treeview(root, height=2)
ko4_node1['columns'] = ('teams','score')
ko4_node1.column("#0", width=0,  stretch=NO)
ko4_node1.column("teams",anchor=CENTER, width=170)
ko4_node1.column("score",anchor=CENTER,width=40)
ko4_node1.heading("teams",text="Teams [Semi Finals]",anchor=CENTER)
ko4_node1.heading("score",text="Score",anchor=CENTER)

ko4_node2 = ttk.Treeview(root, height=2)
ko4_node2['columns'] = ('teams','score')
ko4_node2.column("#0", width=0,  stretch=NO)
ko4_node2.column("teams",anchor=CENTER, width=170)
ko4_node2.column("score",anchor=CENTER,width=40)
ko4_node2.heading("teams",text="Teams [Semi Finals]",anchor=CENTER)
ko4_node2.heading("score",text="Score",anchor=CENTER)

kn4_nodes = [ko4_node1, ko4_node2]

knf_node0 = ttk.Treeview(root, height=2)
knf_node0['columns'] = ('teams','score')
knf_node0.column("#0", width=0,  stretch=NO)
knf_node0.column("teams",anchor=CENTER, width=170)
knf_node0.column("score",anchor=CENTER,width=40)
knf_node0.heading("teams",text="Teams [Third Place Play-Offs]",anchor=CENTER)
knf_node0.heading("score",text="Score",anchor=CENTER)

knf_node1 = ttk.Treeview(root, height=2)
knf_node1['columns'] = ('teams','score')
knf_node1.column("#0", width=0,  stretch=NO)
knf_node1.column("teams",anchor=CENTER, width=170)
knf_node1.column("score",anchor=CENTER,width=40)
knf_node1.heading("teams",text="Teams [Final]",anchor=CENTER)
knf_node1.heading("score",text="Score",anchor=CENTER)

kn5_nodes = [knf_node0, knf_node1]
#endregion

#region POTS
pot1_display = ttk.Treeview(root, height=12)
pot1_display['columns'] = ('number','country')
pot1_display.column("#0", width=0,  stretch=NO)
pot1_display.column("number",anchor=CENTER, width=30)
pot1_display.column("country",anchor=CENTER,width=275)

pot1_display.heading("number",text="No.",anchor=CENTER)
pot1_display.heading("country",text="POT-1 TEAMS",anchor=CENTER)

pot2_display = ttk.Treeview(root, height=12)
pot2_display['columns'] = ('number','country')
pot2_display.column("#0", width=0,  stretch=NO)
pot2_display.column("number",anchor=CENTER, width=30)
pot2_display.column("country",anchor=CENTER,width=275)

pot2_display.heading("number",text="No.",anchor=CENTER)
pot2_display.heading("country",text="POT-2 TEAMS",anchor=CENTER)

pot3_display = ttk.Treeview(root, height=12)
pot3_display['columns'] = ('number','country')
pot3_display.column("#0", width=0,  stretch=NO)
pot3_display.column("number",anchor=CENTER, width=30)
pot3_display.column("country",anchor=CENTER,width=275)

pot3_display.heading("number",text="No.",anchor=CENTER)
pot3_display.heading("country",text="POT-3 TEAMS",anchor=CENTER)

pot4_display = ttk.Treeview(root, height=12)
pot4_display['columns'] = ('number','country')
pot4_display.column("#0", width=0,  stretch=NO)
pot4_display.column("number",anchor=CENTER, width=30)
pot4_display.column("country",anchor=CENTER,width=275)

pot4_display.heading("number",text="No.",anchor=CENTER)
pot4_display.heading("country",text="POT-4 TEAMS",anchor=CENTER)
#endregion

#region  GROUPS
group1_display = ttk.Treeview(root, height=4)
group1_display['columns'] = ('pos','team','m','w','d','l','gd','pts')
group1_display.column("#0", width=0,  stretch=NO)
group1_display.column("pos",anchor=CENTER, width=27)
group1_display.column("team",anchor=CENTER,width=173)
group1_display.column("m",anchor=CENTER,width=25)
group1_display.column("w",anchor=CENTER,width=25)
group1_display.column("d",anchor=CENTER,width=25)
group1_display.column("l",anchor=CENTER,width=25)
group1_display.column("gd",anchor=CENTER,width=25)
group1_display.column("pts",anchor=CENTER,width=30)
group1_display.heading("pos",text="Pos",anchor=CENTER)
group1_display.heading("team",text="(GROUP A) Team:",anchor=CENTER)
group1_display.heading("m",text="P",anchor=CENTER)
group1_display.heading("w",text="W",anchor=CENTER)
group1_display.heading("d",text="D",anchor=CENTER)
group1_display.heading("l",text="L",anchor=CENTER)
group1_display.heading("pts",text="PTS",anchor=CENTER)
group1_display.heading("gd",text="GD",anchor=CENTER)

group2_display = ttk.Treeview(root, height=4)
group2_display['columns'] = ('pos','team','m','w','d','l','gd','pts')
group2_display.column("#0", width=0,  stretch=NO)
group2_display.column("pos",anchor=CENTER, width=27)
group2_display.column("team",anchor=CENTER,width=173)
group2_display.column("m",anchor=CENTER,width=25)
group2_display.column("w",anchor=CENTER,width=25)
group2_display.column("d",anchor=CENTER,width=25)
group2_display.column("l",anchor=CENTER,width=25)
group2_display.column("gd",anchor=CENTER,width=25)
group2_display.column("pts",anchor=CENTER,width=30)
group2_display.heading("pos",text="Pos",anchor=CENTER)
group2_display.heading("team",text="(GROUP B) Team:",anchor=CENTER)
group2_display.heading("m",text="P",anchor=CENTER)
group2_display.heading("w",text="W",anchor=CENTER)
group2_display.heading("d",text="D",anchor=CENTER)
group2_display.heading("l",text="L",anchor=CENTER)
group2_display.heading("pts",text="PTS",anchor=CENTER)
group2_display.heading("gd",text="GD",anchor=CENTER)

group3_display = ttk.Treeview(root, height=4)
group3_display['columns'] = ('pos','team','m','w','d','l','gd','pts')
group3_display.column("#0", width=0,  stretch=NO)
group3_display.column("pos",anchor=CENTER, width=27)
group3_display.column("team",anchor=CENTER,width=173)
group3_display.column("m",anchor=CENTER,width=25)
group3_display.column("w",anchor=CENTER,width=25)
group3_display.column("d",anchor=CENTER,width=25)
group3_display.column("l",anchor=CENTER,width=25)
group3_display.column("gd",anchor=CENTER,width=25)
group3_display.column("pts",anchor=CENTER,width=30)
group3_display.heading("pos",text="Pos",anchor=CENTER)
group3_display.heading("team",text="(GROUP C) Team:",anchor=CENTER)
group3_display.heading("m",text="P",anchor=CENTER)
group3_display.heading("w",text="W",anchor=CENTER)
group3_display.heading("d",text="D",anchor=CENTER)
group3_display.heading("l",text="L",anchor=CENTER)
group3_display.heading("pts",text="PTS",anchor=CENTER)
group3_display.heading("gd",text="GD",anchor=CENTER)


group4_display = ttk.Treeview(root, height=4)
group4_display['columns'] = ('pos','team','m','w','d','l','gd','pts')
group4_display.column("#0", width=0,  stretch=NO)
group4_display.column("pos",anchor=CENTER, width=27)
group4_display.column("team",anchor=CENTER,width=173)
group4_display.column("m",anchor=CENTER,width=25)
group4_display.column("w",anchor=CENTER,width=25)
group4_display.column("d",anchor=CENTER,width=25)
group4_display.column("l",anchor=CENTER,width=25)
group4_display.column("gd",anchor=CENTER,width=25)
group4_display.column("pts",anchor=CENTER,width=30)
group4_display.heading("pos",text="Pos",anchor=CENTER)
group4_display.heading("team",text="(GROUP D) Team:",anchor=CENTER)
group4_display.heading("m",text="P",anchor=CENTER)
group4_display.heading("w",text="W",anchor=CENTER)
group4_display.heading("d",text="D",anchor=CENTER)
group4_display.heading("l",text="L",anchor=CENTER)
group4_display.heading("pts",text="PTS",anchor=CENTER)
group4_display.heading("gd",text="GD",anchor=CENTER)


group5_display = ttk.Treeview(root, height=4)
group5_display['columns'] = ('pos','team','m','w','d','l','gd','pts')
group5_display.column("#0", width=0,  stretch=NO)
group5_display.column("pos",anchor=CENTER, width=27)
group5_display.column("team",anchor=CENTER,width=173)
group5_display.column("m",anchor=CENTER,width=25)
group5_display.column("w",anchor=CENTER,width=25)
group5_display.column("d",anchor=CENTER,width=25)
group5_display.column("l",anchor=CENTER,width=25)
group5_display.column("gd",anchor=CENTER,width=25)
group5_display.column("pts",anchor=CENTER,width=30)
group5_display.heading("pos",text="Pos",anchor=CENTER)
group5_display.heading("team",text="(GROUP E) Team:",anchor=CENTER)
group5_display.heading("m",text="P",anchor=CENTER)
group5_display.heading("w",text="W",anchor=CENTER)
group5_display.heading("d",text="D",anchor=CENTER)
group5_display.heading("l",text="L",anchor=CENTER)
group5_display.heading("pts",text="PTS",anchor=CENTER)
group5_display.heading("gd",text="GD",anchor=CENTER)


group6_display = ttk.Treeview(root, height=4)
group6_display['columns'] = ('pos','team','m','w','d','l','gd','pts')
group6_display.column("#0", width=0,  stretch=NO)
group6_display.column("pos",anchor=CENTER, width=27)
group6_display.column("team",anchor=CENTER,width=173)
group6_display.column("m",anchor=CENTER,width=25)
group6_display.column("w",anchor=CENTER,width=25)
group6_display.column("d",anchor=CENTER,width=25)
group6_display.column("l",anchor=CENTER,width=25)
group6_display.column("gd",anchor=CENTER,width=25)
group6_display.column("pts",anchor=CENTER,width=30)
group6_display.heading("pos",text="Pos",anchor=CENTER)
group6_display.heading("team",text="(GROUP F) Team:",anchor=CENTER)
group6_display.heading("m",text="P",anchor=CENTER)
group6_display.heading("w",text="W",anchor=CENTER)
group6_display.heading("d",text="D",anchor=CENTER)
group6_display.heading("l",text="L",anchor=CENTER)
group6_display.heading("pts",text="PTS",anchor=CENTER)
group6_display.heading("gd",text="GD",anchor=CENTER)


group7_display = ttk.Treeview(root, height=4)
group7_display['columns'] = ('pos','team','m','w','d','l','gd','pts')
group7_display.column("#0", width=0,  stretch=NO)
group7_display.column("pos",anchor=CENTER, width=27)
group7_display.column("team",anchor=CENTER,width=173)
group7_display.column("m",anchor=CENTER,width=25)
group7_display.column("w",anchor=CENTER,width=25)
group7_display.column("d",anchor=CENTER,width=25)
group7_display.column("l",anchor=CENTER,width=25)
group7_display.column("gd",anchor=CENTER,width=25)
group7_display.column("pts",anchor=CENTER,width=30)
group7_display.heading("pos",text="Pos",anchor=CENTER)
group7_display.heading("team",text="(GROUP G) Team:",anchor=CENTER)
group7_display.heading("m",text="P",anchor=CENTER)
group7_display.heading("w",text="W",anchor=CENTER)
group7_display.heading("d",text="D",anchor=CENTER)
group7_display.heading("l",text="L",anchor=CENTER)
group7_display.heading("pts",text="PTS",anchor=CENTER)
group7_display.heading("gd",text="GD",anchor=CENTER)


group8_display = ttk.Treeview(root, height=4)
group8_display['columns'] = ('pos','team','m','w','d','l','gd','pts')
group8_display.column("#0", width=0,  stretch=NO)
group8_display.column("pos",anchor=CENTER, width=27)
group8_display.column("team",anchor=CENTER,width=173)
group8_display.column("m",anchor=CENTER,width=25)
group8_display.column("w",anchor=CENTER,width=25)
group8_display.column("d",anchor=CENTER,width=25)
group8_display.column("l",anchor=CENTER,width=25)
group8_display.column("gd",anchor=CENTER,width=25)
group8_display.column("pts",anchor=CENTER,width=30)
group8_display.heading("pos",text="Pos",anchor=CENTER)
group8_display.heading("team",text="(GROUP H) Team:",anchor=CENTER)
group8_display.heading("m",text="P",anchor=CENTER)
group8_display.heading("w",text="W",anchor=CENTER)
group8_display.heading("d",text="D",anchor=CENTER)
group8_display.heading("l",text="L",anchor=CENTER)
group8_display.heading("pts",text="PTS",anchor=CENTER)
group8_display.heading("gd",text="GD",anchor=CENTER)


group9_display = ttk.Treeview(root, height=4)
group9_display['columns'] = ('pos','team','m','w','d','l','gd','pts')
group9_display.column("#0", width=0,  stretch=NO)
group9_display.column("pos",anchor=CENTER, width=27)
group9_display.column("team",anchor=CENTER,width=173)
group9_display.column("m",anchor=CENTER,width=25)
group9_display.column("w",anchor=CENTER,width=25)
group9_display.column("d",anchor=CENTER,width=25)
group9_display.column("l",anchor=CENTER,width=25)
group9_display.column("gd",anchor=CENTER,width=25)
group9_display.column("pts",anchor=CENTER,width=30)
group9_display.heading("pos",text="Pos",anchor=CENTER)
group9_display.heading("team",text="(GROUP I) Team:",anchor=CENTER)
group9_display.heading("m",text="P",anchor=CENTER)
group9_display.heading("w",text="W",anchor=CENTER)
group9_display.heading("d",text="D",anchor=CENTER)
group9_display.heading("l",text="L",anchor=CENTER)
group9_display.heading("pts",text="PTS",anchor=CENTER)
group9_display.heading("gd",text="GD",anchor=CENTER)


group10_display = ttk.Treeview(root, height=4)
group10_display['columns'] = ('pos','team','m','w','d','l','gd','pts')
group10_display.column("#0", width=0,  stretch=NO)
group10_display.column("pos",anchor=CENTER, width=27)
group10_display.column("team",anchor=CENTER,width=173)
group10_display.column("m",anchor=CENTER,width=25)
group10_display.column("w",anchor=CENTER,width=25)
group10_display.column("d",anchor=CENTER,width=25)
group10_display.column("l",anchor=CENTER,width=25)
group10_display.column("gd",anchor=CENTER,width=25)
group10_display.column("pts",anchor=CENTER,width=30)
group10_display.heading("pos",text="Pos",anchor=CENTER)
group10_display.heading("team",text="(GROUP J) Team:",anchor=CENTER)
group10_display.heading("m",text="P",anchor=CENTER)
group10_display.heading("w",text="W",anchor=CENTER)
group10_display.heading("d",text="D",anchor=CENTER)
group10_display.heading("l",text="L",anchor=CENTER)
group10_display.heading("pts",text="PTS",anchor=CENTER)
group10_display.heading("gd",text="GD",anchor=CENTER)


group11_display = ttk.Treeview(root, height=4)
group11_display['columns'] = ('pos','team','m','w','d','l','gd','pts')
group11_display.column("#0", width=0,  stretch=NO)
group11_display.column("pos",anchor=CENTER, width=27)
group11_display.column("team",anchor=CENTER,width=173)
group11_display.column("m",anchor=CENTER,width=25)
group11_display.column("w",anchor=CENTER,width=25)
group11_display.column("d",anchor=CENTER,width=25)
group11_display.column("l",anchor=CENTER,width=25)
group11_display.column("gd",anchor=CENTER,width=25)
group11_display.column("pts",anchor=CENTER,width=30)
group11_display.heading("pos",text="Pos",anchor=CENTER)
group11_display.heading("team",text="(GROUP K) Team:",anchor=CENTER)
group11_display.heading("m",text="P",anchor=CENTER)
group11_display.heading("w",text="W",anchor=CENTER)
group11_display.heading("d",text="D",anchor=CENTER)
group11_display.heading("l",text="L",anchor=CENTER)
group11_display.heading("pts",text="PTS",anchor=CENTER)
group11_display.heading("gd",text="GD",anchor=CENTER)


group12_display = ttk.Treeview(root, height=4)
group12_display['columns'] = ('pos','team','m','w','d','l','gd','pts')
group12_display.column("#0", width=0,  stretch=NO)
group12_display.column("pos",anchor=CENTER, width=27)
group12_display.column("team",anchor=CENTER,width=173)
group12_display.column("m",anchor=CENTER,width=25)
group12_display.column("w",anchor=CENTER,width=25)
group12_display.column("d",anchor=CENTER,width=25)
group12_display.column("l",anchor=CENTER,width=25)
group12_display.column("gd",anchor=CENTER,width=25)
group12_display.column("pts",anchor=CENTER,width=30)
group12_display.heading("pos",text="Pos",anchor=CENTER)
group12_display.heading("team",text="(GROUP L) Team:",anchor=CENTER)
group12_display.heading("m",text="P",anchor=CENTER)
group12_display.heading("w",text="W",anchor=CENTER)
group12_display.heading("d",text="D",anchor=CENTER)
group12_display.heading("l",text="L",anchor=CENTER)
group12_display.heading("pts",text="PTS",anchor=CENTER)
group12_display.heading("gd",text="GD",anchor=CENTER)

group_display = [group1_display, group2_display, group3_display, group4_display, group5_display, group6_display, group7_display, group8_display, group9_display, group10_display, group11_display, group12_display]

#endregion GROUPS

#region MATCHPROMPTS
match_stats = ttk.Treeview(root, height=4)
match_stats['columns'] = ('team1', 'stat', 'team2')
match_stats.column("#0", width=0,  stretch=NO)
match_stats.column("team1",anchor=CENTER,width=120)
match_stats.column("stat",anchor=CENTER,width=120)
match_stats.column("team2",anchor=CENTER,width=120)
match_stats.heading("team1",text='team1',anchor=CENTER)
match_stats.heading("stat",text='STATISTICS',anchor=CENTER)
match_stats.heading("team2",text='team2',anchor=CENTER)



match_prompt_var = StringVar()
match_prompt_label = Label(root, textvariable=match_prompt_var, font=("Verdana", 10, "bold"))
match_prompt_var.set("--MATCH PROMPT--")

match_life = ttk.Treeview(root, height=8)

treev = ttk.Treeview(root, selectmode ='browse', height = 15)
verscrlbar = ttk.Scrollbar(root, orient ="vertical", command = treev.yview)
treev.configure(xscrollcommand = verscrlbar.set)
treev["columns"] = ("1", "2", "3")
treev['show'] = 'headings'
treev.column("1", width = 40, anchor ='c')
treev.column("2", width = 250, anchor ='w')
treev.column("3", width = 40, anchor ='se')
treev.heading("1", text ="Time")
treev.heading("2", text ="Event")
treev.heading("3", text ="Score")

podiumstat1_var = StringVar()
podiumstat1_var.set("")
podiumstat1_label = Label(root, textvariable=podiumstat1_var, font=("Verdana", 10, "bold"), bg='black', fg='gold')

podiumstat2_var = StringVar()
podiumstat2_var.set("")
podiumstat2_label = Label(root, textvariable=podiumstat2_var, font=("Verdana", 10, "bold"), bg='black', fg='silver')

podiumstat3_var = StringVar()
podiumstat3_var.set("")
podiumstat3_label = Label(root, textvariable=podiumstat3_var, font=("Verdana", 10, "bold"), bg='black', fg='brown')
#endregion

fade_out(intro_credits, 36)
root.mainloop()