
rank = {'rank':[
		{'user': 'Saymon',    'color': '#FF1616', 'score': 1600},
		{'user': 'Henrico',   'color': '#FF7637', 'score': 1400},
		{'user': 'Israel',    'color': '#FF1616', 'score': 1100},
        {'user': 'Oliveira',  'color': '#545454', 'score': 9100},
		{'user': 'Benjamin',  'color': '#F9B11F', 'score': 1100},
		{'user': 'Milena',    'color': '#38B6FF', 'score': 900},
		{'user': 'Gustavo',   'color': '#8C52FF', 'score': 600},
		{'user': 'Jonhana',   'color': '#CF3190', 'score': 600},
		{'user': 'Felipe',    'color': '#2F05FF', 'score': 500},
		{'user': 'Alexandre', 'color': '#000000', 'score': 500},
		{'user': 'Luigi',     'color': '#008037', 'score': 400},
		{'user': 'Daniel',    'color': '#B05A42', 'score': 400},
		{'user': 'Daniel G',  'color': '#50AD29', 'score': 400},
		{'user': 'Vitor',     'color': '#782A89', 'score': 400},
		{'user': 'Luis',      'color': '#FF7637', 'score': 200},
		{'user': 'Luca',      'color': '#545454', 'score': 100},
	]
}



for i in range(len(rank['rank'])):
		if 'Oliveira' in rank['rank'][i]['user']:
			rank['rank'][i]['score'] += 1
			x = True
			break
		else:
			x = False
		
if x:
	print("Oliveira existe")
else:
	print("Oliveira não existe")