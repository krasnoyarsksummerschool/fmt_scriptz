import pickle
# -*- coding: utf-8 -*-

# $URL: svn+ssh://svnuser@klsh.org/home/svnuser/klsh_2011/fmt/scripts/schedule.py $
# $Id: schedule.py 12 2011-07-24 11:44:57Z dennis $

################
#### Судьи: ####
################

# Иван АДО alpha главный физика
# Олег ЗОЛОТОВ главный физика
# Иван КАРЛОВ rho главный физика
# Владислав КОЗЛОВ theta главный физика
# Сергей ЛАМЗИН $o$ главный физика
# Виктория ЛУКОВСКАЯ главный
# Михаил САДОВСКИЙ главный физика
# Мария СЕГИНЁВА $\mu$ главный
# Иван ХАРИТОНОВ delta главный физика
# Денис ШПАКОВ $\sigma$ главный физика
# Максим ЩЕРБАКОВ kappa главный физика
# Анна ЯКОВЛЕВА alpha $\beta$ главный

# Павел АВДЕЕНКО alpha физика
# Никита АСТРАХАНЦЕВ xi физика
# Наталья БЛЯНКИНШТЕЙН o физика
# Евгений БУРОВСКИЙ физика
# Юрий ВОПИЛОВ omega физика
# Мариам ДАУТОВА theta
# Борис ДЕМЕШЕВ
# Вероника ИЛЬЯНЕНКО iota xi
# Лев КАМИНСКИЙ phi
# Ксения КЛОКОВА alpha
# Александр МАКУШКИН varepsilon физика
# Александр МЕНЩИКОВ lambda
# Алексей МИРОНОВ sigma физика
# Максим МУСИН iota
# Евгений ОСТРОУХ omega физика
# Кирилл ПАВЛЕНКО kappa физика
# Мария ПРОХОЖАЕВА epsilon
# Евгений САФРОНЕНКО tau
# Иван СМОЛЯР phi физика
# Александр СНЕТКОВ delta
# Юлия СОПКОВА lambda phi
# Дмитрий ЧЕРНОУС beta
# Антон ШЕЙКИН mu физика
# Елизавета ЯКИМЕНКО delta theta gamma



################################
#### LaTeX to Greek Lookup: ####
################################

latex2greek = {}

latex2greek[ r'$\alpha$' ] = 'α'
latex2greek[ r'$\beta$' ] = 'β'
latex2greek[ r'$\gamma$' ] = 'γ'
latex2greek[ r'$\delta$' ] = 'δ'
latex2greek[ r'$\varepsilon$' ] = 'ε'
latex2greek[ r'$\theta$' ] = 'θ'
latex2greek[ r'$\iota$' ] = 'ι'
latex2greek[ r'$\kappa$' ] = 'κ'
latex2greek[ r'$\lambda$' ] = 'λ'
latex2greek[ r'$\xi$' ] = 'ξ'
latex2greek[ r'$o$' ] = 'ο'
latex2greek[ r'$\rho$' ] = 'ρ'
latex2greek[ r'$\sigma$' ] = 'σ'
latex2greek[ r'$\varphi$' ] = 'φ'
latex2greek[ r'$\omega$' ] = 'ω'
latex2greek[ r'$\chi$' ] = 'χ'
latex2greek[ r'$\psi$' ] = 'ψ'
latex2greek[ r'$\ta$' ] = 'η'



year = 2012

schedule = []

#####################
#### Первый тур: ####
#####################

