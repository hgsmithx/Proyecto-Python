-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.5.2-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             10.2.0.5599
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Volcando estructura de base de datos para proyectovacuna
CREATE DATABASE IF NOT EXISTS `proyectovacuna` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `proyectovacuna`;

-- Volcando estructura para tabla proyectovacuna.paciente
CREATE TABLE IF NOT EXISTS `paciente` (
  `rut` varchar(15) NOT NULL,
  `nombre` varchar(30) DEFAULT NULL,
  `fecha_nac` date DEFAULT NULL,
  PRIMARY KEY (`rut`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla proyectovacuna.paciente: ~7 rows (aproximadamente)
/*!40000 ALTER TABLE `paciente` DISABLE KEYS */;
INSERT INTO `paciente` (`rut`, `nombre`, `fecha_nac`) VALUES
	('12.123.123-4', 'Pedro', '2020-04-14'),
	('18.817.210-5', 'Nacho', '2020-04-14'),
	('18.817.210-6', 'Cesar Mora', '2020-04-22'),
	('18.817.210-8', 'Cesar Mora', '2020-04-29'),
	('19.092.078-K', 'Hugo Smith', '1995-05-16'),
	('19.123.664-5', 'Ignacio Medina', '1996-07-22');
/*!40000 ALTER TABLE `paciente` ENABLE KEYS */;

-- Volcando estructura para tabla proyectovacuna.recibe
CREATE TABLE IF NOT EXISTS `recibe` (
  `rut_paciente` varchar(15) NOT NULL,
  `id_vacuna` int(11) NOT NULL,
  `fecha_vacuna` date DEFAULT curdate(),
  KEY `rut_paciente` (`rut_paciente`),
  KEY `id_vacuna` (`id_vacuna`),
  CONSTRAINT `recibe_ibfk_1` FOREIGN KEY (`rut_paciente`) REFERENCES `paciente` (`rut`),
  CONSTRAINT `recibe_ibfk_2` FOREIGN KEY (`id_vacuna`) REFERENCES `vacuna` (`idVacuna`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla proyectovacuna.recibe: ~10 rows (aproximadamente)
/*!40000 ALTER TABLE `recibe` DISABLE KEYS */;
INSERT INTO `recibe` (`rut_paciente`, `id_vacuna`, `fecha_vacuna`) VALUES
	('19.123.664-5', 2, '2020-04-01'),
	('18.817.210-8', 5, '2020-04-02'),
	('19.123.664-5', 5, '2020-04-02'),
	('18.817.210-5', 5, '2020-04-02'),
	('19.123.664-5', 4, '2020-04-02'),
	('12.123.123-4', 7, '2020-04-02'),
	('19.123.664-5', 46, '2020-04-02'),
	('19.123.664-5', 6, '2020-04-02'),
	('19.123.664-5', 1, '2020-04-02'),
	('19.123.664-5', 7, '2020-04-02');
/*!40000 ALTER TABLE `recibe` ENABLE KEYS */;

-- Volcando estructura para tabla proyectovacuna.vacuna
CREATE TABLE IF NOT EXISTS `vacuna` (
  `idVacuna` int(11) NOT NULL AUTO_INCREMENT,
  `enfermedad` varchar(30) DEFAULT NULL,
  `fecha_registro` date DEFAULT curdate(),
  PRIMARY KEY (`idVacuna`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla proyectovacuna.vacuna: ~9 rows (aproximadamente)
/*!40000 ALTER TABLE `vacuna` DISABLE KEYS */;
INSERT INTO `vacuna` (`idVacuna`, `enfermedad`, `fecha_registro`) VALUES
	(1, 'Tuberculosis', '2020-04-02'),
	(2, 'Malaria', '2020-04-02'),
	(4, 'Coronavirus', '2020-04-02'),
	(5, 'Juana', '2020-04-02'),
	(6, 'Pernil', '2020-04-02'),
	(7, 'Perejil', '2020-04-02'),
	(46, 'Corona', '2020-04-02'),
	(47, 'Tubercu', '2020-04-02');
/*!40000 ALTER TABLE `vacuna` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
