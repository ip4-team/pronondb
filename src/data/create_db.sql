CREATE DATABASE IF NOT EXISTS Pronondb DEFAULT CHARACTER SET utf8;
USE Pronondb

SET FOREIGN_KEY_CHECKS=0;

---------------------------------------------------------------
--  Paciente
---------------------------------------------------------------

DROP TABLE IF EXISTS Paciente;
CREATE TABLE Paciente (
    idPaciente INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, 
    HospitalOrigem CHAR(255) NOT NULL,
    ProntuarioOrigem CHAR(255) NOT NULL,
    Sexo CHAR(10) NOT NULL,
    DataNascimento DATE NOT NULL,
    Pais CHAR(255) NOT NULL,
    Estado CHAR(255) NOT NULL,
    Municipio CHAR(255) NOT NULL,
    TipoAtendimento CHAR(255) NOT NULL,
    TipoParto CHAR(255) NOT NULL,
    Lactante BOOLEAN NOT NULL,
    Etnia CHAR(255) NOT NULL
) ENGINE=InnoDB;

---------------------------------------------------------------
--  Diagnostico
---------------------------------------------------------------

DROP TABLE IF EXISTS Diagnostico;
CREATE TABLE Diagnostico (
    idDiagnostico INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, 
    idPaciente INT UNSIGNED NOT NULL,
    TipoLeucemia CHAR(255) NOT NULL,
    Data DATE NOT NULL,
    FOREIGN KEY (idPaciente) REFERENCES Paciente (idPaciente)
) ENGINE=InnoDB;

---------------------------------------------------------------
--  Coleta
---------------------------------------------------------------

DROP TABLE IF EXISTS Coleta;
CREATE TABLE Coleta (
    idColeta INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    idPaciente INT UNSIGNED NOT NULL,
    Data DATE NOT NULL,
    DiaTratamento DATE NOT NULL,
    MaterialColetado CHAR(255) NOT NULL,
    FOREIGN KEY (idPaciente) REFERENCES Paciente (idPaciente)
) ENGINE=InnoDB;

---------------------------------------------------------------
--  Amostra
---------------------------------------------------------------

DROP TABLE IF EXISTS Amostra;
CREATE TABLE Amostra (
    idAmostra INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    idPaciente INT UNSIGNED NOT NULL,
    idColeta INT UNSIGNED NOT NULL,
    DataExtracao DATE NOT NULL,
    Caixa CHAR(255) NOT NULL,
    PosicaoCaixa CHAR(255) NOT NULL,
    Freezer CHAR(255) NOT NULL,
    ConcentracaoNanovue FLOAT NOT NULL,
    DataNanovue DATE NOT NULL,
    ConcentracaoQubit FLOAT NOT NULL,
    DataQubit DATE NOT NULL,
    FOREIGN KEY (idPaciente) REFERENCES Paciente (idPaciente),
    FOREIGN KEY (idColeta) REFERENCES Coleta (idColeta)
) ENGINE=InnoDB;

DROP TABLE IF EXISTS AmostraRNA;
CREATE TABLE AmostraRNA (
    idAmostraRNA INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    idPaciente INT UNSIGNED NOT NULL,
    idColeta INT UNSIGNED NOT NULL,
    DataExtracao DATE NOT NULL,
    Caixa CHAR(255) NOT NULL,
    PosicaoCaixa CHAR(255) NOT NULL,
    Freezer CHAR(255) NOT NULL,
    ConcentracaoNanovue FLOAT NOT NULL,
    DataNanovue DATE NOT NULL,
    ConcentracaoQubit FLOAT NOT NULL,
    DataQubit DATE NOT NULL,
    IntegridadeTapStation CHAR(255) NOT NULL,
    DataTapeStation DATE NOT NULL,
    FOREIGN KEY (idPaciente) REFERENCES Paciente (idPaciente),
    FOREIGN KEY (idColeta) REFERENCES Coleta (idColeta)
) ENGINE=InnoDB;

---------------------------------------------------------------
--  Teste
---------------------------------------------------------------

DROP TABLE IF EXISTS Teste;
CREATE TABLE Teste (
    idTeste INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    idPaciente INT UNSIGNED NOT NULL,
    idAmostra INT UNSIGNED NOT NULL,
    TesteRealizado CHAR(255) NOT NULL,
    Data DATE NOT NULL,
    FOREIGN KEY (idPaciente) REFERENCES Paciente (idPaciente),
    FOREIGN KEY (idAmostra) REFERENCES Amostra (idAmostra)
) ENGINE=InnoDB;

---------------------------------------------------------------
--  RNASeq
---------------------------------------------------------------

DROP TABLE IF EXISTS RNASeq;
CREATE TABLE RNASeq (
    idRNASeq INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    idPaciente INT UNSIGNED NOT NULL,
    idAmostraRNA INT UNSIGNED NOT NULL,
    Metodo ENUM('Transcriptoma total', 'Ampliseq', 'SMART3seq') NOT NULL,
    DataPreparo DATE NOT NULL,
    DataCorrida DATE NOT NULL,
    Barcode CHAR(255) NOT NULL,
    NomeRegistroIon CHAR(255) NOT NULL,
    Qualidade CHAR(255) NOT NULL,
    FOREIGN KEY (idPaciente) REFERENCES Paciente (idPaciente),
    FOREIGN KEY (idAmostraRNA) REFERENCES AmostraRNA (idAmostraRNA)
) ENGINE=InnoDB;

