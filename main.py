import tkinter as tk
import random
from tkinter import Toplevel, Menu
from tkinter import *
from PIL import *
from PIL import Image, ImageTk

teams = {
    'GERMANY' : 83, 'ARGENTINA': 83, 'BELGIUM': 82, 'ENGLAND': 84,
    'FRANCE': 83, 'PORTUGAL': 85, 'ITALY': 83, 'SPAIN': 84,
    'NETHERLANDS': 82, 'URUGUAY': 81, 'BRAZIL': 80, 'CROATIA': 80,
    'SERBIA': 78, 'SWITZERLAND': 78, 'DENMARK': 79, 'POLAND': 77,
    'MEXICO': 79, 'USA': 76, 'SWEDEN': 78, 'RUSSIA': 77,
    'JAPAN': 75, 'SOUTH KOREA': 75, 'AUSTRALIA': 74, 'NEW ZEALAND': 72,
    'NIGERIA': 76, 'CAMEROON': 74, 'GHANA': 76,
    'COSTA RICA': 74, 'SAUDI ARABIA': 72, 'IRAN': 71,
    'EGYPT': 73, 'TUNISIA': 72, 'MOROCCO': 73,
    'IVORY COAST': 74, 'SENEGAL': 75, 'GABON': 72,
    'CONGO DR': 70, 'ZAMBIA': 71,
    'ANGOLA': 70, 'BURKINA FASO': 71, 'GUINEA': 69,
    'MALI': 70, 'CAPE VERDE': 68, 'BENIN': 67,
    'ZIMBABWE': 66, 'NAMIBIA': 65, 'BOTSWANA': 64,
    'MAURITANIA': 63, 'ETHIOPIA': 62, 'KENYA': 61,
    'UGANDA': 60, 'TANZANIA': 59, 'RWANDA': 58,
    'BURUNDI': 57, 'MOZAMBIQUE': 56,
    'MALAWI': 53, 'LESOTHO': 52,
    'SWAZILAND': 51, 'SOUTH AFRICA': 70,
    'CHILE': 80, 'COLOMBIA': 79, 'PERU': 78, 'ECUADOR': 76,
    'PARAGUAY': 75, 'VENEZUELA': 73, 'BOLIVIA': 72,
    'CZECH REPUBLIC': 79, 'UKRAINE': 78, 'AUSTRIA': 77, 'TURKEY': 76,
    'GREECE': 75, 'SCOTLAND': 74, 'NORWAY': 78,
    'ROMANIA': 77, 'HUNGARY': 76, 'SLOVAKIA': 75, 'BULGARIA': 74,
    'ICELAND': 73, 'FINLAND': 72, 'IRELAND': 71, 'WALES': 70,
    'ALBANIA': 69, 'NORTHERN IRELAND': 68, 'ESTONIA': 67, 'LATVIA': 66,
    'LITHUANIA': 65, 'BELARUS': 64, 'MOLDOVA': 63, 'AZERBAIJAN': 62,
    'ARMENIA': 61, 'GEORGIA': 60, 'KAZAKHSTAN': 59, 'UZBEKISTAN': 58,
    'TURKMENISTAN': 57, 'KYRGYZSTAN': 56, 'TAJIKISTAN': 55,
    'MALTA': 53, 'ANDORRA': 52, 'LIECHTENSTEIN': 51, 'SAN MARINO': 50,
    'PALESTINE': 55, 'SYRIA': 60, 'IRAQ': 62, 'JORDAN': 58,
    'LEBANON': 56, 'OMAN': 61, 'QATAR': 63, 'UNITED ARAB EMIRATES': 65,
    'BAHRAIN': 57, 'KUWAIT': 60, 'YEMEN': 52, 'AFGHANISTAN': 50,
    'PAKISTAN': 48, 'BANGLADESH': 46, 'NEPAL': 44, 'BHUTAN': 42,
    'SRI LANKA': 40, 'MALDIVES': 38,
    'INDIA': 58, 'SINGAPORE': 55, 'MALAYSIA': 62, 'THAILAND': 63,
    'INDONESIA': 60, 'PHILIPPINES': 54, 'VIETNAM': 59, 'MYANMAR': 56,
    'LAOS': 53, 'CAMBODIA': 50, 'BRUNEI': 48, 'TIMOR-LESTE': 46,
    'NORTH KOREA': 56, 'TAIWAN': 55, 'HONG KONG': 52, 'MACAU': 50,
    'BOSNIA': 78, 'CENTRAL AFRICAN REP.': 62, 'CONGO': 63, 'CHINA': 68,
    'COMOROS': 62, 'CUBA': 67, 'CHAD': 63, 'ALGERIA' : 75,  'CANADA' : 73,
    'GUATEMALA' : 71, 'HAITI' : 69, 'HONDURAS' : 71, 'LIBERIA' : 63, 'LIBYA' : 69,
    'MADAGASCAR' : 62, 'MONGOLIA' : 61

}
x = 100
y = 150
year = 2022
yearfont = ("Courier New", 20)
subhead = ('Courier New', 16)
rankfont = ("Verdana", 12)
cwrfont = ("Verdana", 10)
dispfont = ("Impact", 50)
promptfont = ("Tahoma", 12)
versfont = ("Impact", 100)
nmdispfont = ("Impact", 28)
root = Tk()
root.configure(bg="Black")
menubar = Menu(root)
root.title("World Cup Simulator")
root.geometry('1920x1080')
redcanva = Canvas(root, bg="red")
redcanva.place(x=-1, y=-1, width=500, height=1075)
bluecanva = Canvas(root, bg="Blue")
bluecanva.place(x=1500, y=1, width=500, height=1075)
matchrate = (-3,-2,-1,0,1,2)
sorted_teams = sorted(teams.items(), key=lambda x: x[1], reverse=True)
sorted_teams_str = "\n".join([f"{rank+1}. {team} [{rating}]" for rank, (team, rating) in enumerate(sorted_teams[:40])])
sorted_teams_rc1 = "\n".join([f"{rank+1}. {team} [{rating}]" for rank, (team, rating) in enumerate(sorted_teams[:50])])
sorted_teams_rc2 = "\n".join([f"{rank+51}. {team} [{rating}]" for rank, (team, rating) in enumerate(sorted_teams[51:101])])
sorted_teams_rc3 = "\n".join([f"{rank+101}. {team} [{rating}]" for rank, (team, rating) in enumerate(sorted_teams[102:200])])
sorted_wins = "NO DATA"
world_cup_wins = {team: 0 for team in teams}
world_cup_loss = {team: 0 for team in teams}
world_cup_finals = {team: 0 for team in teams}
sorted_leadertc1 = "No Data"
sorted_leadertc2 = "No Data"
sorted_leadertc3 = "No Data"
teamgrowth = (-4,-3,-2,-2,-1,-1,-1,-1,0,0,0,1,1,1,2,2,3,4)
t1namevar = StringVar()
t1namevar.set("0")
t2namevar = StringVar()
t2namevar.set("0")
image1path = f"flags/{str(t1namevar.get()) + '.png'}"
image2path = f"flags/{str(t2namevar.get()) + '.png'}"
image0 = Image.open(image1path)
image0 = image0.resize((150, 100))
flg0 = ImageTk.PhotoImage(image0)
team1flg = Label(root, image=flg0)
team1flg.image = flg0
team2flg = Label(root, image=flg0)
team2flg.image = flg0
im = Image.open('ball.ico')
photo = ImageTk.PhotoImage(im)
root.wm_iconphoto(True, photo)


