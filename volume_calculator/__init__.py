from flask import Flask, Response, request, url_for, render_template
from forms.volume_form import Volume

app=Flask(__name__)

app.config['SECRET_KEY']='hidden-key'

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/volume", methods=['GET', 'POST'])
def volume():
    form=Volume()
    if form.validate():
        diameter=float(request.form['diameter'])
        height=float(request.form['height'])
        calculated_volume=round(3.1415*((diameter/2)**2)*height,ndigits=2)
        return render_template("volume.html",form=form,volume=calculated_volume)
    return render_template("volume.html",form=form)



if __name__ == '__main__':
    app.run(debug=True)
