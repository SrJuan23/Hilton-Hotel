from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from app.models.hotel_model import obtener_hoteles, insertar_hotel
from app.models.categoria_model import obtener_categorias
from app.models.pais_model import obtener_paises

hotel_bp = Blueprint('hotel', __name__, url_prefix='/hoteles')

@hotel_bp.route('/')
@login_required
def listar_hoteles():
    hoteles = obtener_hoteles()
    return render_template('hotel/listar.html', hoteles=hoteles)

@hotel_bp.route('/crear', methods=['GET', 'POST'])
@login_required
def crear_hotel():
    if request.method == 'POST':
        insertar_hotel(
            request.form['nombre'],
            request.form['direccion'],
            request.form['telefono'],
            request.form['anio'],
            request.form['categoria_id'],
            request.form['pais_codigo']
        )
        flash('Hotel registrado correctamente.', 'success')
        return redirect(url_for('hotel.listar_hoteles'))

    categorias = obtener_categorias()
    paises = obtener_paises()
    return render_template('hotel/crear.html', categorias=categorias, paises=paises)
