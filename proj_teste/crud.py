from database import Database


class ClienteCRUD:
    """Classe com todas as operações CRUD para clientes."""
    
    def __init__(self):
        self.db = Database("localhost", "prof", "dev_mysql", "proj_teste")
        self.db.connect()
    
    # =============================================
    # CREATE - Cadastrar novo cliente
    # =============================================
    def cadastrar(self, nome, email, telefone, cidade):
        """Insere um novo cliente no banco de dados."""
        query = """
            INSERT INTO clientes (nome, email, telefone, cidade)
            VALUES (%s, %s, %s, %s)
        """
        valores = (nome, email, telefone, cidade)
        resultado = self.db.executar_query(query, valores)
        
        if resultado:
            print(f"✅ Cliente '{nome}' cadastrado com ID: {resultado.lastrowid}")
            return resultado.lastrowid
        return None
    
    # =============================================
    # READ - Consultar clientes
    # =============================================
    def listar_todos(self):
        """Retorna todos os clientes cadastrados."""
        query = "SELECT * FROM clientes ORDER BY nome"
        return self.db.buscar_dados(query)
    
    def buscar_por_id(self, cliente_id):
        """Busca um cliente específico pelo ID."""
        query = "SELECT * FROM clientes WHERE id = %s"
        resultado = self.db.buscar_dados(query, (cliente_id,))
        return resultado[0] if resultado else None
    
    def buscar_por_nome(self, nome):
        """Busca clientes pelo nome (busca parcial)."""
        query = "SELECT * FROM clientes WHERE nome LIKE %s"
        return self.db.buscar_dados(query, (f"%{nome}%",))
    
    # =============================================
    # UPDATE - Atualizar cliente
    # =============================================
    def atualizar(self, cliente_id, nome, email, telefone, cidade):
        """Atualiza os dados de um cliente existente."""
        query = """
            UPDATE clientes 
            SET nome = %s, email = %s, telefone = %s, cidade = %s
            WHERE id = %s
        """
        valores = (nome, email, telefone, cidade, cliente_id)
        resultado = self.db.executar_query(query, valores)
        
        if resultado:
            print(f"✅ Cliente ID {cliente_id} atualizado!")
            return True
        return False
    
    # =============================================
    # DELETE - Excluir cliente
    # =============================================
    def excluir(self, cliente_id):
        """Remove um cliente do banco de dados."""
        query = "DELETE FROM clientes WHERE id = %s"
        resultado = self.db.executar_query(query, (cliente_id,))
        
        if resultado:
            print(f"🗑️ Cliente ID {cliente_id} excluído!")
            return True
        return False
    
    def fechar(self):
        """Fecha a conexão com o banco."""
        self.db.disconnect()
