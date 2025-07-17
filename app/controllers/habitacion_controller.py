from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from app.models.habitacion_model import obtener_habitaciones, insertar_habitacion
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
