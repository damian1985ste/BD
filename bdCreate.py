import sqlite3
conn = sqlite3.connect('churrinche.db')

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE T_Manejo (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Desc TEXT NOT NULL,
	Estado TEXT)
''')
c.execute('''CREATE TABLE T_Trabajo (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    FechaHora INTERGER NOT NULL)
''')
c.execute('''CREATE TABLE T_Lectura (
    Id INTEGER NOT NULL,
	IdTrab INTERGER NOT NULL,
	IdAnim INTERGER NOT NULL,
	NroCar TEXT NOT NULL,
	FechaHora INTERGER NOT NULL,
	FOREIGN KEY(IdTrab) REFERENCES T_Trabajo(Id),
	FOREIGN KEY(IdAnim) REFERENCES T_Animal(Id))
''')
c.execute('''CREATE TABLE T_Lectura_Manejo (
    IdLectura INTEGER NOT NULL,
    IdManejo INTEGER NOT NULL,
	Valor TEXT,
	FOREIGN KEY(IdLectura) REFERENCES T_Lectura(Id),
	FOREIGN KEY(IdManejo) REFERENCES T_Manejo(Id))
''')
c.execute('''CREATE TABLE T_Animal (
    Id INTEGER NOT NULL,
    NroCar TEXT NOT NULL,
	FechaNac INTERGER)
''')


#Imprimir tablas en la base y su disenio
c.execute("select name from sqlite_master where type = 'table' and name <> 'sqlite_sequence'")
registros = c.fetchall()
for registro in registros:
	print registro
print
c.execute("select sql from sqlite_master where type = 'table' and name <> 'sqlite_sequence'")
registros1 = c.fetchall()
for registro1 in registros1:
	print registro1
	print

	
	
# Insert a row of data
#c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
conn.commit()



# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()