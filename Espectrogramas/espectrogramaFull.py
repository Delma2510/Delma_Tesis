# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 00:06:09 2021

@author: delma
"""

import numpy as np
import matplotlib.pyplot as plt
import obspy 
from obspy import read
from obspy.imaging.cm import obspy_sequential
from scipy import fftpack
import os
from obspy.imaging.spectrogram import spectrogram

#Dir = "Catalogo"
#Dir = "Notec"
ejemplo_dir = "/home/delma/Desktop/Versiones/Datos/"+Dir+"/"

contenido = os.listdir(ejemplo_dir)
#file = []
for fichero in contenido:
	if os.path.isfile(os.path.join(ejemplo_dir, fichero)) and fichero.endswith('.sac'):
		#file.append(fichero)
		path = "/home/delma/Desktop/Versiones/Datos/"+Dir+"/"+fichero[:-5]+"*"
		st = read(path)
		st.detrend("linear")
		st.detrend("demean")
		st.taper(0.01)	
		st[0].filter('highpass', freq=1, corners=4, zerophase=True)
		starttime = st[0].stats.starttime+0
		endtime = st[0].stats.starttime+90
		st.trim(starttime,endtime)
		for tr in st: 
			channel = tr.stats.channel
			title = tr.stats.starttime
			path_out = "/home/delma/Desktop/Versiones/Datos/Espectrogramas/"+Dir+"/"+fichero[:-16]+channel+"_"+Dir+".png"			
			fig = spectrogram(tr.data,st[0].stats.sampling_rate,per_lap=.12,log=True,wlen=1,title = title,clip=([0.0,0.5]),outfile=path_out)
			plt.close(fig)