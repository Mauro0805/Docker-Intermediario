import os
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    ambiente = os.getenv('AMBIENTE', 'desenvolvimento')
    porta = os.getenv('PORTA_APP', '5000')
    return f"Ambiente: {ambiente} | Porta: {porta}"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)