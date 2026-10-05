import psycopg2

# Tenta conectar ao banco de dados
try:
    conexao = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="@100416Mg"
    )

    # Cria um 'cursor' para executar os comandos SQL
    cursor = conexao.cursor()

    print("Conexão com o banco de dados realizada com sucesso!")

    # Vamos buscar aquele Teclado Mecânico que você cadastrou?
    cursor.execute("SELECT nome, preco_revenda FROM Produtos;")
    produtos = cursor.fetchall()

    print("\n--- Produtos no Estoque ---")
    for produto in produtos:
        nome_produto = produto[0]
        preco = produto[1]
        print(f"Produto: {nome_produto} | Preço de Revenda: R$ {preco}")

    # Fecha a conexão para não consumir memória
    cursor.close()
    conexao.close()

except Exception as erro:
    print(f"Erro ao conectar com o banco de dados: {erro}")