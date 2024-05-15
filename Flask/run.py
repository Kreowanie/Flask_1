from flask import Flask, render_template, url_for, redirect, abort

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/aboutme')
def about_me():
    return render_template('aboutme.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# Obsługa ikon Font Awesome
@app.route('/fontawesome')
def font_awesome():
    return redirect("https://fontawesome.com/", code=302)

# Obsługa adresu e-mail
@app.route('/email')
def email():
    return redirect("mailto:twoj@email.com")

# Obsługa strony błędu 404
@app.errorhandler(404)
def page_not_found(error):
    return render_template('error404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
