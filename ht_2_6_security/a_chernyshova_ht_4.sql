-- --------------------------------------------------------
-- Хост:                         127.0.0.1
-- Версия сервера:               5.7.18 - MySQL Community Server (GPL)
-- ОС Сервера:                   Win64
-- HeidiSQL Версия:              9.3.0.4984
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- Дамп структуры базы данных dealership
CREATE DATABASE IF NOT EXISTS `dealership` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `dealership`;


-- Дамп структуры для таблица dealership.cars
CREATE TABLE IF NOT EXISTS `cars` (
  `id_car` int(11) NOT NULL,
  `car_model` varchar(255) NOT NULL,
  `maker` varchar(255) NOT NULL,
  `year_production` int(11) NOT NULL,
  `car_engine` float NOT NULL,
  `cost` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_car`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Дамп данных таблицы dealership.cars: ~17 rows (приблизительно)
/*!40000 ALTER TABLE `cars` DISABLE KEYS */;
INSERT INTO `cars` (`id_car`, `car_model`, `maker`, `year_production`, `car_engine`, `cost`) VALUES
	(1, 'Q3', 'Audi', 2016, 2, 10),
	(2, 'Cherokee', 'Jeep', 2016, 2.5, 34000),
	(3, 'RAV-4', 'Toyota', 2016, 2.4, 27000),
	(4, 'AXLE', 'Lorry', 2013, 2, 20000),
	(6, 'Grand Cherokee', 'Jeep', 2016, 2.5, 47000),
	(7, 'Q3', 'Audi', 2016, 2.2, 31500),
	(8, 'Test1', 'Test', 2000, 2.4, 10000),
	(9, 'Test2', 'Test', 2005, 2.4, 10000),
	(10, 'lorriest', 'lorry', 2015, 2.3, 16000),
	(11, 'Lorry_truck', 'Lorry', 2015, 2, 25000),
	(12, 'Lorry_mini', 'Lorry', 2015, 2, 27000),
	(13, 'Lorry_ven', 'Lorry', 2015, 2, 27000),
	(14, 'test', 'test maker', 2017, 2.5, 15000),
	(17, 'qwe', 'dodge', 2005, 2, 11000),
	(18, 'Q3', 'AUDI', 2017, 2.5, 38000),
	(19, 'Alpha', 'ROMEO', 2017, 2.5, 58000),
	(20, 'Guilia', 'ALPHAROMEO', 2016, 2, 37000);
/*!40000 ALTER TABLE `cars` ENABLE KEYS */;


-- Дамп структуры для таблица dealership.dealership
CREATE TABLE IF NOT EXISTS `dealership` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_car` int(11) NOT NULL,
  `amount` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_car` (`id_car`),
  CONSTRAINT `dealership_ibfk_1` FOREIGN KEY (`id_car`) REFERENCES `cars` (`id_car`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

-- Дамп данных таблицы dealership.dealership: ~10 rows (приблизительно)
/*!40000 ALTER TABLE `dealership` DISABLE KEYS */;
INSERT INTO `dealership` (`id`, `id_car`, `amount`) VALUES
	(1, 1, 20),
	(2, 2, 18),
	(3, 3, 27),
	(4, 4, 11),
	(5, 11, 2),
	(6, 7, 3),
	(8, 6, 1),
	(9, 18, 10),
	(10, 19, 25),
	(11, 20, 5);
/*!40000 ALTER TABLE `dealership` ENABLE KEYS */;


-- Дамп структуры для таблица dealership.lorries
CREATE TABLE IF NOT EXISTS `lorries` (
  `id_lorry` int(11) NOT NULL AUTO_INCREMENT,
  `weight_limit` int(11) NOT NULL,
  `id_car` int(11) NOT NULL,
  PRIMARY KEY (`id_lorry`),
  KEY `id_car` (`id_car`),
  CONSTRAINT `lorries_ibfk_1` FOREIGN KEY (`id_car`) REFERENCES `cars` (`id_car`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- Дамп данных таблицы dealership.lorries: ~4 rows (приблизительно)
/*!40000 ALTER TABLE `lorries` DISABLE KEYS */;
INSERT INTO `lorries` (`id_lorry`, `weight_limit`, `id_car`) VALUES
	(1, 25, 4),
	(2, 38, 11),
	(3, 45, 13),
	(4, 20, 10);
/*!40000 ALTER TABLE `lorries` ENABLE KEYS */;


-- Дамп структуры для таблица dealership.users
CREATE TABLE IF NOT EXISTS `users` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `login` char(50) NOT NULL,
  `password` char(50) NOT NULL,
  `role` int(11) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

-- Дамп данных таблицы dealership.users: ~10 rows (приблизительно)
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` (`ID`, `login`, `password`, `role`) VALUES
	(1, 'admin', '21232f297a57a5a743894a0e4a801fc3', 1),
	(2, 'user', 'ee11cbb19052e40b07aac0ca060c23ee', 0),
	(3, 'reader', '1de9b0a30075ae8c303eb420c103c320', 2),
	(4, 'reader1', '1de9b0a30075ae8c303eb420c103c320', 2),
	(11, 'encoded', 'f5940b84575914413f594076970e8c24', 2);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
