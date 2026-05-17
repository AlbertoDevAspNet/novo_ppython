from database import Database
# Instancia do Banco de Dados 

db= Database("localhost", "prof", "dev_mysql", "proj_teste")

# Teste de Conexão
db.connect()

conexao = db.connect()


if conexao:
    print("Conexão estabelecida com sucesso!")
    cursor = conexao.cursor()
    cursor.execute("SELECT VERSION()")
    versao = cursor.fetchone()
    print(f"📌 MySQL versão: {versao[0]}")
    
    # Desconectar
    db.desconectar()

    
    print("⚠️ Verifique suas credenciais!")
