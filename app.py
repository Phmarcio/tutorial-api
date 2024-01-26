from flask import Flask, jsonify, request

app = Flask(__name__)

livros =[
    {
        'id': 1,
        'titulo':'o senhor do aneis',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'titulo':'o hobbit',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 3,
        'titulo':'O senhor dos anéis - A sociedade do anel',
        'autor': 'J.R.R Tolkien'
    }
]

@app.route('/')
def hello():
    return 'Tutorial - Criando uma API!'

#listar todos os livros
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

#listar livros por ID
@app.route('/livros/<int:id>')
def obter_livros_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

#editar livros
@app.route('/livros/<int:id>', methods=['PUT'])        
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
     
#criar livro
@app.route('/livros', methods=['POST'])
def incluir_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

#excluir livro
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    
    return jsonify(livros)

if __name__ == '__main__':
    app.run(debug=True)