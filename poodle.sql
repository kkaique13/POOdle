create database if not exists poodle;
use poodle;

create table if not exists cliente(
	idCliente int not null auto_increment,
	nome varchar(200) not null,
    dataNascimento date not null,
    endereco varchar(100) not null,
    constraint pk_Cliente primary key (idCliente)
);

create table if not exists pessoa_fisica(
	idCliente int not null,
	CPF varchar(11) not null,
    constraint pk_PessoaF primary key (idCliente),
    constraint fk_PessoaF_CLiente foreign key (idCliente) references cliente(idCliente)
);

create table if not exists pessoa_juridica(
	idCliente int not null,
	CNPJ varchar(14) not null,
    constraint pk_PessoaJ primary key (idCliente),
    constraint fk_PessoaJ_Cliente foreign key (idCliente) references cliente(idCliente)
);

create table if not exists carteira(
	idCarteira int not null auto_increment,
    idCliente int not null,
    investimento varchar(100) not null,
    constraint pk_Carteira primary key (idCarteira),
    constraint fk_Carteira_Cliente foreign key (idCliente) references cliente(idCliente)
);

create table if not exists conta(
	numero int not null auto_increment,
    titular varchar(200) not null,
    saldo decimal(10, 2),
    idCarteira int not null,
    constraint pk_Conta primary key (numero),
    constraint fk_Conta_Carteira foreign key (idCarteira) references carteira(idCarteira)
);

create table if not exists conta_corrente(
	numero int not null,
    limite decimal(7, 2) not null default 2000.00,
    constraint chk_Limite check (limite >= 0 and limite <= 2000),
    constraint pk_ContaCorrente primary key (numero),
    constraint fk_ContaCorrente_Conta foreign key (numero) references conta(numero)
);

create table if not exists conta_poupanca(
	numero int not null,
    rendimento decimal(10, 2),
    constraint pk_ContaPoupanca primary key (numero),
    constraint fk_ContaPoupanca_Conta foreign key (numero) references conta(numero)
);

insert into cliente(nome, dataNascimento, endereco) values (
	'Keren Hapuque',
    '2009-08-17',
    'Rua da Felicidade, 286'
);

insert into cliente(nome, dataNascimento, endereco) values (
	'Kaíque Reis',
    '2009-05-23',
    'Rua da Tristeza, 15'
);

insert into cliente(nome, dataNascimento, endereco) values (
	'Gabriel Gutemberg',
    '2009-08-30',
    'Rua da Dúvida, 293'
);