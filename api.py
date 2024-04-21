
from flask import Flask, request, jsonify, render_template
from gevent import pywsgi, monkey
from werkzeug.exceptions import HTTPException
from exec_cmd import exec_cat_on_file
from flask_cors import CORS
from flask_socketio import SocketIO

monkey.patch_all()

app = Flask(__name__)
CORS(app)
socket = SocketIO(app)

@socket.on('connect')
def connect(socket):
  """
  Gère la connexion d'un client SocketIO.
  """
  print(f"Client connecté : {socket}")

@socket.on('exec_cmd')
def exec_cmd( command):
  """
  Exécute une commande en ligne de commande et envoie la sortie au client.

  Args:
    socket: L'objet SocketIO du client connecté.
    command: La commande à exécuter.
  """
  print(f"Commande reçue : {command}")

  # Exécuter la commande en mode interactif et envoyer la sortie au client
  output_iter = exec_cat_on_file(command)

  for line in output_iter:
    socket.emit('exec_output', line)

@socket.on('disconnect')
def disconnect():
  """
  Gère la déconnexion d'un client SocketIO.
  """
  print(f"Client déconnecté : {socket.sid}")

@app.route('/api/exec', methods=['POST'])
def exec_cmd_api():
  """
  Exécute une commande en ligne de commande et renvoie la sortie.

  Requête:
    - body: JSON contenant la commande à exécuter.

  Réponse:
    - JSON contenant la sortie standard et la sortie d'erreur du programme.
  """
  data = request.get_json()
  command = data['command']

  # Exécuter la commande en mode interactif et renvoyer un générateur
  output_iter = exec_cmd.interactive_cmd(command)

  # Gérer la sortie du programme
  def send_output():
    for line in output_iter:
      yield line

  return Response(send_output(), mimetype='text/plain')

@app.route('/')
def index2():
  """
  Affiche l'interface utilisateur HTML.
  """
  return render_template('index.html')

if __name__ == '__main__':
  server = pywsgi.WSGIServer(('0.0.0.0', 5000), app)
  socketio.run(server)
