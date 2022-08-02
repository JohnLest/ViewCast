-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3307
-- Generation Time: Jul 18, 2022 at 04:41 PM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `viewcast`
--

-- --------------------------------------------------------

--
-- Table structure for table `flux`
--

DROP TABLE IF EXISTS `flux`;
CREATE TABLE IF NOT EXISTS `flux` (
  `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  `url` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `url` (`url`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `flux_data`
--

DROP TABLE IF EXISTS `flux_data`;
CREATE TABLE IF NOT EXISTS `flux_data` (
  `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  `position` tinyint(3) UNSIGNED NOT NULL,
  `time` tinyint(3) UNSIGNED NOT NULL,
  `id_flux` bigint(20) UNSIGNED NOT NULL,
  `id_media` bigint(20) UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  KEY `flux_exist` (`id_flux`),
  KEY `media_exist` (`id_media`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `medias`
--

DROP TABLE IF EXISTS `medias`;
CREATE TABLE IF NOT EXISTS `medias` (
  `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` varchar(15) NOT NULL,
  `id_users` bigint(20) UNSIGNED NOT NULL,
  `id_media_type` tinyint(3) UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_exist` (`id_users`),
  KEY `media_type_exist` (`id_media_type`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `media_type`
--

DROP TABLE IF EXISTS `media_type`;
CREATE TABLE IF NOT EXISTS `media_type` (
  `id` tinyint(3) UNSIGNED NOT NULL AUTO_INCREMENT,
  `type` varchar(5) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `type` (`type`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `media_type`
--

INSERT INTO `media_type` (`id`, `type`) VALUES
(4, 'gif'),
(3, 'jpeg'),
(2, 'jpg'),
(1, 'png');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` varchar(15) NOT NULL,
  `mail` varchar(25) NOT NULL,
  `password` varchar(255) NOT NULL,
  `company` varchar(25) NOT NULL,
  `location` varchar(25) DEFAULT NULL,
  `is_admin` tinyint(1) NOT NULL DEFAULT 0,
  `path_media` varchar(25) NOT NULL
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `mail` (`mail`),
  UNIQUE KEY `path_media` (`path_media`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `flux_data`
--
ALTER TABLE `flux_data`
  ADD CONSTRAINT `flux_exist` FOREIGN KEY (`id_flux`) REFERENCES `flux` (`id`),
  ADD CONSTRAINT `media_exist` FOREIGN KEY (`id_media`) REFERENCES `medias` (`id`);

--
-- Constraints for table `medias`
--
ALTER TABLE `medias`
  ADD CONSTRAINT `media_type_exist` FOREIGN KEY (`id_media_type`) REFERENCES `media_type` (`id`),
  ADD CONSTRAINT `user_exist` FOREIGN KEY (`id_users`) REFERENCES `users` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
