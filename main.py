from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

<input type="submit" name="submit" value="Do Something">
<input type="submit" name="submit" value="Do Something Else">

def buttonUsage():
    if request.method == 'POST':
        if request.form['submit'] == 'Do Something':
            pass # do something
        elif request.form['submit'] == 'Do Something Else':
            pass # do something else
        else:
            pass # unknown
    elif request.method == 'GET':
        return render_template('contact.html', form=form)

if __name__ == "__main__":
    app.run()