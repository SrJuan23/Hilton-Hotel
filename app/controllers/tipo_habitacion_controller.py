from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from app.models.tipo_habitacion_model import obtener_tipos_habitacion, insertar_tipo_habitacion, obtener_tipo_por_id, actualizar_tipo, eliminar_tipo

tipo_bp = Blueprint('tipo', __name__, url_prefix='/tiposhabitacion')

@tipo_bp.route('/')
@login_required
def listar_tipos():
    tipos = obtener_tipos_habitacion()
    return render_template('tipohabitacion/listar.html', tipos=tipos)

@tipo_bp.route('/crear', methods=['GET', 'POST'])
@login_required
def crear_tipo():
    if request.method == 'POST':
        insertar_tipo_habitacion(
            request.form['nombre'],
            request.form['descripcion']
        )
        flash('Tipo de habitación registrado correctamente.', 'success')
        return redirect(url_for('tipo.listar_tipos'))
    return render_template('tipohabitacion/crear.html')

@tipo_bp.route('/tipos_habitacion/editar/<int:tipo_habitacion_id>', methods=['GET', 'POST'])
@login_required
def editar_tipo_habitacion(tipo_habitacion_id):
    tipo = obtener_tipo_por_id(tipo_habitacion_id)
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        if nombre:
            actualizar_tipo(tipo_habitacion_id, nombre, descripcion)
            flash("Tipo actualizado.", "success")
            return redirect(url_for('tipo.listar_tipos'))
        flash("Nombre requerido.", "danger")
    return render_template('tipohabitacion/editar_tipo_habitacion.html', tipo=tipo)

@tipo_bp.route('/tipos_habitacion/eliminar/<int:tipo_habitacion_id>', methods=['POST'])
@login_required
def eliminar_tipo_habitacion(tipo_habitacion_id):
    eliminar_tipo(tipo_habitacion_id)
    flash("Tipo eliminado.", "info")
    return redirect(url_for('tipo.listar_tipos'))