# MATCH ENGINE
def matchsim():
    # TAKE TOP 8 TEAMS -- DRAWSEL USING RANKS
    # SELECT TWO RANDOM TEAMS
    # ASSIGN MRATING [-5, +5], ASSIGN FRATING = MRATING + TRATING
    # COMPARE FRATING, ASSIGN GOALS [1-5] if clear victor, if not assign [0-5]
    # NORMALIZE SCORE
    # STATE VICTOR AND ASSIGN CUPWIN/LOSS
    sorted_teams = sorted(teams.items(), key=lambda x: x[1], reverse=True)
    best8 = sorted_teams[:10]
    team1 = random.choice(best8)
    best8.remove(team1)
    team2 = random.choice(best8)
    best8.remove(team2)
    tr1 = int(''.join(filter(str.isdigit, str(team1[1]))))
    tr2 = int(''.join(filter(str.isdigit, str(team2[1]))))
    mr1 = random.choice(matchrate)
    mr2 = random.choice(matchrate)
    fr1 = mr1 + tr1
    fr2 = mr2 + tr2
    drawsel = (1, 2)
    t1name = team1[0]
    t2name = team2[0]
    world_cup_finals[team1[0]] += 1
    world_cup_finals[team2[0]] += 1
    if fr1 > fr2:
            gnum1 = random.randint(0, 5)
            gs = fr1 - fr2
            gnum2 = abs(gnum1 - gs)
            if gnum1 > 5:
              gnum1 += -2
            elif gnum1 == 5:
                gnum1 += -1
            if gnum2 > 5:
              gnum2 += -2
            elif gnum2 == 5:
                gnum2 += -1
            if gnum1 >= 7:
              gnum1 += -4
            if gnum2 >= 7:
              gnum2 += -4
            if gnum2 > gnum1:
                promptvar.set(str(t1name) + " " + str(gnum1) + " - " + str(gnum2) + " " + str(t2name) + ". " + str(t2name) + " WINS THE " + str(year) + " FIFA WORLD CUP!")
                prompt.place(x=750, y=800)
                world_cup_wins[team2[0]] += 1 
                world_cup_loss[team1[0]] += 1 
            elif gnum1 > gnum2:
                promptvar.set(str(t1name) + " " + str(gnum1) + " - " + str(gnum2) + " " + str(t2name) + ". " + str(t1name) + " WINS THE " + str(year) + " FIFA WORLD CUP!")
                prompt.place(x=750, y=800)                
                world_cup_wins[team1[0]] += 1
                world_cup_loss[team2[0]] += 1
            else:
                tieb = random.choice(drawsel)
                if tieb == 1:
                     promptvar.set(str(t1name) + " " + str(gnum1) + " - " + str(gnum2) + " " + str(t2name) + ". " + str(t1name) + " WINS THE " + str(year) + " FIFA WORLD CUP on penalities.")
                     prompt.place(x=750, y=800)
                     world_cup_wins[team1[0]] += 1
                     world_cup_loss[team2[0]] += 1
                else:
                     promptvar.set(str(t1name) + " " + str(gnum1) + " - " + str(gnum2) + " " + str(t2name) + ". " + str(t2name) + " WINS THE " + str(year) + " FIFA WORLD CUP on penalities.")
                     prompt.place(x=750, y=800)                     
                     world_cup_wins[team2[0]] += 1
                     world_cup_loss[team1[0]] += 1
                     
    elif fr2 > fr1:
            gnum2 = random.randint(0, 4)
            gs = fr2 - fr1
            gnum1 = abs(gnum2 - gs)
            if gnum1 > 5:
             gnum1 += -2
            elif gnum1 == 5:
                gnum1 += -1
            if gnum2 > 5:
             gnum2 += -2
            elif gnum2 == 5:
                gnum2 += -1
            if gnum1 >= 7:
             gnum1 += -4
            if gnum2 >= 7:
             gnum2 += -4
            if gnum2 > gnum1:
                promptvar.set(str(t1name) + " " + str(gnum1) + " - " + str(gnum2) + " " + str(t2name) + ". " + str(t2name) + " WINS THE " + str(year) + " FIFA WORLD CUP!")
                prompt.place(x=750, y=800)
                world_cup_wins[team2[0]] += 1
                world_cup_loss[team1[0]] += 1
                
                
            elif gnum1 > gnum2:
                promptvar.set(str(t1name) + " " + str(gnum1) + " - " + str(gnum2) + " " + str(t2name) + ". " + str(t1name) + " WINS THE " + str(year) + " FIFA WORLD CUP!")
                prompt.place(x=750, y=800)
                world_cup_wins[team1[0]] += 1
                world_cup_loss[team2[0]] += 1
            else:
                tieb = random.choice(drawsel)
                if tieb == 1:
                     promptvar.set(str(t1name) + " " + str(gnum1) + " - " + str(gnum2) + " " + str(t2name) + ". " + str(t1name) + " WINS THE " + str(year) + " FIFA WORLD CUP on penalities.")
                     prompt.place(x=750, y=800)
                     world_cup_wins[team1[0]] += 1
                     world_cup_loss[team2[0]] += 1
                else:
                     promptvar.set(str(t1name) + " " + str(gnum1) + " - " + str(gnum2) + " " + str(t2name) + ". " + str(t2name) + " WINS THE " + str(year) + " FIFA WORLD CUP on penalities.")
                     prompt.place(x=750, y=800)
                     world_cup_wins[team2[0]] += 1
                     world_cup_loss[team1[0]] += 1
    else:
        gnum1 = random.randint(0, 5)
        gs = fr1 - fr2
        gnum2 = abs(gnum1 - gs)
        tieb = random.choice(drawsel)
        if gnum1 >= 5:
             gnum1 += -2
        if gnum2 >= 5:
             gnum2 += -2
        if tieb == 1:
                 promptvar.set(str(t1name) + " " + str(gnum1) + " - " + str(gnum2) + " " + str(t2name) + ". " + str(t1name) + " WINS THE " + str(year) + " FIFA WORLD CUP on penalities.")
                 prompt.place(x=750, y=800)
                 world_cup_wins[team1[0]] += 1
                 world_cup_loss[team2[0]] += 1
        else:
                 promptvar.set(str(t1name) + " " + str(gnum1) + " - " + str(gnum2) + " " + str(t2name) + ". " + str(t2name) + " WINS THE " + str(year) + " FIFA WORLD CUP on penalities.")
                 prompt.place(x=750, y=800)
                 world_cup_wins[team2[0]] += 1
                 world_cup_loss[team1[0]] += 1
    sorted_loss = sorted(world_cup_loss.items(), key=lambda x: x[1], reverse=True)
    sorted_wins = sorted(world_cup_wins.items(), key=lambda x: x[1], reverse=True)
    sorted_finals = sorted(world_cup_finals.items(), key=lambda x: x[1], reverse=True)
    losses = world_cup_loss[team]
    finals = world_cup_wins[team] + world_cup_loss[team]
    sorted_leader20 = "\n".join([f"{rank+1}. {team}: Wins - {wins}" for rank, (team, wins) in enumerate(sorted_wins[:20])])
    leader20var.set(sorted_leader20)
    leader20.place(x=1600, y=141)
    sorted_leadertc1 = "\n".join([f"{rank+1}. {team}: Wins - {wins}" for rank, (team, wins) in enumerate(sorted_wins[:50])])
    sorted_leadertc2 = "\n".join([f"{rank+51}. {team}: Wins - {wins}" for rank, (team, wins) in enumerate(sorted_wins[51:101])])
    sorted_leadertc3 = "\n".join([f"{rank+101}. {team}: Wins - {wins}" for rank, (team, wins) in enumerate(sorted_wins[102:200])])
    ts1var.set(sorted_leadertc1)
    ts2var.set(sorted_leadertc2)
    ts3var.set(sorted_leadertc3)
    t1namevar.set(t1name)
    t2namevar.set(t2name)
    image1path = f"flags/{str(t1namevar.get()) + '.png'}"
    image2path = f"flags/{str(t2namevar.get()) + '.png'}"
    image1 = Image.open(image1path)
    image1 = image1.resize((300, 200))
    flg1 = ImageTk.PhotoImage(image1)
    team1flg.configure(image=flg1)
    team1flg.image = flg1
    team1flg.place(x=550, y=150)
    image2 = Image.open(image2path)
    image2 = image2.resize((300, 200))
    flg2 = ImageTk.PhotoImage(image2)
    team2flg.configure(image=flg2)
    team2flg.image = flg2
    team2flg.place(x=1150, y=150)
    g1dispvar.set(gnum1)
    g1disp.place(x=680, y=400)
    g2dispvar.set(gnum2)
    g2disp.place(x=1280, y=400)
    vers.place(x=970, y=175)
    n1dispvar.set(t1name)
    n2dispvar.set(t2name)
    n1disp.place(x=550, y=360)
    n2disp.place(x=1150, y=360)
    

