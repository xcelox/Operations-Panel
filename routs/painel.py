from flask import Blueprint, render_template, session

painel_bp = Blueprint('painel', __name__)  # Alterado de 'ceint' para 'painel'

@painel_bp.route('/PAINEL')
def PAINEL():
    user_name = session.get('user', 'Usuário')
    return render_template('index.html', user_name=user_name)
