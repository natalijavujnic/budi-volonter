CREATE DATABASE  IF NOT EXISTS `budivolonter` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `budivolonter`;
-- MySQL dump 10.13  Distrib 8.0.36, for macos14 (arm64)
--
-- Host: 127.0.0.1    Database: budivolonter
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `aktivnost`
--

DROP TABLE IF EXISTS `aktivnost`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `aktivnost` (
  `idOrg` int NOT NULL,
  `idAkt` int NOT NULL AUTO_INCREMENT,
  `naziv` varchar(256) NOT NULL,
  `brMesta` int NOT NULL,
  `datumOd` date NOT NULL,
  `datumDo` date NOT NULL,
  `datumRok` date NOT NULL,
  `mesto` varchar(256) NOT NULL DEFAULT 'nije navedeno',
  `lokacija` int NOT NULL,
  PRIMARY KEY (`idAkt`),
  KEY `idx_brakt` (`idAkt`),
  KEY `FK_lokacija_idx` (`lokacija`),
  KEY `FK_korisnik_aktivnost_idx` (`idOrg`),
  CONSTRAINT `FK_korisnik_aktivnost` FOREIGN KEY (`idOrg`) REFERENCES `korisnik` (`idKor`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_lokacija` FOREIGN KEY (`lokacija`) REFERENCES `lokacija` (`idLok`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `aktivnost`
--

LOCK TABLES `aktivnost` WRITE;
/*!40000 ALTER TABLE `aktivnost` DISABLE KEYS */;
/*!40000 ALTER TABLE `aktivnost` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `korisnik`
--

DROP TABLE IF EXISTS `korisnik`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `korisnik` (
  `idKor` int NOT NULL AUTO_INCREMENT,
  `email` varchar(256) NOT NULL,
  `password` varchar(256) NOT NULL,
  `ime` varchar(256) NOT NULL,
  `prezime` varchar(256) DEFAULT NULL,
  `pib` int DEFAULT NULL,
  `telefon` varchar(14) DEFAULT NULL,
  `tip` char(1) NOT NULL,
  `datumRodj` date DEFAULT NULL,
  PRIMARY KEY (`idKor`),
  UNIQUE KEY `email_UNIQUE` (`email`),
  UNIQUE KEY `PIB_UNIQUE` (`pib`),
  UNIQUE KEY `telefon_UNIQUE` (`telefon`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `korisnik`
--

LOCK TABLES `korisnik` WRITE;
/*!40000 ALTER TABLE `korisnik` DISABLE KEYS */;
/*!40000 ALTER TABLE `korisnik` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lokacija`
--

DROP TABLE IF EXISTS `lokacija`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lokacija` (
  `drzava` varchar(256) NOT NULL,
  `kontinent` varchar(256) NOT NULL,
  `idLok` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`idLok`),
  KEY `idx_kontinent` (`kontinent`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lokacija`
--

LOCK TABLES `lokacija` WRITE;
/*!40000 ALTER TABLE `lokacija` DISABLE KEYS */;
/*!40000 ALTER TABLE `lokacija` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oblast`
--

DROP TABLE IF EXISTS `oblast`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `oblast` (
  `oblast` varchar(256) NOT NULL,
  PRIMARY KEY (`oblast`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oblast`
--

LOCK TABLES `oblast` WRITE;
/*!40000 ALTER TABLE `oblast` DISABLE KEYS */;
/*!40000 ALTER TABLE `oblast` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `poruka`
--

DROP TABLE IF EXISTS `poruka`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `poruka` (
  `idPre` int NOT NULL,
  `redBr` varchar(45) NOT NULL,
  `tekst` varchar(2000) NOT NULL,
  `time` timestamp NOT NULL,
  `status` char(1) NOT NULL,
  `idSender` int NOT NULL,
  PRIMARY KEY (`idPre`,`redBr`),
  KEY `FK_sender_poruka_idx` (`idSender`),
  CONSTRAINT `FK_prepiska_poruka` FOREIGN KEY (`idPre`) REFERENCES `prepiska` (`idPre`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_sender_poruka` FOREIGN KEY (`idSender`) REFERENCES `korisnik` (`idKor`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `poruka`
--

LOCK TABLES `poruka` WRITE;
/*!40000 ALTER TABLE `poruka` DISABLE KEYS */;
/*!40000 ALTER TABLE `poruka` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prepiska`
--

DROP TABLE IF EXISTS `prepiska`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prepiska` (
  `idPre` int NOT NULL,
  `idKor1` int NOT NULL,
  `idKor2` int NOT NULL,
  PRIMARY KEY (`idPre`),
  KEY `FK_kor1_prepiska_idx` (`idKor1`),
  KEY `FK_kor2_prepiska_idx` (`idKor2`),
  CONSTRAINT `FK_kor1_prepiska` FOREIGN KEY (`idKor1`) REFERENCES `korisnik` (`idKor`) ON UPDATE CASCADE,
  CONSTRAINT `FK_kor2_prepiska` FOREIGN KEY (`idKor2`) REFERENCES `korisnik` (`idKor`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prepiska`
--

LOCK TABLES `prepiska` WRITE;
/*!40000 ALTER TABLE `prepiska` DISABLE KEYS */;
/*!40000 ALTER TABLE `prepiska` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prijava`
--

DROP TABLE IF EXISTS `prijava`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prijava` (
  `idPri` int NOT NULL,
  `idVol` int NOT NULL,
  `idAkt` int NOT NULL,
  `pismo` varchar(2000) NOT NULL,
  `rezime` blob,
  `status` char(1) NOT NULL,
  `preporukaVol` char(1) DEFAULT NULL,
  `preporukaOrg` char(1) DEFAULT NULL,
  `komVol` varchar(1000) DEFAULT NULL,
  `komOrg` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`idPri`),
  KEY `FK_kor_prijava_idx` (`idVol`),
  KEY `FK_akt_prijava_idx` (`idAkt`),
  CONSTRAINT `FK_akt_prijava` FOREIGN KEY (`idAkt`) REFERENCES `aktivnost` (`idAkt`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_kor_prijava` FOREIGN KEY (`idVol`) REFERENCES `korisnik` (`idKor`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prijava`
--

LOCK TABLES `prijava` WRITE;
/*!40000 ALTER TABLE `prijava` DISABLE KEYS */;
/*!40000 ALTER TABLE `prijava` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pripada`
--

DROP TABLE IF EXISTS `pripada`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pripada` (
  `idAkt` int NOT NULL,
  `oblast` varchar(256) NOT NULL,
  PRIMARY KEY (`idAkt`,`oblast`),
  KEY `FK_oblast_idx` (`oblast`),
  CONSTRAINT `FK_akt_pripada` FOREIGN KEY (`idAkt`) REFERENCES `aktivnost` (`idAkt`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_oblast` FOREIGN KEY (`oblast`) REFERENCES `oblast` (`oblast`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pripada`
--

LOCK TABLES `pripada` WRITE;
/*!40000 ALTER TABLE `pripada` DISABLE KEYS */;
/*!40000 ALTER TABLE `pripada` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vestina`
--

DROP TABLE IF EXISTS `vestina`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vestina` (
  `idAkt` int NOT NULL,
  `redBr` int NOT NULL,
  `opis` varchar(256) NOT NULL,
  PRIMARY KEY (`idAkt`,`redBr`),
  KEY `FK_aktivnostBrAkt_vestina_idx` (`idAkt`),
  CONSTRAINT `FK_akt_vestina` FOREIGN KEY (`idAkt`) REFERENCES `aktivnost` (`idAkt`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vestina`
--

LOCK TABLES `vestina` WRITE;
/*!40000 ALTER TABLE `vestina` DISABLE KEYS */;
/*!40000 ALTER TABLE `vestina` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zanima_ga`
--

DROP TABLE IF EXISTS `zanima_ga`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `zanima_ga` (
  `idKor` int NOT NULL,
  `oblast` varchar(256) NOT NULL,
  PRIMARY KEY (`idKor`,`oblast`),
  KEY `FK_oblast_zanima_ga_idx` (`oblast`),
  CONSTRAINT `FK_korisnik_zanimga_ga` FOREIGN KEY (`idKor`) REFERENCES `korisnik` (`idKor`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_oblast_zanima_ga` FOREIGN KEY (`oblast`) REFERENCES `oblast` (`oblast`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zanima_ga`
--

LOCK TABLES `zanima_ga` WRITE;
/*!40000 ALTER TABLE `zanima_ga` DISABLE KEYS */;
/*!40000 ALTER TABLE `zanima_ga` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-10 23:16:00
