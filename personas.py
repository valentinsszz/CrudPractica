import pyodbc

class Persona:
    def __init__(self):
        self.con = pyodbc.connect('Driver={ODBC Driver 18 for SQL Server};'
                        'Server= ZEIN\\SQLEXPRESS;'
                        'Database=CursoPython;'
                        'Trusted_Connection=yes;'
                        'TrustServerCertificate=yes;'
                        'Encrypt=no;')
        self.cursor = self.con.cursor()   
    
    def mostrar(self):   
        query = ('select * from persona')
        self.cursor.execute(query)
        for i in self.cursor:
            print(i)

    def add(self, Nombre, Pais):
        query = ('insert into persona(nombre, pais)'
                    'values(?,?)')
        self.cursor.execute(query,[Nombre, Pais])
        self.cursor.commit()

    def delete(self, id):
        query = ('delete from persona where id = ?')
        self.cursor.execute(query, [id])
        self.cursor.commit()
    def update(self, Nombre, Pais, id):
        query = ('update persona set nombre=?, pais=? where id =?')
        self.cursor.execute(query, [Nombre, Pais, id])
        self.cursor.commit()
