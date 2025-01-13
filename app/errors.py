from flask import render_template
from app import app, db

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404
#o segundo valor do return é o status do server
@app.errorhandler(500)
def internal_error(error):
    db.session.rollback() # pra nenhuma mudança ocorrer por erro
    return render_template('500.html'), 500 # erro referente a db