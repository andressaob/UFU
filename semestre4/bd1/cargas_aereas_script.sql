/*Adaptado do material do professor Pedro Manoel da Silveira - DCC - UFRJ
Script para criação e população do banco cargas aéreas
*/


CREATE SCHEMA CargasAereas;  --cria um novo esquema para o banco chamado CargasAereas
SET search_path TO CargasAereas;  --muda o esquema corrente para o CargasAereas



CREATE TABLE Empresa (
       CodEmp            VARCHAR(3) NOT NULL,
       Nome              VARCHAR(50) NULL,
       PRIMARY KEY (CodEmp)
);

CREATE TABLE Voo (
       CodVoo               VARCHAR(8) NOT NULL,
       CodEmp               VARCHAR(3) NULL,
       PRIMARY KEY (CodVoo),
       FOREIGN KEY (CodEmp) REFERENCES Empresa(CodEmp)
);


CREATE TABLE Trecho (
       Origem               VARCHAR(50) NOT NULL,
       Destino              VARCHAR(50) NOT NULL,
       Distancia            INT NULL,
       PRIMARY KEY (Origem, Destino)
);

CREATE TABLE Rota (
       CodRota              VARCHAR(8) NOT NULL,
       CodVoo               VARCHAR(8) NOT NULL,
       Origem               VARCHAR(50) NOT NULL,  
       Destino              VARCHAR(50) NOT NULL,
       H_Saida              TIME NULL,
       H_Chegada            TIME NULL,
       PRIMARY KEY (CodRota),
       FOREIGN KEY (Origem, Destino) REFERENCES Trecho(Origem, Destino),
       FOREIGN KEY (CodVoo) REFERENCES Voo(CodVoo)
);

CREATE TABLE Aviao (
       CodAviao             VARCHAR(8) NOT NULL,
       CodEmp               VARCHAR(3) NOT NULL,
       Tipo                 VARCHAR(20) NULL,
       Capacidade           INT NULL,
       PRIMARY KEY (CodAviao)
);


CREATE TABLE Viagem (
       CodRota               VARCHAR(8) NOT NULL,
       Data                  TIMESTAMP NOT NULL,
       H_Saida_Real          TIME NULL,
       H_Chegada_Real        TIME NULL,
       CodAviao              VARCHAR(8) NULL,
       PRIMARY KEY (CodRota, Data),
       FOREIGN KEY (CodAviao) REFERENCES Aviao(CodAviao),
       FOREIGN KEY (CodRota)  REFERENCES Rota(CodRota)
);


INSERT INTO Empresa (CodEmp, Nome) VALUES ('TAM', 'Transportes Aéreos Marília');
INSERT INTO Empresa (CodEmp, Nome) VALUES ('GLO', 'Gol Linhas Aéreas');
INSERT INTO Empresa (CodEmp, Nome) VALUES ('AZU', 'Azul Linhas Aéreas Brasileiras');

INSERT INTO Voo (CodVoo, CodEmp) VALUES ('100', 'GLO');
INSERT INTO Voo (CodVoo, CodEmp) VALUES ('101', 'GLO');
INSERT INTO Voo (CodVoo, CodEmp) VALUES ('150', 'GLO');
INSERT INTO Voo (CodVoo, CodEmp) VALUES ('151', 'GLO');
INSERT INTO Voo (CodVoo, CodEmp) VALUES ('820', 'TAM');
INSERT INTO Voo (CodVoo, CodEmp) VALUES ('821', 'TAM');
INSERT INTO Voo (CodVoo, CodEmp) VALUES ('830', 'TAM');
INSERT INTO Voo (CodVoo, CodEmp) VALUES ('831', 'TAM');
INSERT INTO Voo (CodVoo, CodEmp) VALUES ('200', 'AZU');
INSERT INTO Voo (CodVoo, CodEmp) VALUES ('201', 'AZU');
INSERT INTO Voo (CodVoo, CodEmp) VALUES ('210', 'AZU');
INSERT INTO Voo (CodVoo, CodEmp) VALUES ('211', 'AZU');
INSERT INTO Voo (CodVoo, CodEmp) VALUES ('240', 'AZU');

