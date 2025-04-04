from flask import Flask, render_template,request,redirect,url_for
app = Flask(__name__)
lista=["ciao","ciao2","ciao3","ciao4","ciao5"]
@app.route("/")
def home():
    return render_template("index.html",lista=lista)

@app.route('/aggiungi', methods=['POST'])
def aggiungi():
    elemento = request.form['elemento']
    #aggiunge alla lista
    if elemento:
        lista.append(elemento)
    return redirect(url_for('home'))

@app.route('/rimuovi/<int:indice>', methods=['POST'])
def rimuovi(indice):
    if 0 <= indice < len(lista):
        lista.pop(indice)
    return redirect(url_for('home'))


@app.route("/pulisci", methods=['POST'])
def pulisci():
    lista.clear()
    return redirect(url_for('home'))






























































































if __name__ == "__main__":
    app.run(debug=True)


