from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from app.models.categoria_model import obtener_categorias, insertar_categoria

categoria_bp = Blueprint('categoria', __name__, url_prefix='/categorias')

@categoria_bp.route('/')
@login_required
def listar_categorias():
    categorias = obtener_categorias()
    return render_template('categoria/listar.html', categorias=categorias)

@categoria_bp.route('/crear', methods=['GET', 'POST'])
@login_required
def crear_categoria():
    if request.method == 'POST':
        insertar_categoria(
            request.form['nombre'],
            request.form['descripcion'],
            request.form['servicios_tipicos']
        )
        flash('Categoría registrada correctamente.', 'success')
        return redirect(url_for('categoria.listar_categorias'))
    return render_template('categoria/crear.html')