# RANK
def rankcol():
    rc1.place(x=670, y=141)
    rc2.place(x=920, y=141)
    rc3.place(x=1170, y=141)
# DYNGRW
def growth():
    for team in teams:
        teams[team] += random.choice(teamgrowth)
        teams[team] = max(31, min(99, teams[team]))
# SIMMER
def sim():
    global year
    subhead1.place(x = 120, y = 113)
    subhead2.place(x = 1595, y = 113)
    year += 4
    yearvar.set(str(year) + " FIFA WORLD CUP")
    cup_year.place(x=825, y=40)
    top40.place(x=115, y=141)
    for team in teams:
        teams[team] += random.choice(teamgrowth)
        teams[team] = max(31, min(99, teams[team]))
        sorted_teams = sorted(teams.items(), key=lambda x: x[1], reverse=True)
        sorted_teams_str = "\n".join([f"{rank+1}. {team} [{rating}]" for rank, (team, rating) in enumerate(sorted_teams[:40])])
        sorted_teams_rc1 = "\n".join([f"{rank+1}. {team} [{rating}]" for rank, (team, rating) in enumerate(sorted_teams[:50])])
        sorted_teams_rc2 = "\n".join([f"{rank+51}. {team} [{rating}]" for rank, (team, rating) in enumerate(sorted_teams[51:101])])
        sorted_teams_rc3 = "\n".join([f"{rank+101}. {team} [{rating}]" for rank, (team, rating) in enumerate(sorted_teams[101:200])])
        rc1var.set(sorted_teams_rc1)
        rc2var.set(sorted_teams_rc2)
        rc3var.set(sorted_teams_rc3)
        teamvar.set(sorted_teams_str)
    matchsim()
    growth()
