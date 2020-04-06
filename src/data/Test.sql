-- MariaDB dump 10.17  Distrib 10.4.12-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: Test
-- ------------------------------------------------------
-- Server version	10.4.12-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Amostra`
--

DROP TABLE IF EXISTS `Amostra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Amostra` (
  `idAmostra` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `idPaciente` int(10) unsigned NOT NULL,
  `idColeta` int(10) unsigned NOT NULL,
  `DataExtracao` date NOT NULL,
  `Caixa` char(255) NOT NULL,
  `PosicaoCaixa` char(255) NOT NULL,
  `Freezer` char(255) NOT NULL,
  `ConcentracaoNanovue` float NOT NULL,
  `DataNanovue` date NOT NULL,
  `ConcentracaoQubit` float NOT NULL,
  `DataQubit` date NOT NULL,
  PRIMARY KEY (`idAmostra`),
  KEY `idPaciente` (`idPaciente`),
  KEY `idColeta` (`idColeta`),
  CONSTRAINT `Amostra_ibfk_1` FOREIGN KEY (`idPaciente`) REFERENCES `Paciente` (`idPaciente`),
  CONSTRAINT `Amostra_ibfk_2` FOREIGN KEY (`idColeta`) REFERENCES `Coleta` (`idColeta`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Amostra`
--

