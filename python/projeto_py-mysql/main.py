#importar a biblioteca que serve para conectar o python ao banco de dados
import mysql.connector

#executa uma função da lib que realiza a conexão
conexao = mysql.connector.connect(
#parametros de conexão ao banco de dados
    host = "localhost",
    user = "root",
    password = "admin",
    database = "oficina"
)

print("conectado")

# função cursor() da lib, serve para manipular os dados de envio para o banco
cursor = conexao.cursor()

#comandos e valores para envio de dados em SQL
sql = "insert into funcionarios (nome,idade,data_nascimento) values (%s,%s,%s)"
values = ("pedrinho",15,'2026-04-30')

cursor.execute(sql,values)
conexao.commit()

cursor.execute("select * from funcionarios")
resultados = cursor.fetchall()

for i in resultados:
    print(i)
