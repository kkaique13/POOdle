create database if not exists poodle;
use poodle;

-- Criação de tabelas
create table if not exists cliente (
    idCliente int not null auto_increment,
    nome varchar(200) not null,
    dataNascimento date not null,
    endereco varchar(100) not null,
    constraint pk_Cliente primary key (idCliente)
);

create table if not exists pessoa_fisica (
    idCliente int not null,
    CPF varchar(14) not null,
    constraint pk_PessoaF primary key (idCliente),
    constraint fk_PessoaF_CLiente foreign key (idCliente) references cliente(idCliente) on delete cascade
);

create table if not exists pessoa_juridica (
    idCliente int not null,
    CNPJ varchar(18) not null,
    constraint pk_PessoaJ primary key (idCliente),
    constraint fk_PessoaJ_Cliente foreign key (idCliente) references cliente(idCliente) on delete cascade
);

create table if not exists carteira (
    idCarteira int not null auto_increment,
    idCliente int not null,
    investimento varchar(100) not null,
    constraint pk_Carteira primary key (idCarteira),
    constraint fk_Carteira_Cliente foreign key (idCliente) references cliente(idCliente) on delete restrict
);

create table if not exists conta (
    numero int not null auto_increment,
    titular varchar(200) not null,
    saldo decimal(10, 2),
    idCarteira int,
    constraint pk_Conta primary key (numero),
    constraint fk_Conta_Carteira foreign key (idCarteira) references carteira(idCarteira) on delete set null
);

create table if not exists conta_corrente (
    numero int not null,
    limite decimal(7, 2) not null default 2000.00,
    constraint chk_Limite check (limite >= 0 and limite <= 2000),
    constraint pk_ContaCorrente primary key (numero),
    constraint fk_ContaCorrente_Conta foreign key (numero) references conta(numero) on delete cascade
);

create table if not exists conta_poupanca (
    numero int not null,
    rendimento decimal(10, 2),
    constraint pk_ContaPoupanca primary key (numero),
    constraint fk_ContaPoupanca_Conta foreign key (numero) references conta(numero) on delete cascade
);

-- Inserção de valores
insert into cliente(nome, dataNascimento, endereco) values
	('Keren Hapuque',         '2009-08-17', 'Rua da Felicidade, 286'),
    ('Kaíque Reis',           '2009-05-23', 'Rua da Tristeza, 15'),
    ('Gabriel Gutemberg',     '2009-08-30', 'Rua da Dúvida, 293'),
    ('Ana Beatriz Souza',     '1990-03-12', 'Av. Brasil, 100'),
	('Carlos Eduardo Lima',   '1985-07-25', 'Rua das Flores, 45'),
	('Mariana Alves Costa',   '1998-11-02', 'Rua do Sol, 320'),
	('Pedro Henrique Rocha',  '1979-01-19', 'Av. Atlântica, 77'),
	('Juliana Ferreira',      '2001-06-08', 'Rua da Paz, 12'),
	('Rafael Moreira',        '1993-09-14', 'Rua XV de Novembro, 500'),
    ('Paulo Honório',         '1984-08-15', 'Rua São Bernardo, 67'),
    ('Tech Solutions LTDA',   '2010-04-22', 'Av. Paulista, 1000'),
    ('Empresa Alpha LTDA',    '2005-02-10', 'Rua Comercial, 10'),
	('Beta Comércio SA',      '2008-06-15', 'Av. Industrial, 200'),
	('Gama Serviços ME',      '2012-09-01', 'Rua dos Negócios, 33'),
	('Delta Logística LTDA',  '2015-03-20', 'Rod. BR-101, km 5'),
	('Épsilon Tecnologia SA', '2018-11-11', 'Av. Inovação, 400'),
	('Zeta Alimentos LTDA',   '2001-07-07', 'Rua do Mercado, 88'),
	('Eta Construções ME',    '2014-12-25', 'Av. Obras, 150'),
	('Theta Consultoria SA',  '2019-05-30', 'Rua do Saber, 77'),
	('Iota Transportes LTDA', '2003-08-18', 'Av. das Estradas, 900');

insert into pessoa_fisica(idCliente, CPF) values
	(1,  '529.873.146-02'),
	(2,  '183.650.729-44'),
	(3,  '907.412.583-61'),
	(4,  '364.829.175-08'),
	(5,  '741.058.392-76'),
	(6,  '258.934.617-05'),
	(7,  '619.375.824-40'),
	(8,  '473.028.196-57'),
	(9,  '835.216.470-93'),
	(10, '192.648.305-72');