game_1 = {

    'DATE' : 'когда-то 2012 года',

    'MATCHES' : [
    
    { 'TEAM1' : r'$\rho$', 'TEAM2' : r'$\varepsilon$', 'ROOM' : 'где-то',
      'SENIORJUDGE' : '', 'JUDGES' : '',
      'SCORE1' : 3, 'SCORE2' : 1 },
  
    { 'TEAM1' : r'$\delta$', 'TEAM2' : r'$\gamma$', 'ROOM' : 'где-то',
      'SENIORJUDGE' : '', 'JUDGES' : '',
      'SCORE1' : 4, 'SCORE2' : 3 },
    
    { 'TEAM1' : r'$\sigma$', 'TEAM2' : r'$\lambda$', 'ROOM' : 'где-то',
      'SENIORJUDGE' : '', 'JUDGES' : '',
      'SCORE1' : 2, 'SCORE2' : 2 },
    
    { 'TEAM1' : r'$\iota$', 'TEAM2' : r'$\beta$', 'ROOM' : 'где-то',
      'SENIORJUDGE' : '', 'JUDGES' : '',
      'SCORE1' : 4, 'SCORE2' : 5 },
    
    { 'TEAM1' : r'$\alpha$', 'TEAM2' : r'$\kappa$', 'ROOM' : 'где-то',
      'SENIORJUDGE' : '', 'JUDGES' : '',
      'SCORE1' : 6, 'SCORE2' : 2 },
    
    { 'TEAM1' : r'$\varphi$', 'TEAM2' : r'$o$', 'ROOM' : 'где-то',
      'SENIORJUDGE' : '', 'JUDGES' : '',
      'SCORE1' : 4, 'SCORE2' : 0 },
    
    { 'TEAM1' : r'$\xi$', 'TEAM2' : r'$\omega$', 'ROOM' : 'где-то',
      'SENIORJUDGE' : '', 'JUDGES' : '',
      'SCORE1' : 2, 'SCORE2' : 5 },
    
    { 'TEAM1' : r'$\ta$', 'TEAM2' : r'$\theta$', 'ROOM' : 'где-то',
      'SENIORJUDGE' : '', 'JUDGES' : '',
      'SCORE1' : 3, 'SCORE2' : -1 },
    
    { 'TEAM1' : r'$\chi$', 'TEAM2' : r'$\psi$', 'ROOM' : 'где-то',
      'SENIORJUDGE' : '', 'JUDGES' : '',
      'SCORE1' : 6, 'SCORE2' : 0 }

    ]

    }

schedule.append( game_1 )

game_2 = {

    'DATE' : '21 июля 2011 года',

    'MATCHES' : [
    
        { 'TEAM1' : r'$\rho$', 'TEAM2' : r'$\omega$',
          'ROOM' : '1.1',
          'SENIORJUDGE' : 'Михаил САДОВСКИЙ',
          'JUDGES' : 'Юрий ВОПИЛОВ, Ксения КЛОКОВА, Никита АСТРАХАНЦЕВ',
          'SCORE1' : 9, 'SCORE2' : 0 },
    
        { 'TEAM1' : r'$\delta$', 'TEAM2' : r'$\beta$',
          'ROOM' : '1.2',
          'SENIORJUDGE' : 'Максим ЩЕРБАКОВ',
          'JUDGES' : 'Александр МАКУШКИН, Дмитрий ЧЕРНОУС, Вероника ИЛЬЯНЕНКО',
          'SCORE1' : 8, 'SCORE2' : 2 },
    
        { 'TEAM1' : r'$\sigma$', 'TEAM2' : r'$\ta$',
          'ROOM' : '2.1',
          'SENIORJUDGE' : 'Виктория ЛУКОВСКАЯ',
          'JUDGES' : 'Александр МЕНЩИКОВ, Павел АВДЕЕНКО, Александр СНЕТКОВ',
          'SCORE1' : 6, 'SCORE2' : 4 },
    
        { 'TEAM1' : r'$\iota$', 'TEAM2' : r'$\gamma$',
          'ROOM' : '2.2',
          'SENIORJUDGE' : 'Иван АДО',
          'JUDGES' : 'Борис ДЕМЕШЕВ, Юлия СОПКОВА, Алексей МИРОНОВ',
          'SCORE1' : 6, 'SCORE2' : 0 },
    
        { 'TEAM1' : r'$\sigma$', 'TEAM2' : r'$\ta$',
          'ROOM' : '3.2',
          'SENIORJUDGE' : 'Олег ЗОЛОТОВ',
          'JUDGES' : 'Лев КАМИНСКИЙ, Кирилл ПАВЛЕНКО, Евгений САФРОНЕНКО',
          'SCORE1' : 6, 'SCORE2' : 4 },
    
        { 'TEAM1' : r'$\alpha$', 'TEAM2' : r'$\psi$',
          'ROOM' : 'Вечерний клуб',
          'SENIORJUDGE' : 'Иван КАРЛОВ',
          'JUDGES' : 'Максим МУСИН, Антон ШЕЙКИН, Наталья БЛЯНКИНШТЕЙН',
          'SCORE1' : 8, 'SCORE2' : 2 },
    
        { 'TEAM1' : r'$\beta$', 'TEAM2' : r'$\delta$',
          'ROOM' : 'Биохимлаба 5',
          'SENIORJUDGE' : 'Иван ХАРИТОНОВ',
          'JUDGES' : 'Мариам ДАУТОВА, Евгений БУРОВСКИЙ, Иван СМОЛЯР',
          'SCORE1' : 2, 'SCORE2' : 8 },
    
        { 'TEAM1' : r'$\chi$', 'TEAM2' : r'$\varepsilon$',
          'ROOM' : 'Беседка 1 (столовая если дождь)',
          'SENIORJUDGE' : 'Владислав КОЗЛОВ',
          'JUDGES' : 'Елизавета ЯКИМЕНКО, Евгений ОСТРОУХ',
          'SCORE1' : 3, 'SCORE2' : 1 },
    
        { 'TEAM1' : r'$\theta$', 'TEAM2' : r'$o$',
          'ROOM' : 'Беседка 2 (холл столовой если дождь)',
          'SENIORJUDGE' : 'Мария СЕГИНЁВА',
          'JUDGES' : 'Сергей ЛАМЗИН, Мария ПРОХОЖАЕВА',
          'SCORE1' : 5, 'SCORE2' : 2 }

        ]
        
    }

