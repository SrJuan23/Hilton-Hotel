from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from app.models.tipo_habitacion_model import obtener_tipos_habitacion, insertar_tipo_habitacion

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