LOCK TABLES `Amostra` WRITE;
/*!40000 ALTER TABLE `Amostra` DISABLE KEYS */;
/*!40000 ALTER TABLE `Amostra` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `AmostraRNA`
--

DROP TABLE IF EXISTS `AmostraRNA`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `AmostraRNA` (
  `idAmostra` int(10) unsigned NOT NULL,
  `IntegridadeTapStation` char(255) NOT NULL,
  `DataTapeStation` date DEFAULT NULL,
  KEY `idAmostra` (`idAmostra`),
  CONSTRAINT `AmostraRNA_ibfk_1` FOREIGN KEY (`idAmostra`) REFERENCES `Amostra` (`idAmostra`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AmostraRNA`
--

LOCK TABLES `AmostraRNA` WRITE;
/*!40000 ALTER TABLE `AmostraRNA` DISABLE KEYS */;
/*!40000 ALTER TABLE `AmostraRNA` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Coleta`
--

DROP TABLE IF EXISTS `Coleta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Coleta` (
  `idColeta` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `idPaciente` int(10) unsigned NOT NULL,
  `Data` date NOT NULL,
  `DiaTratamento` date NOT NULL,
  `MaterialColetado` char(255) NOT NULL,
  PRIMARY KEY (`idColeta`),
  KEY `idPaciente` (`idPaciente`),
  CONSTRAINT `Coleta_ibfk_1` FOREIGN KEY (`idPaciente`) REFERENCES `Paciente` (`idPaciente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Coleta`
--

LOCK TABLES `Coleta` WRITE;
/*!40000 ALTER TABLE `Coleta` DISABLE KEYS */;
/*!40000 ALTER TABLE `Coleta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Diagnostico`
--

DROP TABLE IF EXISTS `Diagnostico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Diagnostico` (
  `idDiagnostico` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `idPaciente` int(10) unsigned NOT NULL,
  `TipoLeucemia` char(255) NOT NULL,
  `Data` date NOT NULL,
  PRIMARY KEY (`idDiagnostico`),
  KEY `idPaciente` (`idPaciente`),
  CONSTRAINT `Diagnostico_ibfk_1` FOREIGN KEY (`idPaciente`) REFERENCES `Paciente` (`idPaciente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Diagnostico`
--

LOCK TABLES `Diagnostico` WRITE;
/*!40000 ALTER TABLE `Diagnostico` DISABLE KEYS */;
/*!40000 ALTER TABLE `Diagnostico` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `InfoClinica`
--

DROP TABLE IF EXISTS `InfoClinica`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `InfoClinica` (
  `idInfoClinica` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `idColeta` int(10) unsigned NOT NULL,
  `DataDiagnostico` date NOT NULL,
  `Febre38` smallint(3) unsigned NOT NULL,
  `Hipotensao` smallint(3) unsigned NOT NULL,
  `Hipotermia` smallint(3) unsigned NOT NULL,
  `PerfusaoPeriferica` smallint(3) unsigned NOT NULL,
  `DistensaoAbdominal` smallint(3) unsigned NOT NULL,
  `Letargia` smallint(3) unsigned NOT NULL,
  `Sepse` smallint(3) unsigned NOT NULL,
  `SepseSevera` smallint(3) unsigned NOT NULL,
  `OutrosSinaisClinicos` text NOT NULL,
  `ProvavelSitioInfeccioso` enum('ICS','Pneumonia','Peritonite','Osteomielite','Gastroenterite','Celulite','Miosite','Mucosite','Outra') NOT NULL,
  `CateterPeriferico` tinyint(1) NOT NULL,
  `CVCPermanente` int(11) NOT NULL,
  `CVCTemporario` int(11) NOT NULL,
  `CateterFlebotomia` int(11) NOT NULL,
  `CateterArterial` int(11) NOT NULL,
  `CateterEstado` enum('Removido e não recolocado','Removido e recolocado em outro sítio','Removido e recolocado por cateter guia','Paciente sem cateter','Não','Desconhecido') NOT NULL,
  `InfeccaoTipo` enum('Comunitária','Nosocomial','Colonização') NOT NULL,
  `InfeccaoNosocomial` enum('Intra-hospitalar','Ambulatorial','Home-care','Não') NOT NULL,
  `InfeccaoOrigem` enum('Endógena','Exógena','Desconhecida') DEFAULT NULL,
  PRIMARY KEY (`idInfoClinica`),
  KEY `idColeta` (`idColeta`),
  CONSTRAINT `InfoClinica_ibfk_1` FOREIGN KEY (`idColeta`) REFERENCES `Coleta` (`idColeta`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `InfoClinica`
--

LOCK TABLES `InfoClinica` WRITE;
/*!40000 ALTER TABLE `InfoClinica` DISABLE KEYS */;
/*!40000 ALTER TABLE `InfoClinica` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `InfoMicroBiologica`
--

DROP TABLE IF EXISTS `InfoMicroBiologica`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `InfoMicroBiologica` (
  `idInfoMicroBiologica` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `idPaciente` int(10) unsigned NOT NULL,
  `DataCultura` date NOT NULL,
  `Microrganismo` char(255) NOT NULL,
  `FonteAmostra` enum('Sangue','Veia periferica','Cateter central','DTTP > 2h','DTTP < 2h','DTTP desconhecido','Ponta de cateter','Líquido perineural','Outro líquido estéril','Líquor','Escarro','Aspirado traqueal','Outro aspirado','BAL','Outro lavado','Urina','Biópsia','Outro') NOT NULL,
  PRIMARY KEY (`idInfoMicroBiologica`),
  KEY `idPaciente` (`idPaciente`),
  CONSTRAINT `InfoMicroBiologica_ibfk_1` FOREIGN KEY (`idPaciente`) REFERENCES `Paciente` (`idPaciente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `InfoMicroBiologica`
--

LOCK TABLES `InfoMicroBiologica` WRITE;
/*!40000 ALTER TABLE `InfoMicroBiologica` DISABLE KEYS */;
/*!40000 ALTER TABLE `InfoMicroBiologica` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Internamento`
--

DROP TABLE IF EXISTS `Internamento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Internamento` (
  `idInternamento` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `idPaciente` int(10) unsigned NOT NULL,
  `DataEntrada` date NOT NULL,
  `DiaAlta` date DEFAULT NULL,
  `Motivo` char(255) NOT NULL,
  PRIMARY KEY (`idInternamento`),
  KEY `idPaciente` (`idPaciente`),
  CONSTRAINT `Internamento_ibfk_1` FOREIGN KEY (`idPaciente`) REFERENCES `Paciente` (`idPaciente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Internamento`
--

LOCK TABLES `Internamento` WRITE;
/*!40000 ALTER TABLE `Internamento` DISABLE KEYS */;
/*!40000 ALTER TABLE `Internamento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `LogPreenchimento`
--

DROP TABLE IF EXISTS `LogPreenchimento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `LogPreenchimento` (
  `idLogPreenchimento` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `idPaciente` int(10) unsigned NOT NULL,
  `TipoEntrada` char(255) NOT NULL,
  `Data` date NOT NULL,
  `Nome` char(255) NOT NULL,
  PRIMARY KEY (`idLogPreenchimento`),
  KEY `idPaciente` (`idPaciente`),
  CONSTRAINT `LogPreenchimento_ibfk_1` FOREIGN KEY (`idPaciente`) REFERENCES `Paciente` (`idPaciente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `LogPreenchimento`
--

LOCK TABLES `LogPreenchimento` WRITE;
/*!40000 ALTER TABLE `LogPreenchimento` DISABLE KEYS */;
/*!40000 ALTER TABLE `LogPreenchimento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Medicamento`
--

DROP TABLE IF EXISTS `Medicamento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Medicamento` (
  `idMedicamento` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `idPaciente` int(10) unsigned NOT NULL,
  `idTipoTratamento` int(10) unsigned NOT NULL,
  `Nome` char(255) NOT NULL,
  `DataInicio` date NOT NULL,
  `DataTermino` date NOT NULL,
  PRIMARY KEY (`idMedicamento`),
  KEY `idPaciente` (`idPaciente`),
  CONSTRAINT `Medicamento_ibfk_1` FOREIGN KEY (`idPaciente`) REFERENCES `Paciente` (`idPaciente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Medicamento`
--

LOCK TABLES `Medicamento` WRITE;
/*!40000 ALTER TABLE `Medicamento` DISABLE KEYS */;
/*!40000 ALTER TABLE `Medicamento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Obito`
--

DROP TABLE IF EXISTS `Obito`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Obito` (
  `idObito` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `idPaciente` int(10) unsigned NOT NULL,
  `Data` date NOT NULL,
  `Causa` char(255) NOT NULL,
  PRIMARY KEY (`idObito`),
  KEY `idPaciente` (`idPaciente`),
  CONSTRAINT `Obito_ibfk_1` FOREIGN KEY (`idPaciente`) REFERENCES `Paciente` (`idPaciente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Obito`
--

LOCK TABLES `Obito` WRITE;
/*!40000 ALTER TABLE `Obito` DISABLE KEYS */;
/*!40000 ALTER TABLE `Obito` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Paciente`
--

DROP TABLE IF EXISTS `Paciente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Paciente` (
  `idPaciente` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `HospitalOrigem` char(255) NOT NULL,
  `ProntuarioOrigem` char(255) NOT NULL,
  `Sexo` char(10) NOT NULL,
  `DataNascimento` date NOT NULL,
  `Pais` char(255) NOT NULL,
  `Estado` char(255) NOT NULL,
  `Municipio` char(255) NOT NULL,
  `TipoAtendimento` char(255) NOT NULL,
  `TipoParto` char(255) NOT NULL,
  `Lactante` tinyint(1) NOT NULL,
  `Etnia` char(255) NOT NULL,
  PRIMARY KEY (`idPaciente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Paciente`
--

LOCK TABLES `Paciente` WRITE;
/*!40000 ALTER TABLE `Paciente` DISABLE KEYS */;
/*!40000 ALTER TABLE `Paciente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `RNASeq`
--

DROP TABLE IF EXISTS `RNASeq`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `RNASeq` (
  `idTipoTeste` int(10) unsigned NOT NULL,
  `Metodo` enum('Transcriptoma total','Ampliseq','SMART3seq') NOT NULL,
  `DataPreparo` date NOT NULL,
  `DataCorrida` date NOT NULL,
  `Barcode` char(255) DEFAULT NULL,
  `NomeRegistroIon` char(255) DEFAULT NULL,
  `Qualidade` char(255) DEFAULT NULL,
  KEY `idTipoTeste` (`idTipoTeste`),
  CONSTRAINT `RNASeq_ibfk_1` FOREIGN KEY (`idTipoTeste`) REFERENCES `TipoTeste` (`idTipoTeste`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `RNASeq`
--

LOCK TABLES `RNASeq` WRITE;
/*!40000 ALTER TABLE `RNASeq` DISABLE KEYS */;
/*!40000 ALTER TABLE `RNASeq` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Teste`
--

DROP TABLE IF EXISTS `Teste`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Teste` (
  `idTeste` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `idPaciente` int(10) unsigned NOT NULL,
  `idAmostra` int(10) unsigned NOT NULL,
  `TesteRealizado` char(255) NOT NULL,
  `Data` date NOT NULL,
  PRIMARY KEY (`idTeste`),
  KEY `idPaciente` (`idPaciente`),
  KEY `idAmostra` (`idAmostra`),
  CONSTRAINT `Teste_ibfk_1` FOREIGN KEY (`idPaciente`) REFERENCES `Paciente` (`idPaciente`),
  CONSTRAINT `Teste_ibfk_2` FOREIGN KEY (`idAmostra`) REFERENCES `Amostra` (`idAmostra`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Teste`
--

LOCK TABLES `Teste` WRITE;
/*!40000 ALTER TABLE `Teste` DISABLE KEYS */;
/*!40000 ALTER TABLE `Teste` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TipoTeste`
--

DROP TABLE IF EXISTS `TipoTeste`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TipoTeste` (
  `idTipoTeste` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `idTeste` int(10) unsigned NOT NULL,
  `DescricaoTeste` text NOT NULL,
  PRIMARY KEY (`idTipoTeste`),
  KEY `idTeste` (`idTeste`),
  CONSTRAINT `TipoTeste_ibfk_1` FOREIGN KEY (`idTeste`) REFERENCES `Teste` (`idTeste`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TipoTeste`
--

LOCK TABLES `TipoTeste` WRITE;
/*!40000 ALTER TABLE `TipoTeste` DISABLE KEYS */;
/*!40000 ALTER TABLE `TipoTeste` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TipoTratamento`
--

DROP TABLE IF EXISTS `TipoTratamento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TipoTratamento` (
  `idTipoTratamento` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `Nome` char(255) NOT NULL,
  PRIMARY KEY (`idTipoTratamento`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TipoTratamento`
--

LOCK TABLES `TipoTratamento` WRITE;
/*!40000 ALTER TABLE `TipoTratamento` DISABLE KEYS */;
/*!40000 ALTER TABLE `TipoTratamento` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-03-25 12:37:35
