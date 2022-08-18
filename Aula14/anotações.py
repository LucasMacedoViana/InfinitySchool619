import pymysql.cursors

conexao = pymysql.connect(host='localhost',
                          user='root',
                          password='admin',
                          database='banco',
                          cursorclass=pymysql.cursors.DictCursor)


with conexao.cursor() as cursor:
    sqlIn = "INSERT INTO conta_bancaria (titular, saldo) values ( %s, %s)"
    sqlUp = "update conta_bancaria set "
    sqlDel = "DELETE FROM conta_bancaria WHERE numero_conta = %s"
    cursor. execute(sqlDel, (2,))
    conexao.commit()

cursor = conexao.cursor()

cursor.execute("SELECT * FROM conta_bancaria")

resultado = cursor.fetchall()
print(resultado)

for conta_bancaria in resultado:
    print(conta_bancaria)


