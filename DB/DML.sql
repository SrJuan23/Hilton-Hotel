Use hilton_db;
-- Países
INSERT INTO pais (pais_codigo, nombre) VALUES
(1, 'Colombia'),
(2, 'México'),
(3, 'España'),
(4, 'Argentina');

-- Categorías
INSERT INTO categoria (nombre, descripcion, servicios_tipicos) VALUES
('Económico', '★ - Servicios muy básicos para estancias cortas y bajo presupuesto.', 'Cama, baño (compartido o privado), limpieza básica'),
('Estándar', '★★ - Mayor comodidad, servicios esenciales incluidos.', 'Baño privado, recepción limitada, desayuno opcional'),
('Confort', '★★★ - Buena relación calidad-precio, servicios completos.', 'Recepción 24h, Wi-Fi, restaurante, servicio de habitaciones básico'),
('Superior', '★★★★ - Alta calidad en infraestructura y atención.', 'Piscina, gimnasio, restaurante de nivel, habitaciones amplias y bien decoradas'),
('Lujo', '★★★★★ - Máxima calidad, lujo y servicios personalizados.', 'Spa, mayordomo, concierge, transporte privado, tecnología avanzada'),
('Boutique Hotel', 'Clasificación especial - Hoteles exclusivos con diseño distintivo.', 'Decoración única, ubicación privilegiada, atención personalizada'),
('Resort', 'Clasificación especial - Alojamiento recreativo, ideal para vacaciones.', 'Piscinas, actividades, múltiples restaurantes, entretenimiento'),
('Ecohotel', 'Clasificación especial - Enfoque ecológico y sostenible.', 'Energías renovables, materiales ecológicos, certificaciones ambientales'),
('Hostal / Posada', 'Sin estrellas o ★ - Alojamiento económico e informal.', 'Habitaciones sencillas, baño compartido, ambiente familiar'),
('Apartahotel', 'Clasificación especial - Combinación de hotel y apartamento.', 'Cocina equipada, limpieza periódica, recepción, servicios hoteleros');

-- Tipos de habitación
INSERT INTO tipohabitacion (nombre, descripcion) VALUES
('Individual (Single)', 'Una cama individual, ideal para una sola persona.'),
('Doble (Double)', 'Una cama doble (matrimonial) para dos personas.'),
('Twin', 'Dos camas individuales para dos personas.'),
('Triple', 'Tres camas individuales o una doble + una individual.'),
('Cuádruple', 'Cuatro camas individuales o combinaciones hasta 4 personas.'),
('Matrimonial (King/Queen)', 'Cama Queen o King, ideal para parejas.'),
('Suite', 'Habitación de lujo con sala de estar y servicios premium.'),
('Junior Suite', 'Versión más pequeña de la suite, zona integrada.'),
('Presidencial / Royal Suite', 'Suite de lujo extremo, habitaciones y servicios exclusivos.'),
('Habitación Familiar', 'Diseñada para familias; camas dobles + literas.'),
('Estudio', 'Tipo apartamento con cocina pequeña.'),
('Penthouse', 'Unidad en el último piso, terrazas y vistas.'),
('Habitación Adaptada', 'Para personas con movilidad reducida.'),
('Habitación Comunicada', 'Dos habitaciones unidas, ideal para familias.');


-- Hoteles
INSERT INTO hotel (nombre, direccion, ano_construccion, telefono, categoria_id, pais_codigo) VALUES
('Hilton Bogotá', 'Calle 26 #69B-53, Bogotá', '2015', '6011234567', 1, 1),
('Hilton México City', 'Av. Juárez 70, CDMX', '2010', '5551234567', 2, 2),
('Hilton Madrid', 'Calle Princesa 40, Madrid', '2018', '34911234567', 3, 3);

-- Habitaciones
INSERT INTO habitacion (codigo_habitacion, hotel_id, tipo_habitacion_id) VALUES
('HBG-101', 1, 1),
('HBG-102', 1, 2),
('HMC-201', 2, 2),
('HMC-202', 2, 3),
('HMD-301', 3, 1);

