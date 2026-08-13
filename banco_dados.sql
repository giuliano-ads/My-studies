SQL
-- Criando um banco de dados de estudos
CREATE DATABASE faculdade_ads;

-- Selecionando o banco de dados
USE faculdade_ads;

-- Criando uma tabela de estudantes
CREATE TABLE estudantes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    semestre INT
);

-- Inserindo o seu nome na tabela
INSERT INTO estudantes (nome, semestre) VALUES ('Giuliano', 1);

-- Consultando os dados salvos
SELECT * FROM estudantes;