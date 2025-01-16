from flask import Flask, request, jsonify

app = Flask(__name__)

# Variáveis do servidor (em um banco de dados ou em memória)
variables = {
    'Player1': '0',
    'Player2': '0'
}

# Rota para enviar as variáveis (GET)
@app.route('/get_variable', methods=['GET'])
def get_variable():
    # Pega o nome da variável via parâmetro GET
    var_name = request.args.get('var_name')

    # Verifica se a variável existe
    if var_name and var_name in variables:
        return str(variables[var_name]) # Retorna apenas o valor da variável como string
    else:
        return jsonify({'error': 'Variable not found or missing parameter'}), 404

# Rota para atualizar as variáveis (GET)
@app.route('/set_variable', methods=['GET'])
def set_variable():
    # Pega o nome da variável e o valor via parâmetros GET
    var_name = request.args.get('var_name')
    var_value = request.args.get('var_value')

    if var_name and var_value:
        # Atualiza o valor da variável
        variables[var_name] = var_value
        return jsonify({var_name: var_value}), 200
    else:
        return jsonify({'error': 'Missing variable name or value'}), 400

# Inicia o servidor
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