# VINT
def cleanlabel():
    yearvar.set("                                      ")
    cup_year = Label(root, textvariable=yearvar, font=yearfont)
    cup_year.place(x=825, y=40)
# CWR MENU
def cwr():
    global teams
    clear()
    yearvar.set(str(year) + " WORLD RANKINGS       ")
    cup_year = Label(root, textvariable=yearvar, font=yearfont, bg="Black", fg="White")
    cup_year.place(x=825, y=40)
    rankcol()
# CLEAR FUNC
def clear():
    Simulate.place_forget()
    Continue.place_forget()
    Intro.place_forget()
    cup_year.place_forget()
    top40.place_forget()
    rc1.place_forget()
    rc2.place_forget()
    rc3.place_forget()
    prompt.place_forget()
    leader20.place_forget()
    subhead1.place_forget()
    subhead2.place_forget()
    ts1.place_forget()
    ts2.place_forget()
    ts3.place_forget()
    team1flg.place_forget()
    team2flg.place_forget()
    g1disp.place_forget()
    g2disp.place_forget()
    vers.place_forget()
    n1disp.place_forget()
    n2disp.place_forget()
    

    
# INT SIMMER
def SSim():
    clear()
    Simulate.place(x = 900, y = 900)
    yearvar.set(str(year) + " FIFA WORLD CUP")