schedule.append( game_2 )

game_3 = {

    'DATE' : '25 июля 2011 года',

    'MATCHES' : [
    
        { 'TEAM1' : r'$\rho$', 'TEAM2' : r'$\alpha$',
          'ROOM' : '1.1',
          'SENIORJUDGE' : '',
          'JUDGES' : '',
          'SCORE1' : 7, 'SCORE2' : 1 },
    
        { 'TEAM1' : r'$\delta$', 'TEAM2' : r'$\chi$',
          'ROOM' : '1.2',
          'SENIORJUDGE' : '',
          'JUDGES' : '',
          'SCORE1' : 7, 'SCORE2' : 0 },
    
        { 'TEAM1' : r'$\sigma$', 'TEAM2' : r'$\theta$',
          'ROOM' : '2.1',
          'SENIORJUDGE' : '',
          'JUDGES' : '',
          'SCORE1' : 6, 'SCORE2' : 1 },
    
        { 'TEAM1' : r'$\lambda$', 'TEAM2' : r'$\iota$',
          'ROOM' : '2.2',
          'SENIORJUDGE' : '',
          'JUDGES' : '',
          'SCORE1' : 6, 'SCORE2' : 4 },
    
        { 'TEAM1' : r'$\ta$', 'TEAM2' : r'$\xi$',
          'ROOM' : '3.2',
          'SENIORJUDGE' : '',
          'JUDGES' : '',
          'SCORE1' : 3, 'SCORE2' : 9 },
    
        { 'TEAM1' : r'$\beta$', 'TEAM2' : r'$\kappa$',
          'ROOM' : 'Вечерний клуб',
          'SENIORJUDGE' : '',
          'JUDGES' : '',
          'SCORE1' : 9, 'SCORE2' : 0 },
    
        { 'TEAM1' : r'$\gamma$', 'TEAM2' : r'$\psi$',
          'ROOM' : 'Биохимлаба 5',
          'SENIORJUDGE' : '',
          'JUDGES' : '',
          'SCORE1' : 5, 'SCORE2' : 1 },
    
        { 'TEAM1' : r'$\varphi$', 'TEAM2' : r'$\varepsilon$',
          'ROOM' : 'Беседка 1 (столовая если дождь)',
          'SENIORJUDGE' : '',
          'JUDGES' : '',
          'SCORE1' : 2, 'SCORE2' : -1 },
    
        { 'TEAM1' : r'$o$', 'TEAM2' : r'$\omega$',
          'ROOM' : 'Беседка 2 (холл столовой если дождь)',
          'SENIORJUDGE' : '',
          'JUDGES' : '',
          'SCORE1' : 0, 'SCORE2' : 3  }

        ]

    }

schedule.append( game_3 )

