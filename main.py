from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

###CONTATO### ↓
@app.route('/contato')
def contato():
    return render_template('contato.html')

###PRODUTO### ↓
@app.route('/produto')
def produto():
    return render_template('produto.html')

### EMPRESA ### ↓↓↓
@app.route('/empresa')
def empresa():
    return render_template('empresa.html')

@app.route('/trabalheconosco')
def trabalheconosco():
    return render_template('trabalheconosco.html')

@app.route('/profe')
def profe():
    return render_template('profe.html')

#NADA DEPOIS DO IF ↓↓↓
if __name__ == '__main__':
    app.run(debug=True)

