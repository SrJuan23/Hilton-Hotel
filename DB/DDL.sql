CREATE DATABASE IF NOT EXISTS hilton_db;
USE hilton_db;

-- Tabla pais
CREATE TABLE IF NOT EXISTS pais (
    pais_codigo INT PRIMARY KEY NOT NULL,
    nombre VARCHAR(45) NOT NULL
);

-- Tabla categoria
CREATE TABLE IF NOT EXISTS categoria (
    categoria_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(45) NOT NULL,
    descripcion TEXT NOT NULL,
    servicios_tipicos VARCHAR(100) NOT NULL
);

-- Tabla tipohabitacion
CREATE TABLE IF NOT EXISTS tipohabitacion (
    tipo_habitacion_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(45) NOT NULL,
    descripcion TEXT NOT NULL
);

-- Tabla hotel
CREATE TABLE IF NOT EXISTS hotel (
    hotel_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(45) NOT NULL,
    direccion VARCHAR(100) NOT NULL,
    ano_construccion VARCHAR(4) NOT NULL,
    telefono VARCHAR(45) NOT NULL,
    categoria_id INT NOT NULL,
    pais_codigo INT NOT NULL,
    FOREIGN KEY (categoria_id) REFERENCES categoria(categoria_id),
    FOREIGN KEY (pais_codigo) REFERENCES pais(pais_codigo)
);

-- Tabla habitacion
CREATE TABLE IF NOT EXISTS habitacion (
    habitacion_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    codigo_habitacion VARCHAR(45) NOT NULL,
    hotel_id INT NOT NULL,
    tipo_habitacion_id INT NOT NULL,
    FOREIGN KEY (hotel_id) REFERENCES hotel(hotel_id),
    FOREIGN KEY (tipo_habitacion_id) REFERENCES tipohabitacion(tipo_habitacion_id)
);

-- Tabla usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) NOT NULL UNIQUE,
    clave VARCHAR(200) NOT NULL,
    pais_codigo INT NOT NULL,
    FOREIGN KEY (pais_codigo) REFERENCES pais(pais_codigo)
);
