-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: localhost    Database: movielist
-- ------------------------------------------------------
-- Server version	8.0.42

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
-- Table structure for table `moviedetails`
--

DROP TABLE IF EXISTS `moviedetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `moviedetails` (
  `movie_id` int NOT NULL AUTO_INCREMENT,
  `movie_name` varchar(100) NOT NULL,
  `movie_year` int NOT NULL,
  `movie_language` varchar(20) NOT NULL,
  `movie_genre` varchar(50) NOT NULL,
  `movie_rating` float NOT NULL,
  `movie_quality` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`movie_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1013 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `moviedetails`
--

LOCK TABLES `moviedetails` WRITE;
/*!40000 ALTER TABLE `moviedetails` DISABLE KEYS */;
INSERT INTO `moviedetails` VALUES (1,'The Dark Knight',2008,'English','Action/Crime',9,'720p'),(2,'Avengers: Infinity War',2018,'English','Action/Sci-fi',8.4,'1080p'),(3,'Avengers: Endgame',2019,'English','Action/Sci-fi',8.4,'720p'),(4,'Venom: The Last Dance',2024,'English','Action/Sci-fi',6,'1080p'),(5,'Inception',2010,'English','Action/Sci-f',8.8,'2160p'),(6,'Oppenheimer',2023,'English','Thriller/Biography/History',8.3,'1080p'),(7,'John Wick',2014,'English','Action/Thriller',7.5,'720p'),(8,'How to Train Your Dragon',2025,'English','Fantasy/Adventure',8,'720p'),(9,'Thor: Love and Thunder',2022,'English','Action/Adventure/Fantasy',6.2,'720p'),(10,'The Tomorrow War',2021,'English','Action/Adventure/Thriller',6.6,'480p');
/*!40000 ALTER TABLE `moviedetails` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-07-31  9:21:35
