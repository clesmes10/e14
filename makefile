fecha_mancha.dat : monthrg.dat ejercicio14.py
	python ejercicio14.py
fecha_mancha.pdf : fecha_mancha.dat grafica.py
	python grafica.py
monthrg.dat :
	wget https://raw.githubusercontent.com/ComputoCienciasUniandes/MetodosComputacionalesDatos/master/hands_on/solar/monthrg.dat
