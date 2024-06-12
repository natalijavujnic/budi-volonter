-- MySQL dump 10.13  Distrib 8.0.36, for macos14 (arm64)
--
-- Host: 127.0.0.1    Database: budivolonter
-- ------------------------------------------------------
-- Server version	8.4.0

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
  `opis` varchar(3000) DEFAULT NULL,
  PRIMARY KEY (`idAkt`),
  KEY `idx_brakt` (`idAkt`),
  KEY `FK_lokacija_idx` (`lokacija`),
  KEY `FK_korisnik_aktivnost_idx` (`idOrg`),
  CONSTRAINT `FK_korisnik_aktivnost` FOREIGN KEY (`idOrg`) REFERENCES `korisnik` (`idKor`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_lokacija` FOREIGN KEY (`lokacija`) REFERENCES `lokacija` (`idLok`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=914 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `aktivnost`
--

LOCK TABLES `aktivnost` WRITE;
/*!40000 ALTER TABLE `aktivnost` DISABLE KEYS */;
INSERT INTO `aktivnost` VALUES (2,878,'Čišćenje parka',4,'2024-06-22','2024-06-22','2024-06-20','Beograd',101,'Volontiraj i pridruži se čišćenju parka. Učestvuj u očuvanju prirode, sakupljanju otpada, i unapređenju zelenih površina za sve posetioce.'),(3,879,'Sadnja drveća',5,'2024-04-01','2024-04-01','2024-04-01','Beograd',101,'Volontiraj u sadnji drveća i unapredi zelene površine.'),(3,880,'Edukacija o reciklaži',10,'2024-04-05','2024-04-05','2024-04-03','Beograd',101,'Pridruži se edukaciji o reciklaži i doprinesi očuvanju prirode.'),(3,881,'Čišćenje jezera',8,'2024-04-10','2024-04-10','2024-04-08','Beograd',101,'Učestvuj u čišćenju jezera i poboljšaj kvalitet vode.'),(3,882,'Ekološki seminar',15,'2024-06-25','2024-06-25','2024-06-20','Beograd',101,'Pridruži se ekološkom seminaru i saznaj više o zaštiti životne sredine.'),(3,883,'Čišćenje parka',4,'2024-07-05','2024-07-05','2024-07-01','Beograd',101,'Volontiraj i pridruži se čišćenju parka. Učestvuj u očuvanju prirode, sakupljanju otpada, i unapređenju zelenih površina za sve posetioce.'),(3,884,'Piknik za volontere',20,'2024-07-10','2024-07-10','2024-07-05','Beograd',101,'Pridruži se pikniku za volontere i uživaj u zajedničkim aktivnostima na otvorenom.'),(4,885,'Sadnja cveća',6,'2024-04-02','2024-04-02','2024-04-01','Beograd',101,'Volontiraj u sadnji cveća i unapredi zelene površine.'),(4,886,'Predavanje o biodiverzitetu',12,'2024-04-06','2024-04-06','2024-04-04','Beograd',101,'Pridruži se predavanju o biodiverzitetu i saznaj više o očuvanju prirode.'),(4,887,'Čišćenje reke',7,'2024-04-11','2024-04-11','2024-04-09','Beograd',101,'Učestvuj u čišćenju reke i poboljšaj kvalitet vode.'),(4,888,'Eko radionica',15,'2024-06-26','2024-06-26','2024-06-21','Beograd',101,'Pridruži se eko radionici i saznaj više o zaštiti životne sredine.'),(4,889,'Čišćenje parka',4,'2024-07-06','2024-07-06','2024-07-02','Beograd',101,'Volontiraj i pridruži se čišćenju parka. Učestvuj u očuvanju prirode, sakupljanju otpada, i unapređenju zelenih površina za sve posetioce.'),(4,890,'Sportski dan za volontere',25,'2024-07-12','2024-07-12','2024-07-07','Beograd',101,'Pridruži se sportskom danu za volontere i uživaj u zajedničkim sportskim aktivnostima.'),(5,891,'Sadnja voćaka',5,'2024-04-03','2024-04-03','2024-04-02','Beograd',101,'Volontiraj u sadnji voćaka i unapredi zelene površine.'),(5,892,'Radionica o reciklaži',10,'2024-04-07','2024-04-07','2024-04-05','Beograd',101,'Pridruži se radionici o reciklaži i doprinesi očuvanju prirode.'),(5,893,'Čišćenje šume',8,'2024-04-12','2024-04-12','2024-04-10','Beograd',101,'Učestvuj u čišćenju šume i poboljšaj kvalitet staništa.'),(5,894,'Eko edukacija',15,'2024-06-27','2024-06-27','2024-06-22','Beograd',101,'Pridruži se eko edukaciji i saznaj više o zaštiti životne sredine.'),(5,895,'Čišćenje parka',4,'2024-07-07','2024-07-07','2024-07-03','Beograd',101,'Volontiraj i pridruži se čišćenju parka. Učestvuj u očuvanju prirode, sakupljanju otpada, i unapređenju zelenih površina za sve posetioce.'),(5,896,'Zelena pijaca',20,'2024-07-13','2024-07-13','2024-07-08','Beograd',101,'Pridruži se organizaciji zelene pijace i promoviši ekološki uzgojene proizvode.'),(6,897,'Sadnja žbunja',6,'2024-04-04','2024-04-04','2024-04-03','Beograd',101,'Volontiraj u sadnji žbunja i unapredi zelene površine.'),(6,898,'Predavanje o ekosistemima',12,'2024-04-08','2024-04-08','2024-04-06','Beograd',101,'Pridruži se predavanju o ekosistemima i saznaj više o očuvanju prirode.'),(6,899,'Čišćenje obale',7,'2024-04-13','2024-04-13','2024-04-11','Beograd',101,'Učestvuj u čišćenju obale i poboljšaj kvalitet staništa.'),(6,900,'Eko kamp',15,'2024-06-28','2024-06-28','2024-06-23','Beograd',101,'Pridruži se eko kampu i saznaj više o zaštiti životne sredine.'),(6,901,'Čišćenje parka',4,'2024-07-08','2024-07-08','2024-07-04','Beograd',101,'Volontiraj i pridruži se čišćenju parka. Učestvuj u očuvanju prirode, sakupljanju otpada, i unapređenju zelenih površina za sve posetioce.'),(6,902,'Volonterska biciklijada',25,'2024-07-14','2024-07-14','2024-07-09','Beograd',101,'Pridruži se volonterskoj biciklijadi i uživaj u zajedničkim aktivnostima na otvorenom.'),(7,903,'Sadnja cveća',5,'2024-04-05','2024-04-05','2024-04-04','Beograd',101,'Volontiraj u sadnji cveća i unapredi zelene površine.'),(7,904,'Radionica o kompostiranju',10,'2024-04-09','2024-04-09','2024-04-07','Beograd',101,'Pridruži se radionici o kompostiranju i doprinesi očuvanju prirode.'),(7,905,'Čišćenje livade',8,'2024-04-14','2024-04-14','2024-04-12','Beograd',101,'Učestvuj u čišćenju livade i poboljšaj kvalitet staništa.'),(7,906,'Eko festival',15,'2024-06-29','2024-06-29','2024-06-24','Beograd',101,'Pridruži se eko festivalu i saznaj više o zaštiti životne sredine.'),(7,907,'Čišćenje parka',4,'2024-07-09','2024-07-09','2024-07-05','Beograd',101,'Volontiraj i pridruži se čišćenju parka. Učestvuj u očuvanju prirode, sakupljanju otpada, i unapređenju zelenih površina za sve posetioce.'),(7,908,'Radionica za decu',20,'2024-07-15','2024-07-15','2024-07-10','Beograd',101,'Pridruži se radionici za decu i podstakni njihovu svest o zaštiti prirode.'),(2,909,'Veterinarska kampanja za sterilizaciju',6,'2024-04-29','2024-04-29','2024-04-29','Varšava',102,'Pridružite se našoj kampanji za sterilizaciju kako bismo smanjili broj neželjenih životinja i unaprijedili njihovo blagostanje. Sterilizacija je ključna za kontrolu populacije i sprečavanje patnje životinja. Vaša podrška može spasiti mnoge živote!'),(2,910,'Volontiranje u skloništu za napuštene životinje',19,'2024-04-29','2024-04-29','2024-04-19','Beograd',101,'Postanite deo našeg tima volontirajući u lokalnom skloništu za životinje. Pružite ljubav, brigu i pažnju napuštenim ljubimcima dok čekaju svoj zauvijek dom. Vaša posvećenost može učiniti veliku razliku u životima ovih predivnih bića.'),(2,911,'Edukativni program o zaštiti divljih životinja',7,'2024-04-29','2024-04-29','2024-04-22','Beograd',101,'Učestvujte u našem edukativnom programu o zaštiti divljih životinja i njihovom prirodnom staništu. Naučite kako možete pomoći u očuvanju raznolikosti divljih vrsta i smanjiti negativan uticaj ljudskih aktivnosti na njihov habitat.'),(2,912,'Akcija spašavanja životinja ugroženih požarima',9,'2024-07-15','2024-07-15','2024-07-15','Beograd',101,'Spremimo ruke i srca kako bismo pružili pomoć životinjama pogođenim šumskim požarima. Od spašavanja ugroženih životinja do pružanja hitne veterinarske njege, svaka podrška je od ključnog značaja. Neka naše zajedničke snage postanu spas za životinje u nevolji.'),(2,913,'Peticija za jače zakone o zaštiti životinja',78,'2024-04-29','2024-04-29','2024-04-21','Beograd',101,'Potpišite našu peticiju kojom tražimo jače zakone o zaštiti životinja i strože kazne za zlostavljače. Vaš glas može pokrenuti promene i osigurati da životinje imaju pravo na siguran i dostojanstven život. Budimo njihov glas i borimo se za njihova prava.');
/*!40000 ALTER TABLE `aktivnost` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_korisnik_idKor` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_korisnik_idKor` FOREIGN KEY (`user_id`) REFERENCES `korisnik` (`idKor`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'','admin','logentry'),(2,'','contenttypes','contenttype'),(3,'','sessions','session'),(4,'','budivolonter','aktivnost'),(5,'','budivolonter','korisnik'),(6,'','budivolonter','lokacija'),(7,'','budivolonter','oblast'),(8,'','budivolonter','prepiska'),(9,'','budivolonter','prijava'),(10,'','budivolonter','pripada'),(11,'','budivolonter','vestina'),(12,'','budivolonter','zanimaga'),(13,'','budivolonter','poruka');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'sessions','0001_initial','2024-05-14 00:25:32.235804');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('2sjfb10t8otlov0c1gs6g8ghhpslp9fh','.eJxVjDkOwjAUBe_iGll4SWxT0ucM1t-CA8iR4qRC3B0ipYD2zcx7qQzbWvLWZMkTq4uy6vS7IdBD6g74DvU2a5rrukyod0UftOlhZnleD_fvoEAr39oH5E5SbxnBpq4P7FMIBsgZISMuEhgkHi2OECEaR9F5hiR0loQhqvcH-aM4yg:1s7129:KKGGwpe7lGTcTPuYR_sZrO2AZsjinkQJ20XRctuMrsg','2024-05-28 22:54:09.821389'),('4hqzdlzg67ar79h8ipwny9rl9mc5d0is','.eJxVjEsOwjAMBe-SNYqCXacxS_acoXJiQwsolfpZIe4OlbqA7ZuZ93KdrEvfrbNN3aDu5NAdfrcs5WF1A3qXeht9GesyDdlvit_p7C-j2vO8u38Hvcz9t26JJCtntJgYGzgGoUJXxgyJAoEaB8WY2ihMBmKATCoFIIXMbePeH8y_NyA:1s8LgK:TAKL2gjV_J2QimsoFteO3nPEuLPW3bVe-tZRjyiWS-4','2024-06-01 15:09:08.398785'),('6wxt9aikdmtzv8qoq3z31tspgdunzv74','.eJxVjEEOwiAQRe_C2hAYEFuX7j0DGWYGqRpISrsy3l2bdKHb_977LxVxXUpcu8xxYnVWVh1-t4T0kLoBvmO9NU2tLvOU9KbonXZ9bSzPy-7-HRTs5VuTYXN0KIRAltjjCXKAgKMXBB5zEmKbXCAvg3hvnRWikGGgYMgAqvcHEss4_g:1sFxDd:t0zcot30kXsuRK8Xa7TintJy9EjTtyBtyVbTvpXB5UI','2024-06-22 14:38:57.118041'),('bc9h9wt3q6vslatnc95hzs54kk4pw9qn','.eJxVjEEOwiAQRe_C2hAYEFuX7j0DGWYGqRpISrsy3l2bdKHb_977LxVxXUpcu8xxYnVWoA6_W0J6SN0A37HemqZWl3lKelP0Tru-NpbnZXf_Dgr28q3JsDk6FEIgS-zxBDlAwNELAo85CbFNLpCXQby3zgpRyDBQMGQA1fsDE2Q4_w:1sHOKm:6ScXZLanxC-fXp3m5eE7i5NvkaS_r4oPbX93q8vVwk4','2024-06-26 13:48:16.930038'),('bmjaw4g6bfnlfl03bjxf0d9bxpaftj4j','.eJxVjDsOwjAQBe_iGln-sSSU9JzBWu-ucQDZUpxUiLtDpBTQvpl5LxVxXUpcu8xxYnVWFtThd0xID6kb4TvWW9PU6jJPSW-K3mnX18byvOzu30HBXr41GTZHj0LoyBIHPLkMDnAMgo7HnITYJg8UZJAQrLdCBNkNBIaMQ_X-ADm5OTQ:1sHNuu:23paQeWmez94ElvUlj-RN8leL_e34YKWxsYYPDEpXO8','2024-06-26 13:21:32.661141'),('cwqp6346vbk1udc6htmz9zcfzdjejl1p','.eJxVjEEOwiAQRe_C2hAYEFuX7j0DGWYGqRpISrsy3l2bdKHb_977LxVxXUpcu8xxYnVWYNThd0xID6kb4TvWW9PU6jJPSW-K3mnX18byvOzu30HBXr41GTZHh0IIZIk9niAHCDh6QeAxJyG2yQXyMoj31lkhChkGCoYMoHp_ADa9OS8:1sHOGi:44_55eZ0qP0GuLxw4RoXJUW4qt17kMZCEJ2bVLYw09c','2024-06-26 13:44:04.985321'),('g7ff79thcsii3x9yfmmsc24l1zzm0goi','.eJxVjEEOwiAQRe_C2hAYEFuX7j0DGWYGqRpISrsy3l2bdKHb_977LxVxXUpcu8xxYnVWVh1-t4T0kLoBvmO9NU2tLvOU9KbonXZ9bSzPy-7-HRTs5VuTYXN0KIRAltjjCXKAgKMXBB5zEmKbXCAvg3hvnRWikGGgYMgAqvcHEss4_g:1sD4qG:FJfCO4NnuDVaezNmKGK2o8aDEOQp-dBaj7VI8SdlxXM','2024-06-14 16:10:56.314173'),('hsftp1fu4djs7bwp5djt0elsd4nu6d3i','.eJxVjDkOwjAUBe_iGll4SWxT0ucM1t-CA8iR4qRC3B0ipYD2zcx7qQzbWvLWZMkTq4uy6vS7IdBD6g74DvU2a5rrukyod0UftOlhZnleD_fvoEAr39oH5E5SbxnBpq4P7FMIBsgZISMuEhgkHi2OECEaR9F5hiR0loQhqvcH-aM4yg:1sCHuH:8n2IluPzUGSE3z4sSoyr2c-rZcuEqxeFqp7dbJQITc0','2024-06-12 11:55:49.499163'),('k39q437q8lh7gyhvy9r3msh74p7iw50o','.eJxVjDkOwjAUBe_iGll4SWxT0ucM1t-CA8iR4qRC3B0ipYD2zcx7qQzbWvLWZMkTq4uy6vS7IdBD6g74DvU2a5rrukyod0UftOlhZnleD_fvoEAr39oH5E5SbxnBpq4P7FMIBsgZISMuEhgkHi2OECEaR9F5hiR0loQhqvcH-aM4yg:1sCHJE:oYUphRNHvYrSlIE_GSJ29Vkli_SZweIa_ZIvW_5GY5s','2024-06-12 11:17:32.285504'),('leahixc6qpb374vt6a8g3fpgiaxn01et','.eJxVjDsOgzAQBe_iOrKM8fqTMj1nsJbdJSaJQMJQRbl7QKJI2pl5760ybmvJW5Ulj6yuKqjLL-uRnjIdgh843WdN87QuY6-PRJ-26m5med3O9u-gYC372hA0jpzEIWAbODRgjBkCNATetVYQkmcEdr5PNkqKOxYfxSdhskzq8wXK6DeP:1sHLop:ARXZfTDxSJSylrqiO6CDPA2Ze1shF7QBa-RVisDA5Hg','2024-06-26 11:07:07.808695'),('o8lyqlgzdhlqj486la83ycnvyrjbzz8j','.eJxVjEEOwiAQRe_C2hAYEFuX7j0DGWYGqRpISrsy3l2bdKHb_977LxVxXUpcu8xxYnVWVh1-t4T0kLoBvmO9NU2tLvOU9KbonXZ9bSzPy-7-HRTs5VuTYXN0KIRAltjjCXKAgKMXBB5zEmKbXCAvg3hvnRWikGGgYMgAqvcHEss4_g:1sGgV8:kYUH3TYEPqWdJ1sTC9DBy3k-Tqswbx5fsEblgpgBxFY','2024-06-24 15:00:02.340019'),('rf3n1a20baab2zxc1mrqhvepzvd8g21n','.eJxVjEEOwiAQRe_C2hAYkLYu3fcMZJgZpGpoUtqV8e7apAvd_vfef6mI21ri1mSJE6uLsp06_Y4J6SF1J3zHeps1zXVdpqR3RR-06XFmeV4P9--gYCvfmgybs0MhBLLEHjvIAQIOXhB4yEmIbXKBvPTivXVWiEKGnoIhA6jeHzpSOTU:1sHK49:7UncKVyU4YgqrQarE9jbNwIATekhCQ6Mmh9xBA28x9E','2024-06-26 09:14:49.300730'),('vsc2bjv3c588g3on33sox5mmakyrgm3t','.eJxVjDsOwjAQBe_iGln-sSSU9JzBWu-ucQDZUpxUiLtDpBTQvpl5LxVxXUpcu8xxYnVWFtThd0xID6kb4TvWW9PU6jJPSW-K3mnX18byvOzu30HBXr41GTZHj0LoyBIHPLkMDnAMgo7HnITYJg8UZJAQrLdCBNkNBIaMQ_X-ADm5OTQ:1sHKjI:B0U0yxj7KuGqQgzSFjPUZgQJaFvCGSNH0Qn4VUJ4JOk','2024-06-26 09:57:20.621610'),('vukovu1mwfvto7ycklc3ltlve9lcqh26','.eJxVjDkOwjAUBe_iGll4SWxT0ucM1t-CA8iR4qRC3B0ipYD2zcx7qQzbWvLWZMkTq4uy6vS7IdBD6g74DvU2a5rrukyod0UftOlhZnleD_fvoEAr39oH5E5SbxnBpq4P7FMIBsgZISMuEhgkHi2OECEaR9F5hiR0loQhqvcH-aM4yg:1sCMQt:ic_zpPf9HiE1uc90cWqMnTKdxhEc0ilNnlhEv4mWv-A','2024-06-12 16:45:47.474666'),('zrha08zqigif5zxhd982einap8k1goqs','.eJxVjDkOwjAUBe_iGll4SWxT0ucM1t-CA8iR4qRC3B0ipYD2zcx7qQzbWvLWZMkTq4uy6vS7IdBD6g74DvU2a5rrukyod0UftOlhZnleD_fvoEAr39oH5E5SbxnBpq4P7FMIBsgZISMuEhgkHi2OECEaR9F5hiR0loQhqvcH-aM4yg:1s8LaB:UfbgPCAVZJ8HsuZKoOePwnXINQGjCK63Xkp3AO_TYW0','2024-06-01 15:02:47.852192');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
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
  `last_login` datetime DEFAULT NULL,
  `is_active` tinyint DEFAULT NULL,
  PRIMARY KEY (`idKor`),
  UNIQUE KEY `email_UNIQUE` (`email`),
  UNIQUE KEY `PIB_UNIQUE` (`pib`),
  UNIQUE KEY `telefon_UNIQUE` (`telefon`)
) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `korisnik`
--

LOCK TABLES `korisnik` WRITE;
/*!40000 ALTER TABLE `korisnik` DISABLE KEYS */;
INSERT INTO `korisnik` VALUES (1,'admin@bv.rs','pbkdf2_sha256$720000$fB91HR8EMIQCYYMDbfJEbR$J5KoRCekeUntUSPXc0zTE7fE+dWohcmOXI9sWxm3Dho=','Admin',NULL,NULL,NULL,'A',NULL,'2024-06-11 18:56:44',NULL),(2,'org2@example.com','pbkdf2_sha256$720000$EOmu3yd8YbISsrZrmFRiwy$Id0ELO3cFw2MITGJrNHFDvWGfOVr92KevyLoB7ijGz0=','Udruženje za spasavanje životinja',NULL,987654321,'0222345678','O',NULL,'2024-06-12 13:48:17',NULL),(3,'org3@example.com','pbkdf2_sha256$720000$EOmu3yd8YbISsrZrmFRiwy$Id0ELO3cFw2MITGJrNHFDvWGfOVr92KevyLoB7ijGz0=','Društvo za zaštitu životne sredine',NULL,654321987,'0333456789','O',NULL,NULL,NULL),(4,'org4@example.com','pbkdf2_sha256$720000$EOmu3yd8YbISsrZrmFRiwy$Id0ELO3cFw2MITGJrNHFDvWGfOVr92KevyLoB7ijGz0=','Fondacija za brigu o starijima',NULL,789456123,'0444567890','O',NULL,NULL,NULL),(5,'org5@example.com','pbkdf2_sha256$720000$EOmu3yd8YbISsrZrmFRiwy$Id0ELO3cFw2MITGJrNHFDvWGfOVr92KevyLoB7ijGz0=','Inicijativa za obrazovanje svih',NULL,321654987,'0555678901','O',NULL,NULL,NULL),(6,'org6@example.com','pbkdf2_sha256$720000$EOmu3yd8YbISsrZrmFRiwy$Id0ELO3cFw2MITGJrNHFDvWGfOVr92KevyLoB7ijGz0=','Fondacija za medicinsku pomoć',NULL,456789123,'0666789012','O',NULL,NULL,NULL),(7,'org7@example.com','pbkdf2_sha256$720000$EOmu3yd8YbISsrZrmFRiwy$Id0ELO3cFw2MITGJrNHFDvWGfOVr92KevyLoB7ijGz0=','Agencija za razvoj zajednice',NULL,147258369,'0777890123','O',NULL,NULL,NULL),(8,'org8@example.com','pbkdf2_sha256$720000$EOmu3yd8YbISsrZrmFRiwy$Id0ELO3cFw2MITGJrNHFDvWGfOVr92KevyLoB7ijGz0=','Fondacija umetnika za promene',NULL,963852741,'0888901234','O',NULL,NULL,NULL),(9,'org9@example.com','pbkdf2_sha256$720000$EOmu3yd8YbISsrZrmFRiwy$Id0ELO3cFw2MITGJrNHFDvWGfOVr92KevyLoB7ijGz0=','Udruženje za osnaživanje žena',NULL,258369147,'0999012345','O',NULL,NULL,NULL),(10,'org10@example.com','pbkdf2_sha256$720000$EOmu3yd8YbISsrZrmFRiwy$Id0ELO3cFw2MITGJrNHFDvWGfOVr92KevyLoB7ijGz0=','Fondacija za sport za sve',NULL,147963852,'0100112233','O',NULL,NULL,NULL),(11,'org11@example.com','pbkdf2_sha256$720000$EOmu3yd8YbISsrZrmFRiwy$Id0ELO3cFw2MITGJrNHFDvWGfOVr92KevyLoB7ijGz0=','Društvo za kulturno nasleđe',NULL,369258147,'0111223344','O',NULL,NULL,NULL),(12,'org12@example.com','pbkdf2_sha256$720000$EOmu3yd8YbISsrZrmFRiwy$Id0ELO3cFw2MITGJrNHFDvWGfOVr92KevyLoB7ijGz0=','Grupa za zagovaranje ljudskih prava',NULL,852741963,'0122334455','O',NULL,NULL,NULL),(13,'org13@example.com','pbkdf2_sha256$720000$EOmu3yd8YbISsrZrmFRiwy$Id0ELO3cFw2MITGJrNHFDvWGfOVr92KevyLoB7ijGz0=','Globalna inicijativa za zdravlje',NULL,741852963,'0133445566','O',NULL,NULL,NULL),(14,'org14@example.com','pbkdf2_sha256$720000$EOmu3yd8YbISsrZrmFRiwy$Id0ELO3cFw2MITGJrNHFDvWGfOVr92KevyLoB7ijGz0=','Fondacija Tehnologije za društvo',NULL,963741852,'0144556677','O',NULL,NULL,NULL),(15,'org15@example.com','pbkdf2_sha256$720000$EOmu3yd8YbISsrZrmFRiwy$Id0ELO3cFw2MITGJrNHFDvWGfOVr92KevyLoB7ijGz0=','Fondacija za zaštitu prirode',NULL,852963741,'0155667788','O',NULL,NULL,NULL),(16,'volunteer1@example.com','pbkdf2_sha256$720000$EOmu3yd8YbISsrZrmFRiwy$Id0ELO3cFw2MITGJrNHFDvWGfOVr92KevyLoB7ijGz0=','Jovan','Smiljanić',NULL,NULL,'V','1990-05-15','2024-06-12 13:21:33',NULL),(17,'volunteer2@example.com','pbkdf2_sha256$720000$EOmu3yd8YbISsrZrmFRiwy$Id0ELO3cFw2MITGJrNHFDvWGfOVr92KevyLoB7ijGz0=','Emilija','Jovanović',NULL,NULL,'V','1985-12-03',NULL,NULL),(18,'volunteer3@example.com','pbkdf2_sha256$720000$EOmu3yd8YbISsrZrmFRiwy$Id0ELO3cFw2MITGJrNHFDvWGfOVr92KevyLoB7ijGz0=','Mihajlo','Ilić',NULL,NULL,'V','1992-08-22','2024-06-12 13:42:53',NULL),(19,'volunteer4@example.com','pbkdf2_sha256$720000$EOmu3yd8YbISsrZrmFRiwy$Id0ELO3cFw2MITGJrNHFDvWGfOVr92KevyLoB7ijGz0=','Ema','Petrović',NULL,NULL,'V','1988-04-17','2024-06-12 12:58:47',NULL),(20,'volunteer5@example.com','pbkdf2_sha256$720000$EOmu3yd8YbISsrZrmFRiwy$Id0ELO3cFw2MITGJrNHFDvWGfOVr92KevyLoB7ijGz0=','Kristofer','Braun',NULL,NULL,'V','1995-10-29','2024-06-12 13:44:05',NULL),(21,'volunteer6@example.com','pbkdf2_sha256$720000$EOmu3yd8YbISsrZrmFRiwy$Id0ELO3cFw2MITGJrNHFDvWGfOVr92KevyLoB7ijGz0=','Olivera','Davidović',NULL,NULL,'V','1991-07-08',NULL,NULL),(22,'volunteer7@example.com','pbkdf2_sha256$720000$EOmu3yd8YbISsrZrmFRiwy$Id0ELO3cFw2MITGJrNHFDvWGfOVr92KevyLoB7ijGz0=','Vilijam','Miler',NULL,NULL,'V','1987-02-14','2024-06-12 13:45:23',NULL),(23,'volunteer8@example.com','pbkdf2_sha256$720000$EOmu3yd8YbISsrZrmFRiwy$Id0ELO3cFw2MITGJrNHFDvWGfOVr92KevyLoB7ijGz0=','Sofija','Wilson',NULL,NULL,'V','1993-11-01',NULL,NULL),(24,'volunteer9@example.com','pbkdf2_sha256$720000$EOmu3yd8YbISsrZrmFRiwy$Id0ELO3cFw2MITGJrNHFDvWGfOVr92KevyLoB7ijGz0=','Džejms','Tejlor',NULL,NULL,'V','1986-06-19',NULL,NULL),(25,'volunteer10@example.com','pbkdf2_sha256$720000$EOmu3yd8YbISsrZrmFRiwy$Id0ELO3cFw2MITGJrNHFDvWGfOVr92KevyLoB7ijGz0=','Ava','Anderson',NULL,NULL,'V','1994-09-25',NULL,NULL),(26,'volunteer11@example.com','pbkdf2_sha256$720000$EOmu3yd8YbISsrZrmFRiwy$Id0ELO3cFw2MITGJrNHFDvWGfOVr92KevyLoB7ijGz0=','Dejan','Tomašević',NULL,NULL,'V','1990-05-15',NULL,NULL),(27,'volunteer12@example.com','pbkdf2_sha256$720000$EOmu3yd8YbISsrZrmFRiwy$Id0ELO3cFw2MITGJrNHFDvWGfOVr92KevyLoB7ijGz0=','Isabela','Jakovljević',NULL,NULL,'V','1985-12-03',NULL,NULL),(28,'volunteer13@example.com','pbkdf2_sha256$720000$EOmu3yd8YbISsrZrmFRiwy$Id0ELO3cFw2MITGJrNHFDvWGfOVr92KevyLoB7ijGz0=','Daniel','Beljić',NULL,NULL,'V','1992-08-22',NULL,NULL),(29,'volunteer14@example.com','pbkdf2_sha256$720000$EOmu3yd8YbISsrZrmFRiwy$Id0ELO3cFw2MITGJrNHFDvWGfOVr92KevyLoB7ijGz0=','Mija','Haris',NULL,NULL,'V','1988-04-17',NULL,NULL),(30,'volunteer15@example.com','pbkdf2_sha256$720000$EOmu3yd8YbISsrZrmFRiwy$Id0ELO3cFw2MITGJrNHFDvWGfOVr92KevyLoB7ijGz0=','Josif','Martines',NULL,NULL,'V','1995-10-29','2024-06-12 13:43:27',NULL),(31,'volunteer16@example.com','pbkdf2_sha256$720000$EOmu3yd8YbISsrZrmFRiwy$Id0ELO3cFw2MITGJrNHFDvWGfOVr92KevyLoB7ijGz0=','Ljiljana','Ristić',NULL,NULL,'V','1991-07-08',NULL,NULL),(32,'volunteer17@example.com','pbkdf2_sha256$720000$EOmu3yd8YbISsrZrmFRiwy$Id0ELO3cFw2MITGJrNHFDvWGfOVr92KevyLoB7ijGz0=','Vilijam','Valker',NULL,NULL,'V','1987-02-14',NULL,NULL),(33,'volunteer18@example.com','pbkdf2_sha256$720000$EOmu3yd8YbISsrZrmFRiwy$Id0ELO3cFw2MITGJrNHFDvWGfOVr92KevyLoB7ijGz0=','Sofija','Jung',NULL,NULL,'V','1993-11-01','2024-06-12 12:58:22',NULL),(34,'volunteer19@example.com','pbkdf2_sha256$720000$EOmu3yd8YbISsrZrmFRiwy$Id0ELO3cFw2MITGJrNHFDvWGfOVr92KevyLoB7ijGz0=','Jovan','Kralj',NULL,NULL,'V','1986-06-19',NULL,NULL),(35,'volunteer20@example.com','pbkdf2_sha256$720000$EOmu3yd8YbISsrZrmFRiwy$Id0ELO3cFw2MITGJrNHFDvWGfOVr92KevyLoB7ijGz0=','Olivera','Klark',NULL,NULL,'V','1994-09-25',NULL,NULL),(36,'volunteer21@example.com','pbkdf2_sha256$720000$EOmu3yd8YbISsrZrmFRiwy$Id0ELO3cFw2MITGJrNHFDvWGfOVr92KevyLoB7ijGz0=','Mihajlo','Luis',NULL,NULL,'V','1990-05-15',NULL,NULL),(37,'volunteer22@example.com','pbkdf2_sha256$720000$EOmu3yd8YbISsrZrmFRiwy$Id0ELO3cFw2MITGJrNHFDvWGfOVr92KevyLoB7ijGz0=','Ema','Li',NULL,NULL,'V','1985-12-03',NULL,NULL),(38,'volunteer23@example.com','pbkdf2_sha256$720000$EOmu3yd8YbISsrZrmFRiwy$Id0ELO3cFw2MITGJrNHFDvWGfOVr92KevyLoB7ijGz0=','Daniel','Hal',NULL,NULL,'V','1992-08-22',NULL,NULL),(39,'volunteer24@example.com','pbkdf2_sha256$720000$EOmu3yd8YbISsrZrmFRiwy$Id0ELO3cFw2MITGJrNHFDvWGfOVr92KevyLoB7ijGz0=','Isabela','Alen',NULL,NULL,'V','1988-04-17',NULL,NULL),(40,'volunteer25@example.com','pbkdf2_sha256$720000$EOmu3yd8YbISsrZrmFRiwy$Id0ELO3cFw2MITGJrNHFDvWGfOVr92KevyLoB7ijGz0=','Josif','Jung',NULL,NULL,'V','1995-10-29',NULL,NULL),(41,'volunteer26@example.com','pbkdf2_sha256$720000$EOmu3yd8YbISsrZrmFRiwy$Id0ELO3cFw2MITGJrNHFDvWGfOVr92KevyLoB7ijGz0=','Luka','Petković',NULL,NULL,'V','1990-05-15',NULL,NULL),(42,'volunteer27@example.com','pbkdf2_sha256$720000$EOmu3yd8YbISsrZrmFRiwy$Id0ELO3cFw2MITGJrNHFDvWGfOVr92KevyLoB7ijGz0=','Nikola','Đorđević',NULL,NULL,'V','1985-12-03',NULL,NULL),(43,'volunteer28@example.com','pbkdf2_sha256$720000$EOmu3yd8YbISsrZrmFRiwy$Id0ELO3cFw2MITGJrNHFDvWGfOVr92KevyLoB7ijGz0=','Nikolina','Petrović',NULL,NULL,'V','1992-08-22',NULL,NULL),(44,'volunteer29@example.com','pbkdf2_sha256$720000$EOmu3yd8YbISsrZrmFRiwy$Id0ELO3cFw2MITGJrNHFDvWGfOVr92KevyLoB7ijGz0=','Stefan','Milanović',NULL,NULL,'V','1988-04-17',NULL,NULL),(45,'volunteer30@example.com','pbkdf2_sha256$720000$EOmu3yd8YbISsrZrmFRiwy$Id0ELO3cFw2MITGJrNHFDvWGfOVr92KevyLoB7ijGz0=','Ivana','Marić',NULL,NULL,'V','1995-10-29',NULL,NULL);
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
) ENGINE=InnoDB AUTO_INCREMENT=103 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lokacija`
--

LOCK TABLES `lokacija` WRITE;
/*!40000 ALTER TABLE `lokacija` DISABLE KEYS */;
INSERT INTO `lokacija` VALUES ('Srbija','Evropa',101),('Poljska','Evropa',102);
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
  `idObl` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`idObl`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oblast`
--

LOCK TABLES `oblast` WRITE;
/*!40000 ALTER TABLE `oblast` DISABLE KEYS */;
INSERT INTO `oblast` VALUES ('Ekologija',1),('Rad sa decom',2),('Rad sa osobama sa invaliditetom',3),('Reciklaza',4),('Veganstvo',5),('Umetnost',6),('Zdravstvo',7),('Kultura',8),('Rad sa zivotinjama',9),('Obrazovanje',10);
/*!40000 ALTER TABLE `oblast` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `poruka`
--

DROP TABLE IF EXISTS `poruka`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `poruka` (
  `idPor` int NOT NULL AUTO_INCREMENT,
  `idPre` int NOT NULL,
  `redBr` varchar(45) NOT NULL,
  `tekst` varchar(2000) NOT NULL,
  `time` timestamp NOT NULL,
  `status` char(1) NOT NULL,
  `idSender` int NOT NULL,
  PRIMARY KEY (`idPor`),
  KEY `FK_Prepiska_Poruka_idx` (`idPre`),
  CONSTRAINT `FK_Prepiska_Poruka` FOREIGN KEY (`idPre`) REFERENCES `prepiska` (`idPre`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1002 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `poruka`
--

LOCK TABLES `poruka` WRITE;
/*!40000 ALTER TABLE `poruka` DISABLE KEYS */;
INSERT INTO `poruka` VALUES (1001,101,'1','Korisnik Jovan je zapoceo prepisku','2024-06-12 13:21:48','U',16);
/*!40000 ALTER TABLE `poruka` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prepiska`
--

DROP TABLE IF EXISTS `prepiska`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prepiska` (
  `idPre` int NOT NULL AUTO_INCREMENT,
  `idKor1` int NOT NULL,
  `idKor2` int NOT NULL,
  PRIMARY KEY (`idPre`),
  KEY `FK_kor1_prepiska_idx` (`idKor1`),
  KEY `FK_kor2_prepiska_idx` (`idKor2`),
  CONSTRAINT `FK_kor1_prepiska` FOREIGN KEY (`idKor1`) REFERENCES `korisnik` (`idKor`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_kor2_prepiska` FOREIGN KEY (`idKor2`) REFERENCES `korisnik` (`idKor`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=102 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prepiska`
--

LOCK TABLES `prepiska` WRITE;
/*!40000 ALTER TABLE `prepiska` DISABLE KEYS */;
INSERT INTO `prepiska` VALUES (101,16,2);
/*!40000 ALTER TABLE `prepiska` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prijava`
--

DROP TABLE IF EXISTS `prijava`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prijava` (
  `idPri` int NOT NULL AUTO_INCREMENT,
  `idVol` int NOT NULL,
  `idAkt` int NOT NULL,
  `pismo` varchar(2000) NOT NULL,
  `rezime` mediumblob,
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
) ENGINE=InnoDB AUTO_INCREMENT=1035 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prijava`
--

LOCK TABLES `prijava` WRITE;
/*!40000 ALTER TABLE `prijava` DISABLE KEYS */;
INSERT INTO `prijava` VALUES (1025,16,878,'Volim da ulepsavam zivotnu sredinu za dobit svih nas',NULL,'A','P',NULL,'naucio sam dosta o zastiti divljih zivotinja i njihovoj koristi za prirodu',NULL),(1026,16,888,'Zelim da pomognem',NULL,'D','P',NULL,'organizacija ispostovala',NULL),(1027,16,909,'Obozavam zivotinje',NULL,'A','P',NULL,'odlicno je prosla kampanja',NULL),(1028,16,911,'Zelim da naucim vise o zastiti medveda',NULL,'A','P','P','odlicno','volonter dobar'),(1029,16,913,'Obozavam zivotinje i zelim da im pomognemo',NULL,'A',NULL,'N',NULL,'Volonter je anarhista i ne postuje zakon'),(1030,16,912,'Vatra je opasna sila majke prirode i moramo da ucestvujemo',NULL,'O',NULL,NULL,NULL,NULL),(1031,18,909,'macke ubijaju ptice :(',NULL,'A',NULL,NULL,NULL,NULL),(1032,30,909,'zelim da volontiram',NULL,'A',NULL,NULL,NULL,NULL),(1033,22,909,'prihvatite me',NULL,'A',NULL,NULL,NULL,NULL),(1034,20,909,'zelim da pomognem',NULL,'A','N',NULL,'neprijatnost',NULL);
/*!40000 ALTER TABLE `prijava` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pripada`
--

DROP TABLE IF EXISTS `pripada`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pripada` (
  `idPri` int NOT NULL AUTO_INCREMENT,
  `idObl` int NOT NULL,
  `idAkt` int NOT NULL,
  PRIMARY KEY (`idPri`),
  KEY `FK_Pripada_AKT_idx` (`idAkt`),
  KEY `FK_Pripada_Oblast_idx` (`idObl`),
  CONSTRAINT `FK_Pripada_AKT` FOREIGN KEY (`idAkt`) REFERENCES `aktivnost` (`idAkt`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_Pripada_Oblast` FOREIGN KEY (`idObl`) REFERENCES `oblast` (`idObl`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1008 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pripada`
--

LOCK TABLES `pripada` WRITE;
/*!40000 ALTER TABLE `pripada` DISABLE KEYS */;
INSERT INTO `pripada` VALUES (1002,8,909),(1003,9,909),(1004,1,910),(1005,8,910),(1006,9,910),(1007,9,911);
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
  `idVes` int NOT NULL AUTO_INCREMENT,
  `opis` varchar(256) NOT NULL,
  PRIMARY KEY (`idVes`),
  KEY `FK_aktivnostBrAkt_vestina_idx` (`idAkt`),
  CONSTRAINT `FK_akt_vestina` FOREIGN KEY (`idAkt`) REFERENCES `aktivnost` (`idAkt`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1007 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vestina`
--

LOCK TABLES `vestina` WRITE;
/*!40000 ALTER TABLE `vestina` DISABLE KEYS */;
INSERT INTO `vestina` VALUES (909,1002,''),(910,1003,''),(911,1004,'vozačka dozvola'),(912,1005,''),(913,1006,'');
/*!40000 ALTER TABLE `vestina` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zanima_ga`
--

DROP TABLE IF EXISTS `zanima_ga`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `zanima_ga` (
  `idZan` int NOT NULL AUTO_INCREMENT,
  `idObl` int NOT NULL,
  `idKor` int NOT NULL,
  PRIMARY KEY (`idZan`),
  KEY `FK_zanima_Kor_idx` (`idKor`),
  KEY `FK_zanima_obl_idx` (`idObl`),
  CONSTRAINT `FK_zanima_Kor` FOREIGN KEY (`idKor`) REFERENCES `korisnik` (`idKor`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_zanima_obl` FOREIGN KEY (`idObl`) REFERENCES `oblast` (`idObl`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1091 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zanima_ga`
--

LOCK TABLES `zanima_ga` WRITE;
/*!40000 ALTER TABLE `zanima_ga` DISABLE KEYS */;
INSERT INTO `zanima_ga` VALUES (1,1,16),(1001,2,16),(1002,3,16),(1003,7,16),(1004,2,17),(1005,4,17),(1006,9,17),(1007,1,18),(1008,5,18),(1009,10,18),(1010,3,19),(1011,6,19),(1012,8,19),(1013,2,20),(1014,5,20),(1015,7,20),(1016,1,21),(1017,4,21),(1018,8,21),(1019,2,22),(1020,6,22),(1021,9,22),(1022,3,23),(1023,7,23),(1024,10,23),(1025,4,24),(1026,5,24),(1027,8,24),(1028,1,25),(1029,3,25),(1030,7,25),(1031,2,26),(1032,4,26),(1033,9,26),(1034,1,27),(1035,5,27),(1036,10,27),(1037,3,28),(1038,6,28),(1039,8,28),(1040,2,29),(1041,5,29),(1042,7,29),(1043,1,30),(1044,4,30),(1045,8,30),(1046,2,31),(1047,6,31),(1048,9,31),(1049,3,32),(1050,7,32),(1051,10,32),(1052,4,33),(1053,5,33),(1054,8,33),(1055,1,34),(1056,3,34),(1057,7,34),(1058,2,35),(1059,4,35),(1060,9,35),(1061,1,36),(1062,5,36),(1063,10,36),(1064,3,37),(1065,6,37),(1066,8,37),(1067,2,38),(1068,5,38),(1069,7,38),(1070,1,39),(1071,4,39),(1072,8,39),(1073,2,40),(1074,6,40),(1075,9,40),(1076,3,41),(1077,7,41),(1078,10,41),(1079,4,42),(1080,5,42),(1081,8,42),(1082,1,43),(1083,3,43),(1084,7,43),(1085,2,44),(1086,4,44),(1087,9,44),(1088,1,45),(1089,5,45),(1090,10,45);
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

-- Dump completed on 2024-06-12 15:51:25
