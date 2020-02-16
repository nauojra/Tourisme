-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le :  Dim 16 fév. 2020 à 13:38
-- Version du serveur :  10.4.10-MariaDB
-- Version de PHP :  7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `agence_tourisme`
--

-- --------------------------------------------------------

--
-- Structure de la table `activites`
--

DROP TABLE IF EXISTS `activites`;
CREATE TABLE IF NOT EXISTS `activites` (
  `idActivite` int(11) NOT NULL AUTO_INCREMENT,
  `nomActivite` varchar(100) NOT NULL,
  `typeActivite` varchar(250) NOT NULL,
  `descriptionActivite` varchar(2500) NOT NULL,
  `dateActivite` int(11) NOT NULL,
  `lieuActivite` varchar(100) NOT NULL,
  PRIMARY KEY (`idActivite`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `contact`
--

DROP TABLE IF EXISTS `contact`;
CREATE TABLE IF NOT EXISTS `contact` (
  `idContact` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(50) NOT NULL,
  `nom` varchar(20) NOT NULL,
  `message` varchar(1000) NOT NULL,
  PRIMARY KEY (`idContact`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `guide`
--

DROP TABLE IF EXISTS `guide`;
CREATE TABLE IF NOT EXISTS `guide` (
  `idGuide` int(11) NOT NULL AUTO_INCREMENT,
  `nomGuide` varchar(20) NOT NULL,
  `prenomGuide` varchar(20) NOT NULL,
  `ville` varchar(20) NOT NULL,
  `adresse` varchar(50) NOT NULL,
  `tel` int(14) NOT NULL,
  `mail` varchar(50) NOT NULL,
  `langues` varchar(20) NOT NULL,
  `description` varchar(2500) NOT NULL,
  `note` varchar(1000) NOT NULL,
  PRIMARY KEY (`idGuide`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `hotel`
--

DROP TABLE IF EXISTS `hotel`;
CREATE TABLE IF NOT EXISTS `hotel` (
  `idHotel` int(11) NOT NULL AUTO_INCREMENT,
  `nomHotel` varchar(50) NOT NULL,
  `Description` varchar(2500) NOT NULL,
  `noteHotel` varchar(500) NOT NULL,
  PRIMARY KEY (`idHotel`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `restaurant`
--

DROP TABLE IF EXISTS `restaurant`;
CREATE TABLE IF NOT EXISTS `restaurant` (
  `IdRestaurant` int(11) NOT NULL AUTO_INCREMENT,
  `Nomrestaurant` varchar(20) NOT NULL,
  `LieuRestaurant` varchar(200) NOT NULL,
  `DescriptionRestaurant` varchar(2500) NOT NULL,
  `NoteRestaurant` varchar(2500) NOT NULL,
  PRIMARY KEY (`IdRestaurant`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `transport`
--

DROP TABLE IF EXISTS `transport`;
CREATE TABLE IF NOT EXISTS `transport` (
  `idTransport` int(11) NOT NULL AUTO_INCREMENT,
  `typeTransport` varchar(50) NOT NULL,
  `lienTransport` varchar(500) NOT NULL,
  `description` varchar(2500) NOT NULL,
  PRIMARY KEY (`idTransport`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `visiteguide`
--

DROP TABLE IF EXISTS `visiteguide`;
CREATE TABLE IF NOT EXISTS `visiteguide` (
  `idVisite` int(11) NOT NULL AUTO_INCREMENT,
  `nomVisite` varchar(20) NOT NULL,
  `dateVisite` int(11) NOT NULL,
  `lieuVisite` varchar(50) NOT NULL,
  `nomGuide` varchar(20) NOT NULL,
  `capaciteMax` int(11) NOT NULL,
  `capaciteActuelle` int(11) NOT NULL,
  `commentaire` varchar(1000) NOT NULL,
  PRIMARY KEY (`idVisite`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
