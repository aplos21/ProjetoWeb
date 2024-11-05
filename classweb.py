#01/november/2024-> mms1
# classe usuario referente ao banco de dados da web

import conectar


class User:

    # Inicializador com atributos da instância
    def atrib(self, nome_cliente, setor, telefone,CPF,cargo):
        self.nome_cliente = nome_cliente    
        self.setor = setor  
        self.telefone = telefone        
        self.CPF = CPF   
        self.cargo = cargo   
    # inserir dados na tabela
    def inserir(self):
# ----- conectar ao bando de dados 
        con=conectar.Conexao('localhost','empresas','postgres','123','5432')
        sql = "insert into usuario(nome_cliente, setor, telefone, CPF, cargo) values(" + "'" + self.nome_cliente + "'" + ',' + "'" + self.setor +"'" + ',' +"'" + self.telefone +"'" + ',' +"'" + self.CPF + "'" +',' + "'" +self.cargo +"'" + ");"
        print(con.manipular(sql))
        if con.manipular(sql):
            print('inserido com sucesso!')
        con.fechar()
 
# ----- consultar tabela    
    def consultar(self):
        con=conectar.Conexao('localhost','empresas','postgres','123','5432')
        
        rs=con.consultar("select * from usuario")
        for linha in rs:
            print (linha)
        con.fechar()




#us = User('otarrior', 'oeste', '66666645', '66664548', 'lacaio')
#us.inserir()

us = User()
us.atrib('otar', 'oeste2', '66666625', '66664', 'lac2aio')
us.inserir()
us.consultar()