INSERT INTO Trecho VALUES
(
  'SAO', 'GIG', 400
);
INSERT INTO Trecho VALUES
(
  'GIG', 'POA', 1600
);
INSERT INTO Trecho VALUES
(
  'POA', 'GIG', 1600
);
INSERT INTO Trecho VALUES
(
  'GIG', 'SAO', 400
);
INSERT INTO Trecho VALUES
(
  'GIG', 'SAL', 1600
);
INSERT INTO Trecho VALUES
(
  'SAL', 'GIG', 1600
);
INSERT INTO Trecho VALUES
(
  'SAO', 'BHZ', 600
);
INSERT INTO Trecho VALUES
(
  'BHZ', 'SAO', 600
);


INSERT INTO Rota (CodRota, Origem, Destino, CodVoo, H_Saida, H_Chegada) VALUES
(
  '8201', 'SAO', 'GIG', '820', '8:00', '8:40'
);
INSERT INTO Rota (CodRota, Origem, Destino, CodVoo, H_Saida, H_Chegada) VALUES
(
  '8202', 'GIG', 'POA', '820', '9:20', '11:00'
);
INSERT INTO Rota (CodRota, Origem, Destino, CodVoo, H_Saida, H_Chegada) VALUES
(
  '8211', 'POA', 'GIG', '821', '12:00', '13:40'
);
INSERT INTO Rota (CodRota, Origem, Destino, CodVoo, H_Saida, H_Chegada) VALUES
(
  '8212', 'GIG', 'SAO', '821', '14:20', '15:00'
);
INSERT INTO Rota (CodRota, Origem, Destino, CodVoo, H_Saida, H_Chegada) VALUES
(
  '8301', 'SAO', 'GIG', '830', '10:00', '10:40'
);
INSERT INTO Rota (CodRota, Origem, Destino, CodVoo, H_Saida, H_Chegada) VALUES
(
  '8302', 'GIG', 'SAL', '830', '11:20', '12:50'
);
INSERT INTO Rota (CodRota, Origem, Destino, CodVoo, H_Saida, H_Chegada) VALUES
(
  '8311', 'SAL', 'GIG', '831', '14:00', '15:30'
);
INSERT INTO Rota (CodRota, Origem, Destino, CodVoo, H_Saida, H_Chegada) VALUES
(
  '8312', 'GIG', 'SAO', '831', '16:10', '16:50'
);
INSERT INTO Rota (CodRota, Origem, Destino, CodVoo, H_Saida, H_Chegada) VALUES
(
  '1001', 'POA', 'GIG', '100', '09:00', '10:40'
);
INSERT INTO Rota (CodRota, Origem, Destino, CodVoo, H_Saida, H_Chegada) VALUES
(
  '1002', 'GIG', 'SAL', '100', '11:20', '12:50'
);
INSERT INTO Rota (CodRota, Origem, Destino, CodVoo, H_Saida, H_Chegada) VALUES
(
  '1011', 'SAL', 'GIG', '101', '15:00', '16:30'
);
INSERT INTO Rota (CodRota, Origem, Destino, CodVoo, H_Saida, H_Chegada) VALUES
(
  '1012', 'GIG', 'POA', '101', '17:10', '18:50'
);
INSERT INTO Rota (CodRota, Origem, Destino, CodVoo, H_Saida, H_Chegada) VALUES
(
  '1501', 'POA', 'GIG', '150', '13:30', '15:10'
);
INSERT INTO Rota (CodRota, Origem, Destino, CodVoo, H_Saida, H_Chegada) VALUES
(
  '1502', 'GIG', 'SAO', '150', '15:50', '16:30'
);
INSERT INTO Rota (CodRota, Origem, Destino, CodVoo, H_Saida, H_Chegada) VALUES
(
  '1503', 'SAO', 'BHZ', '150', '17:10', '17:40'
);
INSERT INTO Rota (CodRota, Origem, Destino, CodVoo, H_Saida, H_Chegada) VALUES
(
  '1511', 'BHZ', 'SAO', '151', '18:30', '19:00'
);
INSERT INTO Rota (CodRota, Origem, Destino, CodVoo, H_Saida, H_Chegada) VALUES
(
  '1512', 'SAO', 'GIG', '151', '19:40', '20:20'
);
INSERT INTO Rota (CodRota, Origem, Destino, CodVoo, H_Saida, H_Chegada) VALUES
(
  '1513', 'GIG', 'POA', '151', '21:00', '22:40'
);
INSERT INTO Rota (CodRota, Origem, Destino, CodVoo, H_Saida, H_Chegada) VALUES
(
  '2001', 'SAO', 'GIG', '200', '13:00', '13:40'
);
INSERT INTO Rota (CodRota, Origem, Destino, CodVoo, H_Saida, H_Chegada) VALUES
(
  '2011', 'GIG', 'SAO', '201', '15:00', '15:40'
);
INSERT INTO Rota (CodRota, Origem, Destino, CodVoo, H_Saida, H_Chegada) VALUES
(
  '2101', 'SAO', 'GIG', '210', '21:00', '21:40'
);
INSERT INTO Rota (CodRota, Origem, Destino, CodVoo, H_Saida, H_Chegada) VALUES
(
  '2111', 'GIG', 'SAO', '211', '23:00', '23:40'
);
INSERT INTO Rota (CodRota, Origem, Destino, CodVoo, H_Saida, H_Chegada) VALUES
(
  '2401', 'SAO', 'BHZ', '240', '08:00', '08:30'
);
INSERT INTO Rota (CodRota, Origem, Destino, CodVoo, H_Saida, H_Chegada) VALUES
(
  '2402', 'BHZ', 'SAO', '240', '09:00', '09:30'
);