game_4 = {

    'DATE' : '28 июля 2011 года',

    'MATCHES' : [
    
        { 'TEAM1' : r'$\rho$', 'TEAM2' : r'$\delta$',
          'ROOM' : '1.1',
          'SENIORJUDGE' : '',
          'JUDGES' : '',
          'SCORE1' : 6, 'SCORE2' : 5 },
    
        { 'TEAM1' : r'$\sigma$', 'TEAM2' : r'$\alpha$',
          'ROOM' : '1.2',
          'SENIORJUDGE' : '',
          'JUDGES' : '',
          'SCORE1' : 3, 'SCORE2' : 2 },
    
        { 'TEAM1' : r'$\lambda$', 'TEAM2' : r'$\xi$',
          'ROOM' : '2.1',
          'SENIORJUDGE' : '',
          'JUDGES' : '',
          'SCORE1' : 6, 'SCORE2' : 2 },
    
        { 'TEAM1' : r'$\iota$', 'TEAM2' : r'$\chi$',
          'ROOM' : '2.2',
          'SENIORJUDGE' : '',
          'JUDGES' : '',
          'SCORE1' : 6, 'SCORE2' : -1 },
    
        { 'TEAM1' : r'$\ta$', 'TEAM2' : r'$\varepsilon$',
          'ROOM' : '3.2',
          'SENIORJUDGE' : '',
          'JUDGES' : '',
          'SCORE1' : 4, 'SCORE2' : 0 },
    
        { 'TEAM1' : r'$\beta$', 'TEAM2' : r'$\varphi$',
          'ROOM' : 'Вечерний клуб',
          'SENIORJUDGE' : '',
          'JUDGES' : '',
          'SCORE1' : 0, 'SCORE2' : 0 },
    
        { 'TEAM1' : r'$\gamma$', 'TEAM2' : r'$\omega$',
          'ROOM' : 'Биохимлаба 5',
          'SENIORJUDGE' : '',
          'JUDGES' : '',
          'SCORE1' : 5, 'SCORE2' : 1 },
    
        { 'TEAM1' : r'$\theta$', 'TEAM2' : r'$\kappa$',
          'ROOM' : 'Беседка 1 (столовая если дождь)',
          'SENIORJUDGE' : '',
          'JUDGES' : '',
          'SCORE1' : 3, 'SCORE2' : 2 },
    
        { 'TEAM1' : r'$o$', 'TEAM2' : r'$\psi$',
          'ROOM' : 'Беседка 2 (холл столовой если дождь)',
          'SENIORJUDGE' : '',
          'JUDGES' : '',
          'SCORE1' : 1, 'SCORE2' : 3 }

        ]

    }

schedule.append( game_4 )

game_5 = {

    'DATE' : '1 августа 2011 года',

    'MATCHES' : [
    
        { 'TEAM1' : r'$\rho$', 'TEAM2' : r'$\lambda$',
          'ROOM' : '1.1',
          'SENIORJUDGE' : '',
          'JUDGES' : '',
          'SCORE1' : 7, 'SCORE2' : 6 },
    
        { 'TEAM1' : r'$\delta$', 'TEAM2' : r'$\iota$',
          'ROOM' : '1.2',
          'SENIORJUDGE' : '',
          'JUDGES' : '',
          'SCORE1' : 7, 'SCORE2' : 6 },
    
        { 'TEAM1' : r'$\sigma$', 'TEAM2' : r'$\beta$',
          'ROOM' : '2.1',
          'SENIORJUDGE' : '',
          'JUDGES' : '',
          'SCORE1' : 8, 'SCORE2' : 5 },
    
        { 'TEAM1' : r'$\omega$', 'TEAM2' : r'$\theta$',
          'ROOM' : '2.2',
          'SENIORJUDGE' : '',
          'JUDGES' : '',
          'SCORE1' : 6, 'SCORE2' : 7 },
    
        { 'TEAM1' : r'$\ta$', 'TEAM2' : r'$\chi$',
          'ROOM' : '3.2',
          'SENIORJUDGE' : '',
          'JUDGES' : '',
          'SCORE1' : 2, 'SCORE2' : 10 },
    
        { 'TEAM1' : r'$\alpha$', 'TEAM2' : r'$\varphi$',
          'ROOM' : 'Вечерний клуб',
          'SENIORJUDGE' : '',
          'JUDGES' : '',
          'SCORE1' : 7, 'SCORE2' : 5 },
    
        { 'TEAM1' : r'$\psi$', 'TEAM2' : r'$\kappa$',
          'ROOM' : 'Биохимлаба 5',
          'SENIORJUDGE' : '',
          'JUDGES' : '',
          'SCORE1' : 7, 'SCORE2' : 5 },
    
        { 'TEAM1' : r'$\xi$', 'TEAM2' : r'$\gamma$',
          'ROOM' : 'Беседка 1 (столовая если дождь)',
          'SENIORJUDGE' : '',
          'JUDGES' : '',
          'SCORE1' : 6, 'SCORE2' : 6 },
    
        { 'TEAM1' : r'$\varepsilon$', 'TEAM2' : r'$o$',
          'ROOM' : 'Беседка 2 (холл столовой если дождь)',
          'SENIORJUDGE' : '',
          'JUDGES' : '',
          'SCORE1' : 6, 'SCORE2' : 7 }

        ]

    }

