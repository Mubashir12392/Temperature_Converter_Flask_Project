from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/")
def main():
    return """<h1>Main page</h1>"""


@app.route('/Temperature_Converter', methods=["GET","POST"])
def home():
    
    
    #when request method is get the form will be shown
    if request.method == "GET":
        return render_template("form.html")
    
    #when request method is post the inputs will convert by following methods
    elif request.method == "POST":
        fah = request.form['input']
        cel = request.form['fahrenh']
        if cel == '' and fah == '':
            return render_template('404.html')
        elif cel != '' and fah != '':
            x= int(cel)
            Celsius = (x - 32) * 5/9
            celsius = int(fah)
            Fahrenheit= (celsius * 9/5) +32
            return render_template ('form.html', result= Fahrenheit , result2= Celsius)
        elif fah != '':
            celsius = int(fah)
            Fahrenheit= (celsius * 9/5) +32
            return render_template ('form.html', result= Fahrenheit)
        elif cel != '':
            x= int(cel)
            Celsius = (x - 32) * 5/9
            return render_template ('form.html', result2= Celsius)
        
        