insert into pessoa_juridica(idCliente, CNPJ) values
	(11, '48.271.930/5746-18'),
    (12, '90.735.182/6409-27'),
    (13, '26.508.471/9362-54'),
    (14, '73.194.602/8517-39'),
    (15, '15.830.746/2985-01'),
    (16, '62.049.381/7526-84'),
    (17, '37.482.910/5673-20'),
    (18, '81.925.643/0781-65'),
    (19, '50.371.829/4657-02'),
	(20, '94.720.538/1629-48');

insert into carteira(idCliente, investimento) values
	(1,  'Renda Fixa'),
	(2,  'Ações'),
	(3,  'Fundos Imobiliários'),
	(4,  'Tesouro Direto'),
	(5,  'CDB'),
	(6,  'LCI/LCA'),
	(7,  'Fundos de Investimento'),
	(8,  'Previdência Privada'),
	(9,  'Criptomoedas'),
	(10, 'Poupança'),
	(11, 'Renda Fixa'),
	(12, 'Ações'),
	(13, 'Fundos Imobiliários'),
	(14, 'Tesouro Direto'),
	(15, 'CDB'),
	(16, 'LCI/LCA'),
	(17, 'Fundos de Investimento'),
	(18, 'Previdência Privada'),
	(19, 'Criptomoedas'),
	(20, 'Poupança');

insert into conta(titular, saldo, idCarteira) values
	('Keren Hapuque',          1500.00,  1),
	('Kaíque Reis',             850.50,  2),
	('Gabriel Gutemberg',      2300.75,  3),
	('Ana Beatriz Souza',      5000.00,  4),
	('Carlos Eduardo Lima',     120.00,  5),
	('Mariana Alves Costa',    7800.30,  6),
	('Pedro Henrique Rocha',     45.90,  7),
	('Juliana Ferreira',       3200.00,  8),
	('Rafael Moreira',          910.10,  9),
	('Paulo Honório',          2600.00, 10),
	('Tech Solutions LTDA',   15000.00, 11),
	('Empresa Alpha LTDA',     9800.00, 12),
	('Beta Comércio SA',      12300.50, 13),
	('Gama Serviços ME',       4500.00, 14),
	('Delta Logística LTDA',  18700.25, 15),
	('Épsilon Tecnologia SA', 22000.00, 16),
	('Zeta Alimentos LTDA',    7600.80, 17),
	('Eta Construções ME',     3300.00, 18),
	('Theta Consultoria SA',  11400.60, 19),
	('Iota Transportes LTDA',  6700.40, 20);
    
insert into conta_corrente(numero, limite) values
	(1,  2000.00),
	(2,  1500.00),
	(3,  1000.00),
	(4,  2000.00),
	(5,   500.00),
	(6,  1800.00),
	(7,   300.00),
	(8,  1200.00),
	(9,   800.00),
	(10, 2000.00),
	(11, 2000.00),
	(12, 1500.00),
	(13, 1000.00),
	(14, 2000.00),
	(15,  500.00),
	(16, 1800.00),
	(17,  300.00),
	(18, 1200.00),
	(19,  800.00),
	(20, 2000.00);

insert into conta_poupanca(numero, rendimento) values
	(1,   12.50),
	(2,    8.30),
	(3,   25.00),
	(4,   40.75),
	(5,    1.20),
	(6,   60.00),
	(7,    0.90),
	(8,   30.10),
	(9,    7.45),
	(10, 120.00),
	(11,  18.90),
	(12,  45.20),
	(13,   6.75),
	(14,  33.40),
	(15,  52.10),
	(16,   2.80),
	(17,  71.60),
	(18,  14.35),
	(19,  28.50),
	(20,  95.70);

-- Ajuste de dados para a Consulta 3
-- remove a conta poupança das contas 1 a 10 (deixando só a corrente)
delete from conta_poupanca where numero <= 10;
-- remove a conta corrente das contas 11 a 20 (deixando só a poupança)
delete from conta_corrente where numero > 10;


-- Consultas
-- Consulta 1: Pessoa Física x Pessoa Jurídica
-- seleciona as colunas que vão aparecer na tela
select c.idCliente, c.nome, c.dataNascimento,
-- o case verifica qual tabela tem o dado preenchido para definir o tipo
case 
	when pf.idCliente is not null then 'Pessoa Física'
	when pj.idCliente is not null then 'Pessoa Jurídica'
end as tipo_cliente,
-- o coalesce pega o primeiro valor não nulo (se for pf pega o cpf, se for pj pega o cnpj)
coalesce(pf.CPF, pj.CNPJ) as documento
from cliente c 
-- junta a tabela de pessoa física usando o id como ponte
left join pessoa_fisica pf on c.idCliente = pf.idCliente
-- junta a tabela de pessoa jurídica usando o id como ponte
left join pessoa_juridica pj on c.idCliente = pj.idCliente;

