-- Creacion de las tablas: autores, libros, prestamos --

CREATE TABLE autores (
id SERIAL PRIMARY KEY,
nombre VARCHAR(200)
);

CREATE TABLE libros (
id SERIAL PRIMARY KEY,
titulo VARCHAR(200),
autor_id INTEGER NOT NULL,
disponible BOOLEAN DEFAULT TRUE,
FOREIGN KEY (autor_id) REFERENCES autores(id)
);

CREATE TABLE prestamos (
id SERIAL PRIMARY KEY,
libro_id INTEGER NOT NULL,
nombre_usuario VARCHAR(200) NOT NULL,
fecha_prestamo DATE DEFAULT CURRENT_DATE,
fecha_devolucion DATE,
estado VARCHAR(20) DEFAULT 'activo',
FOREIGN KEY (libro_id) REFERENCES libros(id)
);

-- Agregar registros --

INSERT INTO autores (nombre)
VALUES
('Alexander Dumas'),
('Miguel de Cervantes'),
('George R. R. Martin');

INSERT INTO libros (titulo,autor_id)
VALUES
('El Conde de Montecristo',1),
('Los Tres Mosqueteros',1),
('El Hombre de la Mascara de Hierro',1),
('Don Quixote de la Mancha',2),
('Cancion de Hielo y Fuego',3);

INSERT INTO prestamos (libro_id,nombre_usuario)
VALUES
(3,'David Perez'),
(4,'Angelica Reyes');

-- Querys de prueba --

SELECT * FROM libros;
SELECT * FROM prestamos;

SELECT titulo, prestamos.nombre_usuario
FROM libros
LEFT JOIN prestamos ON prestamos.libro_id = libros.id;

-- Actualizar todos los registros en las tablas a minusculas --

UPDATE libros SET titulo = LOWER(titulo);
UPDATE autores SET nombre = LOWER(nombre);
UPDATE prestamos SET nombre_usuario = LOWER(nombre_usuario);
UPDATE prestamos SET estado = LOWER(estado);