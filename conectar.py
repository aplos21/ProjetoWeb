#31/October/2024 -> mms1

#  programa para conectar com o postgressql



import psycopg2

#con = psycopg2.connect(
#host='localhost', 
#database='empresas',
#user='postgres',
#password  = '123',
#port ='5432'
#
#)
#
#print(con.info)
#print(con.status)
#
#---------------------------------------------------------------------------------
#cursor = con.cursor()
#
#cursor.execute("INSERT INTO usuario (nome_cliente, setor, telefone, CPF, cargo) VALUES('Jose mané', 'leste', '8798554454', '15424548', 'chefe');")
#
#cursor.execute('select * from usuario;')
#rows = cursor.fetchall()
#con.commit()
#con.close()
#for row in rows:
#    print(row)
#
#
#cur.execute("INSERT INTO datacamp_courses(course_name, course_instructor, topic) VALUES('Introduction to SQL','Izzy Weber','Julia')");
#
#


#---------------Class para conectar no banco de dados ----------------------------
class Conexao(object):
    _db=None
    #conectando ao banco de dados
    def __init__(self, mhost, db, usr, pwd, port):
        self._db = psycopg2.connect(host=mhost, database=db, user=usr,  password=pwd, port=port)

    #passar comandos sql
    def manipular(self, sql):
        try:
            cur=self._db.cursor()
            cur.execute(sql)
            cur.close();
            self._db.commit()
        except:
            return False;
        return True;
    #fazer uma consulta ao banco de dados
    def consultar(self, sql):
        rs=None
        try:
            cur=self._db.cursor()
            cur.execute(sql)
            rs=cur.fetchall();
        except:
            return None
        return rs
    #passar para a proxima tupla
    def proximaPK(self, tabela, chave):
        sql='select max('+chave+') from '+tabela
        rs = self.consultar(sql)
        pk = rs[0][0]
        return pk+1
    #fechar o banco de dados
    def fechar(self):
        self._db.close()

#con=Conexao('localhost','empresas','postgres','123','5432')
#
#rs=con.consultar("select * from usuario")
#for linha in rs:
#    print (linha)
#con.fechar()
#

#---- usar em outro cod.py-------
#con=conectar.Conexao('localhost','empresas','postgres','123','5432')
#
#rs=con.consultar("select * from usuario")
#for linha in rs:
#    print (linha)
#con.fechar()