INSERT INTO Aviao (CodAviao, CodEmp, Tipo, Capacidade) VALUES ('002', 'GLO', 'BOEING2', 200);
INSERT INTO Aviao (CodAviao, CodEmp, Tipo, Capacidade) VALUES ('003', 'GLO', 'BOEING4', 350);
INSERT INTO Aviao (CodAviao, CodEmp, Tipo, Capacidade) VALUES ('007', 'TAM', 'BOEING2', 200);
INSERT INTO Aviao (CodAviao, CodEmp, Tipo, Capacidade) VALUES ('008', 'TAM', 'BOEING5', 450);
INSERT INTO Aviao (CodAviao, CodEmp, Tipo, Capacidade) VALUES ('004', 'AZU', 'BOEING5', 450);
INSERT INTO Aviao (CodAviao, CodEmp, Tipo, Capacidade) VALUES ('005', 'AZU', 'BOEING2', 200);
INSERT INTO Aviao (CodAviao, CodEmp, Tipo, Capacidade) VALUES ('006', 'AZU', 'BOEING4', 350);

INSERT INTO Viagem (CodRota, Data, H_Saida_Real, H_Chegada_Real, CodAviao) VALUES
(
  '8201','2022-11-07', '8:10', '8:50', '007'
);
INSERT INTO Viagem (CodRota, Data, H_Saida_Real, H_Chegada_Real, CodAviao) VALUES
(
  '8202','2022-11-07', '9:30', '11:10', '007'
);
INSERT INTO Viagem (CodRota, Data, H_Saida_Real, H_Chegada_Real, CodAviao) VALUES
(
  '8211','2022-11-07', '12:00', '13:40', '007'
);
INSERT INTO Viagem (CodRota, Data, H_Saida_Real, H_Chegada_Real, CodAviao) VALUES
(
  '8212','2022-11-07', '14:20', '15:00', '007'
);
INSERT INTO Viagem (CodRota, Data, H_Saida_Real, H_Chegada_Real, CodAviao) VALUES
(
  '8301','2022-11-07', '10:05', '10:45', '008'
);
INSERT INTO Viagem (CodRota, Data, H_Saida_Real, H_Chegada_Real, CodAviao) VALUES
(
  '8302','2022-11-07', '11:25', '12:55', '008'
);
INSERT INTO Viagem (CodRota, Data, H_Saida_Real, H_Chegada_Real, CodAviao) VALUES
(
  '8311','2022-11-07', '14:00', '15:30', '008'
);
INSERT INTO Viagem (CodRota, Data, H_Saida_Real, H_Chegada_Real, CodAviao) VALUES
(
  '8312','2022-11-07', '16:20', '17:00', '008'
);
INSERT INTO Viagem (CodRota, Data, H_Saida_Real, H_Chegada_Real, CodAviao) VALUES
(
  '1001','2022-11-07', '09:30', '11:10', '002'
);
INSERT INTO Viagem (CodRota, Data, H_Saida_Real, H_Chegada_Real, CodAviao) VALUES
(
  '1002','2022-11-07', '12:00', '13:30', '002'
);
INSERT INTO Viagem (CodRota, Data, H_Saida_Real, H_Chegada_Real, CodAviao) VALUES
(
  '1011','2022-11-07', '15:00', '16:30', '002'
);
INSERT INTO Viagem (CodRota, Data, H_Saida_Real, H_Chegada_Real, CodAviao) VALUES
(
  '1012','2022-11-07', '17:10', '18:50', '002'
);
INSERT INTO Viagem (CodRota, Data, H_Saida_Real, H_Chegada_Real, CodAviao) VALUES
(
  '1501','2022-11-07', '13:30', '15:10', '003'
);
INSERT INTO Viagem (CodRota, Data, H_Saida_Real, H_Chegada_Real, CodAviao) VALUES
(
  '1502','2022-11-07', '15:50', '16:30', '003'
);
INSERT INTO Viagem (CodRota, Data, H_Saida_Real, H_Chegada_Real, CodAviao) VALUES
(
  '1503','2022-11-07', '17:10', '17:40', '003'
);
INSERT INTO Viagem (CodRota, Data, H_Saida_Real, H_Chegada_Real, CodAviao) VALUES
(
  '1511','2022-11-07', '18:30', '19:00', '003'
);
INSERT INTO Viagem (CodRota, Data, H_Saida_Real, H_Chegada_Real, CodAviao) VALUES
(
  '1512','2022-11-07', '19:40', '20:20', '003'
);
INSERT INTO Viagem (CodRota, Data, H_Saida_Real, H_Chegada_Real, CodAviao) VALUES
(
  '1513','2022-11-07', '21:00', '22:40', '003'
);
INSERT INTO Viagem (CodRota, Data, H_Saida_Real, H_Chegada_Real, CodAviao) VALUES
(
  '2001','2022-11-07', '13:00', '13:40', '004'
);
INSERT INTO Viagem (CodRota, Data, H_Saida_Real, H_Chegada_Real, CodAviao) VALUES
(
  '2011','2022-11-07', '15:00', '15:40', '004'
);
INSERT INTO Viagem (CodRota, Data, H_Saida_Real, H_Chegada_Real, CodAviao) VALUES
(
  '2101','2022-11-07', '21:00', '21:40', '005'
);
INSERT INTO Viagem (CodRota, Data, H_Saida_Real, H_Chegada_Real, CodAviao) VALUES
(
  '2111','2022-11-07', '23:00', '23:40', '005'
);
INSERT INTO Viagem (CodRota, Data, H_Saida_Real, H_Chegada_Real, CodAviao) VALUES
(
  '2401','2022-11-07', '08:20', '08:50', '006'
);
INSERT INTO Viagem (CodRota, Data, H_Saida_Real, H_Chegada_Real, CodAviao) VALUES
(
  '2402','2022-11-07', '09:20', '09:50', '006'
);
INSERT INTO Viagem (CodRota, Data, H_Saida_Real, H_Chegada_Real, CodAviao) VALUES
(
  '8201','2022-11-08', '8:00', '8:40', '007'
);
INSERT INTO Viagem (CodRota, Data, H_Saida_Real, H_Chegada_Real, CodAviao) VALUES
(
  '8202','2022-11-08', '9:20', '11:00', '007'
);
INSERT INTO Viagem (CodRota, Data, H_Saida_Real, H_Chegada_Real, CodAviao) VALUES
(
  '8211','2022-11-08', '12:30', '14:10', '007'
);
INSERT INTO Viagem (CodRota, Data, H_Saida_Real, H_Chegada_Real, CodAviao) VALUES
(
  '8212','2022-11-08', '14:50', '15:30', '007'
);
INSERT INTO Viagem (CodRota, Data, H_Saida_Real, H_Chegada_Real, CodAviao) VALUES
(
  '8301','2022-11-08', '10:00', '10:40', '007'
);
INSERT INTO Viagem (CodRota, Data, H_Saida_Real, H_Chegada_Real, CodAviao) VALUES
(
  '8302','2022-11-08', '11:20', '12:50', '008'
);
INSERT INTO Viagem (CodRota, Data, H_Saida_Real, H_Chegada_Real, CodAviao) VALUES
(
  '8311','2022-11-08', '14:10', '15:40', '008'
);
INSERT INTO Viagem (CodRota, Data, H_Saida_Real, H_Chegada_Real, CodAviao) VALUES
(
  '8312','2022-11-08', '16:30', '17:10', '008'
);
INSERT INTO Viagem (CodRota, Data, H_Saida_Real, H_Chegada_Real, CodAviao) VALUES
(
  '1001','2022-11-08', '09:20', '11:00', '002'
);
INSERT INTO Viagem (CodRota, Data, H_Saida_Real, H_Chegada_Real, CodAviao) VALUES
(
  '1002','2022-11-08', '12:10', '13:40', '002'
);
INSERT INTO Viagem (CodRota, Data, H_Saida_Real, H_Chegada_Real, CodAviao) VALUES
(
  '1011','2022-11-08', '15:00', '16:40', '002'
);
INSERT INTO Viagem (CodRota, Data, H_Saida_Real, H_Chegada_Real, CodAviao) VALUES
(
  '1012','2022-11-08', '17:00', '19:00', '002'
);
INSERT INTO Viagem (CodRota, Data, H_Saida_Real, H_Chegada_Real, CodAviao) VALUES
(
  '1501','2022-11-08', '13:20', '15:00', '003'
);
INSERT INTO Viagem (CodRota, Data, H_Saida_Real, H_Chegada_Real, CodAviao) VALUES
(
  '1502','2022-11-08', '15:40', '16:20', '003'
);
INSERT INTO Viagem (CodRota, Data, H_Saida_Real, H_Chegada_Real, CodAviao) VALUES
(
  '1503','2022-11-08', '17:00', '17:30', '003'
);
INSERT INTO Viagem (CodRota, Data, H_Saida_Real, H_Chegada_Real, CodAviao) VALUES
(
  '1511','2022-11-08', '18:50', '19:20', '003'
);
INSERT INTO Viagem (CodRota, Data, H_Saida_Real, H_Chegada_Real, CodAviao) VALUES
(
  '1512','2022-11-08', '19:50', '20:30', '003'
);
INSERT INTO Viagem (CodRota, Data, H_Saida_Real, H_Chegada_Real, CodAviao) VALUES
(
  '1513','2022-11-08', '21:20', '23:00', '003'
);
INSERT INTO Viagem (CodRota, Data, H_Saida_Real, H_Chegada_Real, CodAviao) VALUES
(
  '2001','2022-11-08', '13:00', '13:40', '004'
);
INSERT INTO Viagem (CodRota, Data, H_Saida_Real, H_Chegada_Real, CodAviao) VALUES
(
  '2011','2022-11-08', '15:00', '15:40', '004'
);
INSERT INTO Viagem (CodRota, Data, H_Saida_Real, H_Chegada_Real, CodAviao) VALUES
(
  '2101','2022-11-08', '21:00', '21:40', '005'
);
INSERT INTO Viagem (CodRota, Data, H_Saida_Real, H_Chegada_Real, CodAviao) VALUES
(
  '2111','2022-11-08', '23:00', '23:40', '005'
);
INSERT INTO Viagem (CodRota, Data, H_Saida_Real, H_Chegada_Real, CodAviao) VALUES
(
  '2401','2022-11-08', '08:00', '08:30', '006'
);
INSERT INTO Viagem (CodRota, Data, H_Saida_Real, H_Chegada_Real, CodAviao) VALUES
(
  '2402','2022-11-08', '09:00', '09:30', '006'
);
INSERT INTO Viagem (CodRota, Data, H_Saida_Real, H_Chegada_Real, CodAviao) VALUES
(
  '8201','2022-11-09', '8:00', '8:40', '007'
);
INSERT INTO Viagem (CodRota, Data) VALUES
(
  '8202','2022-11-09'
);
INSERT INTO Viagem (CodRota, Data) VALUES
(
  '8211','2022-11-09'
);
INSERT INTO Viagem (CodRota, Data) VALUES
(
  '8212','2022-11-09'
);
INSERT INTO Viagem (CodRota, Data) VALUES
(
  '8301','2022-11-09'
);
INSERT INTO Viagem (CodRota, Data) VALUES
(
  '8302','2022-11-09'
);
INSERT INTO Viagem (CodRota, Data) VALUES
(
  '8311','2022-11-09'
);
INSERT INTO Viagem (CodRota, Data) VALUES
(
  '8312','2022-11-09'
);
INSERT INTO Viagem (CodRota, Data) VALUES
(
  '1001','2022-11-09'
);
INSERT INTO Viagem (CodRota, Data) VALUES
(
  '1002','2022-11-09'
);
INSERT INTO Viagem (CodRota, Data) VALUES
(
  '1011','2022-11-09'
);
INSERT INTO Viagem (CodRota, Data) VALUES
(
  '1012','2022-11-09'
);
INSERT INTO Viagem (CodRota, Data) VALUES
(
  '1501','2022-11-09'
);
INSERT INTO Viagem (CodRota, Data) VALUES
(
  '1502','2022-11-09'
);
INSERT INTO Viagem (CodRota, Data) VALUES
(
  '1503','2022-11-09'
);
INSERT INTO Viagem (CodRota, Data) VALUES
(
  '1511','2022-11-09'
);
INSERT INTO Viagem (CodRota, Data) VALUES
(
  '1512','2022-11-09'
);
INSERT INTO Viagem (CodRota, Data) VALUES
(
  '1513','2022-11-09'
);
INSERT INTO Viagem (CodRota, Data) VALUES
(
  '2001','2022-11-09'
);
INSERT INTO Viagem (CodRota, Data) VALUES
(
  '2011','2022-11-09'
);
INSERT INTO Viagem (CodRota, Data) VALUES
(
  '2101','2022-11-09'
);
INSERT INTO Viagem (CodRota, Data) VALUES
(
  '2111','2022-11-09'
);
INSERT INTO Viagem (CodRota, Data) VALUES
(
  '2401','2022-11-09'
);
INSERT INTO Viagem (CodRota, Data) VALUES
(
  '2402','2022-11-09'
);

