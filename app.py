from flask import Flask, render_template

from controllers.pubs_controller import pubs_blueprint

import repositories.pub_repository as pub_repository

app = Flask(__name__)

app.register_blueprint(pubs_blueprint)

@app.route('/') 
def home():
    pubs = pub_repository.select_all()
    return render_template('base.html', pubs = pubs)

if __name__ == '__main__':
    app.run(debug=True)