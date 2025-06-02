from flask import Flask, render_template # Criar o site
from flask_socketio import SocketIO, send # Criar o chat

app = Flask(__name__) # Criar o site
app.config["SECRET"] = "!Ld19wk(dk1-3dKJjm2i)SOkQLSl91lç" # Chave de segurança
app.config["DEBUG"] = True #Testar o código
socketio = SocketIO(app, cors_allowed_origins="*") # Criar conexão entre diferentes máquinas que acessarão o site

@socketio.on("message") # Define que a função abaixo vai ser acionada quando o evento 'message' acontecer
def gerenciar_mensagens(mensagem):
    print(f"Mensagem: {mensagem}")
    send(mensagem, broadcast=True) # Envia a msg para todo mundo conectado no site

@app.route("/") # Cria a página do site
def home():
    return render_template("index.html") # A página vai carregar o arquivo html com esse nome.

if __name__ == "__main__":
    socketio.run(app, host='localhost') # Define que o app vai rodar no servidos local
    #Internet local