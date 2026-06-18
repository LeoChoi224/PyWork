-- MySQL dump 10.13  Distrib 8.0.46, for Linux (aarch64)
--
-- Host: localhost    Database: db2604
-- ------------------------------------------------------
-- Server version	8.0.46

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;

/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Account`
--

DROP TABLE IF EXISTS `Account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Account` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '예금번호',
  `balance` bigint DEFAULT '0' COMMENT '잔고',
  `history` longtext COLLATE utf8mb4_unicode_ci COMMENT '입출금내역',
  `branch_name` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '지점명',
  PRIMARY KEY (`id`),
  KEY `FK_Branch_TO_Account` (`branch_name`),
  CONSTRAINT `FK_Branch_TO_Account` FOREIGN KEY (`branch_name`) REFERENCES `Branch` (`name`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='예금계좌';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Account`
--

LOCK TABLES `Account` WRITE;
/*!40000 ALTER TABLE `Account` DISABLE KEYS */;
/*!40000 ALTER TABLE `Account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Branch`
--

DROP TABLE IF EXISTS `Branch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Branch` (
  `name` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '지점명',
  `city` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '도시',
  `asset` bigint DEFAULT '0' COMMENT '자산',
  `engname` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '영문지점',
  `opendate` date NOT NULL COMMENT '지점개설일',
  `phone` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '전화번호',
  PRIMARY KEY (`name`),
  UNIQUE KEY `UQ_phone` (`phone`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='지점';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Branch`
--

LOCK TABLES `Branch` WRITE;
/*!40000 ALTER TABLE `Branch` DISABLE KEYS */;
/*!40000 ALTER TABLE `Branch` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Deposit`
--

DROP TABLE IF EXISTS `Deposit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Deposit` (
  `account_id` int NOT NULL COMMENT '예금번호',
  `member_id` int NOT NULL COMMENT '고객번호',
  `amount` bigint DEFAULT '0' COMMENT '금액',
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '예금일시',
  PRIMARY KEY (`account_id`,`member_id`),
  KEY `FK_Member_TO_Deposit` (`member_id`),
  CONSTRAINT `FK_Account_TO_Deposit` FOREIGN KEY (`account_id`) REFERENCES `Account` (`id`) ON DELETE CASCADE,
  CONSTRAINT `FK_Member_TO_Deposit` FOREIGN KEY (`member_id`) REFERENCES `Member` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='예금';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Deposit`
--

LOCK TABLES `Deposit` WRITE;
/*!40000 ALTER TABLE `Deposit` DISABLE KEYS */;
/*!40000 ALTER TABLE `Deposit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Member`
--

DROP TABLE IF EXISTS `Member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Member` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '고객번호',
  `name` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '이름',
  `address` tinytext COLLATE utf8mb4_unicode_ci COMMENT '주소',
  `birthdate` date DEFAULT NULL COMMENT '생년월일',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='고객';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Member`
--

LOCK TABLES `Member` WRITE;
/*!40000 ALTER TABLE `Member` DISABLE KEYS */;
/*!40000 ALTER TABLE `Member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TEST_DEPARTMENT`
--

DROP TABLE IF EXISTS `TEST_DEPARTMENT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `TEST_DEPARTMENT` (
  `dept_uid` int NOT NULL,
  `dept_name` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `dept_build` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`dept_uid`),
  CONSTRAINT `TEST_DEPARTMENT_chk_1` CHECK ((`dept_build` in (_utf8mb4'K301',_utf8mb4'A203',_utf8mb4'B306')))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TEST_DEPARTMENT`
--

LOCK TABLES `TEST_DEPARTMENT` WRITE;
/*!40000 ALTER TABLE `TEST_DEPARTMENT` DISABLE KEYS */;
INSERT INTO `TEST_DEPARTMENT` VALUES (1,'a과','K301'),(2,'b과','A203'),(3,'c과','B306');
/*!40000 ALTER TABLE `TEST_DEPARTMENT` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TEST_STUDENT`
--

DROP TABLE IF EXISTS `TEST_STUDENT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `TEST_STUDENT` (
  `stu_uid` int NOT NULL,
  `stu_name` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `stu_age` int DEFAULT NULL,
  `stu_grade` int DEFAULT NULL,
  `dept_uid` int DEFAULT NULL,
  PRIMARY KEY (`stu_uid`),
  KEY `dept_uid` (`dept_uid`),
  CONSTRAINT `TEST_STUDENT_ibfk_1` FOREIGN KEY (`dept_uid`) REFERENCES `TEST_DEPARTMENT` (`dept_uid`),
  CONSTRAINT `TEST_STUDENT_chk_1` CHECK ((`stu_age` >= 0)),
  CONSTRAINT `TEST_STUDENT_chk_2` CHECK ((`stu_grade` between 1 and 4))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TEST_STUDENT`
--

LOCK TABLES `TEST_STUDENT` WRITE;
/*!40000 ALTER TABLE `TEST_STUDENT` DISABLE KEYS */;
INSERT INTO `TEST_STUDENT` VALUES (1,'a학생',20,1,1),(2,'b학생',20,2,1),(3,'c학생',20,3,1),(4,'d학생',21,1,2),(5,'e학생',22,1,3);
/*!40000 ALTER TABLE `TEST_STUDENT` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `book`
--

DROP TABLE IF EXISTS `book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `author` varchar(50) NOT NULL,
  `price` int NOT NULL,
  `stock` int NOT NULL DEFAULT '0',
  `published_year` int NOT NULL,
  `regDate` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  CONSTRAINT `book_chk_1` CHECK ((`price` >= 0)),
  CONSTRAINT `book_chk_2` CHECK ((`published_year` between 1900 and 2026))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book`
--

LOCK TABLES `book` WRITE;
/*!40000 ALTER TABLE `book` DISABLE KEYS */;
/*!40000 ALTER TABLE `book` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exam_book`
--

DROP TABLE IF EXISTS `exam_book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `exam_book` (
  `id` int NOT NULL AUTO_INCREMENT,
  `no` varchar(5) DEFAULT NULL,
  `title` varchar(100) NOT NULL,
  `price` int DEFAULT '0',
  `publishedAt` date NOT NULL,
  `createdAt` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `no` (`no`),
  CONSTRAINT `exam_book_chk_1` CHECK ((`price` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exam_book`
--

LOCK TABLES `exam_book` WRITE;
/*!40000 ALTER TABLE `exam_book` DISABLE KEYS */;
INSERT INTO `exam_book` VALUES (1,'A1153','hongmook',999999,'2026-04-10','2026-04-30 08:09:00'),(5,'B2153','hongmook',999999,'2026-04-10','2026-04-30 08:09:11'),(6,'g2153','hongmook',999999,'2026-04-10','2026-04-30 08:09:14'),(7,'A1234','asdkalsd',1231230,'2012-10-10','2026-04-30 08:27:55');
/*!40000 ALTER TABLE `exam_book` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventory`
--

DROP TABLE IF EXISTS `inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventory` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(80) COLLATE utf8mb4_unicode_ci NOT NULL,
  `price` int NOT NULL,
  `stock` int DEFAULT '0',
  `regDate` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  CONSTRAINT `inventory_chk_1` CHECK ((`price` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory`
--

LOCK TABLES `inventory` WRITE;
/*!40000 ALTER TABLE `inventory` DISABLE KEYS */;
INSERT INTO `inventory` VALUES (1,'가나다',5000,50,'2026-04-29 07:39:52'),(4,'최홍묵',1000000000,1,'2026-04-29 08:28:11'),(5,'가즈아',999,50,'2026-04-29 22:30:04'),(6,'abcde',12345,0,'2026-04-29 21:42:39'),(7,'이번엔 0 가자',10000,0,'2026-04-29 21:49:00'),(10,'이거 어도',90,10,'2026-04-29 23:12:37');
/*!40000 ALTER TABLE `inventory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `musicchart`
--

DROP TABLE IF EXISTS `musicchart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `musicchart` (
  `id` int NOT NULL AUTO_INCREMENT,
  `site` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `ranking` int NOT NULL,
  `title` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `artist` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `crawl_at` datetime NOT NULL DEFAULT (now()),
  PRIMARY KEY (`id`),
  CONSTRAINT `musicchart_chk_1` CHECK ((`ranking` >= 1))
) ENGINE=InnoDB AUTO_INCREMENT=1201 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `musicchart`
--

LOCK TABLES `musicchart` WRITE;
/*!40000 ALTER TABLE `musicchart` DISABLE KEYS */;
INSERT INTO `musicchart` VALUES (1,'벅스',1,'갑자기','아이오아이(I.O.I)','2026-06-05 02:42:01'),(2,'벅스',2,'LEMONADE','aespa','2026-06-05 02:42:01'),(3,'벅스',3,'REDRED','CORTIS (코르티스)','2026-06-05 02:42:01'),(4,'벅스',4,'It′s Me','아일릿(ILLIT)','2026-06-05 02:42:01'),(5,'벅스',5,'WDA (Whole Different Animal) (Feat. G-DRAGON)','aespa','2026-06-05 02:42:01'),(6,'벅스',6,'LOVE ATTACK','RESCENE (리센느)','2026-06-05 02:42:01'),(7,'벅스',7,'소문의 낙원','AKMU(악뮤)','2026-06-05 02:42:01'),(8,'벅스',8,'Heavy Serenade','NMIXX','2026-06-05 02:42:01'),(9,'벅스',9,'기쁨, 슬픔, 아름다운 마음','AKMU(악뮤)','2026-06-05 02:42:01'),(10,'벅스',10,'0+0','한로로','2026-06-05 02:42:01'),(11,'벅스',11,'사랑하게 될 거야','한로로','2026-06-05 02:42:01'),(12,'벅스',12,'Drowning','WOODZ','2026-06-05 02:42:01'),(13,'벅스',13,'캐치 캐치','YENA (최예나)','2026-06-05 02:42:01'),(14,'벅스',14,'BOOMPALA','LE SSERAFIM (르세라핌)','2026-06-05 02:42:01'),(15,'벅스',15,'RUDE!','Hearts2Hearts (하츠투하츠)','2026-06-05 02:42:01'),(16,'벅스',16,'404 (New Era)','KiiiKiii (키키)','2026-06-05 02:42:01'),(17,'벅스',17,'Popcorn','도경수(D.O.)','2026-06-05 02:42:01'),(18,'벅스',18,'Good Goodbye','화사 (HWASA)','2026-06-05 02:42:01'),(19,'벅스',19,'입춘','한로로','2026-06-05 02:42:01'),(20,'벅스',20,'Baby Flower','tripleS (트리플에스)','2026-06-05 02:42:01'),(21,'벅스',21,'BANG BANG','IVE (아이브)','2026-06-05 02:42:01'),(22,'벅스',22,'4 Flowers','마마무(Mamamoo)','2026-06-05 02:42:01'),(23,'벅스',23,'모르시나요(PROD.로코베리)','조째즈','2026-06-05 02:42:01'),(24,'벅스',24,'한 페이지가 될 수 있게','DAY6 (데이식스)','2026-06-05 02:42:01'),(25,'벅스',25,'Flashback','엔플라잉(N.Flying)','2026-06-05 02:42:01'),(26,'벅스',26,'LIVE FAST DIE SLOW','태양','2026-06-05 02:42:01'),(27,'벅스',27,'너에게 닿기를','10CM','2026-06-05 02:42:01'),(28,'벅스',28,'멸종위기사랑','이찬혁','2026-06-05 02:42:01'),(29,'벅스',29,'천상연','이창섭','2026-06-05 02:42:01'),(30,'벅스',30,'Who is she','KISS OF LIFE','2026-06-05 02:42:01'),(31,'벅스',31,'나의 하루처럼','성시경','2026-06-05 02:42:01'),(32,'벅스',32,'BUMPA','비비(BIBI)','2026-06-05 02:42:01'),(33,'벅스',33,'소나기','이클립스 (ECLIPSE)','2026-06-05 02:42:01'),(34,'벅스',34,'THAT’S A NO NO','ITZY (있지)','2026-06-05 02:42:01'),(35,'벅스',35,'주저하는 연인들을 위해','잔나비','2026-06-05 02:42:01'),(36,'벅스',36,'별이 될게','황치열','2026-06-05 02:42:01'),(37,'벅스',37,'OVERDRIVE','TWS (투어스)','2026-06-05 02:42:01'),(38,'벅스',38,'청춘만화','이무진','2026-06-05 02:42:01'),(39,'벅스',39,'So Cute','화사 (HWASA)','2026-06-05 02:42:01'),(40,'벅스',40,'타임캡슐','다비치','2026-06-05 02:42:01'),(41,'벅스',41,'like JENNIE','제니 (JENNIE)','2026-06-05 02:42:01'),(42,'벅스',42,'toxic till the end','로제(ROSÉ)','2026-06-05 02:42:01'),(43,'벅스',43,'첫 만남은 계획대로 되지 않아','TWS (투어스)','2026-06-05 02:42:01'),(44,'벅스',44,'BLACKHOLE','IVE (아이브)','2026-06-05 02:42:01'),(45,'벅스',45,'춤 (CHOOM)','BABYMONSTER','2026-06-05 02:42:01'),(46,'벅스',46,'Blue Valentine','NMIXX','2026-06-05 02:42:01'),(47,'벅스',47,'I AM','IVE (아이브)','2026-06-05 02:42:01'),(48,'벅스',48,'HAPPY','DAY6 (데이식스)','2026-06-05 02:42:01'),(49,'벅스',49,'NOT CUTE ANYMORE','아일릿(ILLIT)','2026-06-05 02:42:01'),(50,'벅스',50,'Whiplash','aespa','2026-06-05 02:42:01'),(51,'벅스',51,'Hype Boy','NewJeans','2026-06-05 02:42:01'),(52,'벅스',52,'봄 색깔','AKMU(악뮤)','2026-06-05 02:42:01'),(53,'벅스',53,'달리 표현할 수 없어요','로이킴','2026-06-05 02:42:01'),(54,'벅스',54,'Golden','HUNTR/X','2026-06-05 02:42:01'),(55,'벅스',55,'FAMOUS','ALLDAY PROJECT','2026-06-05 02:42:01'),(56,'벅스',56,'Supernova','aespa','2026-06-05 02:42:01'),(57,'벅스',57,'봄 내음보다 너를','김나영','2026-06-05 02:42:01'),(58,'벅스',58,'뛰어(JUMP)','BLACKPINK','2026-06-05 02:42:01'),(59,'벅스',59,'내게 사랑이 뭐냐고 물어본다면','로이킴','2026-06-05 02:42:01'),(60,'벅스',60,'FOCUS','Hearts2Hearts (하츠투하츠)','2026-06-05 02:42:01'),(61,'벅스',61,'사랑은 봄비처럼... 이별은 겨울비처럼','임현정','2026-06-05 02:42:01'),(62,'벅스',62,'에피소드','이무진','2026-06-05 02:42:01'),(63,'벅스',63,'Body to Body','방탄소년단','2026-06-05 02:42:01'),(64,'벅스',64,'SPAGHETTI (feat. j-hope of BTS)','LE SSERAFIM (르세라핌)','2026-06-05 02:42:01'),(65,'벅스',65,'APT.','로제(ROSÉ)','2026-06-05 02:42:01'),(66,'벅스',66,'모든 날, 모든 순간 (Every day, Every Moment)','폴킴(Paul Kim)','2026-06-05 02:42:01'),(67,'벅스',67,'띠로리 (DDI RO RI)','MEOVV (미야오)','2026-06-05 02:42:01'),(68,'벅스',68,'REBEL HEART','IVE (아이브)','2026-06-05 02:42:01'),(69,'벅스',69,'Love wins all','아이유(IU)','2026-06-05 02:42:01'),(70,'벅스',70,'Love me or Leave me','DAY6 (데이식스)','2026-06-05 02:42:01'),(71,'벅스',71,'어떻게 이별까지 사랑하겠어, 널 사랑하는 거지','AKMU(악뮤)','2026-06-05 02:42:01'),(72,'벅스',72,'SWIM','방탄소년단','2026-06-05 02:42:01'),(73,'벅스',73,'Die With A Smile','Lady Gaga(레이디 가가)','2026-06-05 02:42:01'),(74,'벅스',74,'햇빛 bless you','AKMU(악뮤)','2026-06-05 02:42:01'),(75,'벅스',75,'Welcome to the Show','DAY6 (데이식스)','2026-06-05 02:42:01'),(76,'벅스',76,'Congratulations','DAY6 (데이식스)','2026-06-05 02:42:01'),(77,'벅스',77,'고민중독','QWER','2026-06-05 02:42:01'),(78,'벅스',78,'Flower','오반(OVAN)','2026-06-05 02:42:01'),(79,'벅스',79,'하루에 하루만 더 (Stick With You)','투모로우바이투게더','2026-06-05 02:42:01'),(80,'벅스',80,'HOME SWEET HOME (feat. 태양, 대성)','G-DRAGON','2026-06-05 02:42:01'),(81,'벅스',81,'Ditto','NewJeans','2026-06-05 02:42:01'),(82,'벅스',82,'나는 반딧불','황가람','2026-06-05 02:42:01'),(83,'벅스',83,'그대만 있다면 (여름날 우리 X 너드커넥션 (Nerd Connection))','너드커넥션(Nerd Connection)','2026-06-05 02:42:01'),(84,'벅스',84,'Smile Boy','로이킴','2026-06-05 02:42:01'),(85,'벅스',85,'Soda Pop','Saja Boys','2026-06-05 02:42:01'),(86,'벅스',86,'Magnetic','아일릿(ILLIT)','2026-06-05 02:42:01'),(87,'벅스',87,'STYLE','Hearts2Hearts (하츠투하츠)','2026-06-05 02:42:01'),(88,'벅스',88,'시작의 아이 ❍','박다혜','2026-06-05 02:42:01'),(89,'벅스',89,'ONE MORE TIME','ALLDAY PROJECT','2026-06-05 02:42:01'),(90,'벅스',90,'I DO ME','KiiiKiii (키키)','2026-06-05 02:42:01'),(91,'벅스',91,'벌레를 내고','AKMU(악뮤)','2026-06-05 02:42:01'),(92,'벅스',92,'그대 작은 나의 세상이 되어','카더가든','2026-06-05 02:42:01'),(93,'벅스',93,'Atmos','SHINee (샤이니)','2026-06-05 02:42:01'),(94,'벅스',94,'마치 오늘처럼','정승환','2026-06-05 02:42:01'),(95,'벅스',95,'IF I','TREASURE(트레저)','2026-06-05 02:42:01'),(96,'벅스',96,'GO','BLACKPINK','2026-06-05 02:42:01'),(97,'벅스',97,'오늘만 I LOVE YOU','BOYNEXTDOOR','2026-06-05 02:42:01'),(98,'벅스',98,'XOXZ','IVE (아이브)','2026-06-05 02:42:01'),(99,'벅스',99,'나는 아픈 건 딱 질색이니까','i-dle (아이들)','2026-06-05 02:42:01'),(100,'벅스',100,'사랑인가 봐','멜로망스(MeloMance)','2026-06-05 02:42:01'),(101,'멜론',1,'갑자기','아이오아이 (I.O.I)','2026-06-05 02:42:01'),(102,'멜론',2,'REDRED','CORTIS (코르티스)','2026-06-05 02:42:01'),(103,'멜론',3,'It′s Me','아일릿(ILLIT)','2026-06-05 02:42:01'),(104,'멜론',4,'소문의 낙원','AKMU (악뮤)','2026-06-05 02:42:01'),(105,'멜론',5,'LEMONADE','aespa','2026-06-05 02:42:01'),(106,'멜론',6,'기쁨, 슬픔, 아름다운 마음','AKMU (악뮤)','2026-06-05 02:42:01'),(107,'멜론',7,'캐치 캐치','YENA (최예나)','2026-06-05 02:42:01'),(108,'멜론',8,'RUDE!','Hearts2Hearts (하츠투하츠)','2026-06-05 02:42:01'),(109,'멜론',9,'사랑하게 될 거야','한로로','2026-06-05 02:42:01'),(110,'멜론',10,'Heavy Serenade','NMIXX','2026-06-05 02:42:01'),(111,'멜론',11,'Drowning','WOODZ','2026-06-05 02:42:01'),(112,'멜론',12,'WDA (Whole Different Animal) (Feat. G-DRAGON)','aespa','2026-06-05 02:42:01'),(113,'멜론',13,'0+0','한로로','2026-06-05 02:42:01'),(114,'멜론',14,'404 (New Era)','KiiiKiii (키키)','2026-06-05 02:42:01'),(115,'멜론',15,'BANG BANG','IVE (아이브)','2026-06-05 02:42:01'),(116,'멜론',16,'Good Goodbye','화사 (HWASA)','2026-06-05 02:42:01'),(117,'멜론',17,'SWIM','방탄소년단','2026-06-05 02:42:01'),(118,'멜론',18,'LOVE ATTACK','RESCENE (리센느)','2026-06-05 02:42:01'),(119,'멜론',19,'타임캡슐','다비치','2026-06-05 02:42:01'),(120,'멜론',20,'Popcorn','도경수(D.O.)','2026-06-05 02:42:01'),(121,'멜론',21,'너에게 닿기를','10CM','2026-06-05 02:42:01'),(122,'멜론',22,'Blue Valentine','NMIXX','2026-06-05 02:42:01'),(123,'멜론',23,'멸종위기사랑','이찬혁','2026-06-05 02:42:01'),(124,'멜론',24,'어떻게 이별까지 사랑하겠어, 널 사랑하는 거지','AKMU (악뮤)','2026-06-05 02:42:01'),(125,'멜론',25,'Body to Body','방탄소년단','2026-06-05 02:42:01'),(126,'멜론',26,'어제보다 슬픈 오늘','우디 (Woody)','2026-06-05 02:42:01'),(127,'멜론',27,'뛰어(JUMP)','BLACKPINK','2026-06-05 02:42:01'),(128,'멜론',28,'너의 모든 순간','성시경','2026-06-05 02:42:01'),(129,'멜론',29,'그대 작은 나의 세상이 되어','카더가든','2026-06-05 02:42:01'),(130,'멜론',30,'Golden','HUNTR/X','2026-06-05 02:42:01'),(131,'멜론',31,'소나기','이클립스 (ECLIPSE)','2026-06-05 02:42:01'),(132,'멜론',32,'BOOMPALA','LE SSERAFIM (르세라핌)','2026-06-05 02:42:01'),(133,'멜론',33,'모르시나요(PROD.로코베리)','조째즈','2026-06-05 02:42:01'),(134,'멜론',34,'내게 사랑이 뭐냐고 물어본다면','로이킴','2026-06-05 02:42:01'),(135,'멜론',35,'toxic till the end','로제 (ROSÉ)','2026-06-05 02:42:01'),(136,'멜론',36,'Whiplash','aespa','2026-06-05 02:42:01'),(137,'멜론',37,'천상연','이창섭','2026-06-05 02:42:01'),(138,'멜론',38,'HOME SWEET HOME (feat. 태양, 대성)','G-DRAGON','2026-06-05 02:42:01'),(139,'멜론',39,'청춘만화','이무진','2026-06-05 02:42:01'),(140,'멜론',40,'한 페이지가 될 수 있게','DAY6 (데이식스)','2026-06-05 02:42:01'),(141,'멜론',41,'2.0','방탄소년단','2026-06-05 02:42:01'),(142,'멜론',42,'HAPPY','DAY6 (데이식스)','2026-06-05 02:42:01'),(143,'멜론',43,'그대만 있다면 (여름날 우리 X 너드커넥션 (Nerd Connection))','너드커넥션 (Nerd Connection)','2026-06-05 02:42:01'),(144,'멜론',44,'봄날','방탄소년단','2026-06-05 02:42:01'),(145,'멜론',45,'like JENNIE','제니 (JENNIE)','2026-06-05 02:42:01'),(146,'멜론',46,'Seven (feat. Latto) - Clean Ver.','정국','2026-06-05 02:42:01'),(147,'멜론',47,'Hooligan','방탄소년단','2026-06-05 02:42:01'),(148,'멜론',48,'BLACKHOLE','IVE (아이브)','2026-06-05 02:42:01'),(149,'멜론',49,'사랑은 늘 도망가','임영웅','2026-06-05 02:42:01'),(150,'멜론',50,'입춘','한로로','2026-06-05 02:42:01'),(151,'멜론',51,'모든 날, 모든 순간 (Every day, Every Moment)','폴킴','2026-06-05 02:42:01'),(152,'멜론',52,'사랑인가 봐','멜로망스','2026-06-05 02:42:01'),(153,'멜론',53,'주저하는 연인들을 위해','잔나비','2026-06-05 02:42:01'),(154,'멜론',54,'SPAGHETTI (feat. j-hope of BTS)','LE SSERAFIM (르세라핌)','2026-06-05 02:42:01'),(155,'멜론',55,'예뻤어','DAY6 (데이식스)','2026-06-05 02:42:01'),(156,'멜론',56,'나는 반딧불','황가람','2026-06-05 02:42:01'),(157,'멜론',57,'오늘만 I LOVE YOU','BOYNEXTDOOR','2026-06-05 02:42:01'),(158,'멜론',58,'청혼하지 않을 이유를 못 찾았어','이무진','2026-06-05 02:42:01'),(159,'멜론',59,'FAMOUS','ALLDAY PROJECT','2026-06-05 02:42:01'),(160,'멜론',60,'STYLE','Hearts2Hearts (하츠투하츠)','2026-06-05 02:42:01'),(161,'멜론',61,'사랑은 봄비처럼...이별은 겨울비처럼...','임현정','2026-06-05 02:42:01'),(162,'멜론',62,'눈을 감아도(2026)','순순희(지환)','2026-06-05 02:42:01'),(163,'멜론',63,'Love Love Love (Feat. Yoong Jin Of Casker)','에픽하이 (EPIK HIGH)','2026-06-05 02:42:01'),(164,'멜론',64,'Welcome to the Show','DAY6 (데이식스)','2026-06-05 02:42:01'),(165,'멜론',65,'APT.','로제 (ROSÉ)','2026-06-05 02:42:01'),(166,'멜론',66,'첫 만남은 계획대로 되지 않아','TWS (투어스)','2026-06-05 02:42:01'),(167,'멜론',67,'LIVE FAST DIE SLOW','태양','2026-06-05 02:42:01'),(168,'멜론',68,'FYA','방탄소년단','2026-06-05 02:42:01'),(169,'멜론',69,'TICK TOCK (Feat. ZICO) (Prod. by ZICO, Crush)','김하온 (HAON)','2026-06-05 02:42:01'),(170,'멜론',70,'Dynamite','방탄소년단','2026-06-05 02:42:01'),(171,'멜론',71,'달리 표현할 수 없어요','로이킴','2026-06-05 02:42:01'),(172,'멜론',72,'봄 내음보다 너를','김나영','2026-06-05 02:42:01'),(173,'멜론',73,'REBEL HEART','IVE (아이브)','2026-06-05 02:42:01'),(174,'멜론',74,'시작의 아이 ❍','박다혜','2026-06-05 02:42:01'),(175,'멜론',75,'다정히 내 이름을 부르면','경서예지','2026-06-05 02:42:01'),(176,'멜론',76,'Flower','오반(OVAN)','2026-06-05 02:42:01'),(177,'멜론',77,'ONE MORE TIME','ALLDAY PROJECT','2026-06-05 02:42:01'),(178,'멜론',78,'Like Animals','방탄소년단','2026-06-05 02:42:01'),(179,'멜론',79,'Aliens','방탄소년단','2026-06-05 02:42:01'),(180,'멜론',80,'Love wins all','아이유','2026-06-05 02:42:01'),(181,'멜론',81,'헤어지자 말해요','박재정','2026-06-05 02:42:01'),(182,'멜론',82,'OVERDRIVE','TWS (투어스)','2026-06-05 02:42:01'),(183,'멜론',83,'이 밤을 빌려 말해요','PLAVE','2026-06-05 02:42:01'),(184,'멜론',84,'Die With A Smile','Lady Gaga','2026-06-05 02:42:01'),(185,'멜론',85,'FOCUS','Hearts2Hearts (하츠투하츠)','2026-06-05 02:42:01'),(186,'멜론',86,'Magnetic','아일릿(ILLIT)','2026-06-05 02:42:01'),(187,'멜론',87,'KISS KISS KISS (Feat. 선우 (THE BOYZ)) (Prod. by Hukky Shibaseki)','NOWIMYOUNG (나우아임영)','2026-06-05 02:42:01'),(188,'멜론',88,'Merry Go Round','방탄소년단','2026-06-05 02:42:01'),(189,'멜론',89,'에피소드','이무진','2026-06-05 02:42:01'),(190,'멜론',90,'Hype Boy','NewJeans','2026-06-05 02:42:01'),(191,'멜론',91,'순간을 영원처럼','임영웅','2026-06-05 02:42:01'),(192,'멜론',92,'One More Night','방탄소년단','2026-06-05 02:42:01'),(193,'멜론',93,'Flashback','엔플라잉 (N.Flying)','2026-06-05 02:42:01'),(194,'멜론',94,'Never Ending Story','아이유','2026-06-05 02:42:01'),(195,'멜론',95,'하루에 하루만 더 (Stick With You)','투모로우바이투게더','2026-06-05 02:42:01'),(196,'멜론',96,'NOT CUTE ANYMORE','아일릿(ILLIT)','2026-06-05 02:42:01'),(197,'멜론',97,'I AM','IVE (아이브)','2026-06-05 02:42:01'),(198,'멜론',98,'우리들의 블루스','임영웅','2026-06-05 02:42:01'),(199,'멜론',99,'Soda Pop','KPop Demon Hunters Cast','2026-06-05 02:42:01'),(200,'멜론',100,'Smile Boy','로이킴','2026-06-05 02:42:01'),(201,'지니',1,'갑자기','아이오아이 (I.O.I)','2026-06-05 02:42:01'),(202,'지니',2,'It\'s Me','아일릿(ILLIT)','2026-06-05 02:42:01'),(203,'지니',3,'소문의 낙원','AKMU (악뮤)','2026-06-05 02:42:01'),(204,'지니',4,'REDRED','CORTIS (코르티스)','2026-06-05 02:42:01'),(205,'지니',5,'캐치 캐치','YENA (최예나)','2026-06-05 02:42:01'),(206,'지니',6,'기쁨, 슬픔, 아름다운 마음','AKMU (악뮤)','2026-06-05 02:42:01'),(207,'지니',7,'Drowning','WOODZ','2026-06-05 02:42:01'),(208,'지니',8,'사랑하게 될 거야','한로로','2026-06-05 02:42:01'),(209,'지니',9,'0＋0','한로로','2026-06-05 02:42:01'),(210,'지니',10,'BANG BANG','IVE (아이브)','2026-06-05 02:42:01'),(211,'지니',11,'Good Goodbye','화사 (HWASA)','2026-06-05 02:42:01'),(212,'지니',12,'404 (New Era)','KiiiKiii (키키)','2026-06-05 02:42:01'),(213,'지니',13,'Popcorn','도경수 (D.O.)','2026-06-05 02:42:01'),(214,'지니',14,'타임캡슐','다비치','2026-06-05 02:42:01'),(215,'지니',15,'RUDE!','Hearts2Hearts (하츠투하츠)','2026-06-05 02:42:01'),(216,'지니',16,'멸종위기사랑','이찬혁','2026-06-05 02:42:01'),(217,'지니',17,'LEMONADE','aespa','2026-06-05 02:42:01'),(218,'지니',18,'너에게 닿기를','10CM','2026-06-05 02:42:01'),(219,'지니',19,'WDA (Whole Different Animal) (Feat. G-DRAGON)','aespa','2026-06-05 02:42:01'),(220,'지니',20,'뛰어(JUMP)','BLACKPINK','2026-06-05 02:42:01'),(221,'지니',21,'내게 사랑이 뭐냐고 물어본다면','로이킴','2026-06-05 02:42:01'),(222,'지니',22,'Golden','HUNTR/X & EJAE & Audrey Nuna & REI AMI & KPop Demon Hunters Cast','2026-06-05 02:42:01'),(223,'지니',23,'Blue Valentine','NMIXX','2026-06-05 02:42:01'),(224,'지니',24,'모르시나요 (Prod. by 로코베리)','조째즈','2026-06-05 02:42:01'),(225,'지니',25,'어제보다 슬픈 오늘','우디 (Woody)','2026-06-05 02:42:01'),(226,'지니',26,'청춘만화','이무진','2026-06-05 02:42:01'),(227,'지니',27,'입춘','한로로','2026-06-05 02:42:01'),(228,'지니',28,'사랑은 늘 도망가','임영웅','2026-06-05 02:42:01'),(229,'지니',29,'Heavy Serenade','NMIXX','2026-06-05 02:42:01'),(230,'지니',30,'어떻게 이별까지 사랑하겠어, 널 사랑하는 거지','AKMU (악뮤)','2026-06-05 02:42:01'),(231,'지니',31,'봄 내음보다 너를','김나영','2026-06-05 02:42:01'),(232,'지니',32,'toxic till the end','로제 (ROSÉ)','2026-06-05 02:42:01'),(233,'지니',33,'HAPPY','DAY6 (데이식스)','2026-06-05 02:42:01'),(234,'지니',34,'다시 만날 수 있을까','임영웅','2026-06-05 02:42:01'),(235,'지니',35,'우리들의 블루스','임영웅','2026-06-05 02:42:01'),(236,'지니',36,'그대 작은 나의 세상이 되어','카더가든','2026-06-05 02:42:01'),(237,'지니',37,'시작의 아이','마크툽 (Maktub)','2026-06-05 02:42:01'),(238,'지니',38,'Whiplash','aespa','2026-06-05 02:42:01'),(239,'지니',39,'순간을 영원처럼','임영웅','2026-06-05 02:42:01'),(240,'지니',40,'소나기','이클립스 (ECLIPSE)','2026-06-05 02:42:01'),(241,'지니',41,'한 페이지가 될 수 있게','DAY6 (데이식스)','2026-06-05 02:42:01'),(242,'지니',42,'나는 반딧불','황가람','2026-06-05 02:42:01'),(243,'지니',43,'LOVE ATTACK','RESCENE (리센느)','2026-06-05 02:42:01'),(244,'지니',44,'너의 모든 순간','성시경','2026-06-05 02:42:01'),(245,'지니',45,'돌아보지 마세요','임영웅','2026-06-05 02:42:01'),(246,'지니',46,'HOME SWEET HOME (Feat. 태양 & 대성)','G-DRAGON','2026-06-05 02:42:01'),(247,'지니',47,'그댈 위한 멜로디','임영웅','2026-06-05 02:42:01'),(248,'지니',48,'천국보다 아름다운','임영웅','2026-06-05 02:42:01'),(249,'지니',49,'답장을 보낸지','임영웅','2026-06-05 02:42:01'),(250,'지니',50,'우리에게 안녕','임영웅','2026-06-05 02:42:01'),(251,'지니',51,'들꽃이 될게요','임영웅','2026-06-05 02:42:01'),(252,'지니',52,'Pretender','OFFICIAL HIGE DANDISM','2026-06-05 02:42:01'),(253,'지니',53,'SWIM','방탄소년단','2026-06-05 02:42:01'),(254,'지니',54,'비가 와서','임영웅','2026-06-05 02:42:01'),(255,'지니',55,'like JENNIE','제니 (JENNIE)','2026-06-05 02:42:01'),(256,'지니',56,'ULSSIGU','임영웅','2026-06-05 02:42:01'),(257,'지니',57,'알겠어요 미안해요','임영웅','2026-06-05 02:42:01'),(258,'지니',58,'Wonderful Life','임영웅','2026-06-05 02:42:01'),(259,'지니',59,'나는야 HERO','임영웅','2026-06-05 02:42:01'),(260,'지니',60,'천상연','이창섭','2026-06-05 02:42:01'),(261,'지니',61,'달리 표현할 수 없어요','로이킴','2026-06-05 02:42:01'),(262,'지니',62,'Welcome to the Show','DAY6 (데이식스)','2026-06-05 02:42:01'),(263,'지니',63,'예뻤어','DAY6 (데이식스)','2026-06-05 02:42:01'),(264,'지니',64,'사건의 지평선','윤하 (YOUNHA)','2026-06-05 02:42:01'),(265,'지니',65,'벌써 일년','브라운 아이즈','2026-06-05 02:42:01'),(266,'지니',66,'APT.','로제 (ROSÉ) & Bruno Mars','2026-06-05 02:42:01'),(267,'지니',67,'에피소드','이무진','2026-06-05 02:42:01'),(268,'지니',68,'주저하는 연인들을 위해','잔나비','2026-06-05 02:42:01'),(269,'지니',69,'REBEL HEART','IVE (아이브)','2026-06-05 02:42:01'),(270,'지니',70,'Cruel Summer','Taylor Swift','2026-06-05 02:42:01'),(271,'지니',71,'Soda Pop','Saja Boys & Andrew Choi & Neckwav & Danny Chung & Kevin Woo & samUIL Lee & KPop Demon Hunters Cast','2026-06-05 02:42:01'),(272,'지니',72,'사랑인가 봐','멜로망스 (MeloMance)','2026-06-05 02:42:01'),(273,'지니',73,'눈을 감아도(2026)','순순희 (지환)','2026-06-05 02:42:01'),(274,'지니',74,'TICK TOCK (Feat. ZICO) (Prod. by ZICO, Crush)','김하온 (HAON) & Nosun & Raf Sandou & Marv & 정준혁','2026-06-05 02:42:01'),(275,'지니',75,'고민중독','QWER','2026-06-05 02:42:01'),(276,'지니',76,'MY LOVE (2025)','이예은 & 아샤트리 & 전건호','2026-06-05 02:42:01'),(277,'지니',77,'슬픈 초대장','순순희 (지환)','2026-06-05 02:42:01'),(278,'지니',78,'BLACKHOLE','IVE (아이브)','2026-06-05 02:42:01'),(279,'지니',79,'Die With A Smile','Lady Gaga & Bruno Mars','2026-06-05 02:42:01'),(280,'지니',80,'Flashback','엔플라잉 (N.Flying)','2026-06-05 02:42:01'),(281,'지니',81,'FAMOUS','ALLDAY PROJECT','2026-06-05 02:42:01'),(282,'지니',82,'BOOMPALA','LE SSERAFIM (르세라핌)','2026-06-05 02:42:01'),(283,'지니',83,'모든 날, 모든 순간 (Every day, Every Moment)','폴킴','2026-06-05 02:42:01'),(284,'지니',84,'시작의 아이 ❍','박다혜 & 마크툽 (Maktub)','2026-06-05 02:42:01'),(285,'지니',85,'떠나가요, 떠나지마요 : 시대를 초월한 마음','순순희 (기태) & 백예슬','2026-06-05 02:42:01'),(286,'지니',86,'Stay','The Kid LAROI & Justin Bieber','2026-06-05 02:42:01'),(287,'지니',87,'LIVE FAST DIE SLOW','태양','2026-06-05 02:42:01'),(288,'지니',88,'가까운 듯 먼 그대여','카더가든','2026-06-05 02:42:01'),(289,'지니',89,'그래 늦지 않았어 (2025)','아샤트리 & 이예은 & 전건호','2026-06-05 02:42:01'),(290,'지니',90,'Love Love Love (Feat. Yoong Jin of Casker))','에픽하이 (EPIK HIGH)','2026-06-05 02:42:01'),(291,'지니',91,'Body to Body','방탄소년단','2026-06-05 02:42:01'),(292,'지니',92,'첫 만남은 계획대로 되지 않아','TWS (투어스)','2026-06-05 02:42:01'),(293,'지니',93,'그대만 있다면 (여름날 우리 X 너드커넥션 (Nerd Connection))','너드커넥션 (Nerd Connection)','2026-06-05 02:42:01'),(294,'지니',94,'희재','성시경','2026-06-05 02:42:01'),(295,'지니',95,'다정히 내 이름을 부르면','경서예지 & 전건호','2026-06-05 02:42:01'),(296,'지니',96,'청혼하지 않을 이유를 못 찾았어','이무진','2026-06-05 02:42:01'),(297,'지니',97,'TOO BAD (Feat. Anderson .Paak)','G-DRAGON','2026-06-05 02:42:01'),(298,'지니',98,'비의 랩소디','임재현','2026-06-05 02:42:01'),(299,'지니',99,'내 이름 맑음','QWER','2026-06-05 02:42:01'),(300,'지니',100,'사막에서 꽃을 피우듯','우디 (Woody)','2026-06-05 02:42:01'),(301,'벅스',1,'갑자기','아이오아이(I.O.I)','2026-06-05 02:43:39'),(302,'벅스',2,'LEMONADE','aespa','2026-06-05 02:43:39'),(303,'벅스',3,'REDRED','CORTIS (코르티스)','2026-06-05 02:43:39'),(304,'벅스',4,'It′s Me','아일릿(ILLIT)','2026-06-05 02:43:39'),(305,'벅스',5,'WDA (Whole Different Animal) (Feat. G-DRAGON)','aespa','2026-06-05 02:43:39'),(306,'벅스',6,'LOVE ATTACK','RESCENE (리센느)','2026-06-05 02:43:39'),(307,'벅스',7,'소문의 낙원','AKMU(악뮤)','2026-06-05 02:43:39'),(308,'벅스',8,'Heavy Serenade','NMIXX','2026-06-05 02:43:39'),(309,'벅스',9,'기쁨, 슬픔, 아름다운 마음','AKMU(악뮤)','2026-06-05 02:43:39'),(310,'벅스',10,'0+0','한로로','2026-06-05 02:43:39'),(311,'벅스',11,'사랑하게 될 거야','한로로','2026-06-05 02:43:39'),(312,'벅스',12,'Drowning','WOODZ','2026-06-05 02:43:39'),(313,'벅스',13,'캐치 캐치','YENA (최예나)','2026-06-05 02:43:39'),(314,'벅스',14,'BOOMPALA','LE SSERAFIM (르세라핌)','2026-06-05 02:43:39'),(315,'벅스',15,'RUDE!','Hearts2Hearts (하츠투하츠)','2026-06-05 02:43:39'),(316,'벅스',16,'404 (New Era)','KiiiKiii (키키)','2026-06-05 02:43:39'),(317,'벅스',17,'Popcorn','도경수(D.O.)','2026-06-05 02:43:39'),(318,'벅스',18,'Good Goodbye','화사 (HWASA)','2026-06-05 02:43:39'),(319,'벅스',19,'입춘','한로로','2026-06-05 02:43:39'),(320,'벅스',20,'Baby Flower','tripleS (트리플에스)','2026-06-05 02:43:39'),(321,'벅스',21,'BANG BANG','IVE (아이브)','2026-06-05 02:43:39'),(322,'벅스',22,'4 Flowers','마마무(Mamamoo)','2026-06-05 02:43:39'),(323,'벅스',23,'모르시나요(PROD.로코베리)','조째즈','2026-06-05 02:43:39'),(324,'벅스',24,'한 페이지가 될 수 있게','DAY6 (데이식스)','2026-06-05 02:43:39'),(325,'벅스',25,'Flashback','엔플라잉(N.Flying)','2026-06-05 02:43:39'),(326,'벅스',26,'LIVE FAST DIE SLOW','태양','2026-06-05 02:43:39'),(327,'벅스',27,'너에게 닿기를','10CM','2026-06-05 02:43:39'),(328,'벅스',28,'멸종위기사랑','이찬혁','2026-06-05 02:43:39'),(329,'벅스',29,'천상연','이창섭','2026-06-05 02:43:39'),(330,'벅스',30,'Who is she','KISS OF LIFE','2026-06-05 02:43:39'),(331,'벅스',31,'나의 하루처럼','성시경','2026-06-05 02:43:39'),(332,'벅스',32,'BUMPA','비비(BIBI)','2026-06-05 02:43:39'),(333,'벅스',33,'소나기','이클립스 (ECLIPSE)','2026-06-05 02:43:39'),(334,'벅스',34,'THAT’S A NO NO','ITZY (있지)','2026-06-05 02:43:39'),(335,'벅스',35,'주저하는 연인들을 위해','잔나비','2026-06-05 02:43:39'),(336,'벅스',36,'별이 될게','황치열','2026-06-05 02:43:39'),(337,'벅스',37,'OVERDRIVE','TWS (투어스)','2026-06-05 02:43:39'),(338,'벅스',38,'청춘만화','이무진','2026-06-05 02:43:39'),(339,'벅스',39,'So Cute','화사 (HWASA)','2026-06-05 02:43:39'),(340,'벅스',40,'타임캡슐','다비치','2026-06-05 02:43:39'),(341,'벅스',41,'like JENNIE','제니 (JENNIE)','2026-06-05 02:43:39'),(342,'벅스',42,'toxic till the end','로제(ROSÉ)','2026-06-05 02:43:39'),(343,'벅스',43,'첫 만남은 계획대로 되지 않아','TWS (투어스)','2026-06-05 02:43:39'),(344,'벅스',44,'BLACKHOLE','IVE (아이브)','2026-06-05 02:43:39'),(345,'벅스',45,'춤 (CHOOM)','BABYMONSTER','2026-06-05 02:43:39'),(346,'벅스',46,'Blue Valentine','NMIXX','2026-06-05 02:43:39'),(347,'벅스',47,'I AM','IVE (아이브)','2026-06-05 02:43:39'),(348,'벅스',48,'HAPPY','DAY6 (데이식스)','2026-06-05 02:43:39'),(349,'벅스',49,'NOT CUTE ANYMORE','아일릿(ILLIT)','2026-06-05 02:43:39'),(350,'벅스',50,'Whiplash','aespa','2026-06-05 02:43:39'),(351,'벅스',51,'Hype Boy','NewJeans','2026-06-05 02:43:39'),(352,'벅스',52,'봄 색깔','AKMU(악뮤)','2026-06-05 02:43:39'),(353,'벅스',53,'달리 표현할 수 없어요','로이킴','2026-06-05 02:43:39'),(354,'벅스',54,'Golden','HUNTR/X','2026-06-05 02:43:39'),(355,'벅스',55,'FAMOUS','ALLDAY PROJECT','2026-06-05 02:43:39'),(356,'벅스',56,'Supernova','aespa','2026-06-05 02:43:39'),(357,'벅스',57,'봄 내음보다 너를','김나영','2026-06-05 02:43:39'),(358,'벅스',58,'뛰어(JUMP)','BLACKPINK','2026-06-05 02:43:39'),(359,'벅스',59,'내게 사랑이 뭐냐고 물어본다면','로이킴','2026-06-05 02:43:39'),(360,'벅스',60,'FOCUS','Hearts2Hearts (하츠투하츠)','2026-06-05 02:43:39'),(361,'벅스',61,'사랑은 봄비처럼... 이별은 겨울비처럼','임현정','2026-06-05 02:43:39'),(362,'벅스',62,'에피소드','이무진','2026-06-05 02:43:39'),(363,'벅스',63,'Body to Body','방탄소년단','2026-06-05 02:43:39'),(364,'벅스',64,'SPAGHETTI (feat. j-hope of BTS)','LE SSERAFIM (르세라핌)','2026-06-05 02:43:39'),(365,'벅스',65,'APT.','로제(ROSÉ)','2026-06-05 02:43:39'),(366,'벅스',66,'모든 날, 모든 순간 (Every day, Every Moment)','폴킴(Paul Kim)','2026-06-05 02:43:39'),(367,'벅스',67,'띠로리 (DDI RO RI)','MEOVV (미야오)','2026-06-05 02:43:39'),(368,'벅스',68,'REBEL HEART','IVE (아이브)','2026-06-05 02:43:39'),(369,'벅스',69,'Love wins all','아이유(IU)','2026-06-05 02:43:39'),(370,'벅스',70,'Love me or Leave me','DAY6 (데이식스)','2026-06-05 02:43:39'),(371,'벅스',71,'어떻게 이별까지 사랑하겠어, 널 사랑하는 거지','AKMU(악뮤)','2026-06-05 02:43:39'),(372,'벅스',72,'SWIM','방탄소년단','2026-06-05 02:43:39'),(373,'벅스',73,'Die With A Smile','Lady Gaga(레이디 가가)','2026-06-05 02:43:39'),(374,'벅스',74,'햇빛 bless you','AKMU(악뮤)','2026-06-05 02:43:39'),(375,'벅스',75,'Welcome to the Show','DAY6 (데이식스)','2026-06-05 02:43:39'),(376,'벅스',76,'Congratulations','DAY6 (데이식스)','2026-06-05 02:43:39'),(377,'벅스',77,'고민중독','QWER','2026-06-05 02:43:39'),(378,'벅스',78,'Flower','오반(OVAN)','2026-06-05 02:43:39'),(379,'벅스',79,'하루에 하루만 더 (Stick With You)','투모로우바이투게더','2026-06-05 02:43:39'),(380,'벅스',80,'HOME SWEET HOME (feat. 태양, 대성)','G-DRAGON','2026-06-05 02:43:39'),(381,'벅스',81,'Ditto','NewJeans','2026-06-05 02:43:39'),(382,'벅스',82,'나는 반딧불','황가람','2026-06-05 02:43:39'),(383,'벅스',83,'그대만 있다면 (여름날 우리 X 너드커넥션 (Nerd Connection))','너드커넥션(Nerd Connection)','2026-06-05 02:43:39'),(384,'벅스',84,'Smile Boy','로이킴','2026-06-05 02:43:39'),(385,'벅스',85,'Soda Pop','Saja Boys','2026-06-05 02:43:39'),(386,'벅스',86,'Magnetic','아일릿(ILLIT)','2026-06-05 02:43:39'),(387,'벅스',87,'STYLE','Hearts2Hearts (하츠투하츠)','2026-06-05 02:43:39'),(388,'벅스',88,'시작의 아이 ❍','박다혜','2026-06-05 02:43:39'),(389,'벅스',89,'ONE MORE TIME','ALLDAY PROJECT','2026-06-05 02:43:39'),(390,'벅스',90,'I DO ME','KiiiKiii (키키)','2026-06-05 02:43:39'),(391,'벅스',91,'벌레를 내고','AKMU(악뮤)','2026-06-05 02:43:39'),(392,'벅스',92,'그대 작은 나의 세상이 되어','카더가든','2026-06-05 02:43:39'),(393,'벅스',93,'Atmos','SHINee (샤이니)','2026-06-05 02:43:39'),(394,'벅스',94,'마치 오늘처럼','정승환','2026-06-05 02:43:39'),(395,'벅스',95,'IF I','TREASURE(트레저)','2026-06-05 02:43:39'),(396,'벅스',96,'GO','BLACKPINK','2026-06-05 02:43:39'),(397,'벅스',97,'오늘만 I LOVE YOU','BOYNEXTDOOR','2026-06-05 02:43:39'),(398,'벅스',98,'XOXZ','IVE (아이브)','2026-06-05 02:43:39'),(399,'벅스',99,'나는 아픈 건 딱 질색이니까','i-dle (아이들)','2026-06-05 02:43:39'),(400,'벅스',100,'사랑인가 봐','멜로망스(MeloMance)','2026-06-05 02:43:39'),(401,'멜론',1,'갑자기','아이오아이 (I.O.I)','2026-06-05 02:43:39'),(402,'멜론',2,'REDRED','CORTIS (코르티스)','2026-06-05 02:43:39'),(403,'멜론',3,'It′s Me','아일릿(ILLIT)','2026-06-05 02:43:39'),(404,'멜론',4,'소문의 낙원','AKMU (악뮤)','2026-06-05 02:43:39'),(405,'멜론',5,'LEMONADE','aespa','2026-06-05 02:43:39'),(406,'멜론',6,'기쁨, 슬픔, 아름다운 마음','AKMU (악뮤)','2026-06-05 02:43:39'),(407,'멜론',7,'캐치 캐치','YENA (최예나)','2026-06-05 02:43:39'),(408,'멜론',8,'RUDE!','Hearts2Hearts (하츠투하츠)','2026-06-05 02:43:39'),(409,'멜론',9,'사랑하게 될 거야','한로로','2026-06-05 02:43:39'),(410,'멜론',10,'Heavy Serenade','NMIXX','2026-06-05 02:43:39'),(411,'멜론',11,'Drowning','WOODZ','2026-06-05 02:43:39'),(412,'멜론',12,'WDA (Whole Different Animal) (Feat. G-DRAGON)','aespa','2026-06-05 02:43:39'),(413,'멜론',13,'0+0','한로로','2026-06-05 02:43:39'),(414,'멜론',14,'404 (New Era)','KiiiKiii (키키)','2026-06-05 02:43:39'),(415,'멜론',15,'BANG BANG','IVE (아이브)','2026-06-05 02:43:39'),(416,'멜론',16,'Good Goodbye','화사 (HWASA)','2026-06-05 02:43:39'),(417,'멜론',17,'SWIM','방탄소년단','2026-06-05 02:43:39'),(418,'멜론',18,'LOVE ATTACK','RESCENE (리센느)','2026-06-05 02:43:39'),(419,'멜론',19,'타임캡슐','다비치','2026-06-05 02:43:39'),(420,'멜론',20,'Popcorn','도경수(D.O.)','2026-06-05 02:43:39'),(421,'멜론',21,'너에게 닿기를','10CM','2026-06-05 02:43:39'),(422,'멜론',22,'Blue Valentine','NMIXX','2026-06-05 02:43:39'),(423,'멜론',23,'멸종위기사랑','이찬혁','2026-06-05 02:43:39'),(424,'멜론',24,'어떻게 이별까지 사랑하겠어, 널 사랑하는 거지','AKMU (악뮤)','2026-06-05 02:43:39'),(425,'멜론',25,'Body to Body','방탄소년단','2026-06-05 02:43:39'),(426,'멜론',26,'어제보다 슬픈 오늘','우디 (Woody)','2026-06-05 02:43:39'),(427,'멜론',27,'뛰어(JUMP)','BLACKPINK','2026-06-05 02:43:39'),(428,'멜론',28,'너의 모든 순간','성시경','2026-06-05 02:43:39'),(429,'멜론',29,'그대 작은 나의 세상이 되어','카더가든','2026-06-05 02:43:39'),(430,'멜론',30,'Golden','HUNTR/X','2026-06-05 02:43:39'),(431,'멜론',31,'소나기','이클립스 (ECLIPSE)','2026-06-05 02:43:39'),(432,'멜론',32,'BOOMPALA','LE SSERAFIM (르세라핌)','2026-06-05 02:43:39'),(433,'멜론',33,'모르시나요(PROD.로코베리)','조째즈','2026-06-05 02:43:39'),(434,'멜론',34,'내게 사랑이 뭐냐고 물어본다면','로이킴','2026-06-05 02:43:39'),(435,'멜론',35,'toxic till the end','로제 (ROSÉ)','2026-06-05 02:43:39'),(436,'멜론',36,'Whiplash','aespa','2026-06-05 02:43:39'),(437,'멜론',37,'천상연','이창섭','2026-06-05 02:43:39'),(438,'멜론',38,'HOME SWEET HOME (feat. 태양, 대성)','G-DRAGON','2026-06-05 02:43:39'),(439,'멜론',39,'청춘만화','이무진','2026-06-05 02:43:39'),(440,'멜론',40,'한 페이지가 될 수 있게','DAY6 (데이식스)','2026-06-05 02:43:39'),(441,'멜론',41,'2.0','방탄소년단','2026-06-05 02:43:39'),(442,'멜론',42,'HAPPY','DAY6 (데이식스)','2026-06-05 02:43:39'),(443,'멜론',43,'그대만 있다면 (여름날 우리 X 너드커넥션 (Nerd Connection))','너드커넥션 (Nerd Connection)','2026-06-05 02:43:39'),(444,'멜론',44,'봄날','방탄소년단','2026-06-05 02:43:39'),(445,'멜론',45,'like JENNIE','제니 (JENNIE)','2026-06-05 02:43:39'),(446,'멜론',46,'Seven (feat. Latto) - Clean Ver.','정국','2026-06-05 02:43:39'),(447,'멜론',47,'Hooligan','방탄소년단','2026-06-05 02:43:39'),(448,'멜론',48,'BLACKHOLE','IVE (아이브)','2026-06-05 02:43:39'),(449,'멜론',49,'사랑은 늘 도망가','임영웅','2026-06-05 02:43:39'),(450,'멜론',50,'입춘','한로로','2026-06-05 02:43:39'),(451,'멜론',51,'모든 날, 모든 순간 (Every day, Every Moment)','폴킴','2026-06-05 02:43:39'),(452,'멜론',52,'사랑인가 봐','멜로망스','2026-06-05 02:43:39'),(453,'멜론',53,'주저하는 연인들을 위해','잔나비','2026-06-05 02:43:39'),(454,'멜론',54,'SPAGHETTI (feat. j-hope of BTS)','LE SSERAFIM (르세라핌)','2026-06-05 02:43:39'),(455,'멜론',55,'예뻤어','DAY6 (데이식스)','2026-06-05 02:43:39'),(456,'멜론',56,'나는 반딧불','황가람','2026-06-05 02:43:39'),(457,'멜론',57,'오늘만 I LOVE YOU','BOYNEXTDOOR','2026-06-05 02:43:39'),(458,'멜론',58,'청혼하지 않을 이유를 못 찾았어','이무진','2026-06-05 02:43:39'),(459,'멜론',59,'FAMOUS','ALLDAY PROJECT','2026-06-05 02:43:39'),(460,'멜론',60,'STYLE','Hearts2Hearts (하츠투하츠)','2026-06-05 02:43:39'),(461,'멜론',61,'사랑은 봄비처럼...이별은 겨울비처럼...','임현정','2026-06-05 02:43:39'),(462,'멜론',62,'눈을 감아도(2026)','순순희(지환)','2026-06-05 02:43:39'),(463,'멜론',63,'Love Love Love (Feat. Yoong Jin Of Casker)','에픽하이 (EPIK HIGH)','2026-06-05 02:43:39'),(464,'멜론',64,'Welcome to the Show','DAY6 (데이식스)','2026-06-05 02:43:39'),(465,'멜론',65,'APT.','로제 (ROSÉ)','2026-06-05 02:43:39'),(466,'멜론',66,'첫 만남은 계획대로 되지 않아','TWS (투어스)','2026-06-05 02:43:39'),(467,'멜론',67,'LIVE FAST DIE SLOW','태양','2026-06-05 02:43:39'),(468,'멜론',68,'FYA','방탄소년단','2026-06-05 02:43:39'),(469,'멜론',69,'TICK TOCK (Feat. ZICO) (Prod. by ZICO, Crush)','김하온 (HAON)','2026-06-05 02:43:39'),(470,'멜론',70,'Dynamite','방탄소년단','2026-06-05 02:43:39'),(471,'멜론',71,'달리 표현할 수 없어요','로이킴','2026-06-05 02:43:39'),(472,'멜론',72,'봄 내음보다 너를','김나영','2026-06-05 02:43:39'),(473,'멜론',73,'REBEL HEART','IVE (아이브)','2026-06-05 02:43:39'),(474,'멜론',74,'시작의 아이 ❍','박다혜','2026-06-05 02:43:39'),(475,'멜론',75,'다정히 내 이름을 부르면','경서예지','2026-06-05 02:43:39'),(476,'멜론',76,'Flower','오반(OVAN)','2026-06-05 02:43:39'),(477,'멜론',77,'ONE MORE TIME','ALLDAY PROJECT','2026-06-05 02:43:39'),(478,'멜론',78,'Like Animals','방탄소년단','2026-06-05 02:43:39'),(479,'멜론',79,'Aliens','방탄소년단','2026-06-05 02:43:39'),(480,'멜론',80,'Love wins all','아이유','2026-06-05 02:43:39'),(481,'멜론',81,'헤어지자 말해요','박재정','2026-06-05 02:43:39'),(482,'멜론',82,'OVERDRIVE','TWS (투어스)','2026-06-05 02:43:39'),(483,'멜론',83,'이 밤을 빌려 말해요','PLAVE','2026-06-05 02:43:39'),(484,'멜론',84,'Die With A Smile','Lady Gaga','2026-06-05 02:43:39'),(485,'멜론',85,'FOCUS','Hearts2Hearts (하츠투하츠)','2026-06-05 02:43:39'),(486,'멜론',86,'Magnetic','아일릿(ILLIT)','2026-06-05 02:43:39'),(487,'멜론',87,'KISS KISS KISS (Feat. 선우 (THE BOYZ)) (Prod. by Hukky Shibaseki)','NOWIMYOUNG (나우아임영)','2026-06-05 02:43:39'),(488,'멜론',88,'Merry Go Round','방탄소년단','2026-06-05 02:43:39'),(489,'멜론',89,'에피소드','이무진','2026-06-05 02:43:39'),(490,'멜론',90,'Hype Boy','NewJeans','2026-06-05 02:43:39'),(491,'멜론',91,'순간을 영원처럼','임영웅','2026-06-05 02:43:39'),(492,'멜론',92,'One More Night','방탄소년단','2026-06-05 02:43:39'),(493,'멜론',93,'Flashback','엔플라잉 (N.Flying)','2026-06-05 02:43:39'),(494,'멜론',94,'Never Ending Story','아이유','2026-06-05 02:43:39'),(495,'멜론',95,'하루에 하루만 더 (Stick With You)','투모로우바이투게더','2026-06-05 02:43:39'),(496,'멜론',96,'NOT CUTE ANYMORE','아일릿(ILLIT)','2026-06-05 02:43:39'),(497,'멜론',97,'I AM','IVE (아이브)','2026-06-05 02:43:39'),(498,'멜론',98,'우리들의 블루스','임영웅','2026-06-05 02:43:39'),(499,'멜론',99,'Soda Pop','KPop Demon Hunters Cast','2026-06-05 02:43:39'),(500,'멜론',100,'Smile Boy','로이킴','2026-06-05 02:43:39'),(501,'지니',1,'갑자기','아이오아이 (I.O.I)','2026-06-05 02:43:39'),(502,'지니',2,'It\'s Me','아일릿(ILLIT)','2026-06-05 02:43:39'),(503,'지니',3,'소문의 낙원','AKMU (악뮤)','2026-06-05 02:43:39'),(504,'지니',4,'REDRED','CORTIS (코르티스)','2026-06-05 02:43:39'),(505,'지니',5,'캐치 캐치','YENA (최예나)','2026-06-05 02:43:39'),(506,'지니',6,'기쁨, 슬픔, 아름다운 마음','AKMU (악뮤)','2026-06-05 02:43:39'),(507,'지니',7,'Drowning','WOODZ','2026-06-05 02:43:39'),(508,'지니',8,'사랑하게 될 거야','한로로','2026-06-05 02:43:39'),(509,'지니',9,'0＋0','한로로','2026-06-05 02:43:39'),(510,'지니',10,'BANG BANG','IVE (아이브)','2026-06-05 02:43:39'),(511,'지니',11,'Good Goodbye','화사 (HWASA)','2026-06-05 02:43:39'),(512,'지니',12,'404 (New Era)','KiiiKiii (키키)','2026-06-05 02:43:39'),(513,'지니',13,'Popcorn','도경수 (D.O.)','2026-06-05 02:43:39'),(514,'지니',14,'타임캡슐','다비치','2026-06-05 02:43:39'),(515,'지니',15,'RUDE!','Hearts2Hearts (하츠투하츠)','2026-06-05 02:43:39'),(516,'지니',16,'멸종위기사랑','이찬혁','2026-06-05 02:43:39'),(517,'지니',17,'LEMONADE','aespa','2026-06-05 02:43:39'),(518,'지니',18,'너에게 닿기를','10CM','2026-06-05 02:43:39'),(519,'지니',19,'WDA (Whole Different Animal) (Feat. G-DRAGON)','aespa','2026-06-05 02:43:39'),(520,'지니',20,'뛰어(JUMP)','BLACKPINK','2026-06-05 02:43:39'),(521,'지니',21,'내게 사랑이 뭐냐고 물어본다면','로이킴','2026-06-05 02:43:39'),(522,'지니',22,'Golden','HUNTR/X & EJAE & Audrey Nuna & REI AMI & KPop Demon Hunters Cast','2026-06-05 02:43:39'),(523,'지니',23,'Blue Valentine','NMIXX','2026-06-05 02:43:39'),(524,'지니',24,'모르시나요 (Prod. by 로코베리)','조째즈','2026-06-05 02:43:39'),(525,'지니',25,'어제보다 슬픈 오늘','우디 (Woody)','2026-06-05 02:43:39'),(526,'지니',26,'청춘만화','이무진','2026-06-05 02:43:39'),(527,'지니',27,'입춘','한로로','2026-06-05 02:43:39'),(528,'지니',28,'사랑은 늘 도망가','임영웅','2026-06-05 02:43:39'),(529,'지니',29,'Heavy Serenade','NMIXX','2026-06-05 02:43:39'),(530,'지니',30,'어떻게 이별까지 사랑하겠어, 널 사랑하는 거지','AKMU (악뮤)','2026-06-05 02:43:39'),(531,'지니',31,'봄 내음보다 너를','김나영','2026-06-05 02:43:39'),(532,'지니',32,'toxic till the end','로제 (ROSÉ)','2026-06-05 02:43:39'),(533,'지니',33,'HAPPY','DAY6 (데이식스)','2026-06-05 02:43:39'),(534,'지니',34,'다시 만날 수 있을까','임영웅','2026-06-05 02:43:39'),(535,'지니',35,'우리들의 블루스','임영웅','2026-06-05 02:43:39'),(536,'지니',36,'그대 작은 나의 세상이 되어','카더가든','2026-06-05 02:43:39'),(537,'지니',37,'시작의 아이','마크툽 (Maktub)','2026-06-05 02:43:39'),(538,'지니',38,'Whiplash','aespa','2026-06-05 02:43:39'),(539,'지니',39,'순간을 영원처럼','임영웅','2026-06-05 02:43:39'),(540,'지니',40,'소나기','이클립스 (ECLIPSE)','2026-06-05 02:43:39'),(541,'지니',41,'한 페이지가 될 수 있게','DAY6 (데이식스)','2026-06-05 02:43:39'),(542,'지니',42,'나는 반딧불','황가람','2026-06-05 02:43:39'),(543,'지니',43,'LOVE ATTACK','RESCENE (리센느)','2026-06-05 02:43:39'),(544,'지니',44,'너의 모든 순간','성시경','2026-06-05 02:43:39'),(545,'지니',45,'돌아보지 마세요','임영웅','2026-06-05 02:43:39'),(546,'지니',46,'HOME SWEET HOME (Feat. 태양 & 대성)','G-DRAGON','2026-06-05 02:43:39'),(547,'지니',47,'그댈 위한 멜로디','임영웅','2026-06-05 02:43:39'),(548,'지니',48,'천국보다 아름다운','임영웅','2026-06-05 02:43:39'),(549,'지니',49,'답장을 보낸지','임영웅','2026-06-05 02:43:39'),(550,'지니',50,'우리에게 안녕','임영웅','2026-06-05 02:43:39'),(551,'지니',51,'들꽃이 될게요','임영웅','2026-06-05 02:43:39'),(552,'지니',52,'Pretender','OFFICIAL HIGE DANDISM','2026-06-05 02:43:39'),(553,'지니',53,'SWIM','방탄소년단','2026-06-05 02:43:39'),(554,'지니',54,'비가 와서','임영웅','2026-06-05 02:43:39'),(555,'지니',55,'like JENNIE','제니 (JENNIE)','2026-06-05 02:43:39'),(556,'지니',56,'ULSSIGU','임영웅','2026-06-05 02:43:39'),(557,'지니',57,'알겠어요 미안해요','임영웅','2026-06-05 02:43:39'),(558,'지니',58,'Wonderful Life','임영웅','2026-06-05 02:43:39'),(559,'지니',59,'나는야 HERO','임영웅','2026-06-05 02:43:39'),(560,'지니',60,'천상연','이창섭','2026-06-05 02:43:39'),(561,'지니',61,'달리 표현할 수 없어요','로이킴','2026-06-05 02:43:39'),(562,'지니',62,'Welcome to the Show','DAY6 (데이식스)','2026-06-05 02:43:39'),(563,'지니',63,'예뻤어','DAY6 (데이식스)','2026-06-05 02:43:39'),(564,'지니',64,'사건의 지평선','윤하 (YOUNHA)','2026-06-05 02:43:39'),(565,'지니',65,'벌써 일년','브라운 아이즈','2026-06-05 02:43:39'),(566,'지니',66,'APT.','로제 (ROSÉ) & Bruno Mars','2026-06-05 02:43:39'),(567,'지니',67,'에피소드','이무진','2026-06-05 02:43:39'),(568,'지니',68,'주저하는 연인들을 위해','잔나비','2026-06-05 02:43:39'),(569,'지니',69,'REBEL HEART','IVE (아이브)','2026-06-05 02:43:39'),(570,'지니',70,'Cruel Summer','Taylor Swift','2026-06-05 02:43:39'),(571,'지니',71,'Soda Pop','Saja Boys & Andrew Choi & Neckwav & Danny Chung & Kevin Woo & samUIL Lee & KPop Demon Hunters Cast','2026-06-05 02:43:39'),(572,'지니',72,'사랑인가 봐','멜로망스 (MeloMance)','2026-06-05 02:43:39'),(573,'지니',73,'눈을 감아도(2026)','순순희 (지환)','2026-06-05 02:43:39'),(574,'지니',74,'TICK TOCK (Feat. ZICO) (Prod. by ZICO, Crush)','김하온 (HAON) & Nosun & Raf Sandou & Marv & 정준혁','2026-06-05 02:43:39'),(575,'지니',75,'고민중독','QWER','2026-06-05 02:43:39'),(576,'지니',76,'MY LOVE (2025)','이예은 & 아샤트리 & 전건호','2026-06-05 02:43:39'),(577,'지니',77,'슬픈 초대장','순순희 (지환)','2026-06-05 02:43:39'),(578,'지니',78,'BLACKHOLE','IVE (아이브)','2026-06-05 02:43:39'),(579,'지니',79,'Die With A Smile','Lady Gaga & Bruno Mars','2026-06-05 02:43:39'),(580,'지니',80,'Flashback','엔플라잉 (N.Flying)','2026-06-05 02:43:39'),(581,'지니',81,'FAMOUS','ALLDAY PROJECT','2026-06-05 02:43:39'),(582,'지니',82,'BOOMPALA','LE SSERAFIM (르세라핌)','2026-06-05 02:43:39'),(583,'지니',83,'모든 날, 모든 순간 (Every day, Every Moment)','폴킴','2026-06-05 02:43:39'),(584,'지니',84,'시작의 아이 ❍','박다혜 & 마크툽 (Maktub)','2026-06-05 02:43:39'),(585,'지니',85,'떠나가요, 떠나지마요 : 시대를 초월한 마음','순순희 (기태) & 백예슬','2026-06-05 02:43:39'),(586,'지니',86,'Stay','The Kid LAROI & Justin Bieber','2026-06-05 02:43:39'),(587,'지니',87,'LIVE FAST DIE SLOW','태양','2026-06-05 02:43:39'),(588,'지니',88,'가까운 듯 먼 그대여','카더가든','2026-06-05 02:43:39'),(589,'지니',89,'그래 늦지 않았어 (2025)','아샤트리 & 이예은 & 전건호','2026-06-05 02:43:39'),(590,'지니',90,'Love Love Love (Feat. Yoong Jin of Casker))','에픽하이 (EPIK HIGH)','2026-06-05 02:43:39'),(591,'지니',91,'Body to Body','방탄소년단','2026-06-05 02:43:39'),(592,'지니',92,'첫 만남은 계획대로 되지 않아','TWS (투어스)','2026-06-05 02:43:39'),(593,'지니',93,'그대만 있다면 (여름날 우리 X 너드커넥션 (Nerd Connection))','너드커넥션 (Nerd Connection)','2026-06-05 02:43:39'),(594,'지니',94,'희재','성시경','2026-06-05 02:43:39'),(595,'지니',95,'다정히 내 이름을 부르면','경서예지 & 전건호','2026-06-05 02:43:39'),(596,'지니',96,'청혼하지 않을 이유를 못 찾았어','이무진','2026-06-05 02:43:39'),(597,'지니',97,'TOO BAD (Feat. Anderson .Paak)','G-DRAGON','2026-06-05 02:43:39'),(598,'지니',98,'비의 랩소디','임재현','2026-06-05 02:43:39'),(599,'지니',99,'내 이름 맑음','QWER','2026-06-05 02:43:39'),(600,'지니',100,'사막에서 꽃을 피우듯','우디 (Woody)','2026-06-05 02:43:39'),(601,'벅스',1,'갑자기','아이오아이(I.O.I)','2026-06-05 02:45:14'),(602,'벅스',2,'LEMONADE','aespa','2026-06-05 02:45:14'),(603,'벅스',3,'REDRED','CORTIS (코르티스)','2026-06-05 02:45:14'),(604,'벅스',4,'It′s Me','아일릿(ILLIT)','2026-06-05 02:45:14'),(605,'벅스',5,'WDA (Whole Different Animal) (Feat. G-DRAGON)','aespa','2026-06-05 02:45:14'),(606,'벅스',6,'LOVE ATTACK','RESCENE (리센느)','2026-06-05 02:45:14'),(607,'벅스',7,'소문의 낙원','AKMU(악뮤)','2026-06-05 02:45:14'),(608,'벅스',8,'Heavy Serenade','NMIXX','2026-06-05 02:45:14'),(609,'벅스',9,'기쁨, 슬픔, 아름다운 마음','AKMU(악뮤)','2026-06-05 02:45:14'),(610,'벅스',10,'0+0','한로로','2026-06-05 02:45:14'),(611,'벅스',11,'사랑하게 될 거야','한로로','2026-06-05 02:45:14'),(612,'벅스',12,'Drowning','WOODZ','2026-06-05 02:45:14'),(613,'벅스',13,'캐치 캐치','YENA (최예나)','2026-06-05 02:45:14'),(614,'벅스',14,'BOOMPALA','LE SSERAFIM (르세라핌)','2026-06-05 02:45:14'),(615,'벅스',15,'RUDE!','Hearts2Hearts (하츠투하츠)','2026-06-05 02:45:14'),(616,'벅스',16,'404 (New Era)','KiiiKiii (키키)','2026-06-05 02:45:14'),(617,'벅스',17,'Popcorn','도경수(D.O.)','2026-06-05 02:45:14'),(618,'벅스',18,'Good Goodbye','화사 (HWASA)','2026-06-05 02:45:14'),(619,'벅스',19,'입춘','한로로','2026-06-05 02:45:14'),(620,'벅스',20,'Baby Flower','tripleS (트리플에스)','2026-06-05 02:45:14'),(621,'벅스',21,'BANG BANG','IVE (아이브)','2026-06-05 02:45:14'),(622,'벅스',22,'4 Flowers','마마무(Mamamoo)','2026-06-05 02:45:14'),(623,'벅스',23,'모르시나요(PROD.로코베리)','조째즈','2026-06-05 02:45:14'),(624,'벅스',24,'한 페이지가 될 수 있게','DAY6 (데이식스)','2026-06-05 02:45:14'),(625,'벅스',25,'Flashback','엔플라잉(N.Flying)','2026-06-05 02:45:14'),(626,'벅스',26,'LIVE FAST DIE SLOW','태양','2026-06-05 02:45:14'),(627,'벅스',27,'너에게 닿기를','10CM','2026-06-05 02:45:14'),(628,'벅스',28,'멸종위기사랑','이찬혁','2026-06-05 02:45:14'),(629,'벅스',29,'천상연','이창섭','2026-06-05 02:45:14'),(630,'벅스',30,'Who is she','KISS OF LIFE','2026-06-05 02:45:14'),(631,'벅스',31,'나의 하루처럼','성시경','2026-06-05 02:45:14'),(632,'벅스',32,'BUMPA','비비(BIBI)','2026-06-05 02:45:14'),(633,'벅스',33,'소나기','이클립스 (ECLIPSE)','2026-06-05 02:45:14'),(634,'벅스',34,'THAT’S A NO NO','ITZY (있지)','2026-06-05 02:45:14'),(635,'벅스',35,'주저하는 연인들을 위해','잔나비','2026-06-05 02:45:14'),(636,'벅스',36,'별이 될게','황치열','2026-06-05 02:45:14'),(637,'벅스',37,'OVERDRIVE','TWS (투어스)','2026-06-05 02:45:14'),(638,'벅스',38,'청춘만화','이무진','2026-06-05 02:45:14'),(639,'벅스',39,'So Cute','화사 (HWASA)','2026-06-05 02:45:14'),(640,'벅스',40,'타임캡슐','다비치','2026-06-05 02:45:14'),(641,'벅스',41,'like JENNIE','제니 (JENNIE)','2026-06-05 02:45:14'),(642,'벅스',42,'toxic till the end','로제(ROSÉ)','2026-06-05 02:45:14'),(643,'벅스',43,'첫 만남은 계획대로 되지 않아','TWS (투어스)','2026-06-05 02:45:14'),(644,'벅스',44,'BLACKHOLE','IVE (아이브)','2026-06-05 02:45:14'),(645,'벅스',45,'춤 (CHOOM)','BABYMONSTER','2026-06-05 02:45:14'),(646,'벅스',46,'Blue Valentine','NMIXX','2026-06-05 02:45:14'),(647,'벅스',47,'I AM','IVE (아이브)','2026-06-05 02:45:14'),(648,'벅스',48,'HAPPY','DAY6 (데이식스)','2026-06-05 02:45:14'),(649,'벅스',49,'NOT CUTE ANYMORE','아일릿(ILLIT)','2026-06-05 02:45:14'),(650,'벅스',50,'Whiplash','aespa','2026-06-05 02:45:14'),(651,'벅스',51,'Hype Boy','NewJeans','2026-06-05 02:45:14'),(652,'벅스',52,'봄 색깔','AKMU(악뮤)','2026-06-05 02:45:14'),(653,'벅스',53,'달리 표현할 수 없어요','로이킴','2026-06-05 02:45:14'),(654,'벅스',54,'Golden','HUNTR/X','2026-06-05 02:45:14'),(655,'벅스',55,'FAMOUS','ALLDAY PROJECT','2026-06-05 02:45:14'),(656,'벅스',56,'Supernova','aespa','2026-06-05 02:45:14'),(657,'벅스',57,'봄 내음보다 너를','김나영','2026-06-05 02:45:14'),(658,'벅스',58,'뛰어(JUMP)','BLACKPINK','2026-06-05 02:45:14'),(659,'벅스',59,'내게 사랑이 뭐냐고 물어본다면','로이킴','2026-06-05 02:45:14'),(660,'벅스',60,'FOCUS','Hearts2Hearts (하츠투하츠)','2026-06-05 02:45:14'),(661,'벅스',61,'사랑은 봄비처럼... 이별은 겨울비처럼','임현정','2026-06-05 02:45:14'),(662,'벅스',62,'에피소드','이무진','2026-06-05 02:45:14'),(663,'벅스',63,'Body to Body','방탄소년단','2026-06-05 02:45:14'),(664,'벅스',64,'SPAGHETTI (feat. j-hope of BTS)','LE SSERAFIM (르세라핌)','2026-06-05 02:45:14'),(665,'벅스',65,'APT.','로제(ROSÉ)','2026-06-05 02:45:14'),(666,'벅스',66,'모든 날, 모든 순간 (Every day, Every Moment)','폴킴(Paul Kim)','2026-06-05 02:45:14'),(667,'벅스',67,'띠로리 (DDI RO RI)','MEOVV (미야오)','2026-06-05 02:45:14'),(668,'벅스',68,'REBEL HEART','IVE (아이브)','2026-06-05 02:45:14'),(669,'벅스',69,'Love wins all','아이유(IU)','2026-06-05 02:45:14'),(670,'벅스',70,'Love me or Leave me','DAY6 (데이식스)','2026-06-05 02:45:14'),(671,'벅스',71,'어떻게 이별까지 사랑하겠어, 널 사랑하는 거지','AKMU(악뮤)','2026-06-05 02:45:14'),(672,'벅스',72,'SWIM','방탄소년단','2026-06-05 02:45:14'),(673,'벅스',73,'Die With A Smile','Lady Gaga(레이디 가가)','2026-06-05 02:45:14'),(674,'벅스',74,'햇빛 bless you','AKMU(악뮤)','2026-06-05 02:45:14'),(675,'벅스',75,'Welcome to the Show','DAY6 (데이식스)','2026-06-05 02:45:14'),(676,'벅스',76,'Congratulations','DAY6 (데이식스)','2026-06-05 02:45:14'),(677,'벅스',77,'고민중독','QWER','2026-06-05 02:45:14'),(678,'벅스',78,'Flower','오반(OVAN)','2026-06-05 02:45:14'),(679,'벅스',79,'하루에 하루만 더 (Stick With You)','투모로우바이투게더','2026-06-05 02:45:14'),(680,'벅스',80,'HOME SWEET HOME (feat. 태양, 대성)','G-DRAGON','2026-06-05 02:45:14'),(681,'벅스',81,'Ditto','NewJeans','2026-06-05 02:45:14'),(682,'벅스',82,'나는 반딧불','황가람','2026-06-05 02:45:14'),(683,'벅스',83,'그대만 있다면 (여름날 우리 X 너드커넥션 (Nerd Connection))','너드커넥션(Nerd Connection)','2026-06-05 02:45:14'),(684,'벅스',84,'Smile Boy','로이킴','2026-06-05 02:45:14'),(685,'벅스',85,'Soda Pop','Saja Boys','2026-06-05 02:45:14'),(686,'벅스',86,'Magnetic','아일릿(ILLIT)','2026-06-05 02:45:14'),(687,'벅스',87,'STYLE','Hearts2Hearts (하츠투하츠)','2026-06-05 02:45:14'),(688,'벅스',88,'시작의 아이 ❍','박다혜','2026-06-05 02:45:14'),(689,'벅스',89,'ONE MORE TIME','ALLDAY PROJECT','2026-06-05 02:45:14'),(690,'벅스',90,'I DO ME','KiiiKiii (키키)','2026-06-05 02:45:14'),(691,'벅스',91,'벌레를 내고','AKMU(악뮤)','2026-06-05 02:45:14'),(692,'벅스',92,'그대 작은 나의 세상이 되어','카더가든','2026-06-05 02:45:14'),(693,'벅스',93,'Atmos','SHINee (샤이니)','2026-06-05 02:45:14'),(694,'벅스',94,'마치 오늘처럼','정승환','2026-06-05 02:45:14'),(695,'벅스',95,'IF I','TREASURE(트레저)','2026-06-05 02:45:14'),(696,'벅스',96,'GO','BLACKPINK','2026-06-05 02:45:14'),(697,'벅스',97,'오늘만 I LOVE YOU','BOYNEXTDOOR','2026-06-05 02:45:14'),(698,'벅스',98,'XOXZ','IVE (아이브)','2026-06-05 02:45:14'),(699,'벅스',99,'나는 아픈 건 딱 질색이니까','i-dle (아이들)','2026-06-05 02:45:14'),(700,'벅스',100,'사랑인가 봐','멜로망스(MeloMance)','2026-06-05 02:45:14'),(701,'벅스',1,'갑자기','아이오아이(I.O.I)','2026-06-05 02:45:19'),(702,'벅스',2,'LEMONADE','aespa','2026-06-05 02:45:19'),(703,'벅스',3,'REDRED','CORTIS (코르티스)','2026-06-05 02:45:19'),(704,'벅스',4,'It′s Me','아일릿(ILLIT)','2026-06-05 02:45:19'),(705,'벅스',5,'WDA (Whole Different Animal) (Feat. G-DRAGON)','aespa','2026-06-05 02:45:19'),(706,'벅스',6,'LOVE ATTACK','RESCENE (리센느)','2026-06-05 02:45:19'),(707,'벅스',7,'소문의 낙원','AKMU(악뮤)','2026-06-05 02:45:19'),(708,'벅스',8,'Heavy Serenade','NMIXX','2026-06-05 02:45:19'),(709,'벅스',9,'기쁨, 슬픔, 아름다운 마음','AKMU(악뮤)','2026-06-05 02:45:19'),(710,'벅스',10,'0+0','한로로','2026-06-05 02:45:19'),(711,'벅스',11,'사랑하게 될 거야','한로로','2026-06-05 02:45:19'),(712,'벅스',12,'Drowning','WOODZ','2026-06-05 02:45:19'),(713,'벅스',13,'캐치 캐치','YENA (최예나)','2026-06-05 02:45:19'),(714,'벅스',14,'BOOMPALA','LE SSERAFIM (르세라핌)','2026-06-05 02:45:19'),(715,'벅스',15,'RUDE!','Hearts2Hearts (하츠투하츠)','2026-06-05 02:45:19'),(716,'벅스',16,'404 (New Era)','KiiiKiii (키키)','2026-06-05 02:45:19'),(717,'벅스',17,'Popcorn','도경수(D.O.)','2026-06-05 02:45:19'),(718,'벅스',18,'Good Goodbye','화사 (HWASA)','2026-06-05 02:45:19'),(719,'벅스',19,'입춘','한로로','2026-06-05 02:45:19'),(720,'벅스',20,'Baby Flower','tripleS (트리플에스)','2026-06-05 02:45:19'),(721,'벅스',21,'BANG BANG','IVE (아이브)','2026-06-05 02:45:19'),(722,'벅스',22,'4 Flowers','마마무(Mamamoo)','2026-06-05 02:45:19'),(723,'벅스',23,'모르시나요(PROD.로코베리)','조째즈','2026-06-05 02:45:19'),(724,'벅스',24,'한 페이지가 될 수 있게','DAY6 (데이식스)','2026-06-05 02:45:19'),(725,'벅스',25,'Flashback','엔플라잉(N.Flying)','2026-06-05 02:45:19'),(726,'벅스',26,'LIVE FAST DIE SLOW','태양','2026-06-05 02:45:19'),(727,'벅스',27,'너에게 닿기를','10CM','2026-06-05 02:45:19'),(728,'벅스',28,'멸종위기사랑','이찬혁','2026-06-05 02:45:19'),(729,'벅스',29,'천상연','이창섭','2026-06-05 02:45:19'),(730,'벅스',30,'Who is she','KISS OF LIFE','2026-06-05 02:45:19'),(731,'벅스',31,'나의 하루처럼','성시경','2026-06-05 02:45:19'),(732,'벅스',32,'BUMPA','비비(BIBI)','2026-06-05 02:45:19'),(733,'벅스',33,'소나기','이클립스 (ECLIPSE)','2026-06-05 02:45:19'),(734,'벅스',34,'THAT’S A NO NO','ITZY (있지)','2026-06-05 02:45:19'),(735,'벅스',35,'주저하는 연인들을 위해','잔나비','2026-06-05 02:45:19'),(736,'벅스',36,'별이 될게','황치열','2026-06-05 02:45:19'),(737,'벅스',37,'OVERDRIVE','TWS (투어스)','2026-06-05 02:45:19'),(738,'벅스',38,'청춘만화','이무진','2026-06-05 02:45:19'),(739,'벅스',39,'So Cute','화사 (HWASA)','2026-06-05 02:45:19'),(740,'벅스',40,'타임캡슐','다비치','2026-06-05 02:45:19'),(741,'벅스',41,'like JENNIE','제니 (JENNIE)','2026-06-05 02:45:19'),(742,'벅스',42,'toxic till the end','로제(ROSÉ)','2026-06-05 02:45:19'),(743,'벅스',43,'첫 만남은 계획대로 되지 않아','TWS (투어스)','2026-06-05 02:45:19'),(744,'벅스',44,'BLACKHOLE','IVE (아이브)','2026-06-05 02:45:19'),(745,'벅스',45,'춤 (CHOOM)','BABYMONSTER','2026-06-05 02:45:19'),(746,'벅스',46,'Blue Valentine','NMIXX','2026-06-05 02:45:19'),(747,'벅스',47,'I AM','IVE (아이브)','2026-06-05 02:45:19'),(748,'벅스',48,'HAPPY','DAY6 (데이식스)','2026-06-05 02:45:19'),(749,'벅스',49,'NOT CUTE ANYMORE','아일릿(ILLIT)','2026-06-05 02:45:19'),(750,'벅스',50,'Whiplash','aespa','2026-06-05 02:45:19'),(751,'벅스',51,'Hype Boy','NewJeans','2026-06-05 02:45:19'),(752,'벅스',52,'봄 색깔','AKMU(악뮤)','2026-06-05 02:45:19'),(753,'벅스',53,'달리 표현할 수 없어요','로이킴','2026-06-05 02:45:19'),(754,'벅스',54,'Golden','HUNTR/X','2026-06-05 02:45:19'),(755,'벅스',55,'FAMOUS','ALLDAY PROJECT','2026-06-05 02:45:19'),(756,'벅스',56,'Supernova','aespa','2026-06-05 02:45:19'),(757,'벅스',57,'봄 내음보다 너를','김나영','2026-06-05 02:45:19'),(758,'벅스',58,'뛰어(JUMP)','BLACKPINK','2026-06-05 02:45:19'),(759,'벅스',59,'내게 사랑이 뭐냐고 물어본다면','로이킴','2026-06-05 02:45:19'),(760,'벅스',60,'FOCUS','Hearts2Hearts (하츠투하츠)','2026-06-05 02:45:19'),(761,'벅스',61,'사랑은 봄비처럼... 이별은 겨울비처럼','임현정','2026-06-05 02:45:19'),(762,'벅스',62,'에피소드','이무진','2026-06-05 02:45:19'),(763,'벅스',63,'Body to Body','방탄소년단','2026-06-05 02:45:19'),(764,'벅스',64,'SPAGHETTI (feat. j-hope of BTS)','LE SSERAFIM (르세라핌)','2026-06-05 02:45:19'),(765,'벅스',65,'APT.','로제(ROSÉ)','2026-06-05 02:45:19'),(766,'벅스',66,'모든 날, 모든 순간 (Every day, Every Moment)','폴킴(Paul Kim)','2026-06-05 02:45:19'),(767,'벅스',67,'띠로리 (DDI RO RI)','MEOVV (미야오)','2026-06-05 02:45:19'),(768,'벅스',68,'REBEL HEART','IVE (아이브)','2026-06-05 02:45:19'),(769,'벅스',69,'Love wins all','아이유(IU)','2026-06-05 02:45:19'),(770,'벅스',70,'Love me or Leave me','DAY6 (데이식스)','2026-06-05 02:45:19'),(771,'벅스',71,'어떻게 이별까지 사랑하겠어, 널 사랑하는 거지','AKMU(악뮤)','2026-06-05 02:45:19'),(772,'벅스',72,'SWIM','방탄소년단','2026-06-05 02:45:19'),(773,'벅스',73,'Die With A Smile','Lady Gaga(레이디 가가)','2026-06-05 02:45:19'),(774,'벅스',74,'햇빛 bless you','AKMU(악뮤)','2026-06-05 02:45:19'),(775,'벅스',75,'Welcome to the Show','DAY6 (데이식스)','2026-06-05 02:45:19'),(776,'벅스',76,'Congratulations','DAY6 (데이식스)','2026-06-05 02:45:19'),(777,'벅스',77,'고민중독','QWER','2026-06-05 02:45:19'),(778,'벅스',78,'Flower','오반(OVAN)','2026-06-05 02:45:19'),(779,'벅스',79,'하루에 하루만 더 (Stick With You)','투모로우바이투게더','2026-06-05 02:45:19'),(780,'벅스',80,'HOME SWEET HOME (feat. 태양, 대성)','G-DRAGON','2026-06-05 02:45:19'),(781,'벅스',81,'Ditto','NewJeans','2026-06-05 02:45:19'),(782,'벅스',82,'나는 반딧불','황가람','2026-06-05 02:45:19'),(783,'벅스',83,'그대만 있다면 (여름날 우리 X 너드커넥션 (Nerd Connection))','너드커넥션(Nerd Connection)','2026-06-05 02:45:19'),(784,'벅스',84,'Smile Boy','로이킴','2026-06-05 02:45:19'),(785,'벅스',85,'Soda Pop','Saja Boys','2026-06-05 02:45:19'),(786,'벅스',86,'Magnetic','아일릿(ILLIT)','2026-06-05 02:45:19'),(787,'벅스',87,'STYLE','Hearts2Hearts (하츠투하츠)','2026-06-05 02:45:19'),(788,'벅스',88,'시작의 아이 ❍','박다혜','2026-06-05 02:45:19'),(789,'벅스',89,'ONE MORE TIME','ALLDAY PROJECT','2026-06-05 02:45:19'),(790,'벅스',90,'I DO ME','KiiiKiii (키키)','2026-06-05 02:45:19'),(791,'벅스',91,'벌레를 내고','AKMU(악뮤)','2026-06-05 02:45:19'),(792,'벅스',92,'그대 작은 나의 세상이 되어','카더가든','2026-06-05 02:45:19'),(793,'벅스',93,'Atmos','SHINee (샤이니)','2026-06-05 02:45:19'),(794,'벅스',94,'마치 오늘처럼','정승환','2026-06-05 02:45:19'),(795,'벅스',95,'IF I','TREASURE(트레저)','2026-06-05 02:45:19'),(796,'벅스',96,'GO','BLACKPINK','2026-06-05 02:45:19'),(797,'벅스',97,'오늘만 I LOVE YOU','BOYNEXTDOOR','2026-06-05 02:45:19'),(798,'벅스',98,'XOXZ','IVE (아이브)','2026-06-05 02:45:19'),(799,'벅스',99,'나는 아픈 건 딱 질색이니까','i-dle (아이들)','2026-06-05 02:45:19'),(800,'벅스',100,'사랑인가 봐','멜로망스(MeloMance)','2026-06-05 02:45:19'),(801,'벅스',1,'갑자기','아이오아이(I.O.I)','2026-06-05 02:45:51'),(802,'벅스',2,'LEMONADE','aespa','2026-06-05 02:45:51'),(803,'벅스',3,'REDRED','CORTIS (코르티스)','2026-06-05 02:45:51'),(804,'벅스',4,'It′s Me','아일릿(ILLIT)','2026-06-05 02:45:51'),(805,'벅스',5,'WDA (Whole Different Animal) (Feat. G-DRAGON)','aespa','2026-06-05 02:45:51'),(806,'벅스',6,'LOVE ATTACK','RESCENE (리센느)','2026-06-05 02:45:51'),(807,'벅스',7,'소문의 낙원','AKMU(악뮤)','2026-06-05 02:45:51'),(808,'벅스',8,'Heavy Serenade','NMIXX','2026-06-05 02:45:51'),(809,'벅스',9,'기쁨, 슬픔, 아름다운 마음','AKMU(악뮤)','2026-06-05 02:45:51'),(810,'벅스',10,'0+0','한로로','2026-06-05 02:45:51'),(811,'벅스',11,'사랑하게 될 거야','한로로','2026-06-05 02:45:51'),(812,'벅스',12,'Drowning','WOODZ','2026-06-05 02:45:51'),(813,'벅스',13,'캐치 캐치','YENA (최예나)','2026-06-05 02:45:51'),(814,'벅스',14,'BOOMPALA','LE SSERAFIM (르세라핌)','2026-06-05 02:45:51'),(815,'벅스',15,'RUDE!','Hearts2Hearts (하츠투하츠)','2026-06-05 02:45:51'),(816,'벅스',16,'404 (New Era)','KiiiKiii (키키)','2026-06-05 02:45:51'),(817,'벅스',17,'Popcorn','도경수(D.O.)','2026-06-05 02:45:51'),(818,'벅스',18,'Good Goodbye','화사 (HWASA)','2026-06-05 02:45:51'),(819,'벅스',19,'입춘','한로로','2026-06-05 02:45:51'),(820,'벅스',20,'Baby Flower','tripleS (트리플에스)','2026-06-05 02:45:51'),(821,'벅스',21,'BANG BANG','IVE (아이브)','2026-06-05 02:45:51'),(822,'벅스',22,'4 Flowers','마마무(Mamamoo)','2026-06-05 02:45:51'),(823,'벅스',23,'모르시나요(PROD.로코베리)','조째즈','2026-06-05 02:45:51'),(824,'벅스',24,'한 페이지가 될 수 있게','DAY6 (데이식스)','2026-06-05 02:45:51'),(825,'벅스',25,'Flashback','엔플라잉(N.Flying)','2026-06-05 02:45:51'),(826,'벅스',26,'LIVE FAST DIE SLOW','태양','2026-06-05 02:45:51'),(827,'벅스',27,'너에게 닿기를','10CM','2026-06-05 02:45:51'),(828,'벅스',28,'멸종위기사랑','이찬혁','2026-06-05 02:45:51'),(829,'벅스',29,'천상연','이창섭','2026-06-05 02:45:51'),(830,'벅스',30,'Who is she','KISS OF LIFE','2026-06-05 02:45:51'),(831,'벅스',31,'나의 하루처럼','성시경','2026-06-05 02:45:51'),(832,'벅스',32,'BUMPA','비비(BIBI)','2026-06-05 02:45:51'),(833,'벅스',33,'소나기','이클립스 (ECLIPSE)','2026-06-05 02:45:51'),(834,'벅스',34,'THAT’S A NO NO','ITZY (있지)','2026-06-05 02:45:51'),(835,'벅스',35,'주저하는 연인들을 위해','잔나비','2026-06-05 02:45:51'),(836,'벅스',36,'별이 될게','황치열','2026-06-05 02:45:51'),(837,'벅스',37,'OVERDRIVE','TWS (투어스)','2026-06-05 02:45:51'),(838,'벅스',38,'청춘만화','이무진','2026-06-05 02:45:51'),(839,'벅스',39,'So Cute','화사 (HWASA)','2026-06-05 02:45:51'),(840,'벅스',40,'타임캡슐','다비치','2026-06-05 02:45:51'),(841,'벅스',41,'like JENNIE','제니 (JENNIE)','2026-06-05 02:45:51'),(842,'벅스',42,'toxic till the end','로제(ROSÉ)','2026-06-05 02:45:51'),(843,'벅스',43,'첫 만남은 계획대로 되지 않아','TWS (투어스)','2026-06-05 02:45:51'),(844,'벅스',44,'BLACKHOLE','IVE (아이브)','2026-06-05 02:45:51'),(845,'벅스',45,'춤 (CHOOM)','BABYMONSTER','2026-06-05 02:45:51'),(846,'벅스',46,'Blue Valentine','NMIXX','2026-06-05 02:45:51'),(847,'벅스',47,'I AM','IVE (아이브)','2026-06-05 02:45:51'),(848,'벅스',48,'HAPPY','DAY6 (데이식스)','2026-06-05 02:45:51'),(849,'벅스',49,'NOT CUTE ANYMORE','아일릿(ILLIT)','2026-06-05 02:45:51'),(850,'벅스',50,'Whiplash','aespa','2026-06-05 02:45:51'),(851,'벅스',51,'Hype Boy','NewJeans','2026-06-05 02:45:51'),(852,'벅스',52,'봄 색깔','AKMU(악뮤)','2026-06-05 02:45:51'),(853,'벅스',53,'달리 표현할 수 없어요','로이킴','2026-06-05 02:45:51'),(854,'벅스',54,'Golden','HUNTR/X','2026-06-05 02:45:51'),(855,'벅스',55,'FAMOUS','ALLDAY PROJECT','2026-06-05 02:45:51'),(856,'벅스',56,'Supernova','aespa','2026-06-05 02:45:51'),(857,'벅스',57,'봄 내음보다 너를','김나영','2026-06-05 02:45:51'),(858,'벅스',58,'뛰어(JUMP)','BLACKPINK','2026-06-05 02:45:51'),(859,'벅스',59,'내게 사랑이 뭐냐고 물어본다면','로이킴','2026-06-05 02:45:51'),(860,'벅스',60,'FOCUS','Hearts2Hearts (하츠투하츠)','2026-06-05 02:45:51'),(861,'벅스',61,'사랑은 봄비처럼... 이별은 겨울비처럼','임현정','2026-06-05 02:45:51'),(862,'벅스',62,'에피소드','이무진','2026-06-05 02:45:51'),(863,'벅스',63,'Body to Body','방탄소년단','2026-06-05 02:45:51'),(864,'벅스',64,'SPAGHETTI (feat. j-hope of BTS)','LE SSERAFIM (르세라핌)','2026-06-05 02:45:51'),(865,'벅스',65,'APT.','로제(ROSÉ)','2026-06-05 02:45:51'),(866,'벅스',66,'모든 날, 모든 순간 (Every day, Every Moment)','폴킴(Paul Kim)','2026-06-05 02:45:51'),(867,'벅스',67,'띠로리 (DDI RO RI)','MEOVV (미야오)','2026-06-05 02:45:51'),(868,'벅스',68,'REBEL HEART','IVE (아이브)','2026-06-05 02:45:51'),(869,'벅스',69,'Love wins all','아이유(IU)','2026-06-05 02:45:51'),(870,'벅스',70,'Love me or Leave me','DAY6 (데이식스)','2026-06-05 02:45:51'),(871,'벅스',71,'어떻게 이별까지 사랑하겠어, 널 사랑하는 거지','AKMU(악뮤)','2026-06-05 02:45:51'),(872,'벅스',72,'SWIM','방탄소년단','2026-06-05 02:45:51'),(873,'벅스',73,'Die With A Smile','Lady Gaga(레이디 가가)','2026-06-05 02:45:51'),(874,'벅스',74,'햇빛 bless you','AKMU(악뮤)','2026-06-05 02:45:51'),(875,'벅스',75,'Welcome to the Show','DAY6 (데이식스)','2026-06-05 02:45:51'),(876,'벅스',76,'Congratulations','DAY6 (데이식스)','2026-06-05 02:45:51'),(877,'벅스',77,'고민중독','QWER','2026-06-05 02:45:51'),(878,'벅스',78,'Flower','오반(OVAN)','2026-06-05 02:45:51'),(879,'벅스',79,'하루에 하루만 더 (Stick With You)','투모로우바이투게더','2026-06-05 02:45:51'),(880,'벅스',80,'HOME SWEET HOME (feat. 태양, 대성)','G-DRAGON','2026-06-05 02:45:51'),(881,'벅스',81,'Ditto','NewJeans','2026-06-05 02:45:51'),(882,'벅스',82,'나는 반딧불','황가람','2026-06-05 02:45:51'),(883,'벅스',83,'그대만 있다면 (여름날 우리 X 너드커넥션 (Nerd Connection))','너드커넥션(Nerd Connection)','2026-06-05 02:45:51'),(884,'벅스',84,'Smile Boy','로이킴','2026-06-05 02:45:51'),(885,'벅스',85,'Soda Pop','Saja Boys','2026-06-05 02:45:51'),(886,'벅스',86,'Magnetic','아일릿(ILLIT)','2026-06-05 02:45:51'),(887,'벅스',87,'STYLE','Hearts2Hearts (하츠투하츠)','2026-06-05 02:45:51'),(888,'벅스',88,'시작의 아이 ❍','박다혜','2026-06-05 02:45:51'),(889,'벅스',89,'ONE MORE TIME','ALLDAY PROJECT','2026-06-05 02:45:51'),(890,'벅스',90,'I DO ME','KiiiKiii (키키)','2026-06-05 02:45:51'),(891,'벅스',91,'벌레를 내고','AKMU(악뮤)','2026-06-05 02:45:51'),(892,'벅스',92,'그대 작은 나의 세상이 되어','카더가든','2026-06-05 02:45:51'),(893,'벅스',93,'Atmos','SHINee (샤이니)','2026-06-05 02:45:51'),(894,'벅스',94,'마치 오늘처럼','정승환','2026-06-05 02:45:51'),(895,'벅스',95,'IF I','TREASURE(트레저)','2026-06-05 02:45:51'),(896,'벅스',96,'GO','BLACKPINK','2026-06-05 02:45:51'),(897,'벅스',97,'오늘만 I LOVE YOU','BOYNEXTDOOR','2026-06-05 02:45:51'),(898,'벅스',98,'XOXZ','IVE (아이브)','2026-06-05 02:45:51'),(899,'벅스',99,'나는 아픈 건 딱 질색이니까','i-dle (아이들)','2026-06-05 02:45:51'),(900,'벅스',100,'사랑인가 봐','멜로망스(MeloMance)','2026-06-05 02:45:51'),(901,'벅스',1,'갑자기','아이오아이(I.O.I)','2026-06-05 02:46:11'),(902,'벅스',2,'LEMONADE','aespa','2026-06-05 02:46:11'),(903,'벅스',3,'REDRED','CORTIS (코르티스)','2026-06-05 02:46:11'),(904,'벅스',4,'It′s Me','아일릿(ILLIT)','2026-06-05 02:46:11'),(905,'벅스',5,'WDA (Whole Different Animal) (Feat. G-DRAGON)','aespa','2026-06-05 02:46:11'),(906,'벅스',6,'LOVE ATTACK','RESCENE (리센느)','2026-06-05 02:46:11'),(907,'벅스',7,'소문의 낙원','AKMU(악뮤)','2026-06-05 02:46:11'),(908,'벅스',8,'Heavy Serenade','NMIXX','2026-06-05 02:46:11'),(909,'벅스',9,'기쁨, 슬픔, 아름다운 마음','AKMU(악뮤)','2026-06-05 02:46:11'),(910,'벅스',10,'0+0','한로로','2026-06-05 02:46:11'),(911,'벅스',11,'사랑하게 될 거야','한로로','2026-06-05 02:46:11'),(912,'벅스',12,'Drowning','WOODZ','2026-06-05 02:46:11'),(913,'벅스',13,'캐치 캐치','YENA (최예나)','2026-06-05 02:46:11'),(914,'벅스',14,'BOOMPALA','LE SSERAFIM (르세라핌)','2026-06-05 02:46:11'),(915,'벅스',15,'RUDE!','Hearts2Hearts (하츠투하츠)','2026-06-05 02:46:11'),(916,'벅스',16,'404 (New Era)','KiiiKiii (키키)','2026-06-05 02:46:11'),(917,'벅스',17,'Popcorn','도경수(D.O.)','2026-06-05 02:46:11'),(918,'벅스',18,'Good Goodbye','화사 (HWASA)','2026-06-05 02:46:11'),(919,'벅스',19,'입춘','한로로','2026-06-05 02:46:11'),(920,'벅스',20,'Baby Flower','tripleS (트리플에스)','2026-06-05 02:46:11'),(921,'벅스',21,'BANG BANG','IVE (아이브)','2026-06-05 02:46:11'),(922,'벅스',22,'4 Flowers','마마무(Mamamoo)','2026-06-05 02:46:11'),(923,'벅스',23,'모르시나요(PROD.로코베리)','조째즈','2026-06-05 02:46:11'),(924,'벅스',24,'한 페이지가 될 수 있게','DAY6 (데이식스)','2026-06-05 02:46:11'),(925,'벅스',25,'Flashback','엔플라잉(N.Flying)','2026-06-05 02:46:11'),(926,'벅스',26,'LIVE FAST DIE SLOW','태양','2026-06-05 02:46:11'),(927,'벅스',27,'너에게 닿기를','10CM','2026-06-05 02:46:11'),(928,'벅스',28,'멸종위기사랑','이찬혁','2026-06-05 02:46:11'),(929,'벅스',29,'천상연','이창섭','2026-06-05 02:46:11'),(930,'벅스',30,'Who is she','KISS OF LIFE','2026-06-05 02:46:11'),(931,'벅스',31,'나의 하루처럼','성시경','2026-06-05 02:46:11'),(932,'벅스',32,'BUMPA','비비(BIBI)','2026-06-05 02:46:11'),(933,'벅스',33,'소나기','이클립스 (ECLIPSE)','2026-06-05 02:46:11'),(934,'벅스',34,'THAT’S A NO NO','ITZY (있지)','2026-06-05 02:46:11'),(935,'벅스',35,'주저하는 연인들을 위해','잔나비','2026-06-05 02:46:11'),(936,'벅스',36,'별이 될게','황치열','2026-06-05 02:46:11'),(937,'벅스',37,'OVERDRIVE','TWS (투어스)','2026-06-05 02:46:11'),(938,'벅스',38,'청춘만화','이무진','2026-06-05 02:46:11'),(939,'벅스',39,'So Cute','화사 (HWASA)','2026-06-05 02:46:11'),(940,'벅스',40,'타임캡슐','다비치','2026-06-05 02:46:11'),(941,'벅스',41,'like JENNIE','제니 (JENNIE)','2026-06-05 02:46:11'),(942,'벅스',42,'toxic till the end','로제(ROSÉ)','2026-06-05 02:46:11'),(943,'벅스',43,'첫 만남은 계획대로 되지 않아','TWS (투어스)','2026-06-05 02:46:11'),(944,'벅스',44,'BLACKHOLE','IVE (아이브)','2026-06-05 02:46:11'),(945,'벅스',45,'춤 (CHOOM)','BABYMONSTER','2026-06-05 02:46:11'),(946,'벅스',46,'Blue Valentine','NMIXX','2026-06-05 02:46:11'),(947,'벅스',47,'I AM','IVE (아이브)','2026-06-05 02:46:11'),(948,'벅스',48,'HAPPY','DAY6 (데이식스)','2026-06-05 02:46:11'),(949,'벅스',49,'NOT CUTE ANYMORE','아일릿(ILLIT)','2026-06-05 02:46:11'),(950,'벅스',50,'Whiplash','aespa','2026-06-05 02:46:11'),(951,'벅스',51,'Hype Boy','NewJeans','2026-06-05 02:46:11'),(952,'벅스',52,'봄 색깔','AKMU(악뮤)','2026-06-05 02:46:11'),(953,'벅스',53,'달리 표현할 수 없어요','로이킴','2026-06-05 02:46:11'),(954,'벅스',54,'Golden','HUNTR/X','2026-06-05 02:46:11'),(955,'벅스',55,'FAMOUS','ALLDAY PROJECT','2026-06-05 02:46:11'),(956,'벅스',56,'Supernova','aespa','2026-06-05 02:46:11'),(957,'벅스',57,'봄 내음보다 너를','김나영','2026-06-05 02:46:11'),(958,'벅스',58,'뛰어(JUMP)','BLACKPINK','2026-06-05 02:46:11'),(959,'벅스',59,'내게 사랑이 뭐냐고 물어본다면','로이킴','2026-06-05 02:46:11'),(960,'벅스',60,'FOCUS','Hearts2Hearts (하츠투하츠)','2026-06-05 02:46:11'),(961,'벅스',61,'사랑은 봄비처럼... 이별은 겨울비처럼','임현정','2026-06-05 02:46:11'),(962,'벅스',62,'에피소드','이무진','2026-06-05 02:46:11'),(963,'벅스',63,'Body to Body','방탄소년단','2026-06-05 02:46:11'),(964,'벅스',64,'SPAGHETTI (feat. j-hope of BTS)','LE SSERAFIM (르세라핌)','2026-06-05 02:46:11'),(965,'벅스',65,'APT.','로제(ROSÉ)','2026-06-05 02:46:11'),(966,'벅스',66,'모든 날, 모든 순간 (Every day, Every Moment)','폴킴(Paul Kim)','2026-06-05 02:46:11'),(967,'벅스',67,'띠로리 (DDI RO RI)','MEOVV (미야오)','2026-06-05 02:46:11'),(968,'벅스',68,'REBEL HEART','IVE (아이브)','2026-06-05 02:46:11'),(969,'벅스',69,'Love wins all','아이유(IU)','2026-06-05 02:46:11'),(970,'벅스',70,'Love me or Leave me','DAY6 (데이식스)','2026-06-05 02:46:11'),(971,'벅스',71,'어떻게 이별까지 사랑하겠어, 널 사랑하는 거지','AKMU(악뮤)','2026-06-05 02:46:11'),(972,'벅스',72,'SWIM','방탄소년단','2026-06-05 02:46:11'),(973,'벅스',73,'Die With A Smile','Lady Gaga(레이디 가가)','2026-06-05 02:46:11'),(974,'벅스',74,'햇빛 bless you','AKMU(악뮤)','2026-06-05 02:46:11'),(975,'벅스',75,'Welcome to the Show','DAY6 (데이식스)','2026-06-05 02:46:11'),(976,'벅스',76,'Congratulations','DAY6 (데이식스)','2026-06-05 02:46:11'),(977,'벅스',77,'고민중독','QWER','2026-06-05 02:46:11'),(978,'벅스',78,'Flower','오반(OVAN)','2026-06-05 02:46:11'),(979,'벅스',79,'하루에 하루만 더 (Stick With You)','투모로우바이투게더','2026-06-05 02:46:11'),(980,'벅스',80,'HOME SWEET HOME (feat. 태양, 대성)','G-DRAGON','2026-06-05 02:46:11'),(981,'벅스',81,'Ditto','NewJeans','2026-06-05 02:46:11'),(982,'벅스',82,'나는 반딧불','황가람','2026-06-05 02:46:11'),(983,'벅스',83,'그대만 있다면 (여름날 우리 X 너드커넥션 (Nerd Connection))','너드커넥션(Nerd Connection)','2026-06-05 02:46:11'),(984,'벅스',84,'Smile Boy','로이킴','2026-06-05 02:46:11'),(985,'벅스',85,'Soda Pop','Saja Boys','2026-06-05 02:46:11'),(986,'벅스',86,'Magnetic','아일릿(ILLIT)','2026-06-05 02:46:11'),(987,'벅스',87,'STYLE','Hearts2Hearts (하츠투하츠)','2026-06-05 02:46:11'),(988,'벅스',88,'시작의 아이 ❍','박다혜','2026-06-05 02:46:11'),(989,'벅스',89,'ONE MORE TIME','ALLDAY PROJECT','2026-06-05 02:46:11'),(990,'벅스',90,'I DO ME','KiiiKiii (키키)','2026-06-05 02:46:11'),(991,'벅스',91,'벌레를 내고','AKMU(악뮤)','2026-06-05 02:46:11'),(992,'벅스',92,'그대 작은 나의 세상이 되어','카더가든','2026-06-05 02:46:11'),(993,'벅스',93,'Atmos','SHINee (샤이니)','2026-06-05 02:46:11'),(994,'벅스',94,'마치 오늘처럼','정승환','2026-06-05 02:46:11'),(995,'벅스',95,'IF I','TREASURE(트레저)','2026-06-05 02:46:11'),(996,'벅스',96,'GO','BLACKPINK','2026-06-05 02:46:11'),(997,'벅스',97,'오늘만 I LOVE YOU','BOYNEXTDOOR','2026-06-05 02:46:11'),(998,'벅스',98,'XOXZ','IVE (아이브)','2026-06-05 02:46:11'),(999,'벅스',99,'나는 아픈 건 딱 질색이니까','i-dle (아이들)','2026-06-05 02:46:11'),(1000,'벅스',100,'사랑인가 봐','멜로망스(MeloMance)','2026-06-05 02:46:11'),(1001,'멜론',1,'갑자기','아이오아이 (I.O.I)','2026-06-05 02:46:11'),(1002,'멜론',2,'REDRED','CORTIS (코르티스)','2026-06-05 02:46:11'),(1003,'멜론',3,'It′s Me','아일릿(ILLIT)','2026-06-05 02:46:11'),(1004,'멜론',4,'소문의 낙원','AKMU (악뮤)','2026-06-05 02:46:11'),(1005,'멜론',5,'LEMONADE','aespa','2026-06-05 02:46:11'),(1006,'멜론',6,'기쁨, 슬픔, 아름다운 마음','AKMU (악뮤)','2026-06-05 02:46:11'),(1007,'멜론',7,'캐치 캐치','YENA (최예나)','2026-06-05 02:46:11'),(1008,'멜론',8,'RUDE!','Hearts2Hearts (하츠투하츠)','2026-06-05 02:46:11'),(1009,'멜론',9,'사랑하게 될 거야','한로로','2026-06-05 02:46:11'),(1010,'멜론',10,'Heavy Serenade','NMIXX','2026-06-05 02:46:11'),(1011,'멜론',11,'Drowning','WOODZ','2026-06-05 02:46:11'),(1012,'멜론',12,'WDA (Whole Different Animal) (Feat. G-DRAGON)','aespa','2026-06-05 02:46:11'),(1013,'멜론',13,'0+0','한로로','2026-06-05 02:46:11'),(1014,'멜론',14,'404 (New Era)','KiiiKiii (키키)','2026-06-05 02:46:11'),(1015,'멜론',15,'BANG BANG','IVE (아이브)','2026-06-05 02:46:11'),(1016,'멜론',16,'Good Goodbye','화사 (HWASA)','2026-06-05 02:46:11'),(1017,'멜론',17,'SWIM','방탄소년단','2026-06-05 02:46:11'),(1018,'멜론',18,'LOVE ATTACK','RESCENE (리센느)','2026-06-05 02:46:11'),(1019,'멜론',19,'타임캡슐','다비치','2026-06-05 02:46:11'),(1020,'멜론',20,'Popcorn','도경수(D.O.)','2026-06-05 02:46:11'),(1021,'멜론',21,'너에게 닿기를','10CM','2026-06-05 02:46:11'),(1022,'멜론',22,'Blue Valentine','NMIXX','2026-06-05 02:46:11'),(1023,'멜론',23,'멸종위기사랑','이찬혁','2026-06-05 02:46:11'),(1024,'멜론',24,'어떻게 이별까지 사랑하겠어, 널 사랑하는 거지','AKMU (악뮤)','2026-06-05 02:46:11'),(1025,'멜론',25,'Body to Body','방탄소년단','2026-06-05 02:46:11'),(1026,'멜론',26,'어제보다 슬픈 오늘','우디 (Woody)','2026-06-05 02:46:11'),(1027,'멜론',27,'뛰어(JUMP)','BLACKPINK','2026-06-05 02:46:11'),(1028,'멜론',28,'너의 모든 순간','성시경','2026-06-05 02:46:11'),(1029,'멜론',29,'그대 작은 나의 세상이 되어','카더가든','2026-06-05 02:46:11'),(1030,'멜론',30,'Golden','HUNTR/X','2026-06-05 02:46:11'),(1031,'멜론',31,'소나기','이클립스 (ECLIPSE)','2026-06-05 02:46:11'),(1032,'멜론',32,'BOOMPALA','LE SSERAFIM (르세라핌)','2026-06-05 02:46:11'),(1033,'멜론',33,'모르시나요(PROD.로코베리)','조째즈','2026-06-05 02:46:11'),(1034,'멜론',34,'내게 사랑이 뭐냐고 물어본다면','로이킴','2026-06-05 02:46:11'),(1035,'멜론',35,'toxic till the end','로제 (ROSÉ)','2026-06-05 02:46:11'),(1036,'멜론',36,'Whiplash','aespa','2026-06-05 02:46:11'),(1037,'멜론',37,'천상연','이창섭','2026-06-05 02:46:11'),(1038,'멜론',38,'HOME SWEET HOME (feat. 태양, 대성)','G-DRAGON','2026-06-05 02:46:11'),(1039,'멜론',39,'청춘만화','이무진','2026-06-05 02:46:11'),(1040,'멜론',40,'한 페이지가 될 수 있게','DAY6 (데이식스)','2026-06-05 02:46:11'),(1041,'멜론',41,'2.0','방탄소년단','2026-06-05 02:46:11'),(1042,'멜론',42,'HAPPY','DAY6 (데이식스)','2026-06-05 02:46:11'),(1043,'멜론',43,'그대만 있다면 (여름날 우리 X 너드커넥션 (Nerd Connection))','너드커넥션 (Nerd Connection)','2026-06-05 02:46:11'),(1044,'멜론',44,'봄날','방탄소년단','2026-06-05 02:46:11'),(1045,'멜론',45,'like JENNIE','제니 (JENNIE)','2026-06-05 02:46:11'),(1046,'멜론',46,'Seven (feat. Latto) - Clean Ver.','정국','2026-06-05 02:46:11'),(1047,'멜론',47,'Hooligan','방탄소년단','2026-06-05 02:46:11'),(1048,'멜론',48,'BLACKHOLE','IVE (아이브)','2026-06-05 02:46:11'),(1049,'멜론',49,'사랑은 늘 도망가','임영웅','2026-06-05 02:46:11'),(1050,'멜론',50,'입춘','한로로','2026-06-05 02:46:11'),(1051,'멜론',51,'모든 날, 모든 순간 (Every day, Every Moment)','폴킴','2026-06-05 02:46:11'),(1052,'멜론',52,'사랑인가 봐','멜로망스','2026-06-05 02:46:11'),(1053,'멜론',53,'주저하는 연인들을 위해','잔나비','2026-06-05 02:46:11'),(1054,'멜론',54,'SPAGHETTI (feat. j-hope of BTS)','LE SSERAFIM (르세라핌)','2026-06-05 02:46:11'),(1055,'멜론',55,'예뻤어','DAY6 (데이식스)','2026-06-05 02:46:11'),(1056,'멜론',56,'나는 반딧불','황가람','2026-06-05 02:46:11'),(1057,'멜론',57,'오늘만 I LOVE YOU','BOYNEXTDOOR','2026-06-05 02:46:11'),(1058,'멜론',58,'청혼하지 않을 이유를 못 찾았어','이무진','2026-06-05 02:46:11'),(1059,'멜론',59,'FAMOUS','ALLDAY PROJECT','2026-06-05 02:46:11'),(1060,'멜론',60,'STYLE','Hearts2Hearts (하츠투하츠)','2026-06-05 02:46:11'),(1061,'멜론',61,'사랑은 봄비처럼...이별은 겨울비처럼...','임현정','2026-06-05 02:46:11'),(1062,'멜론',62,'눈을 감아도(2026)','순순희(지환)','2026-06-05 02:46:11'),(1063,'멜론',63,'Love Love Love (Feat. Yoong Jin Of Casker)','에픽하이 (EPIK HIGH)','2026-06-05 02:46:11'),(1064,'멜론',64,'Welcome to the Show','DAY6 (데이식스)','2026-06-05 02:46:11'),(1065,'멜론',65,'APT.','로제 (ROSÉ)','2026-06-05 02:46:11'),(1066,'멜론',66,'첫 만남은 계획대로 되지 않아','TWS (투어스)','2026-06-05 02:46:11'),(1067,'멜론',67,'LIVE FAST DIE SLOW','태양','2026-06-05 02:46:11'),(1068,'멜론',68,'FYA','방탄소년단','2026-06-05 02:46:11'),(1069,'멜론',69,'TICK TOCK (Feat. ZICO) (Prod. by ZICO, Crush)','김하온 (HAON)','2026-06-05 02:46:11'),(1070,'멜론',70,'Dynamite','방탄소년단','2026-06-05 02:46:11'),(1071,'멜론',71,'달리 표현할 수 없어요','로이킴','2026-06-05 02:46:11'),(1072,'멜론',72,'봄 내음보다 너를','김나영','2026-06-05 02:46:11'),(1073,'멜론',73,'REBEL HEART','IVE (아이브)','2026-06-05 02:46:11'),(1074,'멜론',74,'시작의 아이 ❍','박다혜','2026-06-05 02:46:11'),(1075,'멜론',75,'다정히 내 이름을 부르면','경서예지','2026-06-05 02:46:11'),(1076,'멜론',76,'Flower','오반(OVAN)','2026-06-05 02:46:11'),(1077,'멜론',77,'ONE MORE TIME','ALLDAY PROJECT','2026-06-05 02:46:11'),(1078,'멜론',78,'Like Animals','방탄소년단','2026-06-05 02:46:11'),(1079,'멜론',79,'Aliens','방탄소년단','2026-06-05 02:46:11'),(1080,'멜론',80,'Love wins all','아이유','2026-06-05 02:46:11'),(1081,'멜론',81,'헤어지자 말해요','박재정','2026-06-05 02:46:11'),(1082,'멜론',82,'OVERDRIVE','TWS (투어스)','2026-06-05 02:46:11'),(1083,'멜론',83,'이 밤을 빌려 말해요','PLAVE','2026-06-05 02:46:11'),(1084,'멜론',84,'Die With A Smile','Lady Gaga','2026-06-05 02:46:11'),(1085,'멜론',85,'FOCUS','Hearts2Hearts (하츠투하츠)','2026-06-05 02:46:11'),(1086,'멜론',86,'Magnetic','아일릿(ILLIT)','2026-06-05 02:46:11'),(1087,'멜론',87,'KISS KISS KISS (Feat. 선우 (THE BOYZ)) (Prod. by Hukky Shibaseki)','NOWIMYOUNG (나우아임영)','2026-06-05 02:46:11'),(1088,'멜론',88,'Merry Go Round','방탄소년단','2026-06-05 02:46:11'),(1089,'멜론',89,'에피소드','이무진','2026-06-05 02:46:11'),(1090,'멜론',90,'Hype Boy','NewJeans','2026-06-05 02:46:11'),(1091,'멜론',91,'순간을 영원처럼','임영웅','2026-06-05 02:46:11'),(1092,'멜론',92,'One More Night','방탄소년단','2026-06-05 02:46:11'),(1093,'멜론',93,'Flashback','엔플라잉 (N.Flying)','2026-06-05 02:46:11'),(1094,'멜론',94,'Never Ending Story','아이유','2026-06-05 02:46:11'),(1095,'멜론',95,'하루에 하루만 더 (Stick With You)','투모로우바이투게더','2026-06-05 02:46:11'),(1096,'멜론',96,'NOT CUTE ANYMORE','아일릿(ILLIT)','2026-06-05 02:46:11'),(1097,'멜론',97,'I AM','IVE (아이브)','2026-06-05 02:46:11'),(1098,'멜론',98,'우리들의 블루스','임영웅','2026-06-05 02:46:11'),(1099,'멜론',99,'Soda Pop','KPop Demon Hunters Cast','2026-06-05 02:46:11'),(1100,'멜론',100,'Smile Boy','로이킴','2026-06-05 02:46:11'),(1101,'지니',1,'갑자기','아이오아이 (I.O.I)','2026-06-05 02:46:11'),(1102,'지니',2,'It\'s Me','아일릿(ILLIT)','2026-06-05 02:46:11'),(1103,'지니',3,'소문의 낙원','AKMU (악뮤)','2026-06-05 02:46:11'),(1104,'지니',4,'REDRED','CORTIS (코르티스)','2026-06-05 02:46:11'),(1105,'지니',5,'캐치 캐치','YENA (최예나)','2026-06-05 02:46:11'),(1106,'지니',6,'기쁨, 슬픔, 아름다운 마음','AKMU (악뮤)','2026-06-05 02:46:11'),(1107,'지니',7,'Drowning','WOODZ','2026-06-05 02:46:11'),(1108,'지니',8,'사랑하게 될 거야','한로로','2026-06-05 02:46:11'),(1109,'지니',9,'0＋0','한로로','2026-06-05 02:46:11'),(1110,'지니',10,'BANG BANG','IVE (아이브)','2026-06-05 02:46:11'),(1111,'지니',11,'Good Goodbye','화사 (HWASA)','2026-06-05 02:46:11'),(1112,'지니',12,'404 (New Era)','KiiiKiii (키키)','2026-06-05 02:46:11'),(1113,'지니',13,'Popcorn','도경수 (D.O.)','2026-06-05 02:46:11'),(1114,'지니',14,'타임캡슐','다비치','2026-06-05 02:46:11'),(1115,'지니',15,'RUDE!','Hearts2Hearts (하츠투하츠)','2026-06-05 02:46:11'),(1116,'지니',16,'멸종위기사랑','이찬혁','2026-06-05 02:46:11'),(1117,'지니',17,'LEMONADE','aespa','2026-06-05 02:46:11'),(1118,'지니',18,'너에게 닿기를','10CM','2026-06-05 02:46:11'),(1119,'지니',19,'WDA (Whole Different Animal) (Feat. G-DRAGON)','aespa','2026-06-05 02:46:11'),(1120,'지니',20,'뛰어(JUMP)','BLACKPINK','2026-06-05 02:46:11'),(1121,'지니',21,'내게 사랑이 뭐냐고 물어본다면','로이킴','2026-06-05 02:46:11'),(1122,'지니',22,'Golden','HUNTR/X & EJAE & Audrey Nuna & REI AMI & KPop Demon Hunters Cast','2026-06-05 02:46:11'),(1123,'지니',23,'Blue Valentine','NMIXX','2026-06-05 02:46:11'),(1124,'지니',24,'모르시나요 (Prod. by 로코베리)','조째즈','2026-06-05 02:46:11'),(1125,'지니',25,'어제보다 슬픈 오늘','우디 (Woody)','2026-06-05 02:46:11'),(1126,'지니',26,'청춘만화','이무진','2026-06-05 02:46:11'),(1127,'지니',27,'입춘','한로로','2026-06-05 02:46:11'),(1128,'지니',28,'사랑은 늘 도망가','임영웅','2026-06-05 02:46:11'),(1129,'지니',29,'Heavy Serenade','NMIXX','2026-06-05 02:46:11'),(1130,'지니',30,'어떻게 이별까지 사랑하겠어, 널 사랑하는 거지','AKMU (악뮤)','2026-06-05 02:46:11'),(1131,'지니',31,'봄 내음보다 너를','김나영','2026-06-05 02:46:11'),(1132,'지니',32,'toxic till the end','로제 (ROSÉ)','2026-06-05 02:46:11'),(1133,'지니',33,'HAPPY','DAY6 (데이식스)','2026-06-05 02:46:11'),(1134,'지니',34,'다시 만날 수 있을까','임영웅','2026-06-05 02:46:11'),(1135,'지니',35,'우리들의 블루스','임영웅','2026-06-05 02:46:11'),(1136,'지니',36,'그대 작은 나의 세상이 되어','카더가든','2026-06-05 02:46:11'),(1137,'지니',37,'시작의 아이','마크툽 (Maktub)','2026-06-05 02:46:11'),(1138,'지니',38,'Whiplash','aespa','2026-06-05 02:46:11'),(1139,'지니',39,'순간을 영원처럼','임영웅','2026-06-05 02:46:11'),(1140,'지니',40,'소나기','이클립스 (ECLIPSE)','2026-06-05 02:46:11'),(1141,'지니',41,'한 페이지가 될 수 있게','DAY6 (데이식스)','2026-06-05 02:46:11'),(1142,'지니',42,'나는 반딧불','황가람','2026-06-05 02:46:11'),(1143,'지니',43,'LOVE ATTACK','RESCENE (리센느)','2026-06-05 02:46:11'),(1144,'지니',44,'너의 모든 순간','성시경','2026-06-05 02:46:11'),(1145,'지니',45,'돌아보지 마세요','임영웅','2026-06-05 02:46:11'),(1146,'지니',46,'HOME SWEET HOME (Feat. 태양 & 대성)','G-DRAGON','2026-06-05 02:46:11'),(1147,'지니',47,'그댈 위한 멜로디','임영웅','2026-06-05 02:46:11'),(1148,'지니',48,'천국보다 아름다운','임영웅','2026-06-05 02:46:11'),(1149,'지니',49,'답장을 보낸지','임영웅','2026-06-05 02:46:11'),(1150,'지니',50,'우리에게 안녕','임영웅','2026-06-05 02:46:11'),(1151,'지니',51,'들꽃이 될게요','임영웅','2026-06-05 02:46:11'),(1152,'지니',52,'Pretender','OFFICIAL HIGE DANDISM','2026-06-05 02:46:11'),(1153,'지니',53,'SWIM','방탄소년단','2026-06-05 02:46:11'),(1154,'지니',54,'비가 와서','임영웅','2026-06-05 02:46:11'),(1155,'지니',55,'like JENNIE','제니 (JENNIE)','2026-06-05 02:46:11'),(1156,'지니',56,'ULSSIGU','임영웅','2026-06-05 02:46:11'),(1157,'지니',57,'알겠어요 미안해요','임영웅','2026-06-05 02:46:11'),(1158,'지니',58,'Wonderful Life','임영웅','2026-06-05 02:46:11'),(1159,'지니',59,'나는야 HERO','임영웅','2026-06-05 02:46:11'),(1160,'지니',60,'천상연','이창섭','2026-06-05 02:46:11'),(1161,'지니',61,'달리 표현할 수 없어요','로이킴','2026-06-05 02:46:11'),(1162,'지니',62,'Welcome to the Show','DAY6 (데이식스)','2026-06-05 02:46:11'),(1163,'지니',63,'예뻤어','DAY6 (데이식스)','2026-06-05 02:46:11'),(1164,'지니',64,'사건의 지평선','윤하 (YOUNHA)','2026-06-05 02:46:11'),(1165,'지니',65,'벌써 일년','브라운 아이즈','2026-06-05 02:46:11'),(1166,'지니',66,'APT.','로제 (ROSÉ) & Bruno Mars','2026-06-05 02:46:11'),(1167,'지니',67,'에피소드','이무진','2026-06-05 02:46:11'),(1168,'지니',68,'주저하는 연인들을 위해','잔나비','2026-06-05 02:46:11'),(1169,'지니',69,'REBEL HEART','IVE (아이브)','2026-06-05 02:46:11'),(1170,'지니',70,'Cruel Summer','Taylor Swift','2026-06-05 02:46:11'),(1171,'지니',71,'Soda Pop','Saja Boys & Andrew Choi & Neckwav & Danny Chung & Kevin Woo & samUIL Lee & KPop Demon Hunters Cast','2026-06-05 02:46:11'),(1172,'지니',72,'사랑인가 봐','멜로망스 (MeloMance)','2026-06-05 02:46:11'),(1173,'지니',73,'눈을 감아도(2026)','순순희 (지환)','2026-06-05 02:46:11'),(1174,'지니',74,'TICK TOCK (Feat. ZICO) (Prod. by ZICO, Crush)','김하온 (HAON) & Nosun & Raf Sandou & Marv & 정준혁','2026-06-05 02:46:11'),(1175,'지니',75,'고민중독','QWER','2026-06-05 02:46:11'),(1176,'지니',76,'MY LOVE (2025)','이예은 & 아샤트리 & 전건호','2026-06-05 02:46:11'),(1177,'지니',77,'슬픈 초대장','순순희 (지환)','2026-06-05 02:46:11'),(1178,'지니',78,'BLACKHOLE','IVE (아이브)','2026-06-05 02:46:11'),(1179,'지니',79,'Die With A Smile','Lady Gaga & Bruno Mars','2026-06-05 02:46:11'),(1180,'지니',80,'Flashback','엔플라잉 (N.Flying)','2026-06-05 02:46:11'),(1181,'지니',81,'FAMOUS','ALLDAY PROJECT','2026-06-05 02:46:11'),(1182,'지니',82,'BOOMPALA','LE SSERAFIM (르세라핌)','2026-06-05 02:46:11'),(1183,'지니',83,'모든 날, 모든 순간 (Every day, Every Moment)','폴킴','2026-06-05 02:46:11'),(1184,'지니',84,'시작의 아이 ❍','박다혜 & 마크툽 (Maktub)','2026-06-05 02:46:11'),(1185,'지니',85,'떠나가요, 떠나지마요 : 시대를 초월한 마음','순순희 (기태) & 백예슬','2026-06-05 02:46:11'),(1186,'지니',86,'Stay','The Kid LAROI & Justin Bieber','2026-06-05 02:46:11'),(1187,'지니',87,'LIVE FAST DIE SLOW','태양','2026-06-05 02:46:11'),(1188,'지니',88,'가까운 듯 먼 그대여','카더가든','2026-06-05 02:46:11'),(1189,'지니',89,'그래 늦지 않았어 (2025)','아샤트리 & 이예은 & 전건호','2026-06-05 02:46:11'),(1190,'지니',90,'Love Love Love (Feat. Yoong Jin of Casker))','에픽하이 (EPIK HIGH)','2026-06-05 02:46:11'),(1191,'지니',91,'Body to Body','방탄소년단','2026-06-05 02:46:11'),(1192,'지니',92,'첫 만남은 계획대로 되지 않아','TWS (투어스)','2026-06-05 02:46:11'),(1193,'지니',93,'그대만 있다면 (여름날 우리 X 너드커넥션 (Nerd Connection))','너드커넥션 (Nerd Connection)','2026-06-05 02:46:11'),(1194,'지니',94,'희재','성시경','2026-06-05 02:46:11'),(1195,'지니',95,'다정히 내 이름을 부르면','경서예지 & 전건호','2026-06-05 02:46:11'),(1196,'지니',96,'청혼하지 않을 이유를 못 찾았어','이무진','2026-06-05 02:46:11'),(1197,'지니',97,'TOO BAD (Feat. Anderson .Paak)','G-DRAGON','2026-06-05 02:46:11'),(1198,'지니',98,'비의 랩소디','임재현','2026-06-05 02:46:11'),(1199,'지니',99,'내 이름 맑음','QWER','2026-06-05 02:46:11'),(1200,'지니',100,'사막에서 꽃을 피우듯','우디 (Woody)','2026-06-05 02:46:11');
/*!40000 ALTER TABLE `musicchart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `phonebook`
--

DROP TABLE IF EXISTS `phonebook`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `phonebook` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(80) COLLATE utf8mb4_unicode_ci NOT NULL,
  `phonenum` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT '010-0000-0000',
  `email` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `regdate` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phonebook`
--

LOCK TABLES `phonebook` WRITE;
/*!40000 ALTER TABLE `phonebook` DISABLE KEYS */;
INSERT INTO `phonebook` VALUES (4,'아이언맨','111-1111-1111','ironman@mail.com','2026-04-28 05:25:16'),(5,'캡틴아메리카','222-2222-2222','captain@mail.com','2026-04-28 05:25:16'),(6,'토르','3333-3333-3333','thor@mail.com','2026-04-28 05:25:16'),(7,'양정운','010-0000-0000',NULL,'2026-05-07 23:57:47');
/*!40000 ALTER TABLE `phonebook` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `r_book`
--

DROP TABLE IF EXISTS `r_book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `r_book` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '도서 제목',
  `author` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '도서 저자',
  `created_at` datetime NOT NULL DEFAULT (now()) COMMENT '도서 등록 일시',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `r_book`
--

LOCK TABLES `r_book` WRITE;
/*!40000 ALTER TABLE `r_book` DISABLE KEYS */;
INSERT INTO `r_book` VALUES (1,'객체지향의 사실과 오해','조영호','2026-06-15 06:13:30'),(2,'클린 코드','로버트 마틴','2026-06-15 06:13:30'),(3,'이펙티브 파이썬','브렛 슬라킨','2026-06-15 06:13:30'),(4,'FastAPI를 사용한 파이썬 웹 개발','압둘라지즈 압둘라지즈 아디','2026-06-15 06:13:30'),(5,'혼자 공부하는 파이썬','윤인성','2026-06-15 06:13:30'),(6,'Do it! 점프 투 파이썬','박응용','2026-06-15 06:13:30'),(9,'오늘 뭐 먹지','최홍묵','2026-06-15 08:02:41'),(10,'메롱~~~~~~~~~~','최홍묵이','2026-06-15 08:06:36'),(11,'27분전 ~','집에 가자','2026-06-15 08:23:13');
/*!40000 ALTER TABLE `r_book` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `r_post`
--

DROP TABLE IF EXISTS `r_post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `r_post` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '작성자',
  `subject` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '게시글 제목',
  `content` text COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '게시글 내용',
  `viewcnt` int NOT NULL COMMENT '게시글 조회수',
  `created_at` datetime NOT NULL DEFAULT (now()) COMMENT '게시글 작성일',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `r_post`
--

LOCK TABLES `r_post` WRITE;
/*!40000 ALTER TABLE `r_post` DISABLE KEYS */;
INSERT INTO `r_post` VALUES (1,'홍길동','가나다라','마바사아',0,'2026-06-16 02:13:54'),(2,'나폴레옹','abcd','efgh',0,'2026-06-16 02:13:54'),(3,'아이언맨','I am IronMan','나는 아이언맨',2,'2026-06-16 02:13:54'),(4,'캡틴아메리카','I am loser','나는 찌질이',3,'2026-06-16 02:13:54'),(5,'최홍묵','메롱메롱','',0,'2026-06-16 03:26:36'),(7,'Doky123','밖에 비온다','주륵주륵 네 통장에 비온다 주륵주륵 밖에 비온다 주륵주륵주륵',1,'2026-06-16 05:37:08'),(8,'비와이','영원히 ','비와',5,'2026-06-16 06:11:32'),(9,'스겜','스겜123qew','스게게게게',7,'2026-06-16 06:55:33');
/*!40000 ALTER TABLE `r_post` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `r_survey`
--

DROP TABLE IF EXISTS `r_survey`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `r_survey` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '이름',
  `age` int NOT NULL COMMENT '나이',
  `gender` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'MALE' COMMENT '성별',
  `area` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '거주지역',
  `favorite` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '이상형(들)',
  `created_at` datetime NOT NULL DEFAULT (now()) COMMENT '작성일',
  PRIMARY KEY (`id`),
  CONSTRAINT `check_age_non_negative` CHECK ((`age` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `r_survey`
--

LOCK TABLES `r_survey` WRITE;
/*!40000 ALTER TABLE `r_survey` DISABLE KEYS */;
INSERT INTO `r_survey` VALUES (1,'홍길동',21,'MALE','서울','고윤정,장원영,카리나','2026-06-17 05:31:20'),(2,'최홍묵',31,'MALE','경기도','고윤정','2026-06-17 05:31:20'),(3,'아이언맨',41,'MALE','서울','카리나,장원영','2026-06-17 05:31:20'),(4,'캡틴아메리카',71,'MALE','서울','카리나','2026-06-17 05:31:20'),(5,'손흥민',35,'MALE','기타','장원영,카리나','2026-06-17 07:14:00'),(8,'이강인',31,'MALE','서울','카리나,장원영','2026-06-17 07:39:03'),(12,'추아홀',36,'MALE','기타','장원영,카리나','2026-06-17 08:10:09');
/*!40000 ALTER TABLE `r_survey` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_credit`
--

DROP TABLE IF EXISTS `t_credit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_credit` (
  `grade` char(3) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `min_point` int DEFAULT NULL,
  `max_point` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_credit`
--

LOCK TABLES `t_credit` WRITE;
/*!40000 ALTER TABLE `t_credit` DISABLE KEYS */;
INSERT INTO `t_credit` VALUES ('A+',96,100),('A0',90,95),('B+',86,89),('B0',80,85),('C+',76,79),('C0',70,75),('D',0,69);
/*!40000 ALTER TABLE `t_credit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_customer`
--

DROP TABLE IF EXISTS `t_customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_customer` (
  `c_no` int DEFAULT NULL,
  `c_name` varchar(12) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `c_jumin` char(13) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `c_point` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_customer`
--

LOCK TABLES `t_customer` WRITE;
/*!40000 ALTER TABLE `t_customer` DISABLE KEYS */;
INSERT INTO `t_customer` VALUES (20110001,'서진수','8510231369824',980000),(20110002,'서재수','8502241128467',73000),(20110003,'이미경','8506152123648',320000),(20110004,'김재수','8512251063421',65000),(20110005,'박동호','8503031639826',180000),(20110006,'김신영','8601232186327',153000),(20110007,'신은경','8604212298371',273000),(20110008,'오나라','8609112118379',315000),(20110009,'김설희','8601202378641',542000),(20110010,'임세현','8610122196482',265000),(20110011,'최순규','8711291186223',110000),(20110012,'정현영','8704021358674',99000),(20110013,'안광훈','8709131276431',470000),(20110014,'모병환','8702261196365',298000),(20110015,'노정호','8712141254963',420000),(20110016,'이윤나','8808192157498',598000),(20110017,'안은수','8801051776346',625000),(20110018,'인영민','8808091786954',670000),(20110019,'김지영','8803242114563',770000),(20110020,'허우','8802232116784',730000);
/*!40000 ALTER TABLE `t_customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_department`
--

DROP TABLE IF EXISTS `t_department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_department` (
  `deptno` int NOT NULL,
  `dname` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `part` int DEFAULT NULL,
  `build` varchar(14) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`deptno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_department`
--

LOCK TABLES `t_department` WRITE;
/*!40000 ALTER TABLE `t_department` DISABLE KEYS */;
INSERT INTO `t_department` VALUES (10,'공과대학',NULL,NULL),(20,'인문대학',NULL,NULL),(100,'컴퓨터정보학부',10,NULL),(101,'컴퓨터공학과',100,'정보관'),(102,'멀티미디어공학과',100,'멀티미디어관'),(103,'소프트웨어공학과',100,'소프트웨어관'),(200,'메카트로닉스학부',10,NULL),(201,'전자공학과',200,'전자제어관'),(202,'기계공학과',200,'기계실험관'),(203,'화학공학과',200,'화학실습관'),(300,'인문사회학부',20,NULL),(301,'문헌정보학과',300,'인문관');
/*!40000 ALTER TABLE `t_department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_dept`
--

DROP TABLE IF EXISTS `t_dept`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_dept` (
  `DEPTNO` int NOT NULL,
  `DNAME` varchar(14) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `LOC` varchar(13) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`DEPTNO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_dept`
--

LOCK TABLES `t_dept` WRITE;
/*!40000 ALTER TABLE `t_dept` DISABLE KEYS */;
INSERT INTO `t_dept` VALUES (10,'ACCOUNTING','NEW YORK'),(20,'RESEARCH','DALLAS'),(30,'SALES','CHICAGO'),(40,'OPERATIONS','BOSTON');
/*!40000 ALTER TABLE `t_dept` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_dept2`
--

DROP TABLE IF EXISTS `t_dept2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_dept2` (
  `DCODE` varchar(6) COLLATE utf8mb4_unicode_ci NOT NULL,
  `DNAME` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `PDEPT` varchar(6) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `AREA` varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`DCODE`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_dept2`
--

LOCK TABLES `t_dept2` WRITE;
/*!40000 ALTER TABLE `t_dept2` DISABLE KEYS */;
INSERT INTO `t_dept2` VALUES ('0001','사장실','','포항본사'),('1000','경영지원부','0001','서울지사'),('1001','재무관리팀','1000','서울지사'),('1002','총무팀','1000','서울지사'),('1003','기술부','0001','포항본사'),('1004','H/W지원','1003','대전지사'),('1005','S/W지원','1003','경기지사'),('1006','영업부','0001','포항본사'),('1007','영업기획팀','1006','포항본사'),('1008','영업1팀','1007','부산지사'),('1009','영업2팀','1007','경기지사'),('1010','영업3팀','1007','서울지사'),('1011','영업4팀','1007','울산지사');
/*!40000 ALTER TABLE `t_dept2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_emp`
--

DROP TABLE IF EXISTS `t_emp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_emp` (
  `EMPNO` int NOT NULL,
  `ENAME` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `JOB` varchar(9) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `MGR` int DEFAULT NULL,
  `HIREDATE` datetime DEFAULT NULL,
  `SAL` int DEFAULT NULL,
  `COMM` int DEFAULT NULL,
  `DEPTNO` int DEFAULT NULL,
  PRIMARY KEY (`EMPNO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_emp`
--

LOCK TABLES `t_emp` WRITE;
/*!40000 ALTER TABLE `t_emp` DISABLE KEYS */;
INSERT INTO `t_emp` VALUES (7369,'SMITH','CLERK',7902,'1990-12-17 00:00:00',800,NULL,20),(7499,'ALLEN','SALESMAN',7698,'1991-02-20 00:00:00',1600,300,30),(7521,'WARD','SALESMAN',7698,'1992-02-22 00:00:00',1250,500,30),(7566,'JONES','MANAGER',7839,'1991-04-02 00:00:00',2975,NULL,20),(7654,'MARTIN','SALESMAN',7698,'1991-09-28 00:00:00',1250,1400,30),(7698,'BLAKE','MANAGER',7839,'1991-05-01 00:00:00',2850,NULL,30),(7782,'CLARK','MANAGER',7839,'1991-06-09 00:00:00',2450,NULL,10),(7788,'SCOTT','ANALYST',7566,'1997-04-17 00:00:00',3000,NULL,20),(7839,'KING','PRESIDENT',NULL,'1991-11-17 00:00:00',5000,NULL,10),(7844,'TURNER','SALESMAN',7698,'1991-09-08 00:00:00',1500,0,30),(7876,'ADAMS','CLERK',7788,'1997-05-23 00:00:00',1100,NULL,20),(7900,'JAMES','CLERK',7698,'1991-12-03 00:00:00',950,NULL,30),(7902,'FORD','ANALYST',7566,'1991-12-03 00:00:00',3000,NULL,20),(7934,'MILLER','CLERK',7782,'1992-01-23 00:00:00',1300,NULL,10);
/*!40000 ALTER TABLE `t_emp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_emp2`
--

DROP TABLE IF EXISTS `t_emp2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_emp2` (
  `EMPNO` int NOT NULL,
  `NAME` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `BIRTHDAY` date DEFAULT NULL,
  `DEPTNO` varchar(6) COLLATE utf8mb4_unicode_ci NOT NULL,
  `EMP_TYPE` varchar(8) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `TEL` varchar(15) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `HOBBY` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `PAY` int DEFAULT NULL,
  `POST` varchar(8) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `PEMPNO` int DEFAULT NULL,
  PRIMARY KEY (`EMPNO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_emp2`
--

LOCK TABLES `t_emp2` WRITE;
/*!40000 ALTER TABLE `t_emp2` DISABLE KEYS */;
INSERT INTO `t_emp2` VALUES (20000101,'나사장','1974-01-25','0001','정규직','054)223-0001','음악감상',100000000,'대표이사',NULL),(20030331,'백원만','1986-05-25','1001','정규직','02)6255-8010','자전거타기',60000000,'차장',20060101),(20030402,'유관순','1982-08-15','1004','정규직','042)998-7005','등산',51000000,'과장',20066102),(20050303,'천만득','1983-06-15','1002','정규직','02)6255-8020','마라톤',56000000,'과장',20060101),(20060101,'전부장','1983-03-22','1000','정규직','02)6255-8000','독서',72000000,'부장',20000101),(20060212,'이윤나','1982-12-15','1007','정규직','054)223-4600',NULL,49000000,'과장',20070112),(20060303,'김문호','1981-09-25','1005','정규직','031)564-3340','등산',35000000,'대리',20066102),(20066102,'일지매','1982-07-05','1003','정규직','052)223-4000','음악감상',75000000,'부장',20000101),(20070112,'노정호','1986-11-05','1006','정규직','054)223-4500','수영',68000000,'부장',20000101),(20070201,'최일도','1985-04-15','1000','정규직','02)6255-8005','운동',50000000,'과장',20060101),(20100101,'이태백','1995-01-25','1008','계약직','051)123-4567','등산',30000000,NULL,20060212),(20100102,'김설악','1993-03-22','1009','계약직','031)234-5678','낚시',30000000,NULL,20060212),(20100119,'장금강','1990-11-05','1004','인턴직','042)901-2345','술',20000000,NULL,20030402),(20100203,'최오대','1992-04-15','1010','계약직','02)2345-6789','바둑',30000000,NULL,20060212),(20100210,'나한라','1990-12-15','1005','인턴직','031)345-3456','독서',20000000,NULL,20060303),(20100305,'정북악','1990-06-15','1008','수습직','051)567-8901','독서',22000000,NULL,20060212),(20100308,'강월악','1990-09-25','1011','인턴직','053)890-1234','골프',20000000,NULL,20060212),(20100334,'박지리','1991-05-25','1011','계약직','053)456-7890','노래',30000000,NULL,20060212),(20100407,'윤주왕','1990-08-15','1010','수습직','02)2789-0123','오락',22000000,NULL,20060212),(20106106,'유도봉','1990-07-05','1009','수습직','031)678-9012','술',22000000,NULL,20060212);
/*!40000 ALTER TABLE `t_emp2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_emp3`
--

DROP TABLE IF EXISTS `t_emp3`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_emp3` (
  `id` int NOT NULL AUTO_INCREMENT,
  `empno` int NOT NULL,
  `name` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=828 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_emp3`
--

LOCK TABLES `t_emp3` WRITE;
/*!40000 ALTER TABLE `t_emp3` DISABLE KEYS */;
INSERT INTO `t_emp3` VALUES (1,20000101,'나사장'),(2,20030331,'백원만'),(3,20030402,'유관순'),(4,20050303,'천만득'),(5,20060101,'전부장'),(6,20060212,'이윤나'),(7,20060303,'김문호'),(8,20066102,'일지매'),(9,20070112,'노정호'),(10,20070201,'최일도'),(11,20100101,'이태백'),(12,20100102,'김설악'),(13,20100119,'장금강'),(14,20100203,'최오대'),(15,20100210,'나한라'),(16,20100305,'정북악'),(17,20100308,'강월악'),(18,20100334,'박지리'),(19,20100407,'윤주왕'),(20,20106106,'유도봉'),(32,20000101,'나사장'),(33,20030331,'백원만'),(34,20030402,'유관순'),(35,20050303,'천만득'),(36,20060101,'전부장'),(37,20060212,'이윤나'),(38,20060303,'김문호'),(39,20066102,'일지매'),(40,20070112,'노정호'),(41,20070201,'최일도'),(42,20100101,'이태백'),(43,20100102,'김설악'),(44,20100119,'장금강'),(45,20100203,'최오대'),(46,20100210,'나한라'),(47,20100305,'정북악'),(48,20100308,'강월악'),(49,20100334,'박지리'),(50,20100407,'윤주왕'),(51,20106106,'유도봉'),(63,20000101,'나사장'),(64,20030331,'백원만'),(65,20030402,'유관순'),(66,20050303,'천만득'),(67,20060101,'전부장'),(68,20060212,'이윤나'),(69,20060303,'김문호'),(70,20066102,'일지매'),(71,20070112,'노정호'),(72,20070201,'최일도'),(73,20100101,'이태백'),(74,20100102,'김설악'),(75,20100119,'장금강'),(76,20100203,'최오대'),(77,20100210,'나한라'),(78,20100305,'정북악'),(79,20100308,'강월악'),(80,20100334,'박지리'),(81,20100407,'윤주왕'),(82,20106106,'유도봉'),(83,20000101,'나사장'),(84,20030331,'백원만'),(85,20030402,'유관순'),(86,20050303,'천만득'),(87,20060101,'전부장'),(88,20060212,'이윤나'),(89,20060303,'김문호'),(90,20066102,'일지매'),(91,20070112,'노정호'),(92,20070201,'최일도'),(93,20100101,'이태백'),(94,20100102,'김설악'),(95,20100119,'장금강'),(96,20100203,'최오대'),(97,20100210,'나한라'),(98,20100305,'정북악'),(99,20100308,'강월악'),(100,20100334,'박지리'),(101,20100407,'윤주왕'),(102,20106106,'유도봉'),(126,20000101,'나사장'),(127,20030331,'백원만'),(128,20030402,'유관순'),(129,20050303,'천만득'),(130,20060101,'전부장'),(131,20060212,'이윤나'),(132,20060303,'김문호'),(133,20066102,'일지매'),(134,20070112,'노정호'),(135,20070201,'최일도'),(136,20100101,'이태백'),(137,20100102,'김설악'),(138,20100119,'장금강'),(139,20100203,'최오대'),(140,20100210,'나한라'),(141,20100305,'정북악'),(142,20100308,'강월악'),(143,20100334,'박지리'),(144,20100407,'윤주왕'),(145,20106106,'유도봉'),(146,20000101,'나사장'),(147,20030331,'백원만'),(148,20030402,'유관순'),(149,20050303,'천만득'),(150,20060101,'전부장'),(151,20060212,'이윤나'),(152,20060303,'김문호'),(153,20066102,'일지매'),(154,20070112,'노정호'),(155,20070201,'최일도'),(156,20100101,'이태백'),(157,20100102,'김설악'),(158,20100119,'장금강'),(159,20100203,'최오대'),(160,20100210,'나한라'),(161,20100305,'정북악'),(162,20100308,'강월악'),(163,20100334,'박지리'),(164,20100407,'윤주왕'),(165,20106106,'유도봉'),(166,20000101,'나사장'),(167,20030331,'백원만'),(168,20030402,'유관순'),(169,20050303,'천만득'),(170,20060101,'전부장'),(171,20060212,'이윤나'),(172,20060303,'김문호'),(173,20066102,'일지매'),(174,20070112,'노정호'),(175,20070201,'최일도'),(176,20100101,'이태백'),(177,20100102,'김설악'),(178,20100119,'장금강'),(179,20100203,'최오대'),(180,20100210,'나한라'),(181,20100305,'정북악'),(182,20100308,'강월악'),(183,20100334,'박지리'),(184,20100407,'윤주왕'),(185,20106106,'유도봉'),(186,20000101,'나사장'),(187,20030331,'백원만'),(188,20030402,'유관순'),(189,20050303,'천만득'),(190,20060101,'전부장'),(191,20060212,'이윤나'),(192,20060303,'김문호'),(193,20066102,'일지매'),(194,20070112,'노정호'),(195,20070201,'최일도'),(196,20100101,'이태백'),(197,20100102,'김설악'),(198,20100119,'장금강'),(199,20100203,'최오대'),(200,20100210,'나한라'),(201,20100305,'정북악'),(202,20100308,'강월악'),(203,20100334,'박지리'),(204,20100407,'윤주왕'),(205,20106106,'유도봉'),(253,20000101,'나사장'),(254,20030331,'백원만'),(255,20030402,'유관순'),(256,20050303,'천만득'),(257,20060101,'전부장'),(258,20060212,'이윤나'),(259,20060303,'김문호'),(260,20066102,'일지매'),(261,20070112,'노정호'),(262,20070201,'최일도'),(263,20100101,'이태백'),(264,20100102,'김설악'),(265,20100119,'장금강'),(266,20100203,'최오대'),(267,20100210,'나한라'),(268,20100305,'정북악'),(269,20100308,'강월악'),(270,20100334,'박지리'),(271,20100407,'윤주왕'),(272,20106106,'유도봉'),(273,20000101,'나사장'),(274,20030331,'백원만'),(275,20030402,'유관순'),(276,20050303,'천만득'),(277,20060101,'전부장'),(278,20060212,'이윤나'),(279,20060303,'김문호'),(280,20066102,'일지매'),(281,20070112,'노정호'),(282,20070201,'최일도'),(283,20100101,'이태백'),(284,20100102,'김설악'),(285,20100119,'장금강'),(286,20100203,'최오대'),(287,20100210,'나한라'),(288,20100305,'정북악'),(289,20100308,'강월악'),(290,20100334,'박지리'),(291,20100407,'윤주왕'),(292,20106106,'유도봉'),(293,20000101,'나사장'),(294,20030331,'백원만'),(295,20030402,'유관순'),(296,20050303,'천만득'),(297,20060101,'전부장'),(298,20060212,'이윤나'),(299,20060303,'김문호'),(300,20066102,'일지매'),(301,20070112,'노정호'),(302,20070201,'최일도'),(303,20100101,'이태백'),(304,20100102,'김설악'),(305,20100119,'장금강'),(306,20100203,'최오대'),(307,20100210,'나한라'),(308,20100305,'정북악'),(309,20100308,'강월악'),(310,20100334,'박지리'),(311,20100407,'윤주왕'),(312,20106106,'유도봉'),(313,20000101,'나사장'),(314,20030331,'백원만'),(315,20030402,'유관순'),(316,20050303,'천만득'),(317,20060101,'전부장'),(318,20060212,'이윤나'),(319,20060303,'김문호'),(320,20066102,'일지매'),(321,20070112,'노정호'),(322,20070201,'최일도'),(323,20100101,'이태백'),(324,20100102,'김설악'),(325,20100119,'장금강'),(326,20100203,'최오대'),(327,20100210,'나한라'),(328,20100305,'정북악'),(329,20100308,'강월악'),(330,20100334,'박지리'),(331,20100407,'윤주왕'),(332,20106106,'유도봉'),(333,20000101,'나사장'),(334,20030331,'백원만'),(335,20030402,'유관순'),(336,20050303,'천만득'),(337,20060101,'전부장'),(338,20060212,'이윤나'),(339,20060303,'김문호'),(340,20066102,'일지매'),(341,20070112,'노정호'),(342,20070201,'최일도'),(343,20100101,'이태백'),(344,20100102,'김설악'),(345,20100119,'장금강'),(346,20100203,'최오대'),(347,20100210,'나한라'),(348,20100305,'정북악'),(349,20100308,'강월악'),(350,20100334,'박지리'),(351,20100407,'윤주왕'),(352,20106106,'유도봉'),(353,20000101,'나사장'),(354,20030331,'백원만'),(355,20030402,'유관순'),(356,20050303,'천만득'),(357,20060101,'전부장'),(358,20060212,'이윤나'),(359,20060303,'김문호'),(360,20066102,'일지매'),(361,20070112,'노정호'),(362,20070201,'최일도'),(363,20100101,'이태백'),(364,20100102,'김설악'),(365,20100119,'장금강'),(366,20100203,'최오대'),(367,20100210,'나한라'),(368,20100305,'정북악'),(369,20100308,'강월악'),(370,20100334,'박지리'),(371,20100407,'윤주왕'),(372,20106106,'유도봉'),(373,20000101,'나사장'),(374,20030331,'백원만'),(375,20030402,'유관순'),(376,20050303,'천만득'),(377,20060101,'전부장'),(378,20060212,'이윤나'),(379,20060303,'김문호'),(380,20066102,'일지매'),(381,20070112,'노정호'),(382,20070201,'최일도'),(383,20100101,'이태백'),(384,20100102,'김설악'),(385,20100119,'장금강'),(386,20100203,'최오대'),(387,20100210,'나한라'),(388,20100305,'정북악'),(389,20100308,'강월악'),(390,20100334,'박지리'),(391,20100407,'윤주왕'),(392,20106106,'유도봉'),(393,20000101,'나사장'),(394,20030331,'백원만'),(395,20030402,'유관순'),(396,20050303,'천만득'),(397,20060101,'전부장'),(398,20060212,'이윤나'),(399,20060303,'김문호'),(400,20066102,'일지매'),(401,20070112,'노정호'),(402,20070201,'최일도'),(403,20100101,'이태백'),(404,20100102,'김설악'),(405,20100119,'장금강'),(406,20100203,'최오대'),(407,20100210,'나한라'),(408,20100305,'정북악'),(409,20100308,'강월악'),(410,20100334,'박지리'),(411,20100407,'윤주왕'),(412,20106106,'유도봉'),(508,20000101,'나사장'),(509,20030331,'백원만'),(510,20030402,'유관순'),(511,20050303,'천만득'),(512,20060101,'전부장'),(513,20060212,'이윤나'),(514,20060303,'김문호'),(515,20066102,'일지매'),(516,20070112,'노정호'),(517,20070201,'최일도'),(518,20100101,'이태백'),(519,20100102,'김설악'),(520,20100119,'장금강'),(521,20100203,'최오대'),(522,20100210,'나한라'),(523,20100305,'정북악'),(524,20100308,'강월악'),(525,20100334,'박지리'),(526,20100407,'윤주왕'),(527,20106106,'유도봉'),(528,20000101,'나사장'),(529,20030331,'백원만'),(530,20030402,'유관순'),(531,20050303,'천만득'),(532,20060101,'전부장'),(533,20060212,'이윤나'),(534,20060303,'김문호'),(535,20066102,'일지매'),(536,20070112,'노정호'),(537,20070201,'최일도'),(538,20100101,'이태백'),(539,20100102,'김설악'),(540,20100119,'장금강'),(541,20100203,'최오대'),(542,20100210,'나한라'),(543,20100305,'정북악'),(544,20100308,'강월악'),(545,20100334,'박지리'),(546,20100407,'윤주왕'),(547,20106106,'유도봉'),(548,20000101,'나사장'),(549,20030331,'백원만'),(550,20030402,'유관순'),(551,20050303,'천만득'),(552,20060101,'전부장'),(553,20060212,'이윤나'),(554,20060303,'김문호'),(555,20066102,'일지매'),(556,20070112,'노정호'),(557,20070201,'최일도'),(558,20100101,'이태백'),(559,20100102,'김설악'),(560,20100119,'장금강'),(561,20100203,'최오대'),(562,20100210,'나한라'),(563,20100305,'정북악'),(564,20100308,'강월악'),(565,20100334,'박지리'),(566,20100407,'윤주왕'),(567,20106106,'유도봉'),(568,20000101,'나사장'),(569,20030331,'백원만'),(570,20030402,'유관순'),(571,20050303,'천만득'),(572,20060101,'전부장'),(573,20060212,'이윤나'),(574,20060303,'김문호'),(575,20066102,'일지매'),(576,20070112,'노정호'),(577,20070201,'최일도'),(578,20100101,'이태백'),(579,20100102,'김설악'),(580,20100119,'장금강'),(581,20100203,'최오대'),(582,20100210,'나한라'),(583,20100305,'정북악'),(584,20100308,'강월악'),(585,20100334,'박지리'),(586,20100407,'윤주왕'),(587,20106106,'유도봉'),(588,20000101,'나사장'),(589,20030331,'백원만'),(590,20030402,'유관순'),(591,20050303,'천만득'),(592,20060101,'전부장'),(593,20060212,'이윤나'),(594,20060303,'김문호'),(595,20066102,'일지매'),(596,20070112,'노정호'),(597,20070201,'최일도'),(598,20100101,'이태백'),(599,20100102,'김설악'),(600,20100119,'장금강'),(601,20100203,'최오대'),(602,20100210,'나한라'),(603,20100305,'정북악'),(604,20100308,'강월악'),(605,20100334,'박지리'),(606,20100407,'윤주왕'),(607,20106106,'유도봉'),(608,20000101,'나사장'),(609,20030331,'백원만'),(610,20030402,'유관순'),(611,20050303,'천만득'),(612,20060101,'전부장'),(613,20060212,'이윤나'),(614,20060303,'김문호'),(615,20066102,'일지매'),(616,20070112,'노정호'),(617,20070201,'최일도'),(618,20100101,'이태백'),(619,20100102,'김설악'),(620,20100119,'장금강'),(621,20100203,'최오대'),(622,20100210,'나한라'),(623,20100305,'정북악'),(624,20100308,'강월악'),(625,20100334,'박지리'),(626,20100407,'윤주왕'),(627,20106106,'유도봉'),(628,20000101,'나사장'),(629,20030331,'백원만'),(630,20030402,'유관순'),(631,20050303,'천만득'),(632,20060101,'전부장'),(633,20060212,'이윤나'),(634,20060303,'김문호'),(635,20066102,'일지매'),(636,20070112,'노정호'),(637,20070201,'최일도'),(638,20100101,'이태백'),(639,20100102,'김설악'),(640,20100119,'장금강'),(641,20100203,'최오대'),(642,20100210,'나한라'),(643,20100305,'정북악'),(644,20100308,'강월악'),(645,20100334,'박지리'),(646,20100407,'윤주왕'),(647,20106106,'유도봉'),(648,20000101,'나사장'),(649,20030331,'백원만'),(650,20030402,'유관순'),(651,20050303,'천만득'),(652,20060101,'전부장'),(653,20060212,'이윤나'),(654,20060303,'김문호'),(655,20066102,'일지매'),(656,20070112,'노정호'),(657,20070201,'최일도'),(658,20100101,'이태백'),(659,20100102,'김설악'),(660,20100119,'장금강'),(661,20100203,'최오대'),(662,20100210,'나한라'),(663,20100305,'정북악'),(664,20100308,'강월악'),(665,20100334,'박지리'),(666,20100407,'윤주왕'),(667,20106106,'유도봉'),(668,20000101,'나사장'),(669,20030331,'백원만'),(670,20030402,'유관순'),(671,20050303,'천만득'),(672,20060101,'전부장'),(673,20060212,'이윤나'),(674,20060303,'김문호'),(675,20066102,'일지매'),(676,20070112,'노정호'),(677,20070201,'최일도'),(678,20100101,'이태백'),(679,20100102,'김설악'),(680,20100119,'장금강'),(681,20100203,'최오대'),(682,20100210,'나한라'),(683,20100305,'정북악'),(684,20100308,'강월악'),(685,20100334,'박지리'),(686,20100407,'윤주왕'),(687,20106106,'유도봉'),(688,20000101,'나사장'),(689,20030331,'백원만'),(690,20030402,'유관순'),(691,20050303,'천만득'),(692,20060101,'전부장'),(693,20060212,'이윤나'),(694,20060303,'김문호'),(695,20066102,'일지매'),(696,20070112,'노정호'),(697,20070201,'최일도'),(698,20100101,'이태백'),(699,20100102,'김설악'),(700,20100119,'장금강'),(701,20100203,'최오대'),(702,20100210,'나한라'),(703,20100305,'정북악'),(704,20100308,'강월악'),(705,20100334,'박지리'),(706,20100407,'윤주왕'),(707,20106106,'유도봉'),(708,20000101,'나사장'),(709,20030331,'백원만'),(710,20030402,'유관순'),(711,20050303,'천만득'),(712,20060101,'전부장'),(713,20060212,'이윤나'),(714,20060303,'김문호'),(715,20066102,'일지매'),(716,20070112,'노정호'),(717,20070201,'최일도'),(718,20100101,'이태백'),(719,20100102,'김설악'),(720,20100119,'장금강'),(721,20100203,'최오대'),(722,20100210,'나한라'),(723,20100305,'정북악'),(724,20100308,'강월악'),(725,20100334,'박지리'),(726,20100407,'윤주왕'),(727,20106106,'유도봉'),(728,20000101,'나사장'),(729,20030331,'백원만'),(730,20030402,'유관순'),(731,20050303,'천만득'),(732,20060101,'전부장'),(733,20060212,'이윤나'),(734,20060303,'김문호'),(735,20066102,'일지매'),(736,20070112,'노정호'),(737,20070201,'최일도'),(738,20100101,'이태백'),(739,20100102,'김설악'),(740,20100119,'장금강'),(741,20100203,'최오대'),(742,20100210,'나한라'),(743,20100305,'정북악'),(744,20100308,'강월악'),(745,20100334,'박지리'),(746,20100407,'윤주왕'),(747,20106106,'유도봉'),(748,20000101,'나사장'),(749,20030331,'백원만'),(750,20030402,'유관순'),(751,20050303,'천만득'),(752,20060101,'전부장'),(753,20060212,'이윤나'),(754,20060303,'김문호'),(755,20066102,'일지매'),(756,20070112,'노정호'),(757,20070201,'최일도'),(758,20100101,'이태백'),(759,20100102,'김설악'),(760,20100119,'장금강'),(761,20100203,'최오대'),(762,20100210,'나한라'),(763,20100305,'정북악'),(764,20100308,'강월악'),(765,20100334,'박지리'),(766,20100407,'윤주왕'),(767,20106106,'유도봉'),(768,20000101,'나사장'),(769,20030331,'백원만'),(770,20030402,'유관순'),(771,20050303,'천만득'),(772,20060101,'전부장'),(773,20060212,'이윤나'),(774,20060303,'김문호'),(775,20066102,'일지매'),(776,20070112,'노정호'),(777,20070201,'최일도'),(778,20100101,'이태백'),(779,20100102,'김설악'),(780,20100119,'장금강'),(781,20100203,'최오대'),(782,20100210,'나한라'),(783,20100305,'정북악'),(784,20100308,'강월악'),(785,20100334,'박지리'),(786,20100407,'윤주왕'),(787,20106106,'유도봉'),(788,20000101,'나사장'),(789,20030331,'백원만'),(790,20030402,'유관순'),(791,20050303,'천만득'),(792,20060101,'전부장'),(793,20060212,'이윤나'),(794,20060303,'김문호'),(795,20066102,'일지매'),(796,20070112,'노정호'),(797,20070201,'최일도'),(798,20100101,'이태백'),(799,20100102,'김설악'),(800,20100119,'장금강'),(801,20100203,'최오대'),(802,20100210,'나한라'),(803,20100305,'정북악'),(804,20100308,'강월악'),(805,20100334,'박지리'),(806,20100407,'윤주왕'),(807,20106106,'유도봉'),(808,20000101,'나사장'),(809,20030331,'백원만'),(810,20030402,'유관순'),(811,20050303,'천만득'),(812,20060101,'전부장'),(813,20060212,'이윤나'),(814,20060303,'김문호'),(815,20066102,'일지매'),(816,20070112,'노정호'),(817,20070201,'최일도'),(818,20100101,'이태백'),(819,20100102,'김설악'),(820,20100119,'장금강'),(821,20100203,'최오대'),(822,20100210,'나한라'),(823,20100305,'정북악'),(824,20100308,'강월악'),(825,20100334,'박지리'),(826,20100407,'윤주왕'),(827,20106106,'유도봉');
/*!40000 ALTER TABLE `t_emp3` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_emp4`
--

DROP TABLE IF EXISTS `t_emp4`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_emp4` (
  `no` int NOT NULL,
  `name` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `jumin` varchar(13) COLLATE utf8mb4_unicode_ci NOT NULL,
  `area` int DEFAULT NULL,
  `deptno` varchar(6) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`no`),
  UNIQUE KEY `emp4_jumin_uk` (`jumin`),
  KEY `emp4_deptno_fk` (`deptno`),
  CONSTRAINT `emp4_deptno_fk` FOREIGN KEY (`deptno`) REFERENCES `t_dept2` (`DCODE`) ON DELETE CASCADE,
  CONSTRAINT `emp4_area_ck` CHECK ((`area` < 5))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_emp4`
--

LOCK TABLES `t_emp4` WRITE;
/*!40000 ALTER TABLE `t_emp4` DISABLE KEYS */;
/*!40000 ALTER TABLE `t_emp4` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_exam01`
--

DROP TABLE IF EXISTS `t_exam01`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_exam01` (
  `studno` int DEFAULT NULL,
  `total` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_exam01`
--

LOCK TABLES `t_exam01` WRITE;
/*!40000 ALTER TABLE `t_exam01` DISABLE KEYS */;
INSERT INTO `t_exam01` VALUES (9411,97),(9412,78),(9413,83),(9414,62),(9415,88),(9511,92),(9512,87),(9513,81),(9514,79),(9515,95),(9611,89),(9612,77),(9613,86),(9614,82),(9615,87),(9711,91),(9712,88),(9713,82),(9714,83),(9715,84);
/*!40000 ALTER TABLE `t_exam01` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_gift`
--

DROP TABLE IF EXISTS `t_gift`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_gift` (
  `g_no` int DEFAULT NULL,
  `g_name` varchar(15) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `g_start` int DEFAULT NULL,
  `g_end` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_gift`
--

LOCK TABLES `t_gift` WRITE;
/*!40000 ALTER TABLE `t_gift` DISABLE KEYS */;
INSERT INTO `t_gift` VALUES (1,'참치세트',1,100000),(2,'샴푸세트',100001,200000),(3,'세차용품세트',200001,300000),(4,'주방용품세트',300001,400000),(5,'산악용자전거',400001,500000),(6,'LCD모니터',500001,600000),(7,'노트북',600001,700000),(8,'벽걸이TV',700001,800000),(9,'드럼세탁기',800001,900000),(10,'양쪽문냉장고',900001,1000000);
/*!40000 ALTER TABLE `t_gift` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_member`
--

DROP TABLE IF EXISTS `t_member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_member` (
  `m_no` int NOT NULL,
  `m_name` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `m_jumin` char(13) COLLATE utf8mb4_unicode_ci NOT NULL,
  `m_passwd` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `m_id` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `m_question` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `m_answer` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`m_jumin`),
  UNIQUE KEY `m_id` (`m_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_member`
--

LOCK TABLES `t_member` WRITE;
/*!40000 ALTER TABLE `t_member` DISABLE KEYS */;
INSERT INTO `t_member` VALUES (1003,'서새알','1410234567890','c1234','daddy','아빠이름?','서유딩'),(1004,'서공룡알','1609223456789','d1234','mommy','엄마이름?','김초딩'),(1002,'김초딩','8509222345678','b1234','bobby','남편이름?','서유딩'),(1001,'서유딩','8510231234567','a1234','simson','아내이름?','김초딩');
/*!40000 ALTER TABLE `t_member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_post`
--

DROP TABLE IF EXISTS `t_post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_post` (
  `post` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `s_age` int DEFAULT NULL,
  `e_age` int DEFAULT NULL,
  `s_year` int DEFAULT NULL,
  `e_year` int DEFAULT NULL,
  `s_pay` int DEFAULT NULL,
  `e_pay` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_post`
--

LOCK TABLES `t_post` WRITE;
/*!40000 ALTER TABLE `t_post` DISABLE KEYS */;
INSERT INTO `t_post` VALUES ('주임',0,24,1,2,12000000,29990000),('대리',25,28,3,5,30000000,45000000),('과장',29,32,6,8,45010000,51000000),('차장',33,36,9,10,51010000,60000000),('부장',37,40,11,13,60010000,75000000),('이사',41,55,14,99,75010000,100000000);
/*!40000 ALTER TABLE `t_post` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_product`
--

DROP TABLE IF EXISTS `t_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_product` (
  `p_code` int NOT NULL,
  `p_name` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `p_price` decimal(10,0) DEFAULT NULL,
  PRIMARY KEY (`p_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_product`
--

LOCK TABLES `t_product` WRITE;
/*!40000 ALTER TABLE `t_product` DISABLE KEYS */;
INSERT INTO `t_product` VALUES (100,'새우짱',800),(101,'감자짱',900),(102,'맛큰산',1000),(103,'에이서',900),(104,'맛짱구',800),(105,'샤보레',1500);
/*!40000 ALTER TABLE `t_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_professor`
--

DROP TABLE IF EXISTS `t_professor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_professor` (
  `PROFNO` int NOT NULL,
  `NAME` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `ID` varchar(15) COLLATE utf8mb4_unicode_ci NOT NULL,
  `POSITION` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `PAY` int NOT NULL,
  `HIREDATE` date NOT NULL,
  `BONUS` int DEFAULT NULL,
  `DEPTNO` int DEFAULT NULL,
  `EMAIL` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `HPAGE` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`PROFNO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_professor`
--

LOCK TABLES `t_professor` WRITE;
/*!40000 ALTER TABLE `t_professor` DISABLE KEYS */;
INSERT INTO `t_professor` VALUES (1001,'조인형','captain','정교수',550,'1990-06-23',100,101,'captain@abc.net','http://www.abc.net'),(1002,'박승곤','sweety','조교수',380,'1997-01-30',60,101,'sweety@abc.net','http://www.abc.net'),(1003,'송도권','powerman','전임강사',270,'2008-03-22',NULL,101,'pman@power.com','http://www.power.com'),(2001,'양선희','lamb1','전임강사',250,'2011-09-01',NULL,102,'lamb1@hamail.net',NULL),(2002,'김영조','number1','조교수',350,'1995-11-30',80,102,'number1@naver.com','http://num1.naver.com'),(2003,'주승재','bluedragon','정교수',490,'1992-04-29',90,102,'bdragon@naver.com',NULL),(3001,'김도형','angel1004','정교수',530,'1991-10-23',110,103,'angel1004@hanmir.com',NULL),(3002,'나한열','naone10','조교수',330,'2007-07-01',50,103,'naone10@empal.com',NULL),(3003,'김현정','only-u','전임강사',290,'2012-02-24',NULL,103,'only_u@abc.com',NULL),(4001,'심슨','simson','정교수',570,'1991-10-23',130,201,'chebin@daum.net',NULL),(4002,'최슬기','gogogo','조교수',330,'2019-08-30',NULL,201,'gogogo@def.com',NULL),(4003,'박원범','mypride','조교수',310,'2009-12-01',50,202,'mypride@hanmail.net',NULL),(4004,'차범철','ironman','전임강사',260,'2019-01-28',NULL,202,'ironman@naver.com',NULL),(4005,'바비','standkang','정교수',500,'1995-09-18',80,203,'standkang@naver.com',NULL),(4006,'전민','napeople','전임강사',220,'2020-06-28',NULL,301,'napeople@jass.com',NULL),(4007,'허은','silver-her','조교수',290,'2011-05-23',30,301,'silver-her@daum.net',NULL);
/*!40000 ALTER TABLE `t_professor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_sales`
--

DROP TABLE IF EXISTS `t_sales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_sales` (
  `s_date` varchar(8) COLLATE utf8mb4_unicode_ci NOT NULL,
  `s_code` int NOT NULL,
  `s_qty` int DEFAULT NULL,
  `s_total` int DEFAULT NULL,
  `s_store` varchar(5) COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_sales`
--

LOCK TABLES `t_sales` WRITE;
/*!40000 ALTER TABLE `t_sales` DISABLE KEYS */;
INSERT INTO `t_sales` VALUES ('20180101',100,3,2400,'1000'),('20180101',101,5,4500,'1001'),('20180101',102,2,2000,'1003'),('20180101',103,6,5400,'1004'),('20180102',102,2,2000,'1000'),('20180102',103,5,4500,'1002'),('20180102',104,3,2400,'1002'),('20180102',105,2,3000,'1000'),('20180103',100,10,8000,'1004'),('20180103',100,2,1600,'1000'),('20180103',100,3,2400,'1001'),('20180103',101,4,3600,'1003'),('20180104',100,2,1600,'1002'),('20180104',100,4,3200,'1003'),('20180104',100,5,4000,'1004'),('20180104',101,3,2700,'1001'),('20180104',101,4,3600,'1002'),('20180104',101,3,2700,'1003'),('20180104',102,4,4000,'1001'),('20180104',102,2,2000,'1002'),('20180104',103,2,1800,'1003');
/*!40000 ALTER TABLE `t_sales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_student`
--

DROP TABLE IF EXISTS `t_student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `t_student` (
  `studno` int NOT NULL,
  `name` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `id` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `grade` int DEFAULT NULL,
  `jumin` varchar(13) COLLATE utf8mb4_unicode_ci NOT NULL,
  `birthday` date DEFAULT NULL,
  `tel` varchar(15) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `height` int DEFAULT NULL,
  `weight` int DEFAULT NULL,
  `deptno1` int DEFAULT NULL,
  `deptno2` int DEFAULT NULL,
  `profno` int DEFAULT NULL,
  PRIMARY KEY (`studno`),
  UNIQUE KEY `id` (`id`),
  CONSTRAINT `t_student_chk_1` CHECK ((`grade` between 1 and 6))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_student`
--

LOCK TABLES `t_student` WRITE;
/*!40000 ALTER TABLE `t_student` DISABLE KEYS */;
INSERT INTO `t_student` VALUES (9411,'서진수','75true',4,'9510231901813','1995-10-23','055)381-2158',180,72,101,201,1001),(9412,'서재수','pooh94',4,'9502241128467','1995-02-24','051)426-1700',172,64,102,NULL,2001),(9413,'이미경','angel000',4,'9506152123648','1995-06-15','053)266-8947',168,52,103,203,3002),(9414,'김재수','gunmandu',4,'9512251063421','1995-12-25','02)6255-9875',177,83,201,NULL,4001),(9415,'박동호','pincle1',4,'9503031639826','1995-03-03','031)740-6388',182,70,202,NULL,4003),(9511,'김신영','bingo',3,'9601232186327','1996-01-23','055)333-6328',164,48,101,NULL,1002),(9512,'신은경','jjang1',3,'9604122298371','1996-04-12','051)418-9627',161,42,102,201,2002),(9513,'오나라','nara5',3,'9609112118379','1996-09-11','051)724-9618',177,55,202,NULL,4003),(9514,'구유미','guyume',3,'9601202378641','1996-01-20','055)296-3784',160,58,301,101,4007),(9515,'임세현','shyun1',3,'9610122196482','1996-10-12','02)312-9838',171,54,201,NULL,4001),(9611,'일지매','onejimae',2,'9711291186223','1997-11-29','02)6788-4861',182,72,101,NULL,1002),(9612,'김진욱','samjang7',2,'9704021358674','1997-04-02','055)488-2998',171,70,102,NULL,2001),(9613,'안광훈','nonnon1',2,'9709131276431','1997-09-13','053)736-4981',175,82,201,NULL,4002),(9614,'김문호','munho',2,'9702261196365','1997-02-26','02)6175-3945',166,51,201,NULL,4003),(9615,'노정호','star123',2,'9712141254963','1997-12-14','051)785-6984',184,62,301,NULL,4007),(9711,'이윤나','prettygirl',1,'9808192157498','1998-08-19','055)278-3649',162,48,101,NULL,NULL),(9712,'안은수','silverwt',1,'9801051776346','1998-01-05','02)381-5440',175,63,201,NULL,NULL),(9713,'인영민','youngmin',1,'9808091786954','1998-08-09','031)345-5677',173,69,201,NULL,NULL),(9714,'김주현','kimjh',1,'9803241981987','1998-03-24','055)423-9870',179,81,102,NULL,NULL),(9715,'허우','wooya2702',1,'9802232116784','1998-02-23','02)6122-2345',163,51,103,NULL,NULL);
/*!40000 ALTER TABLE `t_student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test_book`
--

DROP TABLE IF EXISTS `test_book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test_book` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `author` varchar(80) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `releaseDate` date DEFAULT NULL,
  `price` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test_book`
--

LOCK TABLES `test_book` WRITE;
/*!40000 ALTER TABLE `test_book` DISABLE KEYS */;
/*!40000 ALTER TABLE `test_book` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test_movie`
--

DROP TABLE IF EXISTS `test_movie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test_movie` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `director` varchar(80) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `ributors` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `openDate` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test_movie`
--

LOCK TABLES `test_movie` WRITE;
/*!40000 ALTER TABLE `test_movie` DISABLE KEYS */;
INSERT INTO `test_movie` VALUES (1,'가나다','홍','묵','2026-04-01'),(2,'라마바','묵','홍','2026-04-02');
/*!40000 ALTER TABLE `test_movie` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `uploaded_files`
--

DROP TABLE IF EXISTS `uploaded_files`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `uploaded_files` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `original_name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `uploaded_name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `uploaded_at` datetime NOT NULL DEFAULT (now()),
  PRIMARY KEY (`id`),
  KEY `ix_uploaded_files_id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `uploaded_files`
--

LOCK TABLES `uploaded_files` WRITE;
/*!40000 ALTER TABLE `uploaded_files` DISABLE KEYS */;
INSERT INTO `uploaded_files` VALUES (1,'mandu','face02.png','356ad51529d248f68ef4e894c93604a1.png','2026-06-17 01:35:18'),(2,'mandu','face03.png','b83926c85c59414fb4fab38a83ae0650.png','2026-06-17 01:35:34'),(3,'mandu','face01.png','dee2cfc1b16243d2806f6dbf59b0dcf2.png','2026-06-17 01:35:44'),(4,'mandu','test3.xlsx','3381d5bd05fe4b2cae4e528ee8747969.xlsx','2026-06-17 01:36:02'),(5,'토르','face04.png','d491601f8e5949fb953c97f33a08ac9e.png','2026-06-18 02:08:32');
/*!40000 ALTER TABLE `uploaded_files` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-06-18  2:39:15
