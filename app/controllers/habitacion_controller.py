from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from app.models.habitacion_model import obtener_habitaciones, insertar_habitacion, obtener_habitacion_por_id, actualizar_habitacion, eliminar_habitacion
from app.models.hotel_model import obtener_hoteles
from app.models.tipo_habitacion_model import obtener_tipos_habitacion
from app.models.hotel_model import obtener_hoteles
from app.models.tipo_habitacion_model import obtener_tipos_habitacion

habitacion_bp = Blueprint('habitacion', __name__, url_prefix='/habitaciones')

@habitacion_bp.route('/')
@login_required
def listar_habitaciones():
    habitaciones = obtener_habitaciones()
    return render_template('habitacion/listar.html', habitaciones=habitaciones)

@habitacion_bp.route('/crear', methods=['GET', 'POST'])
@login_required
def crear_habitacion():
    if request.method == 'POST':
        insertar_habitacion(
            request.form['codigo_habitacion'],
            request.form['hotel_id'],
            request.form['tipo_habitacion_id']
        )
        flash('Habitación registrada correctamente.', 'success')
        return redirect(url_for('habitacion.listar_habitaciones'))

    hoteles = obtener_hoteles()
    tipos = obtener_tipos_habitacion()
    return render_template('habitacion/crear.html', hoteles=hoteles, tipos=tipos)

@habitacion_bp.route('/habitaciones/editar/<int:habitacion_id>', methods=['GET', 'POST'])
@login_required
def editar_habitacion(habitacion_id):
    habitacion = obtener_habitacion_por_id(habitacion_id)
    hoteles = obtener_hoteles()
    tipos = obtener_tipos_habitacion()
    if request.method == 'POST':
        codigo_habitacion = request.form['codigo']
        hotel_id = request.form['hotel_id']
        tipo_habitacion_id = request.form['tipo_habitacion_id']
        actualizar_habitacion(habitacion_id, codigo_habitacion, hotel_id, tipo_habitacion_id)
        flash("Habitación actualizada.", "success")
        return redirect(url_for('habitacion.listar_habitaciones'))
    return render_template('habitacion/editar_habitacion.html', habitacion=habitacion, hoteles=hoteles, tipos=tipos)

@habitacion_bp.route('/habitaciones/eliminar/<int:habitacion_id>', methods=['POST'])
@login_required
def eliminar_habitacion_route(habitacion_id):
    eliminar_habitacion(habitacion_id)
    flash("Habitación eliminada.", "info")
    return redirect(url_for('habitacion.listar_habitaciones'))