-- Consulta 2: Carteira e conta do cliente
-- seleciona o nome do cliente, o investimento, a conta e o saldo
select c.nome as cliente, cart.investimento, ct.numero as numero_conta, ct.saldo
from cliente c
-- junta a tabela carteira com o cliente
join carteira cart on c.idCliente = cart.idCliente
-- junta a tabela conta com a carteira
join conta ct on cart.idCarteira = ct.idCarteira
-- ordena do maior saldo para o menor
order by ct.saldo desc;

-- Consulta 3: Conta corrente x Conta poupança
select c.nome as titular, ct.numero as conta, ct.saldo,
-- verifica se o número da conta existe na tabela de corrente ou poupança
case 
	when cc.numero is not null then 'Conta Corrente'
	when cp.numero is not null then 'Conta Poupança'
end as tipo_conta, cc.limite, cp.rendimento
from conta ct
join carteira cart on ct.idCarteira = cart.idCarteira
join cliente c on cart.idCliente = c.idCliente
-- left join para tentar achar os dados na conta corrente
left join conta_corrente cc on ct.numero = cc.numero
-- left join para tentar achar os dados na conta poupança
left join conta_poupanca cp on ct.numero = cp.numero;

-- Consulta 4: Total de dinheiro no banco por tipo de cliente
select 
-- classifica o cliente usando a mesma lógica do case
case 
	when pf.idCliente is not null then 'Pessoa Física'
	when pj.idCliente is not null then 'Pessoa Jurídica'
end as tipo_cliente,
-- soma todos os saldos encontrados para cada tipo
sum(ct.saldo) as total_dinheiro_investido
from cliente c
left join pessoa_fisica pf on c.idCliente = pf.idCliente
left join pessoa_juridica pj on c.idCliente = pj.idCliente
join carteira cart on c.idCliente = cart.idCliente
join conta ct on cart.idCarteira = ct.idCarteira
-- agrupa o resultado pelo tipo de cliente
group by tipo_cliente;

-- Consulta 5: Quantos clientes estão em cada investimento
select investimento, count(*) as quantidade_clientes
from carteira
-- agrupa pela coluna de investimento
group by investimento
-- ordena da maior quantidade para a menor
order by quantidade_clientes desc;

-- Consulta 6: Auditoria das contas
-- seleciona os dados da conta (tabela da esquerda) e do cliente (tabela da direita)
select ct.numero as conta, ct.saldo, c.nome as titular, cart.investimento
-- o 'from' inicia pela tabela conta
from conta ct
-- o 'left join' tenta juntar a carteira
left join carteira cart on ct.idCarteira = cart.idCarteira
-- o 'right join' força o banco a trazer todos os clientes, mesmo se não tiverem conta
right join cliente c on cart.idCliente = c.idCliente;

-- Views
-- cria (ou substitui se já existir) uma view chamada vw_clientes_detalhados
create or replace view vw_clientes_detalhados as
select c.idCliente, c.nome, c.dataNascimento, c.endereco,
case 
	when pf.idCliente is not null then 'Pessoa Física'
	when pj.idCliente is not null then 'Pessoa Jurídica'
end as tipo_cliente,
coalesce(pf.CPF, pj.CNPJ) as documento
from cliente c
left join pessoa_fisica pf on c.idCliente = pf.idCliente
left join pessoa_juridica pj on c.idCliente = pj.idCliente;

-- cria (ou substitui) a view vw_contas_completas
create or replace view vw_contas_completas as
select ct.numero as numero_conta, c.nome as titular, cart.investimento, ct.saldo,
case 
	when cc.numero is not null then 'Corrente'
	when cp.numero is not null then 'Poupança'
end as tipo_conta, cc.limite, cp.rendimento
from conta ct
join carteira cart on ct.idCarteira = cart.idCarteira
join cliente c on cart.idCliente = c.idCliente
left join conta_corrente cc on ct.numero = cc.numero
left join conta_poupanca cp on ct.numero = cp.numero;

-- cria (ou substitui) a view vw_volume_financeiro
create or replace view vw_volume_financeiro as
select 
case 
	when pf.idCliente is not null then 'Pessoa Física'
	when pj.idCliente is not null then 'Pessoa Jurídica'
end as tipo_cliente,
    count(distinct c.idCliente) as qtd_clientes,
    sum(ct.saldo) as total_saldo
from cliente c
left join pessoa_fisica pf on c.idCliente = pf.idCliente
left join pessoa_juridica pj on c.idCliente = pj.idCliente
join carteira cart on c.idCliente = cart.idCliente
join conta ct on cart.idCarteira = ct.idCarteira
-- agrupa os resultados pelo tipo de cliente
group by tipo_cliente;

-- Ver todos os clientes detalhados (pessoa física e jurídica)
select * from vw_clientes_detalhados;

-- Ver todas as contas com seus titulares e tipos
select * from vw_contas_completas;

-- Ver o volume financeiro separado por pf e pj
select * from vw_volume_financeiro;