schedule.append( game_5 )

"""
game_6 = {

    'DATE' : '4 августа 2011 года',

    'MATCHES' : [
    
        { 'TEAM1' : r'$$', 'TEAM2' : r'$$',
          'ROOM' : '1.1',
          'SENIORJUDGE' : '',
          'JUDGES' : '',
          'SCORE1' : None, 'SCORE2' : None },
    
        { 'TEAM1' : r'$$', 'TEAM2' : r'$$',
          'ROOM' : '1.2',
          'SENIORJUDGE' : '',
          'JUDGES' : '',
          'SCORE1' : None, 'SCORE2' : None },
    
        { 'TEAM1' : r'$$', 'TEAM2' : r'$$',
          'ROOM' : '2.1',
          'SENIORJUDGE' : '',
          'JUDGES' : '',
          'SCORE1' : None, 'SCORE2' : None },
    
        { 'TEAM1' : r'$$', 'TEAM2' : r'$$',
          'ROOM' : '2.2',
          'SENIORJUDGE' : '',
          'JUDGES' : '',
          'SCORE1' : None, 'SCORE2' : None },
    
        { 'TEAM1' : r'$$', 'TEAM2' : r'$$',
          'ROOM' : '3.2',
          'SENIORJUDGE' : '',
          'JUDGES' : '',
          'SCORE1' : None, 'SCORE2' : None },
    
        { 'TEAM1' : r'$$', 'TEAM2' : r'$$',
          'ROOM' : 'Вечерний клуб',
          'SENIORJUDGE' : '',
          'JUDGES' : '',
          'SCORE1' : None, 'SCORE2' : None },
    
        { 'TEAM1' : r'$$', 'TEAM2' : r'$$',
          'ROOM' : 'Биохимлаба 5',
          'SENIORJUDGE' : '',
          'JUDGES' : '',
          'SCORE1' : None, 'SCORE2' : None },
    
        { 'TEAM1' : r'$$', 'TEAM2' : r'$$',
          'ROOM' : 'Беседка 1 (столовая если дождь)',
          'SENIORJUDGE' : '',
          'JUDGES' : '',
          'SCORE1' : None, 'SCORE2' : None },
    
        { 'TEAM1' : r'$$', 'TEAM2' : r'$$',
          'ROOM' : 'Беседка 2 (холл столовой если дождь)',
          'SENIORJUDGE' : '',
          'JUDGES' : '',
          'SCORE1' : None, 'SCORE2' : None }

        ]

    }

schedule.append( game_6 )
"""

#################
#### Свалка: ####
#################

svalka_date = '5 августа 2012 года'

empty_svalka = [

    { 'TEAM' : r'$\alpha$',
      'JUDGE' : '',
      'SCORES' : [ ( None, 0 ), ( None, 0 ), ( None, 0 ), ( None, 0 ) ] },

    { 'TEAM' : r'$\beta$',
      'JUDGE' : '',
      'SCORES' : [ ( None, 0 ), ( None, 0 ), ( None, 0 ), ( None, 0 ) ] },

    { 'TEAM' : r'$\gamma$',
      'JUDGE' : '',
      'SCORES' : [ ( None, 0 ), ( None, 0 ), ( None, 0 ), ( None, 0 ) ] },

    { 'TEAM' : r'$\delta$',
      'JUDGE' : '',
      'SCORES' : [ ( None, 0 ), ( None, 0 ), ( None, 0 ), ( None, 0 ) ] },

    { 'TEAM' : r'$\varepsilon$',
      'JUDGE' : '',
      'SCORES' : [ ( None, 0 ), ( None, 0 ), ( None, 0 ), ( None, 0 ) ] },

    { 'TEAM' : r'$\theta$',
      'JUDGE' : '',
      'SCORES' : [ ( None, 0 ), ( None, 0 ), ( None, 0 ), ( None, 0 ) ] },

    { 'TEAM' : r'$\iota$',
      'JUDGE' : '',
      'SCORES' : [ ( None, 0 ), ( None, 0 ), ( None, 0 ), ( None, 0 ) ] },

    { 'TEAM' : r'$\kappa$',
      'JUDGE' : '',
      'SCORES' : [ ( None, 0 ), ( None, 0 ), ( None, 0 ), ( None, 0 ) ] },

    { 'TEAM' : r'$\lambda$',
      'JUDGE' : '',
      'SCORES' : [ ( None, 0 ), ( None, 0 ), ( None, 0 ), ( None, 0 ) ] },

    { 'TEAM' : r'$\ta$',
      'JUDGE' : '',
      'SCORES' : [ ( None, 0 ), ( None, 0 ), ( None, 0 ), ( None, 0 ) ] },

    { 'TEAM' : r'$\xi$',
      'JUDGE' : '',
      'SCORES' : [ ( None, 0 ), ( None, 0 ), ( None, 0 ), ( None, 0 ) ] },

    { 'TEAM' : r'$o$',
      'JUDGE' : '',
      'SCORES' : [ ( None, 0 ), ( None, 0 ), ( None, 0 ), ( None, 0 ) ] },

    { 'TEAM' : r'$\chi$',
      'JUDGE' : '',
      'SCORES' : [ ( None, 0 ), ( None, 0 ), ( None, 0 ), ( None, 0 ) ] },

    { 'TEAM' : r'$\rho$',
      'JUDGE' : '',
      'SCORES' : [ ( None, 0 ), ( None, 0 ), ( None, 0 ), ( None, 0 ) ] },

    { 'TEAM' : r'$\sigma$',
      'JUDGE' : '',
      'SCORES' : [ ( None, 0 ), ( None, 0 ), ( None, 0 ), ( None, 0 ) ] },

    { 'TEAM' : r'$\psi$',
      'JUDGE' : '',
      'SCORES' : [ ( None, 0 ), ( None, 0 ), ( None, 0 ), ( None, 0 ) ] },

    { 'TEAM' : r'$\varphi$',
      'JUDGE' : '',
      'SCORES' : [ ( None, 0 ), ( None, 0 ), ( None, 0 ), ( None, 0 ) ] },

    { 'TEAM' : r'$\omega$',
      'JUDGE' : '',
      'SCORES' : [ ( None, 0 ), ( None, 0 ), ( None, 0 ), ( None, 0 ) ] }
]