# INT
def cont():
    Continue.place_forget()
    Intro.place_forget()
    menubar.add_cascade(label="Simulate", menu=Sim)
    menubar.add_cascade(label="Statistics", menu=Stat)
    menubar.add_cascade(label="Application", menu=App)
# STAT MENU
def stat():
    clear()
    yearvar.set(" CUP STATISTICS ")
    cup_year.place(x=825, y=40)
    ts1.place(x=520, y=140)
    ts2.place(x=860, y=140)
    ts3.place(x=1200, y=140)

Intro = Label(root, text= " Welcome to World Cup Simulator, a fun little tool used to predict future FIFA WORLD CUP results. Click CONTINUE to Proceed.", bg="Black", fg="White")
Intro.place(x = 640, y = 500)
yearvar = StringVar()
cup_year = Label(root, textvariable=yearvar, font=yearfont, bg="Black", fg="White")
teamvar = StringVar()
teamvar.set(sorted_teams_str)
top40 = Label(root, textvariable=teamvar, font=rankfont, justify=LEFT, bg="Red", fg="White")
rc1var = StringVar()
rc1var.set(sorted_teams_rc1)
rc1 = Label(root, textvariable=rc1var, font=cwrfont, justify=LEFT, bg="Black", fg="White")
rc2var = StringVar()
rc2var.set(sorted_teams_rc2)
rc2 = Label(root, textvariable=rc2var, font=cwrfont, justify=LEFT, bg="Black", fg="White")
rc3var = StringVar()
rc3var.set(sorted_teams_rc3)
rc3 = Label(root, textvariable=rc3var, font=cwrfont, justify=LEFT, bg="Black", fg="White")
promptvar = StringVar()
promptvar.set("")
prompt = Label(root, textvariable=promptvar, font=promptfont, justify=CENTER, bg="Black", fg="White")
prompt.place_forget()
leader20var = StringVar()
leader20var.set("")
leader20 = Label(root, textvariable=leader20var, font=rankfont, justify=LEFT, bg="Blue", fg="Gold")
subhead1 = Label(root, text="TOP 40 TEAMS:-", font=subhead, bg="Red", fg="White")
subhead1.place_forget()
subhead2 = Label(root, text="MOST WORLD CUP WINS:-", font=subhead, justify=LEFT, bg="Blue", fg="Gold")
subhead2.place_forget()
ts1var = StringVar()
ts1var.set(sorted_leadertc1)
ts1 = Label(root, textvariable=ts1var, font=cwrfont, justify=LEFT, bg="Black", fg="White")
ts2var = StringVar()
ts2var.set(sorted_leadertc2)
ts2 = Label(root, textvariable=ts2var, font=cwrfont, justify=LEFT, bg="Black", fg="White")
ts3var = StringVar()
ts3var.set(sorted_leadertc3)
ts3 = Label(root, textvariable=ts3var, font=cwrfont, justify=LEFT, bg="Black", fg="White")
team2flg = Label(root)
team2flg.place_forget()
g1dispvar = StringVar()
g1disp = Label(root, textvariable=g1dispvar, bg="Black", fg="White", font=dispfont)
g1disp.place_forget()
g2dispvar = StringVar()
g2disp = Label(root, textvariable=g2dispvar, bg="Black", fg="White", font=dispfont)
g2disp.place_forget()
vers = Label(root, text="V.", bg="Black", fg="White", font=versfont)
n1dispvar = StringVar()
n2dispvar = StringVar()
n1disp = Label(root, textvariable=n1dispvar, bg="Black", fg="White", font=nmdispfont, justify=LEFT)
n2disp = Label(root, textvariable=n2dispvar, bg="Black", fg="White", font=nmdispfont, justify=LEFT)
n1disp.place_forget()
n2disp.place_forget()


Continue = Button(root, text= "CONTINUE", command= cont)
Continue.place(x = 960, y = 540)
Simulate = Button(root, text = "SIMULATE", command= sim, font= yearfont, bg="Yellow", fg="Black")

Sim = Menu(menubar, tearoff=0)
Sim.add_command(label="Sim", command=SSim)
Stat = Menu(menubar, tearoff=0)
Stat.add_command(label="Current World Ranking", command=cwr)
Stat.add_command(label="Cup Statistics", command=stat)
Stat.add_command(label="Graph")
App = Menu(menubar, tearoff=0)
App.add_command(label="Save As")
App.add_command(label="Quit", command=root.quit)


sorted_loss = sorted(world_cup_loss.items(), key=lambda x: x[1], reverse=True)
sorted_wins = sorted(world_cup_wins.items(), key=lambda x: x[1], reverse=True)
sorted_finals = sorted(world_cup_finals.items(), key=lambda x: x[1], reverse=True)
for team, wins in sorted_wins:
     losses = world_cup_loss[team]
     finals = world_cup_wins[team] + world_cup_loss[team]
     print(f"{team}: Wins - {wins}, Losses - {losses}, Finals - {finals}")


root.config(menu=menubar)  
root.mainloop()