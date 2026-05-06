
CREATE DATABASE barbearia;
USE barbearia;

CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    telefone VARCHAR(20),
    email VARCHAR(100),
    data_cadastro DATETIME DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE barbeiros (
    id_barbeiro INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    especialidade VARCHAR(100),
    telefone VARCHAR(20)
);


CREATE TABLE servicos (
    id_servico INT AUTO_INCREMENT PRIMARY KEY,
    nome_servico VARCHAR(100) NOT NULL,
    preco DECIMAL(10,2) NOT NULL,
    duracao_minutos INT
);


CREATE TABLE agendamentos (
    id_agendamento INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    id_barbeiro INT,
    data_hora DATETIME NOT NULL,
    status VARCHAR(50) DEFAULT 'Agendado',
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY (id_barbeiro) REFERENCES barbeiros(id_barbeiro)
);


CREATE TABLE itens_agendamento (
    id_item INT AUTO_INCREMENT PRIMARY KEY,
    id_agendamento INT,
    id_servico INT,
    quantidade INT DEFAULT 1,
    FOREIGN KEY (id_agendamento) REFERENCES agendamentos(id_agendamento),
    FOREIGN KEY (id_servico) REFERENCES servicos(id_servico)
);