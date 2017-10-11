#!/usr/bin/python
import sqlite3
conn = sqlite3.connect('churrinche.db')
c = conn.cursor()

class animal:
  def __init__(self, NroCarav, FechaNac = 0 ):
    '''Esta funcion crea la instancia de la clase animal'''
    self.NroCarav = NroCarav
    self.FechaNac = FechaNac
	#Escribir en la base de datos
	conn = sqlite3.connect('churrinche.db')
	c = conn.cursor()
	if c.execute('SELECT * FROM T_Animal WHERE NroCarav = (?)',self.NroCarav).fetchone():
		conn.close()
		return('El animal ya existe')
	else:
		c.execute('INSERT INTO T_Animal(NroCarav, FechaNac) VALUES (?,?)', self.NroCarav, self.FechaNac)
		Id = c.execute('SELECT Id FROM T_Animal WHERE NroCarav = (?)',self.NroCarav).fetchone()
		conn.commit()
		conn.close()
		return(Id)
		
#def setFechaNac(self, FechaNac):

#def setNroCarav(self, NroCarav)

#def getAnimalbyId(self, Id):

#def getAnimalbyNroCarav(self, NroCarav):	

#  def beep(self, t_sec):
    ''' Esta funcion emite un pitido de duracion t_sec'''
#    self.gpio.output(self.pin,1)
#    time.sleep(t_sec)
#    self.gpio.output(self.pin,0)
    
#  def beepXk(self, k_pitidos, t_pit_sec = 0.2, t_sil_sec = 0.2):
    '''Esta funcion emite un numero k_pitidos de pitidos
    sonando por un tiempo en segundos de t_pit_sec y haciendo
    un silencio de t_sil_sec segundos para cada pitido'''
#    for k in range(k_pitidos):
#      self.gpio.output(self.pin,1)
#      time.sleep(t_pit_sec)
#      self.gpio.output(self.pin,0)
#      time.sleep(t_sil_sec)