from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from app.models.hotel_model import obtener_hoteles, obtener_hotel_por_id, actualizar_hotel,eliminar_hotel_por_id,insertar_hotel
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

@hotel_bp.route('/hoteles/eliminar/<int:hotel_id>', methods=['POST'])
@login_required
def eliminar_hotel(hotel_id):
    eliminar_hotel_por_id(hotel_id)
    flash("Hotel eliminado correctamente.", "success")
    return redirect(url_for('hotel.listar_hoteles'))

@hotel_bp.route('/hoteles/editar/<int:hotel_id>', methods=['GET', 'POST'])
@login_required
def editar_hotel(hotel_id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        ano_construccion = request.form['anio']
        categoria_id = request.form['categoria_id']
        pais_codigo = request.form['pais_codigo']

        if not nombre or not direccion or not pais_codigo or not categoria_id or not ano_construccion or not telefono:
            flash("Todos los campos son obligatorios.", "danger")
            return render_template('hoteles/editar_hotel.html', hotel=hotel, categorias=categorias)

        actualizar_hotel(hotel_id, nombre, direccion, ano_construccion, telefono, categoria_id, pais_codigo)
        flash("Hotel actualizado correctamente.", "success")
        return redirect(url_for('hotel.listar_hoteles'))

    hotel = obtener_hotel_por_id(hotel_id)
    categorias = obtener_categorias()
    paises = obtener_paises()
    return render_template('hotel/editar_hotel.html', hotel=hotel, categorias=categorias, paises=paises)