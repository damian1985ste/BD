import sqlite3
conn = sqlite3.connect('churrinche.db')
c = conn.cursor()


# Do this instead
#t = ('RHAT',)
#c.execute('SELECT * FROM stocks WHERE symbol=?', t)
#print c.fetchone()


###------------------T_Manejo-----------------------
### CARGA DATOS EN TABLA T_Manejo ###
# Larger example that inserts many records at a time
nombres = [('Lectura','A'),
            ('Aftosa','A'),
            ('Vientre vacio','M')]
print(nombres)
c.executemany('INSERT INTO T_Manejo(Desc, Estado) VALUES (?,?)', nombres)
### LEE LOS DATOS EN LA TABLA T_Atributos ###

for row in c.execute('SELECT * FROM T_Manejo'):
    print row
###------------------------------------------------------



'''
###------------------T_Cfg_Planilla-----------------------
### CARGA DATOS EN TABLA T_Cfg_Planilla ###
# Larger example that inserts many records at a time
nombres = [('Lectura',),
            ('Aftosa',),
            ('Vientre vacio',)]
print(nombres)
c.executemany('INSERT INTO T_Atributos(Nombre) VALUES (?)', nombres)
### LEE LOS DATOS EN LA TABLA T_Atributos ###
for row in c.execute('SELECT * FROM T_Atributos'):
    print row
###------------------------------------------------------
'''


# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()