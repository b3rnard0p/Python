CREATE DATABASE cadastros;

USE cadastros;

CREATE TABLE itens (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    quantidade INT NOT NULL
);

SELECT * FROM itens;