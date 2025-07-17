-- Países
INSERT INTO pais (pais_codigo, nombre) VALUES
(1, 'Colombia'),
(2, 'México'),
(3, 'España'),
(4, 'Argentina');

-- Categorías
INSERT INTO categoria (nombre, descripcion, servicios_tipicos) VALUES
('Lujo', 'Hotel 5 estrellas', 'Spa, Restaurante gourmet, Piscina'),
('Económico', 'Hotel 3 estrellas', 'WiFi, desayuno incluido'),
('Negocios', 'Hotel ejecutivo', 'Centro de negocios, salas de reuniones');

-- Tipos de habitación
INSERT INTO tipohabitacion (nombre, descripcion) VALUES
('Individual', 'Una cama individual, ideal para una persona'),
('Doble', 'Una cama doble para dos personas'),
('Suite', 'Habitación de lujo con sala y jacuzzi');

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

-- Usuarios
INSERT INTO usuarios (nombre, correo, clave, pais_codigo) VALUES
('Admin Hilton', 'admin@hilton.com', '$2b$12$eRvXm1tKUYkMfuW9XkTGEuRwVIEiWdquYcZhYy7ixm74S04H5ImCS', 1), -- clave: admin123
('Juan Pérez', 'juan@correo.com', '$2b$12$sdjkfhksdjhfksdjhfkjsdhfksjdfhksdjfhksdf2', 2),
('María López', 'maria@correo.com', '$2b$12$83hdkf82hfksjdfhksdf2h3kjfsd7fhs', 3),
('Carlos Méndez', 'carlos@correo.com', '$2b$12$ajfh72gfh28fhw9df8y92fhsdf72', 1);
