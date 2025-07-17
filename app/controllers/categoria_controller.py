from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from app.models.categoria_model import obtener_categorias, insertar_categoria, obtener_categoria_por_id, actualizar_categoria, eliminar_categoria

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

@categoria_bp.route('/categorias/editar/<int:categoria_id>', methods=['GET', 'POST'])
@login_required
def editar_categoria(categoria_id):
    categoria = obtener_categoria_por_id(categoria_id)
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        servicios_tipicos = request.form['servicios']
        if nombre and descripcion and servicios_tipicos:
            actualizar_categoria(categoria_id, nombre, descripcion, servicios_tipicos)
            flash("Categoría actualizada.", "success")
            return redirect(url_for('categoria.listar_categorias'))
        flash("Nombre requerido.", "danger")
    return render_template('categoria/editar_categoria.html', categoria=categoria)

@categoria_bp.route('/categorias/eliminar/<int:categoria_id>', methods=['POST'])
@login_required
def eliminar_categoria_route(categoria_id):
    eliminar_categoria(categoria_id)
    flash("Categoría eliminada.", "info")
    return redirect(url_for('categoria.listar_categorias'))
