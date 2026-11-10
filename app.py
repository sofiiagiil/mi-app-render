from flask import Flask
import socket
import datetime

# Creamos la aplicación web
app = Flask(__name__)

# Página principal
@app.route("/")
def home():
    return """
    <h1><h1>¡Hola! Esta es nuestra aplicación ASIR desplegada en Render.</h1></h1>
    <p><p>Hemos modificado nuestra aplicación para comprobar el despliegue automático.</p>
    <p>Visita <a href="/status">/status</a> para ver información del servidor.</p>
    """

# Página secundaria
@app.route("/status")
def status():
    info = {
        "servidor": socket.gethostname(),
        "hora_actual": datetime.datetime.now().isoformat()
    }

    return info

# Ejecución local
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