################### if svalka.pkl exists, load it; otherwise use default
 
try:
  svalka_file=open('svalka.pkl','rb')
  svalka = pickle.load(svalka_file)
  svalka_file.close()
except IOError:
  print "empty svalka loaded..."
  svalka=empty_svalka


def add_results(num,team1, team2, score1, score2):
	game=schedule[num]
	
	matches=game["MATCHES"]
	found=0
	for match in matches:
		if match['TEAM1']==team1: found=1
		if match['TEAM2']==team1: found=2
	
	if found==0:
		schedule[num]["MATCHES"].append({'TEAM1':team1,'TEAM2':team2, 'SCORE1':score1, 'SCORE2':score2})

print "loading schedule (fmt results) from tab separated file..."
f=open("fmt_results.txt", 'rb')
lines=0

#NOTE: update with number of FMT games (main part)
games=6
teams=18

schedule=[]

"""
game_1 = {

    'DATE' : 'когда-то 2012 года',

    'MATCHES' : [
    
    { 'TEAM1' : r'$\rho$', 'TEAM2' : r'$\varepsilon$', 'ROOM' : 'где-то',
      'SENIORJUDGE' : '', 'JUDGES' : '',
      'SCORE1' : 3, 'SCORE2' : 1 },
"""
for game in range(0,games):
	schedule.append({'DATE' : 'когда-то 2012 года','MATCHES' :[]})
	

for line in f:
	lines=lines+1
	#skip header in tab separated file
	if lines<3:
		continue
	
	s=line.strip().split("	")

	for game in range(0,games):
		team1=s[0]
		team2=s[2+4*game]
		score1=float(s[3+4*game])
		score2=float(s[4+4*game])
		
		add_results(game, team1, team2, score1, score2)

	
	print s
"""
#debug print out of schedule
for game in range(0,games):
	print schedule[game]
	print len(schedule[game]['MATCHES'])


for t in latex2greek:
	print t
	
print "-"

def get_score(team, num):
	game=schedule[num]
	for match in game["MATCHES"]:
		if match["TEAM1"]==team:
			return match["TEAM1"], match["TEAM2"], match["SCORE1"], match["SCORE2"]
		if match["TEAM2"]==team:
			return match["TEAM2"], match["TEAM1"], match["SCORE2"], match["SCORE1"]
	print "Oops!!"
	

for team in latex2greek:
	line=""
	print team
	for match in range(0,4):
		print match
		if match==0:
			line=line+get_score(team,match)[0]+", "+get_score(team,match)[1]
		line=line+", "+str(get_score(team,match)[2])+", "+str(get_score(team,match)[3])
		
	print line
"""	