---------------------------------------------------------------
--  Internamento
---------------------------------------------------------------

DROP TABLE IF EXISTS Internamento;
CREATE TABLE Internamento (
    idInternamento INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    idPaciente INT UNSIGNED NOT NULL,
    DataEntrada DATE NOT NULL,
    DiaAlta DATE,
    Motivo CHAR(255) NOT NULL,
    FOREIGN KEY (idPaciente) REFERENCES Paciente (idPaciente)
) ENGINE=InnoDB;

---------------------------------------------------------------
--  InfoClinica
---------------------------------------------------------------

DROP TABLE IF EXISTS InfoClinica;
CREATE TABLE InfoClinica (
    idInfoClinica INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    idColeta INT UNSIGNED NOT NULL,
    DataDiagnostico DATE NOT NULL,
    Febre38 SMALLINT(3) UNSIGNED NOT NULL,
    Hipotensao SMALLINT(3) UNSIGNED NOT NULL,
    Hipotermia SMALLINT(3) UNSIGNED NOT NULL,
    PerfusaoPeriferica SMALLINT(3) UNSIGNED NOT NULL,
    DistensaoAbdominal SMALLINT(3) UNSIGNED NOT NULL,
    Letargia SMALLINT(3) UNSIGNED NOT NULL,
    Sepse SMALLINT(3) UNSIGNED NOT NULL,
    SepseSevera SMALLINT(3) UNSIGNED NOT NULL,
    OutrosSinaisClinicos TEXT NOT NULL,
    ProvavelSitioInfeccioso ENUM('ICS', 'Pneumonia', 'Peritonite', 'Osteomielite', 'Gastroenterite', 'Celulite', 'Miosite', 'Mucosite', 'Outra') NOT NULL,
    CateterPeriferico BOOLEAN NOT NULL,
    CVCPermanente INT NOT NULL,
    CVCTemporario INT NOT NULL,
    CateterFlebotomia INT NOT NULL,
    CateterArterial INT NOT NULL,
    CateterEstado ENUM('Removido e não recolocado', 'Removido e recolocado em outro sítio', 'Removido e recolocado por cateter guia', 'Paciente sem cateter', 'Não', 'Desconhecido') NOT NULL,
    InfeccaoTipo ENUM('Comunitária', 'Nosocomial', 'Colonização') NOT NULL,
    InfeccaoNosocomial ENUM('Intra-hospitalar', 'Ambulatorial', 'Home-care', 'Não') NOT NULL,
    InfeccaoOrigem ENUM('Endógena', 'Exógena', 'Desconhecida') NOT NULL, 
    FOREIGN KEY (idColeta) REFERENCES Coleta (idColeta)
) ENGINE=InnoDB;

---------------------------------------------------------------
--  InfoMicroBiologica
---------------------------------------------------------------

DROP TABLE IF EXISTS InfoMicroBiologica;
CREATE TABLE InfoMicroBiologica (
    idInfoMicroBiologica INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    idPaciente INT UNSIGNED NOT NULL,
    DataCultura DATE NOT NULL,
    Microrganismo CHAR(255) NOT NULL,
    FonteAmostra ENUM('Sangue', 'Veia periferica', 'Cateter central', 'DTTP > 2h', 'DTTP < 2h', 'DTTP desconhecido', 'Ponta de cateter', 'Líquido perineural', 'Outro líquido estéril', 'Líquor', 'Escarro', 'Aspirado traqueal', 'Outro aspirado', 'BAL', 'Outro lavado', 'Urina', 'Biópsia', 'Outro') NOT NULL,
    FOREIGN KEY (idPaciente) REFERENCES Paciente (idPaciente)
) ENGINE=InnoDB;

---------------------------------------------------------------
--  Obito
---------------------------------------------------------------

DROP TABLE IF EXISTS Obito;
CREATE TABLE Obito (
    idObito INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    idPaciente INT UNSIGNED NOT NULL,
    Data DATE NOT NULL,
    Causa CHAR(255) NOT NULL,
    FOREIGN KEY (idPaciente) REFERENCES Paciente (idPaciente)
) ENGINE=InnoDB;

---------------------------------------------------------------
--  Medicamento
---------------------------------------------------------------

DROP TABLE IF EXISTS Medicamento;
CREATE TABLE Medicamento (
    idMedicamento INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    idPaciente INT UNSIGNED NOT NULL,
    TipoTratamento CHAR(255) NOT NULL,
    Nome CHAR(255) NOT NULL,
    DataInicio DATE NOT NULL,
    DataTermino DATE NOT NULL,
    FOREIGN KEY (idPaciente) REFERENCES Paciente (idPaciente)
) ENGINE=InnoDB;

---------------------------------------------------------------
--  TipoTratamento
---------------------------------------------------------------

DROP TABLE IF EXISTS TipoTratamento;
CREATE TABLE TipoTratamento (
    idTipoTratamento INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    Nome CHAR(255) NOT NULL
) ENGINE=InnoDB;

---------------------------------------------------------------
--  LogPreenchimento
---------------------------------------------------------------

DROP TABLE IF EXISTS LogPreenchimento;
CREATE TABLE LogPreenchimento (
    idLogPreenchimento INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    Comando CHAR(255) NOT NULL,
    Query CHAR(255) NOT NULL,
    Tabela CHAR(255) NOT NULL,
    Data DATETIME NOT NULL,
    Nome CHAR(255) NOT NULL
) ENGINE=InnoDB;
