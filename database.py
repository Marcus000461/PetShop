import sqlite3

def conectar():
    return sqlite3.connect("petshop.db")

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()

    # Tabela de Pets
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        especie TEXT NOT NULL,
        raca TEXT NOT NULL,
        idade INTEGER NOT NULL,
        responsavel TEXT NOT NULL,
        telefone TEXT NOT NULL,
        data_cadastro DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Nova Tabela: Agendamentos (Conectada à tabela de pets pelo id_pet)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS agendamentos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_pet INTEGER NOT NULL,
        servico TEXT NOT NULL,
        data_hora TEXT NOT NULL,
        FOREIGN KEY (id_pet) REFERENCES pets (id)
    )
    """)

    conn.commit()
    conn.close()

def salvar_pet(nome, especie, raca, idade, responsavel, telefone):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO pets (nome, especie, raca, idade, responsavel, telefone)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (nome, especie, raca, idade, responsavel, telefone))
    conn.commit()
    conn.close()
    print(f"🐾 {nome} cadastrado com sucesso!")

def listar_pets():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pets")
    resultado = cursor.fetchall()
    conn.close()
    return resultado

def deletar_pet(id_pet):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM pets WHERE id = ?", (id_pet,))
    conn.commit()
    conn.close()
    print(f"🗑️ Pet com ID {id_pet} removido com sucesso!")

def atualizar_pet(id_pet, nova_idade, novo_telefone):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
    UPDATE pets 
    SET idade = ?, telefone = ? 
    WHERE id = ?
    """, (nova_idade, novo_telefone, id_pet))
    conn.commit()
    conn.close()
    print(f"🔄 Dados do pet com ID {id_pet} atualizados com sucesso!")

# --- NOVAS FUNÇÕES PARA O AGENDAMENTO ---

def salvar_agendamento(id_pet, servico, data_hora):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO agendamentos (id_pet, servico, data_hora)
    VALUES (?, ?, ?)
    """, (id_pet, servico, data_hora))
    conn.commit()
    conn.close()
    print(f"📅 Serviço de {servico} agendado com sucesso!")

def listar_agendamentos():
    conn = conectar()
    cursor = conn.cursor()
    
   
    cursor.execute("""
    SELECT agendamentos.id, pets.nome, agendamentos.servico, agendamentos.data_hora
    FROM agendamentos
    JOIN pets ON agendamentos.id_pet = pets.id
    """)
    resultado = cursor.fetchall()
    conn.close()
    return resultado