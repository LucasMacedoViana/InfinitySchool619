#pip install pymysql --- instalando o pacote

import pymysql.cursors



#criando conexão com o banco de dados
conexao = pymysql.connect(host='localhost',
                            user= 'root',
                            passwd='admin',
                            database='escola',
                            cursorclass=pymysql.cursors.DictCursor)
#criando função para listar
def listar():
    with conexao.cursor() as cursor:
        try:
            #comando sql
            sql = "select * from aluno"
            cursor.execute(sql)
            #criar umavariavel para "fatiar" o resultado da pesquisa
            resultado = cursor.fetchall()
            print(resultado)
            #printando com laço de repetição
            for aluno in resultado:
                print(resultado)
        #caso dê algum erro
        except:
            print("Erro ao consultar os dados!")

def inserir(nome, idade, curso):
    with conexao.cursor() as cursor:
        try:
            sql = "insert into aluno (nome,idade, curso) values (%s, %s, %s)"
            cursor.execute(sql,(nome,idade,curso))
            conexao.commit()
            print("Aluno cadastrado")
        except:
             print("Erro ao cadastrar")

def alterar(nome, idade, curso, matricula):
    with conexao.cursor() as cursor:
        try:
            sql = "update aluno set nome = %s, idade = %s, curso = %s where matricula = %s"
            cursor.execute(sql,(nome, idade, curso, matricula))
            conexao.commit()
            print("Aluno alterado com sucesso!")
        except:
            print("Erro ao alterar!")

def excluir (matricula):
    with conexao.cursor() as cursor:
        try:
            sql = "delete from aluno where matricula = %s"
            cursor.execute(sql,(matricula,))
            conexao.commit()
            print("Aluno excluido com sucesso")
        except:
            print("Erro ao excluir")
#excluir()
inserir("Lucas", 27, "python")
listar()
#alterar("Lucas", 30, "GoLang",2 )
#listar()

#------------------------------------------------------------------
