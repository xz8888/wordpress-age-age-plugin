-- MySQL dump 10.13  Distrib 5.5.11, for osx10.6 (i386)
--
-- Host: localhost    Database: isobar_au
-- ------------------------------------------------------
-- Server version	5.5.11

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `about_about`
--

DROP TABLE IF EXISTS `about_about`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `about_about` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `video_image` varchar(100) NOT NULL,
  `video` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `about_about`
--

LOCK TABLES `about_about` WRITE;
/*!40000 ALTER TABLE `about_about` DISABLE KEYS */;
/*!40000 ALTER TABLE `about_about` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `about_about_translation`
--

DROP TABLE IF EXISTS `about_about_translation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `about_about_translation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tagline` longtext NOT NULL,
  `left_header` varchar(100) NOT NULL,
  `left_body` longtext NOT NULL,
  `right_header` varchar(100) NOT NULL,
  `right_body` longtext NOT NULL,
  `language_code` varchar(15) NOT NULL,
  `master_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `language_code` (`language_code`,`master_id`),
  KEY `about_about_translation_11e09408` (`language_code`),
  KEY `about_about_translation_64d805fc` (`master_id`),
  CONSTRAINT `master_id_refs_id_4092a661` FOREIGN KEY (`master_id`) REFERENCES `about_about` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `about_about_translation`
--

LOCK TABLES `about_about_translation` WRITE;
/*!40000 ALTER TABLE `about_about_translation` DISABLE KEYS */;
/*!40000 ALTER TABLE `about_about_translation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_bda51c3c` (`group_id`),
  KEY `auth_group_permissions_1e014c8f` (`permission_id`),
  CONSTRAINT `group_id_refs_id_3cea63fe` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `permission_id_refs_id_a7792de1` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_message`
--

DROP TABLE IF EXISTS `auth_message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_message` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `auth_message_fbfc09f1` (`user_id`),
  CONSTRAINT `user_id_refs_id_9af0b65a` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_message`
--

LOCK TABLES `auth_message` WRITE;
/*!40000 ALTER TABLE `auth_message` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_e4470c6e` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_728de91f` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=139 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add message',4,'add_message'),(11,'Can change message',4,'change_message'),(12,'Can delete message',4,'delete_message'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add site',7,'add_site'),(20,'Can change site',7,'change_site'),(21,'Can delete site',7,'delete_site'),(22,'Can add log entry',8,'add_logentry'),(23,'Can change log entry',8,'change_logentry'),(24,'Can delete log entry',8,'delete_logentry'),(25,'Can add flat page',9,'add_flatpage'),(26,'Can change flat page',9,'change_flatpage'),(27,'Can delete flat page',9,'delete_flatpage'),(28,'Can add item',10,'add_item'),(29,'Can change item',10,'change_item'),(30,'Can delete item',10,'delete_item'),(31,'Can add layout item',11,'add_layoutitem'),(32,'Can change layout item',11,'change_layoutitem'),(33,'Can delete layout item',11,'delete_layoutitem'),(34,'Can add layout',12,'add_layout'),(35,'Can change layout',12,'change_layout'),(36,'Can delete layout',12,'delete_layout'),(37,'Can add case study translation',13,'add_casestudytranslation'),(38,'Can change case study translation',13,'change_casestudytranslation'),(39,'Can delete case study translation',13,'delete_casestudytranslation'),(40,'Can add Case Study',14,'add_casestudy'),(41,'Can change Case Study',14,'change_casestudy'),(42,'Can delete Case Study',14,'delete_casestudy'),(43,'Can add award',15,'add_award'),(44,'Can change award',15,'change_award'),(45,'Can delete award',15,'delete_award'),(46,'Can add about translation',16,'add_abouttranslation'),(47,'Can change about translation',16,'change_abouttranslation'),(48,'Can delete about translation',16,'delete_abouttranslation'),(49,'Can add About page',17,'add_about'),(50,'Can change About page',17,'change_about'),(51,'Can delete About page',17,'delete_about'),(52,'Can add department',18,'add_department'),(53,'Can change department',18,'change_department'),(54,'Can delete department',18,'delete_department'),(55,'Can add person translation',19,'add_persontranslation'),(56,'Can change person translation',19,'change_persontranslation'),(57,'Can delete person translation',19,'delete_persontranslation'),(58,'Can add person',20,'add_person'),(59,'Can change person',20,'change_person'),(60,'Can delete person',20,'delete_person'),(61,'Can add footer',21,'add_footer'),(62,'Can change footer',21,'change_footer'),(63,'Can delete footer',21,'delete_footer'),(64,'Can add Social link',22,'add_social'),(65,'Can change Social link',22,'change_social'),(66,'Can delete Social link',22,'delete_social'),(67,'Can add Phone number',23,'add_phone'),(68,'Can change Phone number',23,'change_phone'),(69,'Can delete Phone number',23,'delete_phone'),(70,'Can add Email address',24,'add_email'),(71,'Can change Email address',24,'change_email'),(72,'Can delete Email address',24,'delete_email'),(73,'Can add promo translation',25,'add_promotranslation'),(74,'Can change promo translation',25,'change_promotranslation'),(75,'Can delete promo translation',25,'delete_promotranslation'),(76,'Can add promo',26,'add_promo'),(77,'Can change promo',26,'change_promo'),(78,'Can delete promo',26,'delete_promo'),(79,'Can add person',27,'add_person'),(80,'Can change person',27,'change_person'),(81,'Can delete person',27,'delete_person'),(82,'Can add location',28,'add_location'),(83,'Can change location',28,'change_location'),(84,'Can delete location',28,'delete_location'),(85,'Can add link',29,'add_link'),(86,'Can change link',29,'change_link'),(87,'Can delete link',29,'delete_link'),(88,'Can add map',30,'add_map'),(89,'Can change map',30,'change_map'),(90,'Can delete map',30,'delete_map'),(91,'Can add Category',31,'add_category'),(92,'Can change Category',31,'change_category'),(93,'Can delete Category',31,'delete_category'),(94,'Can add story translation',32,'add_storytranslation'),(95,'Can change story translation',32,'change_storytranslation'),(96,'Can delete story translation',32,'delete_storytranslation'),(97,'Can add Story',33,'add_story'),(98,'Can change Story',33,'change_story'),(99,'Can delete Story',33,'delete_story'),(100,'Can add related link',34,'add_relatedlink'),(101,'Can change related link',34,'change_relatedlink'),(102,'Can delete related link',34,'delete_relatedlink'),(103,'Can add friend',35,'add_friend'),(104,'Can change friend',35,'change_friend'),(105,'Can delete friend',35,'delete_friend'),(106,'Can add application',36,'add_application'),(107,'Can change application',36,'change_application'),(108,'Can delete application',36,'delete_application'),(109,'Can add share',37,'add_share'),(110,'Can change share',37,'change_share'),(111,'Can delete share',37,'delete_share'),(112,'Can add posterous account',38,'add_posterousaccount'),(113,'Can change posterous account',38,'change_posterousaccount'),(114,'Can delete posterous account',38,'delete_posterousaccount'),(115,'Can add posterous post',39,'add_posterouspost'),(116,'Can change posterous post',39,'change_posterouspost'),(117,'Can delete posterous post',39,'delete_posterouspost'),(118,'Can add twitter account',40,'add_twitteraccount'),(119,'Can change twitter account',40,'change_twitteraccount'),(120,'Can delete twitter account',40,'delete_twitteraccount'),(121,'Can add twitter tweet',41,'add_twittertweet'),(122,'Can change twitter tweet',41,'change_twittertweet'),(123,'Can delete twitter tweet',41,'delete_twittertweet'),(124,'Can add Analytics',42,'add_analytics'),(125,'Can change Analytics',42,'change_analytics'),(126,'Can delete Analytics',42,'delete_analytics'),(127,'Can add promo box',43,'add_promobox'),(128,'Can change promo box',43,'change_promobox'),(129,'Can delete promo box',43,'delete_promobox'),(130,'Can add migration history',44,'add_migrationhistory'),(131,'Can change migration history',44,'change_migrationhistory'),(132,'Can delete migration history',44,'delete_migrationhistory'),(133,'Can add job translation',45,'add_jobtranslation'),(134,'Can change job translation',45,'change_jobtranslation'),(135,'Can delete job translation',45,'delete_jobtranslation'),(136,'Can add job',46,'add_job'),(137,'Can change job',46,'change_job'),(138,'Can delete job',46,'delete_job');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'admin','','','arthurnn@gmail.com','sha1$69fd6$b7421054472126fca9f235169aabbb93df6429ae',1,1,1,'2011-07-12 18:15:38','2011-07-12 18:15:38');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_fbfc09f1` (`user_id`),
  KEY `auth_user_groups_bda51c3c` (`group_id`),
  CONSTRAINT `user_id_refs_id_831107f1` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `group_id_refs_id_f0ee9890` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_fbfc09f1` (`user_id`),
  KEY `auth_user_user_permissions_1e014c8f` (`permission_id`),
  CONSTRAINT `user_id_refs_id_f2045483` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `permission_id_refs_id_67e79cb` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `common_item`
--

DROP TABLE IF EXISTS `common_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `common_item` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `subclass` varchar(100) NOT NULL,
  `active` tinyint(1) NOT NULL,
  `title` varchar(200) NOT NULL,
  `order` int(11) NOT NULL,
  `created` datetime NOT NULL,
  `updated` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `common_item`
--

LOCK TABLES `common_item` WRITE;
/*!40000 ALTER TABLE `common_item` DISABLE KEYS */;
/*!40000 ALTER TABLE `common_item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contact_link`
--

DROP TABLE IF EXISTS `contact_link`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contact_link` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `url` varchar(200) NOT NULL,
  `image` varchar(100) NOT NULL,
  `order` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contact_link`
--

LOCK TABLES `contact_link` WRITE;
/*!40000 ALTER TABLE `contact_link` DISABLE KEYS */;
/*!40000 ALTER TABLE `contact_link` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contact_location`
--

DROP TABLE IF EXISTS `contact_location`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contact_location` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `address` longtext NOT NULL,
  `latitude` varchar(15) NOT NULL,
  `longitude` varchar(15) NOT NULL,
  `order` int(11) NOT NULL,
  `map_image` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contact_location`
--

LOCK TABLES `contact_location` WRITE;
/*!40000 ALTER TABLE `contact_location` DISABLE KEYS */;
/*!40000 ALTER TABLE `contact_location` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contact_map`
--

DROP TABLE IF EXISTS `contact_map`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contact_map` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `centre_point_latitude` varchar(15) NOT NULL,
  `centre_point_longitude` varchar(15) NOT NULL,
  `zoom_level` varchar(2) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contact_map`
--

LOCK TABLES `contact_map` WRITE;
/*!40000 ALTER TABLE `contact_map` DISABLE KEYS */;
/*!40000 ALTER TABLE `contact_map` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contact_person`
--

DROP TABLE IF EXISTS `contact_person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contact_person` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `description` varchar(100) NOT NULL,
  `telephone` varchar(20) NOT NULL,
  `order` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contact_person`
--

LOCK TABLES `contact_person` WRITE;
/*!40000 ALTER TABLE `contact_person` DISABLE KEYS */;
/*!40000 ALTER TABLE `contact_person` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_fbfc09f1` (`user_id`),
  KEY `django_admin_log_e4470c6e` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_288599e6` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `user_id_refs_id_c8665aa` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'permission','auth','permission'),(2,'group','auth','group'),(3,'user','auth','user'),(4,'message','auth','message'),(5,'content type','contenttypes','contenttype'),(6,'session','sessions','session'),(7,'site','sites','site'),(8,'log entry','admin','logentry'),(9,'flat page','flatpages','flatpage'),(10,'item','common','item'),(11,'layout item','home','layoutitem'),(12,'layout','home','layout'),(13,'case study translation','work','casestudytranslation'),(14,'Case Study','work','casestudy'),(15,'award','work','award'),(16,'about translation','about','abouttranslation'),(17,'About page','about','about'),(18,'department','people','department'),(19,'person translation','people','persontranslation'),(20,'person','people','person'),(21,'footer','footer','footer'),(22,'Social link','footer','social'),(23,'Phone number','footer','phone'),(24,'Email address','footer','email'),(25,'promo translation','footer','promotranslation'),(26,'promo','footer','promo'),(27,'person','contact','person'),(28,'location','contact','location'),(29,'link','contact','link'),(30,'map','contact','map'),(31,'Category','news','category'),(32,'story translation','news','storytranslation'),(33,'Story','news','story'),(34,'related link','news','relatedlink'),(35,'friend','news','friend'),(36,'application','social','application'),(37,'share','social','share'),(38,'posterous account','social','posterousaccount'),(39,'posterous post','social','posterouspost'),(40,'twitter account','social','twitteraccount'),(41,'twitter tweet','social','twittertweet'),(42,'Analytics','social','analytics'),(43,'promo box','social','promobox'),(44,'migration history','south','migrationhistory'),(45,'job translation','jobs','jobtranslation'),(46,'job','jobs','job');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_flatpage`
--

DROP TABLE IF EXISTS `django_flatpage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_flatpage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(100) NOT NULL,
  `title` varchar(200) NOT NULL,
  `content` longtext NOT NULL,
  `enable_comments` tinyint(1) NOT NULL,
  `template_name` varchar(70) NOT NULL,
  `registration_required` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_flatpage_a4b49ab` (`url`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_flatpage`
--

LOCK TABLES `django_flatpage` WRITE;
/*!40000 ALTER TABLE `django_flatpage` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_flatpage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_flatpage_sites`
--

DROP TABLE IF EXISTS `django_flatpage_sites`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_flatpage_sites` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `flatpage_id` int(11) NOT NULL,
  `site_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `flatpage_id` (`flatpage_id`,`site_id`),
  KEY `django_flatpage_sites_dedefef8` (`flatpage_id`),
  KEY `django_flatpage_sites_6223029` (`site_id`),
  CONSTRAINT `flatpage_id_refs_id_c0e84f5a` FOREIGN KEY (`flatpage_id`) REFERENCES `django_flatpage` (`id`),
  CONSTRAINT `site_id_refs_id_4e3eeb57` FOREIGN KEY (`site_id`) REFERENCES `django_site` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_flatpage_sites`
--

LOCK TABLES `django_flatpage_sites` WRITE;
/*!40000 ALTER TABLE `django_flatpage_sites` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_flatpage_sites` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_c25c2c28` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_site`
--

DROP TABLE IF EXISTS `django_site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_site`
--

LOCK TABLES `django_site` WRITE;
/*!40000 ALTER TABLE `django_site` DISABLE KEYS */;
INSERT INTO `django_site` VALUES (1,'example.com','example.com');
/*!40000 ALTER TABLE `django_site` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `footer_email`
--

DROP TABLE IF EXISTS `footer_email`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `footer_email` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `address` varchar(200) NOT NULL,
  `order` int(11) NOT NULL,
  `footer_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `footer_email_c2a35841` (`footer_id`),
  CONSTRAINT `footer_id_refs_item_ptr_id_6836175d` FOREIGN KEY (`footer_id`) REFERENCES `footer_footer` (`item_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `footer_email`
--

LOCK TABLES `footer_email` WRITE;
/*!40000 ALTER TABLE `footer_email` DISABLE KEYS */;
/*!40000 ALTER TABLE `footer_email` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `footer_footer`
--

DROP TABLE IF EXISTS `footer_footer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `footer_footer` (
  `item_ptr_id` int(11) NOT NULL,
  PRIMARY KEY (`item_ptr_id`),
  CONSTRAINT `item_ptr_id_refs_id_3da4f033` FOREIGN KEY (`item_ptr_id`) REFERENCES `common_item` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `footer_footer`
--

LOCK TABLES `footer_footer` WRITE;
/*!40000 ALTER TABLE `footer_footer` DISABLE KEYS */;
/*!40000 ALTER TABLE `footer_footer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `footer_phone`
--

DROP TABLE IF EXISTS `footer_phone`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `footer_phone` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number` varchar(100) NOT NULL,
  `order` int(11) NOT NULL,
  `footer_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `footer_phone_c2a35841` (`footer_id`),
  CONSTRAINT `footer_id_refs_item_ptr_id_9d788c1` FOREIGN KEY (`footer_id`) REFERENCES `footer_footer` (`item_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `footer_phone`
--

LOCK TABLES `footer_phone` WRITE;
/*!40000 ALTER TABLE `footer_phone` DISABLE KEYS */;
/*!40000 ALTER TABLE `footer_phone` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `footer_promo`
--

DROP TABLE IF EXISTS `footer_promo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `footer_promo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `image` varchar(100) NOT NULL,
  `footer_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `footer_promo_c2a35841` (`footer_id`),
  CONSTRAINT `footer_id_refs_item_ptr_id_fe0593de` FOREIGN KEY (`footer_id`) REFERENCES `footer_footer` (`item_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `footer_promo`
--

LOCK TABLES `footer_promo` WRITE;
/*!40000 ALTER TABLE `footer_promo` DISABLE KEYS */;
/*!40000 ALTER TABLE `footer_promo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `footer_promo_translation`
--

DROP TABLE IF EXISTS `footer_promo_translation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `footer_promo_translation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` longtext NOT NULL,
  `language_code` varchar(15) NOT NULL,
  `master_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `language_code` (`language_code`,`master_id`),
  KEY `footer_promo_translation_11e09408` (`language_code`),
  KEY `footer_promo_translation_64d805fc` (`master_id`),
  CONSTRAINT `master_id_refs_id_aa9a741b` FOREIGN KEY (`master_id`) REFERENCES `footer_promo` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `footer_promo_translation`
--

LOCK TABLES `footer_promo_translation` WRITE;
/*!40000 ALTER TABLE `footer_promo_translation` DISABLE KEYS */;
/*!40000 ALTER TABLE `footer_promo_translation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `footer_social`
--

DROP TABLE IF EXISTS `footer_social`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `footer_social` (
  `item_ptr_id` int(11) NOT NULL,
  `link` varchar(200) NOT NULL,
  `image` varchar(100) NOT NULL,
  `footer_id` int(11) NOT NULL,
  PRIMARY KEY (`item_ptr_id`),
  KEY `footer_social_c2a35841` (`footer_id`),
  CONSTRAINT `footer_id_refs_item_ptr_id_b9ab3375` FOREIGN KEY (`footer_id`) REFERENCES `footer_footer` (`item_ptr_id`),
  CONSTRAINT `item_ptr_id_refs_id_3f39f26b` FOREIGN KEY (`item_ptr_id`) REFERENCES `common_item` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `footer_social`
--

LOCK TABLES `footer_social` WRITE;
/*!40000 ALTER TABLE `footer_social` DISABLE KEYS */;
/*!40000 ALTER TABLE `footer_social` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_layout`
--

DROP TABLE IF EXISTS `home_layout`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `home_layout` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `case_study_large_1_id` int(11) NOT NULL,
  `case_study_large_2_id` int(11) NOT NULL,
  `case_study_large_3_id` int(11) NOT NULL,
  `case_study_small_1_id` int(11) NOT NULL,
  `case_study_small_2_id` int(11) NOT NULL,
  `case_study_small_3_id` int(11) NOT NULL,
  `news_story_1_id` int(11) NOT NULL,
  `news_story_2_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `home_layout_6976e82c` (`case_study_large_1_id`),
  KEY `home_layout_87e12c4f` (`case_study_large_2_id`),
  KEY `home_layout_36228116` (`case_study_large_3_id`),
  KEY `home_layout_ac0d5200` (`case_study_small_1_id`),
  KEY `home_layout_6dc13c4d` (`case_study_small_2_id`),
  KEY `home_layout_a78cb62e` (`case_study_small_3_id`),
  KEY `home_layout_b264a833` (`news_story_1_id`),
  KEY `home_layout_6910d2ec` (`news_story_2_id`),
  CONSTRAINT `news_story_2_id_refs_layoutitem_ptr_id_a0e5c74f` FOREIGN KEY (`news_story_2_id`) REFERENCES `news_story` (`layoutitem_ptr_id`),
  CONSTRAINT `case_study_large_1_id_refs_layoutitem_ptr_id_48bee05d` FOREIGN KEY (`case_study_large_1_id`) REFERENCES `work_casestudy` (`layoutitem_ptr_id`),
  CONSTRAINT `case_study_large_2_id_refs_layoutitem_ptr_id_48bee05d` FOREIGN KEY (`case_study_large_2_id`) REFERENCES `work_casestudy` (`layoutitem_ptr_id`),
  CONSTRAINT `case_study_large_3_id_refs_layoutitem_ptr_id_48bee05d` FOREIGN KEY (`case_study_large_3_id`) REFERENCES `work_casestudy` (`layoutitem_ptr_id`),
  CONSTRAINT `case_study_small_1_id_refs_layoutitem_ptr_id_48bee05d` FOREIGN KEY (`case_study_small_1_id`) REFERENCES `work_casestudy` (`layoutitem_ptr_id`),
  CONSTRAINT `case_study_small_2_id_refs_layoutitem_ptr_id_48bee05d` FOREIGN KEY (`case_study_small_2_id`) REFERENCES `work_casestudy` (`layoutitem_ptr_id`),
  CONSTRAINT `case_study_small_3_id_refs_layoutitem_ptr_id_48bee05d` FOREIGN KEY (`case_study_small_3_id`) REFERENCES `work_casestudy` (`layoutitem_ptr_id`),
  CONSTRAINT `news_story_1_id_refs_layoutitem_ptr_id_a0e5c74f` FOREIGN KEY (`news_story_1_id`) REFERENCES `news_story` (`layoutitem_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_layout`
--

LOCK TABLES `home_layout` WRITE;
/*!40000 ALTER TABLE `home_layout` DISABLE KEYS */;
/*!40000 ALTER TABLE `home_layout` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_layoutitem`
--

DROP TABLE IF EXISTS `home_layoutitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `home_layoutitem` (
  `item_ptr_id` int(11) NOT NULL,
  PRIMARY KEY (`item_ptr_id`),
  CONSTRAINT `item_ptr_id_refs_id_1d53561b` FOREIGN KEY (`item_ptr_id`) REFERENCES `common_item` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_layoutitem`
--

LOCK TABLES `home_layoutitem` WRITE;
/*!40000 ALTER TABLE `home_layoutitem` DISABLE KEYS */;
/*!40000 ALTER TABLE `home_layoutitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jobs_job`
--

DROP TABLE IF EXISTS `jobs_job`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jobs_job` (
  `item_ptr_id` int(11) NOT NULL,
  `contact` varchar(200) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `specification` varchar(100) NOT NULL,
  PRIMARY KEY (`item_ptr_id`),
  UNIQUE KEY `slug` (`slug`),
  CONSTRAINT `item_ptr_id_refs_id_e288ddf9` FOREIGN KEY (`item_ptr_id`) REFERENCES `common_item` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobs_job`
--

LOCK TABLES `jobs_job` WRITE;
/*!40000 ALTER TABLE `jobs_job` DISABLE KEYS */;
/*!40000 ALTER TABLE `jobs_job` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jobs_job_translation`
--

DROP TABLE IF EXISTS `jobs_job_translation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jobs_job_translation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `body` longtext NOT NULL,
  `language_code` varchar(15) NOT NULL,
  `master_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `language_code` (`language_code`,`master_id`),
  KEY `jobs_job_translation_11e09408` (`language_code`),
  KEY `jobs_job_translation_64d805fc` (`master_id`),
  CONSTRAINT `master_id_refs_item_ptr_id_bf9a8525` FOREIGN KEY (`master_id`) REFERENCES `jobs_job` (`item_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobs_job_translation`
--

LOCK TABLES `jobs_job_translation` WRITE;
/*!40000 ALTER TABLE `jobs_job_translation` DISABLE KEYS */;
/*!40000 ALTER TABLE `jobs_job_translation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `news_category`
--

DROP TABLE IF EXISTS `news_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `news_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `slug` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `news_category`
--

LOCK TABLES `news_category` WRITE;
/*!40000 ALTER TABLE `news_category` DISABLE KEYS */;
/*!40000 ALTER TABLE `news_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `news_friend`
--

DROP TABLE IF EXISTS `news_friend`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `news_friend` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `description` varchar(200) NOT NULL,
  `url` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `news_friend`
--

LOCK TABLES `news_friend` WRITE;
/*!40000 ALTER TABLE `news_friend` DISABLE KEYS */;
/*!40000 ALTER TABLE `news_friend` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `news_relatedlink`
--

DROP TABLE IF EXISTS `news_relatedlink`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `news_relatedlink` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `story_id` int(11) NOT NULL,
  `description` varchar(200) NOT NULL,
  `url` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `news_relatedlink_f5ae222e` (`story_id`),
  CONSTRAINT `story_id_refs_layoutitem_ptr_id_580e8d23` FOREIGN KEY (`story_id`) REFERENCES `news_story` (`layoutitem_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `news_relatedlink`
--

LOCK TABLES `news_relatedlink` WRITE;
/*!40000 ALTER TABLE `news_relatedlink` DISABLE KEYS */;
/*!40000 ALTER TABLE `news_relatedlink` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `news_story`
--

DROP TABLE IF EXISTS `news_story`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `news_story` (
  `layoutitem_ptr_id` int(11) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `created_by_id` int(11) DEFAULT NULL,
  `author_id` int(11) DEFAULT NULL,
  `category_id` int(11) DEFAULT NULL,
  `sticky` tinyint(1) NOT NULL,
  `image` varchar(100) NOT NULL,
  `publish_date` datetime NOT NULL,
  `country` varchar(10) NOT NULL,
  `external_db_id` int(11) DEFAULT NULL,
  `publish_to_external` tinyint(1) NOT NULL,
  `posting_agency` varchar(200) NOT NULL,
  PRIMARY KEY (`layoutitem_ptr_id`),
  UNIQUE KEY `slug` (`slug`),
  KEY `news_story_b5de30be` (`created_by_id`),
  KEY `news_story_cc846901` (`author_id`),
  KEY `news_story_42dc49bc` (`category_id`),
  CONSTRAINT `author_id_refs_layoutitem_ptr_id_d5e45b18` FOREIGN KEY (`author_id`) REFERENCES `people_person` (`layoutitem_ptr_id`),
  CONSTRAINT `category_id_refs_id_b101d80d` FOREIGN KEY (`category_id`) REFERENCES `news_category` (`id`),
  CONSTRAINT `layoutitem_ptr_id_refs_item_ptr_id_2ab15f16` FOREIGN KEY (`layoutitem_ptr_id`) REFERENCES `home_layoutitem` (`item_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `news_story`
--

LOCK TABLES `news_story` WRITE;
/*!40000 ALTER TABLE `news_story` DISABLE KEYS */;
/*!40000 ALTER TABLE `news_story` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `news_story_translation`
--

DROP TABLE IF EXISTS `news_story_translation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `news_story_translation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `body` longtext NOT NULL,
  `language_code` varchar(15) NOT NULL,
  `master_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `language_code` (`language_code`,`master_id`),
  KEY `news_story_translation_11e09408` (`language_code`),
  KEY `news_story_translation_64d805fc` (`master_id`),
  CONSTRAINT `master_id_refs_layoutitem_ptr_id_6a84909b` FOREIGN KEY (`master_id`) REFERENCES `news_story` (`layoutitem_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `news_story_translation`
--

LOCK TABLES `news_story_translation` WRITE;
/*!40000 ALTER TABLE `news_story_translation` DISABLE KEYS */;
/*!40000 ALTER TABLE `news_story_translation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `people_department`
--

DROP TABLE IF EXISTS `people_department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `people_department` (
  `item_ptr_id` int(11) NOT NULL,
  `colour` varchar(7) NOT NULL,
  `slug` varchar(50) NOT NULL,
  PRIMARY KEY (`item_ptr_id`),
  UNIQUE KEY `slug` (`slug`),
  CONSTRAINT `item_ptr_id_refs_id_be9c73f4` FOREIGN KEY (`item_ptr_id`) REFERENCES `common_item` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `people_department`
--

LOCK TABLES `people_department` WRITE;
/*!40000 ALTER TABLE `people_department` DISABLE KEYS */;
/*!40000 ALTER TABLE `people_department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `people_person`
--

DROP TABLE IF EXISTS `people_person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `people_person` (
  `layoutitem_ptr_id` int(11) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `role` varchar(100) NOT NULL,
  `image` varchar(100) NOT NULL,
  `department_id` int(11) NOT NULL,
  PRIMARY KEY (`layoutitem_ptr_id`),
  UNIQUE KEY `slug` (`slug`),
  KEY `people_person_2ae7390` (`department_id`),
  CONSTRAINT `department_id_refs_item_ptr_id_a824ccbc` FOREIGN KEY (`department_id`) REFERENCES `people_department` (`item_ptr_id`),
  CONSTRAINT `layoutitem_ptr_id_refs_item_ptr_id_90ecafd` FOREIGN KEY (`layoutitem_ptr_id`) REFERENCES `home_layoutitem` (`item_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `people_person`
--

LOCK TABLES `people_person` WRITE;
/*!40000 ALTER TABLE `people_person` DISABLE KEYS */;
/*!40000 ALTER TABLE `people_person` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `people_person_translation`
--

DROP TABLE IF EXISTS `people_person_translation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `people_person_translation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `body` longtext NOT NULL,
  `language_code` varchar(15) NOT NULL,
  `master_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `language_code` (`language_code`,`master_id`),
  KEY `people_person_translation_11e09408` (`language_code`),
  KEY `people_person_translation_64d805fc` (`master_id`),
  CONSTRAINT `master_id_refs_layoutitem_ptr_id_803fc4d1` FOREIGN KEY (`master_id`) REFERENCES `people_person` (`layoutitem_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `people_person_translation`
--

LOCK TABLES `people_person_translation` WRITE;
/*!40000 ALTER TABLE `people_person_translation` DISABLE KEYS */;
/*!40000 ALTER TABLE `people_person_translation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `social_analytics`
--

DROP TABLE IF EXISTS `social_analytics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `social_analytics` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(25) NOT NULL,
  `position` varchar(20) NOT NULL,
  `embed` longtext NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `position` (`position`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `social_analytics`
--

LOCK TABLES `social_analytics` WRITE;
/*!40000 ALTER TABLE `social_analytics` DISABLE KEYS */;
/*!40000 ALTER TABLE `social_analytics` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `social_application`
--

DROP TABLE IF EXISTS `social_application`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `social_application` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `install` varchar(20) NOT NULL,
  `order` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `install` (`install`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `social_application`
--

LOCK TABLES `social_application` WRITE;
/*!40000 ALTER TABLE `social_application` DISABLE KEYS */;
/*!40000 ALTER TABLE `social_application` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `social_posterousaccount`
--

DROP TABLE IF EXISTS `social_posterousaccount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `social_posterousaccount` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `site_uid` varchar(15) NOT NULL,
  `user` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `social_posterousaccount`
--

LOCK TABLES `social_posterousaccount` WRITE;
/*!40000 ALTER TABLE `social_posterousaccount` DISABLE KEYS */;
/*!40000 ALTER TABLE `social_posterousaccount` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `social_posterouspost`
--

DROP TABLE IF EXISTS `social_posterouspost`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `social_posterouspost` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` varchar(100) NOT NULL,
  `title` varchar(100) NOT NULL,
  `created` datetime NOT NULL,
  `url` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `social_posterouspost`
--

LOCK TABLES `social_posterouspost` WRITE;
/*!40000 ALTER TABLE `social_posterouspost` DISABLE KEYS */;
/*!40000 ALTER TABLE `social_posterouspost` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `social_promobox`
--

DROP TABLE IF EXISTS `social_promobox`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `social_promobox` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `body` longtext NOT NULL,
  `url_title` varchar(100) NOT NULL,
  `url` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `social_promobox`
--

LOCK TABLES `social_promobox` WRITE;
/*!40000 ALTER TABLE `social_promobox` DISABLE KEYS */;
/*!40000 ALTER TABLE `social_promobox` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `social_share`
--

DROP TABLE IF EXISTS `social_share`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `social_share` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `install` varchar(20) NOT NULL,
  `order` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `install` (`install`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `social_share`
--

LOCK TABLES `social_share` WRITE;
/*!40000 ALTER TABLE `social_share` DISABLE KEYS */;
/*!40000 ALTER TABLE `social_share` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `social_twitteraccount`
--

DROP TABLE IF EXISTS `social_twitteraccount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `social_twitteraccount` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `screen_name` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `social_twitteraccount`
--

LOCK TABLES `social_twitteraccount` WRITE;
/*!40000 ALTER TABLE `social_twitteraccount` DISABLE KEYS */;
/*!40000 ALTER TABLE `social_twitteraccount` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `social_twittertweet`
--

DROP TABLE IF EXISTS `social_twittertweet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `social_twittertweet` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `text` varchar(140) NOT NULL,
  `created` datetime NOT NULL,
  `user_id` varchar(25) NOT NULL,
  `uid` varchar(200) NOT NULL,
  `screen_name` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uid` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `social_twittertweet`
--

LOCK TABLES `social_twittertweet` WRITE;
/*!40000 ALTER TABLE `social_twittertweet` DISABLE KEYS */;
/*!40000 ALTER TABLE `social_twittertweet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `south_migrationhistory`
--

DROP TABLE IF EXISTS `south_migrationhistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `south_migrationhistory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_name` varchar(255) NOT NULL,
  `migration` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `south_migrationhistory`
--

LOCK TABLES `south_migrationhistory` WRITE;
/*!40000 ALTER TABLE `south_migrationhistory` DISABLE KEYS */;
/*!40000 ALTER TABLE `south_migrationhistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `work_award`
--

DROP TABLE IF EXISTS `work_award`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `work_award` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `description` varchar(200) NOT NULL,
  `image` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `case_study_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `work_award_1d7168bc` (`case_study_id`),
  CONSTRAINT `case_study_id_refs_layoutitem_ptr_id_b1bf1163` FOREIGN KEY (`case_study_id`) REFERENCES `work_casestudy` (`layoutitem_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `work_award`
--

LOCK TABLES `work_award` WRITE;
/*!40000 ALTER TABLE `work_award` DISABLE KEYS */;
/*!40000 ALTER TABLE `work_award` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `work_casestudy`
--

DROP TABLE IF EXISTS `work_casestudy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `work_casestudy` (
  `layoutitem_ptr_id` int(11) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `created_by_id` int(11) DEFAULT NULL,
  `hero_image` varchar(100) NOT NULL,
  `video_image` varchar(100) NOT NULL,
  `video` varchar(100) NOT NULL,
  `url` varchar(200) NOT NULL,
  `publish_date` date NOT NULL,
  `country` varchar(10) NOT NULL,
  `external_db_id` int(11) DEFAULT NULL,
  `publish_to_external` tinyint(1) NOT NULL,
  `posting_agency` varchar(200) NOT NULL,
  `share_url` varchar(200) NOT NULL,
  PRIMARY KEY (`layoutitem_ptr_id`),
  UNIQUE KEY `slug` (`slug`),
  KEY `work_casestudy_b5de30be` (`created_by_id`),
  CONSTRAINT `layoutitem_ptr_id_refs_item_ptr_id_6d80eb48` FOREIGN KEY (`layoutitem_ptr_id`) REFERENCES `home_layoutitem` (`item_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `work_casestudy`
--

LOCK TABLES `work_casestudy` WRITE;
/*!40000 ALTER TABLE `work_casestudy` DISABLE KEYS */;
/*!40000 ALTER TABLE `work_casestudy` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `work_casestudy_translation`
--

DROP TABLE IF EXISTS `work_casestudy_translation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `work_casestudy_translation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `body` longtext NOT NULL,
  `language_code` varchar(15) NOT NULL,
  `master_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `language_code` (`language_code`,`master_id`),
  KEY `work_casestudy_translation_11e09408` (`language_code`),
  KEY `work_casestudy_translation_64d805fc` (`master_id`),
  CONSTRAINT `master_id_refs_layoutitem_ptr_id_b897d4d5` FOREIGN KEY (`master_id`) REFERENCES `work_casestudy` (`layoutitem_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `work_casestudy_translation`
--

LOCK TABLES `work_casestudy_translation` WRITE;
/*!40000 ALTER TABLE `work_casestudy_translation` DISABLE KEYS */;
/*!40000 ALTER TABLE `work_casestudy_translation` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2011-07-12 13:15:59
