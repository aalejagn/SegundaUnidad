-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS punto_venta;
USE punto_venta;

-- Crear la tabla cliente
CREATE TABLE IF NOT EXISTS cliente (
    telefono VARCHAR(15) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(200),
    rfc VARCHAR(13),
    correo VARCHAR(100)
);
