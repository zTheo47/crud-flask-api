from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def conectar():
    conn = sqlite3.connect('banco.db')
    conn.row_factory = sqlite3.Row
    return conn

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

criar_tabela()

@app.route('/usuarios', methods=['GET'])
def listar():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    conn.close()

    resultado = []
    for u in usuarios:
        resultado.append({
            "id": u["id"],
            "nome": u["nome"],
            "idade": u["idade"]
        })

    return jsonify(resultado)

@app.route('/usuarios', methods=['POST'])
def criar():
    dados = request.json
    nome = dados['nome']
    idade = dados['idade']

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO usuarios (nome, idade) VALUES (?, ?)",
        (nome, idade)
    )
    conn.commit()
    conn.close()

    return jsonify({"mensagem": "Usuário criado com sucesso"})

@app.route('/usuarios/<int:id>', methods=['PUT'])
def atualizar(id):
    dados = request.json
    nome = dados['nome']
    idade = dados['idade']

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE usuarios SET nome = ?, idade = ? WHERE id = ?",
        (nome, idade, id)
    )
    conn.commit()
    conn.close()

    return jsonify({"mensagem": "Usuário atualizado"})

@app.route('/usuarios/<int:id>', methods=['DELETE'])
def deletar(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    return jsonify({"mensagem": "Usuário deletado"})

if __name__ == '__main__':
    app.run(debug=True)