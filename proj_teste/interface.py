import tkinter as tk
from tkinter import ttk, messagebox
from crud import ClienteCRUD


class SistemaCadastro:
    """Interface gráfica do sistema de cadastro de clientes."""
    
    def __init__(self):
        self.crud = ClienteCRUD()
        self.janela = tk.Tk()
        self.janela.title("📋 Sistema de Cadastro de Clientes")
        self.janela.geometry("800x600")
        self.janela.configure(bg="#f0f0f0")
        
        self.criar_widgets()
        self.atualizar_tabela()
    
    def criar_widgets(self):
        """Cria todos os componentes da interface."""
        
        # ============ FRAME SUPERIOR - Formulário ============
        frame_form = tk.LabelFrame(
            self.janela, 
            text=" Dados do Cliente ",
            font=("Arial", 12, "bold"),
            padx=15, pady=15,
            bg="#f0f0f0"
        )
        frame_form.pack(fill="x", padx=15, pady=(15, 5))
        
        # Campo Nome
        tk.Label(frame_form, text="Nome:", font=("Arial", 10), bg="#f0f0f0"
            ).grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.entry_nome = tk.Entry(frame_form, width=35, font=("Arial", 10))
        self.entry_nome.grid(row=0, column=1, padx=5, pady=5)
        
        # Campo Email
        tk.Label(frame_form, text="Email:", font=("Arial", 10), bg="#f0f0f0"
            ).grid(row=0, column=2, sticky="e", padx=5, pady=5)
        self.entry_email = tk.Entry(frame_form, width=35, font=("Arial", 10))
        self.entry_email.grid(row=0, column=3, padx=5, pady=5)
        
        # Campo Telefone
        tk.Label(frame_form, text="Telefone:", font=("Arial", 10), bg="#f0f0f0"
            ).grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.entry_telefone = tk.Entry(frame_form, width=35, font=("Arial", 10))
        self.entry_telefone.grid(row=1, column=1, padx=5, pady=5)
        
        # Campo Cidade
        tk.Label(frame_form, text="Cidade:", font=("Arial", 10), bg="#f0f0f0"
            ).grid(row=1, column=2, sticky="e", padx=5, pady=5)
        self.entry_cidade = tk.Entry(frame_form, width=35, font=("Arial", 10))
        self.entry_cidade.grid(row=1, column=3, padx=5, pady=5)
        
        # ============ FRAME DE BOTÕES ============
        frame_botoes = tk.Frame(self.janela, bg="#f0f0f0")
        frame_botoes.pack(fill="x", padx=15, pady=10)
        
        botoes = [
            ("➕ Cadastrar", "#4CAF50", self.cadastrar_cliente),
            ("✏️ Atualizar", "#2196F3", self.atualizar_cliente),
            ("🗑️ Excluir", "#f44336", self.excluir_cliente),
            ("🔍 Buscar", "#FF9800", self.buscar_cliente),
            ("🧹 Limpar", "#9E9E9E", self.limpar_campos),
        ]
        
        for texto, cor, comando in botoes:
            tk.Button(
                frame_botoes,
                text=texto,
                command=comando,
                bg=cor,
                fg="white",
                font=("Arial", 10, "bold"),
                width=12,
                cursor="hand2",
                relief="flat",
                activebackground=cor
            ).pack(side="left", padx=4)
        
        # ============ FRAME DA TABELA ============
        frame_tabela = tk.LabelFrame(
            self.janela,
            text=" Clientes Cadastrados ",
            font=("Arial", 12, "bold"),
            padx=10, pady=10,
            bg="#f0f0f0"
        )
        frame_tabela.pack(fill="both", expand=True, padx=15, pady=(5, 15))
        
        # Scrollbar
        scroll_y = tk.Scrollbar(frame_tabela, orient="vertical")
        scroll_y.pack(side="right", fill="y")
        
        # Treeview (tabela)
        colunas = ("ID", "Nome", "Email", "Telefone", "Cidade")
        self.tabela = ttk.Treeview(
            frame_tabela,
            columns=colunas,
            show="headings",
            yscrollcommand=scroll_y.set,
            height=12
        )
        scroll_y.config(command=self.tabela.yview)
        
        # Configurar colunas
        larguras = {"ID": 50, "Nome": 180, "Email": 200, "Telefone": 130, "Cidade": 120}
        for col in colunas:
            self.tabela.heading(col, text=col)
            self.tabela.column(col, width=larguras[col], anchor="center")
        
        self.tabela.pack(fill="both", expand=True)
        
        # Evento de clique na tabela
        self.tabela.bind("<<TreeviewSelect>>", self.selecionar_cliente)
        
        # ============ BARRA DE STATUS ============
        self.status_var = tk.StringVar(value="Pronto")
        barra_status = tk.Label(
            self.janela,
            textvariable=self.status_var,
            relief="sunken",
            anchor="w",
            font=("Arial", 9),
            bg="#e0e0e0",
            padx=10
        )
        barra_status.pack(fill="x", side="bottom")
    
    # ====================================================
    # MÉTODOS CRUD
    # ====================================================
    
    def cadastrar_cliente(self):
        """Cadastra um novo cliente."""
        nome = self.entry_nome.get().strip()
        email = self.entry_email.get().strip()
        telefone = self.entry_telefone.get().strip()
        cidade = self.entry_cidade.get().strip()
        
        if not nome or not email:
            messagebox.showwarning("Atenção", "Nome e Email são obrigatórios!")
            return
        
        self.crud.cadastrar(nome, email, telefone, cidade)
        self.atualizar_tabela()
        self.limpar_campos()
        self.status_var.set(f"✅ Cliente '{nome}' cadastrado com sucesso!")
        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
    
    def atualizar_cliente(self):
        """Atualiza o cliente selecionado."""
        selecionado = self.tabela.selection()
        if not selecionado:
            messagebox.showwarning("Atenção", "Selecione um cliente na tabela!")
            return
        
        item = self.tabela.item(selecionado[0])
        cliente_id = item["values"][0]
        
        nome = self.entry_nome.get().strip()
        email = self.entry_email.get().strip()
        telefone = self.entry_telefone.get().strip()
        cidade = self.entry_cidade.get().strip()
        
        if not nome or not email:
            messagebox.showwarning("Atenção", "Nome e Email são obrigatórios!")
            return
        
        self.crud.atualizar(cliente_id, nome, email, telefone, cidade)
        self.atualizar_tabela()
        self.limpar_campos()
        self.status_var.set(f"✅ Cliente ID {cliente_id} atualizado!")
    
    def excluir_cliente(self):
        """Exclui o cliente selecionado."""
        selecionado = self.tabela.selection()
        if not selecionado:
            messagebox.showwarning("Atenção", "Selecione um cliente na tabela!")
            return
        
        confirmar = messagebox.askyesno(
            "Confirmar Exclusão",
            "Tem certeza que deseja excluir este cliente?"
        )
        
        if confirmar:
            item = self.tabela.item(selecionado[0])
            cliente_id = item["values"][0]
            self.crud.excluir(cliente_id)
            self.atualizar_tabela()
            self.limpar_campos()
            self.status_var.set(f"🗑️ Cliente ID {cliente_id} excluído!")
    
    def buscar_cliente(self):
        """Busca clientes pelo nome."""
        nome = self.entry_nome.get().strip()
        if not nome:
            self.atualizar_tabela()
            return
        
        resultados = self.crud.buscar_por_nome(nome)
        self.tabela.delete(*self.tabela.get_children())
        for cliente in resultados:
            self.tabela.insert("", "end", values=cliente[:5])
        
        self.status_var.set(f"🔍 {len(resultados)} resultado(s) encontrado(s)")
    
    def selecionar_cliente(self, event):
        """Preenche os campos ao selecionar um cliente na tabela."""
        selecionado = self.tabela.selection()
        if selecionado:
            item = self.tabela.item(selecionado[0])
            valores = item["values"]
            
            self.limpar_campos()
            self.entry_nome.insert(0, valores[1])
            self.entry_email.insert(0, valores[2])
            self.entry_telefone.insert(0, valores[3])
            self.entry_cidade.insert(0, valores[4])
    
    def atualizar_tabela(self):
        """Recarrega os dados da tabela."""
        self.tabela.delete(*self.tabela.get_children())
        clientes = self.crud.listar_todos()
        for cliente in clientes:
            self.tabela.insert("", "end", values=cliente[:5])
        self.status_var.set(f"📋 {len(clientes)} cliente(s) cadastrado(s)")
    
    def limpar_campos(self):
        """Limpa todos os campos do formulário."""
        self.entry_nome.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_telefone.delete(0, tk.END)
        self.entry_cidade.delete(0, tk.END)
    
    def executar(self):
        """Inicia o loop principal da interface."""
        self.janela.mainloop()
        self.crud.fechar()
