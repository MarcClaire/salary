-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : lun. 01 avr. 2024 à 19:10
-- Version du serveur : 10.4.28-MariaDB
-- Version de PHP : 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `salary2`
--

-- --------------------------------------------------------

--
-- Structure de la table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Déchargement des données de la table `auth_group`
--

INSERT INTO `auth_group` (`id`, `name`) VALUES
(1, 'RESSOURCES HUMAINES'),
(2, 'MOYENS GENERAUX'),
(3, 'AGENT');

-- --------------------------------------------------------

--
-- Structure de la table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Structure de la table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Déchargement des données de la table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add categorie', 7, 'add_categorie'),
(26, 'Can change categorie', 7, 'change_categorie'),
(27, 'Can delete categorie', 7, 'delete_categorie'),
(28, 'Can view categorie', 7, 'view_categorie'),
(29, 'Can add contrat', 8, 'add_contrat'),
(30, 'Can change contrat', 8, 'change_contrat'),
(31, 'Can delete contrat', 8, 'delete_contrat'),
(32, 'Can view contrat', 8, 'view_contrat'),
(33, 'Can add diplome', 9, 'add_diplome'),
(34, 'Can change diplome', 9, 'change_diplome'),
(35, 'Can delete diplome', 9, 'delete_diplome'),
(36, 'Can view diplome', 9, 'view_diplome'),
(37, 'Can add mode calcule', 10, 'add_modecalcule'),
(38, 'Can change mode calcule', 10, 'change_modecalcule'),
(39, 'Can delete mode calcule', 10, 'delete_modecalcule'),
(40, 'Can view mode calcule', 10, 'view_modecalcule'),
(41, 'Can add paiement', 11, 'add_paiement'),
(42, 'Can change paiement', 11, 'change_paiement'),
(43, 'Can delete paiement', 11, 'delete_paiement'),
(44, 'Can view paiement', 11, 'view_paiement'),
(45, 'Can add situation matrimoniale', 12, 'add_situationmatrimoniale'),
(46, 'Can change situation matrimoniale', 12, 'change_situationmatrimoniale'),
(47, 'Can delete situation matrimoniale', 12, 'delete_situationmatrimoniale'),
(48, 'Can view situation matrimoniale', 12, 'view_situationmatrimoniale'),
(49, 'Can add specialite', 13, 'add_specialite'),
(50, 'Can change specialite', 13, 'change_specialite'),
(51, 'Can delete specialite', 13, 'delete_specialite'),
(52, 'Can view specialite', 13, 'view_specialite'),
(53, 'Can add structure', 14, 'add_structure'),
(54, 'Can change structure', 14, 'change_structure'),
(55, 'Can delete structure', 14, 'delete_structure'),
(56, 'Can view structure', 14, 'view_structure'),
(57, 'Can add type contrat', 15, 'add_typecontrat'),
(58, 'Can change type contrat', 15, 'change_typecontrat'),
(59, 'Can delete type contrat', 15, 'delete_typecontrat'),
(60, 'Can view type contrat', 15, 'view_typecontrat'),
(61, 'Can add pointage', 16, 'add_pointage'),
(62, 'Can change pointage', 16, 'change_pointage'),
(63, 'Can delete pointage', 16, 'delete_pointage'),
(64, 'Can view pointage', 16, 'view_pointage'),
(65, 'Can add employe', 17, 'add_employe'),
(66, 'Can change employe', 17, 'change_employe'),
(67, 'Can delete employe', 17, 'delete_employe'),
(68, 'Can view employe', 17, 'view_employe'),
(69, 'Can add annee', 18, 'add_annee'),
(70, 'Can change annee', 18, 'change_annee'),
(71, 'Can delete annee', 18, 'delete_annee'),
(72, 'Can view annee', 18, 'view_annee'),
(73, 'Can add mois', 19, 'add_mois'),
(74, 'Can change mois', 19, 'change_mois'),
(75, 'Can delete mois', 19, 'delete_mois'),
(76, 'Can view mois', 19, 'view_mois'),
(77, 'Can add dossiers', 20, 'add_dossiers'),
(78, 'Can change dossiers', 20, 'change_dossiers'),
(79, 'Can delete dossiers', 20, 'delete_dossiers'),
(80, 'Can view dossiers', 20, 'view_dossiers'),
(81, 'Can add type_paiement', 21, 'add_type_paiement'),
(82, 'Can change type_paiement', 21, 'change_type_paiement'),
(83, 'Can delete type_paiement', 21, 'delete_type_paiement'),
(84, 'Can view type_paiement', 21, 'view_type_paiement'),
(85, 'Can add parametre_calcul', 22, 'add_parametre_calcul'),
(86, 'Can change parametre_calcul', 22, 'change_parametre_calcul'),
(87, 'Can delete parametre_calcul', 22, 'delete_parametre_calcul'),
(88, 'Can view parametre_calcul', 22, 'view_parametre_calcul'),
(89, 'Can add tranche_charge', 23, 'add_tranche_charge'),
(90, 'Can change tranche_charge', 23, 'change_tranche_charge'),
(91, 'Can delete tranche_charge', 23, 'delete_tranche_charge'),
(92, 'Can view tranche_charge', 23, 'view_tranche_charge'),
(93, 'Can add tranche_revenu', 24, 'add_tranche_revenu'),
(94, 'Can change tranche_revenu', 24, 'change_tranche_revenu'),
(95, 'Can delete tranche_revenu', 24, 'delete_tranche_revenu'),
(96, 'Can view tranche_revenu', 24, 'view_tranche_revenu'),
(97, 'Can add constante_calcule', 25, 'add_constante_calcule'),
(98, 'Can change constante_calcule', 25, 'change_constante_calcule'),
(99, 'Can delete constante_calcule', 25, 'delete_constante_calcule'),
(100, 'Can view constante_calcule', 25, 'view_constante_calcule'),
(101, 'Can add parametre_ifc', 26, 'add_parametre_ifc'),
(102, 'Can change parametre_ifc', 26, 'change_parametre_ifc'),
(103, 'Can delete parametre_ifc', 26, 'delete_parametre_ifc'),
(104, 'Can view parametre_ifc', 26, 'view_parametre_ifc'),
(105, 'Can add elementsalaire', 27, 'add_elementsalaire'),
(106, 'Can change elementsalaire', 27, 'change_elementsalaire'),
(107, 'Can delete elementsalaire', 27, 'delete_elementsalaire'),
(108, 'Can view elementsalaire', 27, 'view_elementsalaire'),
(109, 'Can add jour ferier', 28, 'add_jourferier'),
(110, 'Can change jour ferier', 28, 'change_jourferier'),
(111, 'Can delete jour ferier', 28, 'delete_jourferier'),
(112, 'Can view jour ferier', 28, 'view_jourferier'),
(113, 'Can add nuit', 29, 'add_nuit'),
(114, 'Can change nuit', 29, 'change_nuit'),
(115, 'Can delete nuit', 29, 'delete_nuit'),
(116, 'Can view nuit', 29, 'view_nuit'),
(117, 'Can add tarif heure sup', 30, 'add_tarifheuresup'),
(118, 'Can change tarif heure sup', 30, 'change_tarifheuresup'),
(119, 'Can delete tarif heure sup', 30, 'delete_tarifheuresup'),
(120, 'Can view tarif heure sup', 30, 'view_tarifheuresup'),
(121, 'Can add taxe', 31, 'add_taxe'),
(122, 'Can change taxe', 31, 'change_taxe'),
(123, 'Can delete taxe', 31, 'delete_taxe'),
(124, 'Can view taxe', 31, 'view_taxe'),
(125, 'Can add contrat_doc', 32, 'add_contrat_doc'),
(126, 'Can change contrat_doc', 32, 'change_contrat_doc'),
(127, 'Can delete contrat_doc', 32, 'delete_contrat_doc'),
(128, 'Can view contrat_doc', 32, 'view_contrat_doc'),
(129, 'Can add contrat doc', 32, 'add_contratdoc'),
(130, 'Can change contrat doc', 32, 'change_contratdoc'),
(131, 'Can delete contrat doc', 32, 'delete_contratdoc'),
(132, 'Can view contrat doc', 32, 'view_contratdoc');

-- --------------------------------------------------------

--
-- Structure de la table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Déchargement des données de la table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$390000$xR3XyfscNJM4Xo6vlMWUqu$QGFuivRBET9cT8M17V6zzdDxJHnZaJJ9uAVcgr5BCxU=', '2024-04-01 17:09:46.089655', 0, 'Jessica', 'jessica', '', 'jessicanikiema31@gmail.com', 0, 1, '2024-04-01 14:29:34.285833'),
(2, 'pbkdf2_sha256$390000$0YkyEeXVcJfqip8mxmOltr$yjRY8y1yBoWb0nD97CrupprmiD/U3eRgwnqfLXAReqQ=', '2024-04-01 14:31:15.954727', 0, 'milfay', 'milfay', '', 'milfay19@gmail.com', 0, 0, '2024-04-01 14:31:15.677661'),
(3, 'pbkdf2_sha256$390000$C4naypfnAWx98XM4CoBrPl$p7WWamWJLUbfd31RVf8eoxqvNKT6i8cLbapJ1zUo+ek=', '2024-04-01 14:33:23.413954', 0, 'mil', 'mil', '', 'milfay19@gmail.com', 0, 0, '2024-04-01 14:33:23.237531'),
(4, 'pbkdf2_sha256$390000$IFd7okTj1neKuoFrW77yNX$kbkJvrjKJ9tDcNg7V11vnPk8b7eI14mSomJm2BwWBBk=', '2024-04-01 17:02:02.038905', 1, 'admin', '', '', 'admin@admin.com', 1, 1, '2024-04-01 14:46:47.463444'),
(5, 'pbkdf2_sha256$390000$Y7PcIZ5UXHu4aqN11zIrJh$LYTa0TC4utCr2QV9q5+E1KZl1YyKK119TNzedtvMjWo=', '2024-04-01 17:07:46.417578', 0, 'millogov', 'MILLOGOV', '', 'milfay19@gmail.com', 0, 0, '2024-04-01 17:07:46.262458');

-- --------------------------------------------------------

--
-- Structure de la table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Déchargement des données de la table `auth_user_groups`
--

INSERT INTO `auth_user_groups` (`id`, `user_id`, `group_id`) VALUES
(1, 1, 1);

-- --------------------------------------------------------

--
-- Structure de la table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Structure de la table `calcul_constante_calcule`
--

CREATE TABLE `calcul_constante_calcule` (
  `id` bigint(20) NOT NULL,
  `diviseur_ifc` double NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Déchargement des données de la table `calcul_constante_calcule`
--

INSERT INTO `calcul_constante_calcule` (`id`, `diviseur_ifc`) VALUES
(1, 36000);

-- --------------------------------------------------------

--
-- Structure de la table `calcul_parametre_calcul`
--

CREATE TABLE `calcul_parametre_calcul` (
  `id` bigint(20) NOT NULL,
  `p_taux_horaire` double DEFAULT NULL,
  `min_prime_aciennete` double DEFAULT NULL,
  `taux_cnss` double DEFAULT NULL,
  `taux_prime_aciennete` double DEFAULT NULL,
  `taux_augmentation_prime` double DEFAULT NULL,
  `p_prime_quart` double DEFAULT NULL,
  `p_prime_panier` double DEFAULT NULL,
  `controle_cnss_taux_sal_brute` double DEFAULT NULL,
  `controle_cnss_taux_sal_base` double DEFAULT NULL,
  `controle_plafond_logement` double DEFAULT NULL,
  `controle_plafond_transport` double DEFAULT NULL,
  `controle_plafond_fonction` double DEFAULT NULL,
  `max_controle_plafond_logement` double DEFAULT NULL,
  `max_controle_plafond_transport` double DEFAULT NULL,
  `max_controle_plafond_fonction` double DEFAULT NULL,
  `taux_abatement_iuts_cadre` double DEFAULT NULL,
  `taux_abatement_iuts_non_cadre` double DEFAULT NULL,
  `taux_cnss_patronale` double DEFAULT NULL,
  `tpa` double DEFAULT NULL,
  `controle_plafond_panier` double DEFAULT NULL,
  `controle_plafond_risque` double DEFAULT NULL,
  `max_controle_plafond_panier` double DEFAULT NULL,
  `max_controle_plafond_risque` double DEFAULT NULL,
  `taux_effort_paix` double DEFAULT NULL,
  `nb_jour_travail_normal` int(11) DEFAULT NULL,
  `p_prime_quart_sftp` double DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Déchargement des données de la table `calcul_parametre_calcul`
--

INSERT INTO `calcul_parametre_calcul` (`id`, `p_taux_horaire`, `min_prime_aciennete`, `taux_cnss`, `taux_prime_aciennete`, `taux_augmentation_prime`, `p_prime_quart`, `p_prime_panier`, `controle_cnss_taux_sal_brute`, `controle_cnss_taux_sal_base`, `controle_plafond_logement`, `controle_plafond_transport`, `controle_plafond_fonction`, `max_controle_plafond_logement`, `max_controle_plafond_transport`, `max_controle_plafond_fonction`, `taux_abatement_iuts_cadre`, `taux_abatement_iuts_non_cadre`, `taux_cnss_patronale`, `tpa`, `controle_plafond_panier`, `controle_plafond_risque`, `max_controle_plafond_panier`, `max_controle_plafond_risque`, `taux_effort_paix`, `nb_jour_travail_normal`, `p_prime_quart_sftp`) VALUES
(1, 173.33, 3, 0.055, 0.05, 0.01, 12, 3, 0.055, 0.08, 0.2, 0.05, 0.05, 75000, 30000, 50000, 0.2, 0.25, 0.16, 0.03, 0.05, 0.05, 30000, 30000, 0.01, 30, 0.05);

-- --------------------------------------------------------

--
-- Structure de la table `calcul_parametre_ifc`
--

CREATE TABLE `calcul_parametre_ifc` (
  `id` bigint(20) NOT NULL,
  `taux` double NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Déchargement des données de la table `calcul_parametre_ifc`
--

INSERT INTO `calcul_parametre_ifc` (`id`, `taux`) VALUES
(1, 25);

-- --------------------------------------------------------

--
-- Structure de la table `calcul_tranche_charge`
--

CREATE TABLE `calcul_tranche_charge` (
  `id` bigint(20) NOT NULL,
  `nombre` double DEFAULT NULL,
  `taux` double DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Déchargement des données de la table `calcul_tranche_charge`
--

INSERT INTO `calcul_tranche_charge` (`id`, `nombre`, `taux`) VALUES
(1, 1, 0.08),
(2, 2, 0.1),
(3, 3, 0.12),
(4, 0, 0);

-- --------------------------------------------------------

--
-- Structure de la table `calcul_tranche_revenu`
--

CREATE TABLE `calcul_tranche_revenu` (
  `id` bigint(20) NOT NULL,
  `min` double DEFAULT NULL,
  `max` double DEFAULT NULL,
  `taux` double DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Déchargement des données de la table `calcul_tranche_revenu`
--

INSERT INTO `calcul_tranche_revenu` (`id`, `min`, `max`, `taux`) VALUES
(1, 0, 30000, 0),
(2, 30000, 50000, 0.121),
(3, 50000, 80000, 0.139),
(4, 80000, 120000, 0.157),
(5, 120000, 170000, 0.184),
(6, 170000, 250000, 0.217),
(7, 250000, 0, 0.25);

-- --------------------------------------------------------

--
-- Structure de la table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `object_repr` varchar(200) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Déchargement des données de la table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'employe', 'categorie'),
(8, 'employe', 'contrat'),
(9, 'employe', 'diplome'),
(10, 'employe', 'modecalcule'),
(11, 'employe', 'paiement'),
(12, 'employe', 'situationmatrimoniale'),
(13, 'employe', 'specialite'),
(14, 'employe', 'structure'),
(15, 'employe', 'typecontrat'),
(16, 'employe', 'pointage'),
(17, 'employe', 'employe'),
(18, 'employe', 'annee'),
(19, 'employe', 'mois'),
(20, 'employe', 'dossiers'),
(21, 'employe', 'type_paiement'),
(22, 'calcul', 'parametre_calcul'),
(23, 'calcul', 'tranche_charge'),
(24, 'calcul', 'tranche_revenu'),
(25, 'calcul', 'constante_calcule'),
(26, 'calcul', 'parametre_ifc'),
(27, 'elementSal', 'elementsalaire'),
(28, 'parametre', 'jourferier'),
(29, 'parametre', 'nuit'),
(30, 'parametre', 'tarifheuresup'),
(31, 'parametre', 'taxe'),
(32, 'employe', 'contratdoc');

-- --------------------------------------------------------

--
-- Structure de la table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Déchargement des données de la table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-02-20 20:50:33.381991'),
(2, 'auth', '0001_initial', '2024-02-20 20:50:39.184735'),
(3, 'admin', '0001_initial', '2024-02-20 20:50:40.457642'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-02-20 20:50:40.488875'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-02-20 20:50:40.504498'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-02-20 20:50:41.090795'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-02-20 20:50:41.360526'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-02-20 20:50:41.824292'),
(9, 'auth', '0004_alter_user_username_opts', '2024-02-20 20:50:41.940181'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-02-20 20:50:42.209870'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-02-20 20:50:42.225497'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-02-20 20:50:42.263280'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-02-20 20:50:42.463852'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-02-20 20:50:42.880695'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-02-20 20:50:43.112605'),
(16, 'auth', '0011_update_proxy_permissions', '2024-02-20 20:50:43.128230'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-02-20 20:50:43.397899'),
(18, 'calcul', '0001_initial', '2024-02-20 20:50:43.582975'),
(19, 'calcul', '0002_parametre_calcul_taux_cnss_patronale', '2024-02-20 20:50:43.999915'),
(20, 'calcul', '0003_parametre_calcul_tpa', '2024-02-20 20:50:44.200518'),
(21, 'calcul', '0004_tranche_charge_tranche_revenu', '2024-02-20 20:50:44.485889'),
(22, 'calcul', '0005_parametre_calcul_controle_plafond_panier_and_more', '2024-02-20 20:50:45.874889'),
(23, 'calcul', '0006_parametre_calcul_taux_effort_paix', '2024-02-20 20:50:46.122377'),
(24, 'calcul', '0007_constante_calcule_parametre_ifc', '2024-02-20 20:50:46.423293'),
(25, 'elementSal', '0001_initial', '2024-02-20 20:50:46.561405'),
(26, 'employe', '0001_initial', '2024-02-20 20:50:54.131697'),
(27, 'employe', '0002_contrat_indemnite_risque', '2024-02-20 20:50:54.617140'),
(28, 'employe', '0003_rename_prime_nourritur_contrat_prime_nourriture_and_more', '2024-02-20 20:50:54.933728'),
(29, 'employe', '0004_paiement_tpa', '2024-02-20 20:50:55.203467'),
(30, 'employe', '0005_alter_employe_nombre_enfant', '2024-02-20 20:50:55.234688'),
(31, 'employe', '0006_annee_mois_remove_paiement_periode_paiement_annee_and_more', '2024-02-20 20:50:57.209600'),
(32, 'employe', '0007_alter_paiement_annee_alter_paiement_mois', '2024-02-20 20:50:58.128051'),
(33, 'employe', '0008_alter_structure_telephone', '2024-02-20 20:50:58.359894'),
(34, 'employe', '0009_remove_employe_cv_remove_employe_diplome_and_more', '2024-02-20 20:51:00.234811'),
(35, 'employe', '0010_contrat_prime_astreinte', '2024-02-20 20:51:00.821211'),
(36, 'employe', '0011_paiement_effort_paix', '2024-02-20 20:51:01.137763'),
(37, 'employe', '0012_paiement_indemnite_fonction_and_more', '2024-02-20 20:51:03.792922'),
(38, 'employe', '0013_type_paiement_paiement_type_paiement', '2024-02-20 20:51:04.733651'),
(39, 'employe', '0014_employe_nom_mere_employe_nom_pere_and_more', '2024-02-20 20:51:07.373243'),
(40, 'employe', '0015_employe_numero_cnib_employe_profession', '2024-02-20 20:51:08.291708'),
(41, 'parametre', '0001_initial', '2024-02-20 20:51:08.862433'),
(42, 'sessions', '0001_initial', '2024-02-20 20:51:09.279351'),
(43, 'employe', '0016_contrat_doc', '2024-02-29 07:51:39.922357'),
(44, 'employe', '0017_rename_contrat_doc_contratdoc', '2024-02-29 08:09:33.478696'),
(45, 'employe', '0018_contrat_contrat_doc_alter_contratdoc_id', '2024-03-09 10:05:43.389913'),
(46, 'employe', '0014_alter_employe_categorie_and_more', '2024-03-11 15:05:02.366946'),
(47, 'employe', '0015_alter_employe_situation_matrimoniale', '2024-03-11 15:05:02.524748'),
(48, 'employe', '0016_alter_structure_description_structure_and_more', '2024-03-11 15:05:02.556437'),
(49, 'employe', '0017_contratdoc_employe_nom_mere_employe_nom_pere_and_more', '2024-03-11 15:09:18.741380'),
(50, 'employe', '0018_type_paiement_code', '2024-03-12 12:52:48.885523'),
(51, 'employe', '0019_remove_contrat_contrat_doc_and_more', '2024-03-22 15:05:51.226086'),
(52, 'employe', '0020_alter_contrat_prime_lait', '2024-03-25 12:21:16.834450'),
(53, 'employe', '0021_alter_contrat_indemnite_fonction_and_more', '2024-03-25 12:23:03.680181'),
(54, 'employe', '0022_contrat_poste', '2024-03-25 12:28:12.700752'),
(55, 'employe', '0023_contrat_augementation_special_pourcentage_and_more', '2024-03-26 16:05:26.896455'),
(56, 'employe', '0024_alter_contrat_augementation_special_pourcentage_and_more', '2024-03-27 13:12:01.733540'),
(57, 'employe', '0025_paiement_augementation_special_pourcentage_and_more', '2024-03-29 08:24:56.746797'),
(58, 'calcul', '0008_parametre_calcul_nb_jour_travail_normal', '2024-03-29 12:01:39.200622'),
(59, 'employe', '0026_pointage_nb_jour_travail_normal', '2024-03-29 13:51:11.771305'),
(60, 'calcul', '0009_alter_parametre_calcul_nb_jour_travail_normal', '2024-03-29 14:10:45.990347'),
(61, 'calcul', '0010_parametre_calcul_p_prime_quart_sftp', '2024-03-29 16:58:37.569764');

-- --------------------------------------------------------

--
-- Structure de la table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Déchargement des données de la table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('zqdhzufz54mh2kcgr7zafh0tape08c2j', 'e30:1rrIfG:l9hWDCYc0rzd5iqLD-tg1k2-K2DowTdbIIEFqatzoIQ', '2024-04-15 14:29:34.528631'),
('mo21d24jglhx9hz0hmhp5a8jwt0y19nb', 'e30:1rrIgt:B_ahIMQhBjW9tnkCBDQJaMdpKTtjCpI8Vd4CIYtSptI', '2024-04-15 14:31:15.954727'),
('vri9yvq6lwvtm7xwksjbeiko3v48dthp', 'e30:1rrIix:7mNmNrtNq7SmSOSTO66g_IXOlN_VSNM-yQVCNmwf1GI', '2024-04-15 14:33:23.412953'),
('19rrak8u8r5trn5zywxy5u79fr1dydjg', '.eJxVjDsOwjAQRO_iGln-x6akzxmsXduLA8iR4qRC3J1ESgHlzHszbxZhW2vcelnilNmVWXb57RDSs7QD5Ae0-8zT3NZlQn4o_KSdj3Mur9vp_h1U6HVf-2ScBB80CZAIeUAj9VCcl9YKS8I7QiGUC47CHgySU0oXncEnGSixzxfJsjdK:1rrL8M:wjq7037HB9MbK2zls0KE4ocKyFvhNahVuukDrDtFC4A', '2024-04-15 17:07:46.433585'),
('e10jqbi5m8fyv1v6znrxoybihphgpxdm', '.eJxVjMsOwiAQRf-FtSE8B3Dp3m8gAwxSNTQp7cr479qkC93ec859sYjb2uI2aIlTYWcm2el3S5gf1HdQ7thvM89zX5cp8V3hBx38Ohd6Xg7376DhaN9aQEFnlE4OFDpvLILVUlbyutYqgpcuoCCnKEGuWZAWKIMFabQByIW9P8jzN0I:1rrLAI:Qtbt3Ryui_2EwUdDMF20mb0RvGtU0dBNh80vPj3nm5I', '2024-04-15 17:09:46.089655');

-- --------------------------------------------------------

--
-- Structure de la table `elementsal`
--

CREATE TABLE `elementsal` (
  `id` bigint(20) NOT NULL,
  `intitule_element` varchar(20) NOT NULL,
  `description` varchar(255) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Déchargement des données de la table `elementsal`
--

INSERT INTO `elementsal` (`id`, `intitule_element`, `description`) VALUES
(1, 'Indemnité de risque', 'jhjbb');

-- --------------------------------------------------------

--
-- Structure de la table `employe_annee`
--

CREATE TABLE `employe_annee` (
  `id` bigint(20) NOT NULL,
  `exercice` varchar(10) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Déchargement des données de la table `employe_annee`
--

INSERT INTO `employe_annee` (`id`, `exercice`) VALUES
(1, '2024');

-- --------------------------------------------------------

--
-- Structure de la table `employe_categorie`
--

CREATE TABLE `employe_categorie` (
  `id` bigint(20) NOT NULL,
  `categorie` varchar(50) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Déchargement des données de la table `employe_categorie`
--

INSERT INTO `employe_categorie` (`id`, `categorie`) VALUES
(1, 'Technicien'),
(2, 'Ingénieur'),
(3, 'Ingenieur de travaux'),
(4, 'tecnicien');

-- --------------------------------------------------------

--
-- Structure de la table `employe_contrat`
--

CREATE TABLE `employe_contrat` (
  `id` bigint(20) NOT NULL,
  `description_poste` longtext NOT NULL,
  `description_profil` longtext NOT NULL,
  `lieu_affectation` varchar(255) NOT NULL,
  `cadre` tinyint(1) NOT NULL,
  `date_debut` date NOT NULL,
  `date_fin` date NOT NULL,
  `salaire_base` double NOT NULL,
  `indemnite_logement` double DEFAULT NULL,
  `indemnite_transport` double DEFAULT NULL,
  `indemnite_fonction` double DEFAULT NULL,
  `prime_nourriture` double DEFAULT NULL,
  `prime_lait` double DEFAULT NULL,
  `prime_salissure` double DEFAULT NULL,
  `nombre_annee_travail` int(11) DEFAULT NULL,
  `prime_anciennete` tinyint(1) DEFAULT NULL,
  `prime_quart` tinyint(1) NOT NULL,
  `prime_panier` tinyint(1) NOT NULL,
  `diplome_requis_id` bigint(20) NOT NULL,
  `employe_id` bigint(20) NOT NULL,
  `mode_calcul_id` bigint(20) NOT NULL,
  `structure_id` bigint(20) NOT NULL,
  `type_contrat_id` bigint(20) NOT NULL,
  `indemnite_risque` double DEFAULT NULL,
  `prime_astreinte` double DEFAULT NULL,
  `poste` varchar(255) DEFAULT NULL,
  `augementation_special_pourcentage` double NOT NULL,
  `augmentation_octobre_2019` double NOT NULL,
  `sursalaire` double NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Déchargement des données de la table `employe_contrat`
--

INSERT INTO `employe_contrat` (`id`, `description_poste`, `description_profil`, `lieu_affectation`, `cadre`, `date_debut`, `date_fin`, `salaire_base`, `indemnite_logement`, `indemnite_transport`, `indemnite_fonction`, `prime_nourriture`, `prime_lait`, `prime_salissure`, `nombre_annee_travail`, `prime_anciennete`, `prime_quart`, `prime_panier`, `diplome_requis_id`, `employe_id`, `mode_calcul_id`, `structure_id`, `type_contrat_id`, `indemnite_risque`, `prime_astreinte`, `poste`, `augementation_special_pourcentage`, `augmentation_octobre_2019`, `sursalaire`) VALUES
(8, 'Assurer le suivi et la maintenance du matériel informatique\r\n    Tenir à jour la fiche de gestion du matériel informatique\r\n    Assurer une maintenance préventive de premier niveau (dépoussiérage)\r\n    Tenir un cahier d’entretien préventif et curatif de chaque ordinateur, chaque imprimante et chaque scanner\r\n    Suivre les réaffectations du matériel\r\n    Produire un reporting mensuel sur l’état de santé du matériel informatique\r\n    Maintenir la performance des ordinateurs\r\n    Réaliser au moins une fois par semaine des relevés de temps sur la performance des ordinateurs et mettre en place des mesures correctives en cas d’écart\r\n    Réaliser un inventaire physique du matériel informatique au moins une fois par an. Justifier les écarts par rapport à l’inventaire précédent\r\n    Suivre les sauvegardes\r\n    Assurer un contrôle journalier du système de sauvegarde mis en place\r\n    Diagnostiquer, corriger et relancer systématiquement les sauvegardes en échecs\r\n    Produire un rapport hebdomadaire et mensuel des sauvegardes\r\n    Suivre les applications de sécurité\r\n    S’assurer que les points sentinelle installés sur les postes de travail sont à jour et opérationnels\r\n    Suivre le système de vidéosurveillance\r\n    En relation avec les opérateurs de la vidéosurveillance, s’assurer que toutes les caméras sont opérationnelles\r\n    Suivre le système de vidéoconférence\r\n    Assister les utilisateurs du système de vidéoconférence\r\n    Assurer le maintien à jour de l’application système Yealink en collaboration avec le prestataire\r\n    Produire des rapports\r\n    Produire en fin de mois un reporting complet des tâches réalisées sur la période écoulée depuis le précèdent reporting\r\n    Assurer le support utilisateurs\r\n    Faire enregistrer ou enregistrer dans l’outil intranet « kit » la demande d’assistance de l’utilisateur\r\n    Traiter ensuite la demande d’assistance de l’utilisateur dans les meilleurs délais\r\n    Faire clôturer ou clôturer la demande d’assistance une fois l’utilisateur satisfait\r\n    Extraire sur kit des temps de connexion\r\n    Extraire sur kit les temps de connexion hebdomadaire et les transmettre par mail au groupe Kit\r\n    Assurer une maintenance de premier niveau du réseau informatique\r\n    Effectuer un dépoussiérage des armoires informatiques autres que celles du datacenter\r\n    Établir un diagnostic des prises RJ45 défectueuses par des tests de continuité du câble entre la prise et le switch\r\n    Établir ou mettre à jour les modes opératoires des tâches informatiques\r\n    Établir ou mettre à jour les modes opératoires\r\n    Configurer des téléphones IP\r\n    Configurer les téléphones IP pour les utilisateurs\r\n    Former les utilisateurs\r\n    Former les utilisateurs sur les outils et les applications informatiques selon les besoins exprimés.', 'Bac+2 / Bac+3 en Maintenance informatique et support\r\nExpérience antérieure minimale de 03 ans\r\nAvoir des connaissances approfondies en systèmes informatiques Windows dont les systèmes serveurs minimum à partir de la version Windows serveur 2012 R2 et plus\r\nMaitriser l’anglais technique.', 'Ouagadougou', 0, '2024-03-19', '2025-06-19', 217119, 30000, 0, 0, 0, 7500, 5000, 0, 0, 1, 1, 2, 21, 1, 4, 1, 10000, 0, 'Informaticien', 25000, 10000, 15000),
(9, 'AGENT', 'AGENT', 'HOUNDE', 1, '2018-06-01', '2023-01-02', 260000, 30000, 0, 0, 20000, 10000, 0, 5, 1, 1, 1, 1, 26, 3, 6, 2, 10000, 0, 'AGENT DE MENAGE', 12000, 15000, 103000);

-- --------------------------------------------------------

--
-- Structure de la table `employe_diplome`
--

CREATE TABLE `employe_diplome` (
  `id` bigint(20) NOT NULL,
  `diplome` varchar(50) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Déchargement des données de la table `employe_diplome`
--

INSERT INTO `employe_diplome` (`id`, `diplome`) VALUES
(1, 'Licence'),
(2, 'Master'),
(3, 'Bac');

-- --------------------------------------------------------

--
-- Structure de la table `employe_dossiers`
--

CREATE TABLE `employe_dossiers` (
  `id` bigint(20) NOT NULL,
  `libelle` varchar(50) NOT NULL,
  `file` varchar(100) DEFAULT NULL,
  `employe_id` bigint(20) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Structure de la table `employe_employe`
--

CREATE TABLE `employe_employe` (
  `id` bigint(20) NOT NULL,
  `nom` varchar(255) NOT NULL,
  `prenoms` varchar(255) NOT NULL,
  `lieu_naissance` varchar(255) NOT NULL,
  `date_naissance` date NOT NULL,
  `sexe` varchar(10) NOT NULL,
  `nombre_enfant` int(11) NOT NULL,
  `telephone` varchar(128) NOT NULL,
  `email` varchar(254) NOT NULL,
  `adresse` varchar(255) NOT NULL,
  `option` varchar(255) DEFAULT NULL,
  `numero_cnss` varchar(20) DEFAULT NULL,
  `numero_matricule` varchar(20) DEFAULT NULL,
  `categorie_id` bigint(20) DEFAULT NULL,
  `dernier_diplome_id` bigint(20) DEFAULT NULL,
  `situation_matrimoniale_id` bigint(20) DEFAULT NULL,
  `specialite_id` bigint(20) DEFAULT NULL,
  `nom_mere` varchar(255) DEFAULT NULL,
  `nom_pere` varchar(255) DEFAULT NULL,
  `numero_cnib` varchar(10) DEFAULT NULL,
  `personne_prevenir` varchar(255) DEFAULT NULL,
  `photo_cnib` varchar(100) DEFAULT NULL,
  `photo_identite` varchar(100) DEFAULT NULL,
  `profession` varchar(255) DEFAULT NULL,
  `sous_couvert` varchar(255) DEFAULT NULL,
  `telephone_prevenir` varchar(128) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Déchargement des données de la table `employe_employe`
--

INSERT INTO `employe_employe` (`id`, `nom`, `prenoms`, `lieu_naissance`, `date_naissance`, `sexe`, `nombre_enfant`, `telephone`, `email`, `adresse`, `option`, `numero_cnss`, `numero_matricule`, `categorie_id`, `dernier_diplome_id`, `situation_matrimoniale_id`, `specialite_id`, `nom_mere`, `nom_pere`, `numero_cnib`, `personne_prevenir`, `photo_cnib`, `photo_identite`, `profession`, `sous_couvert`, `telephone_prevenir`) VALUES
(27, 'YAMEOGO', 'HENRIETTE CARINE', '', '2000-01-11', 'F', 0, '', '', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', '', NULL, NULL, NULL),
(26, 'OUATTARA', 'DJENEBA', 'BOBO DIOULASSO', '1998-10-10', 'F', 2, '+22676767575', 'OUATTARA@gmail.com', 'OUAGADOUGOU', 'GESTION', '132456987421G', '', 1, 1, 2, 1, 'SANOU ADJARA', 'OUATTARA ALI', 'B7206542', 'OUATTARA ALI', '', '', 'AGENT DE MENAGE', '', '+22677787778'),
(21, 'Ouattara', 'Ezedine', 'Bobo', '1989-03-07', 'M', 3, '+22676848355', 'pharminter@gmail.com', '01BP3931 OUAGA', 'Securité', '002030', '903020', 2, 2, 2, 3, 'Traore Bintou', 'Ouattara Aziz', '', 'Ouattara Issouf', '', '', '', '', '+22670605000');

-- --------------------------------------------------------

--
-- Structure de la table `employe_modecalcule`
--

CREATE TABLE `employe_modecalcule` (
  `id` bigint(20) NOT NULL,
  `mode_calcul` varchar(50) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Déchargement des données de la table `employe_modecalcule`
--

INSERT INTO `employe_modecalcule` (`id`, `mode_calcul`) VALUES
(1, 'RESSOURCES HUMAINES'),
(2, 'KARMA'),
(3, 'SFTP');

-- --------------------------------------------------------

--
-- Structure de la table `employe_mois`
--

CREATE TABLE `employe_mois` (
  `id` bigint(20) NOT NULL,
  `libelle` varchar(20) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Déchargement des données de la table `employe_mois`
--

INSERT INTO `employe_mois` (`id`, `libelle`) VALUES
(1, 'Janvier'),
(2, 'Février'),
(3, 'Mars'),
(4, 'Avril'),
(5, 'Mai'),
(6, 'Juin'),
(7, 'Juillet'),
(8, 'Août'),
(9, 'Septembre'),
(10, 'Octobre'),
(11, 'Novembre'),
(12, 'Décembre');

-- --------------------------------------------------------

--
-- Structure de la table `employe_paiement`
--

CREATE TABLE `employe_paiement` (
  `id` bigint(20) NOT NULL,
  `salaire_net` double DEFAULT NULL,
  `salaire_brut` double DEFAULT NULL,
  `salaire_base` double DEFAULT NULL,
  `cotitsation_cnss` double DEFAULT NULL,
  `cnss_patronal` double DEFAULT NULL,
  `iuts` double DEFAULT NULL,
  `surplus_salaire` double DEFAULT NULL,
  `relicat_salaire` double DEFAULT NULL,
  `payer` tinyint(1) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `updated_at` datetime(6) NOT NULL,
  `contrat_id` bigint(20) DEFAULT NULL,
  `tpa` double DEFAULT NULL,
  `annee_id` bigint(20) DEFAULT NULL,
  `mois_id` bigint(20) DEFAULT NULL,
  `effort_paix` double DEFAULT NULL,
  `indemnite_fonction` double DEFAULT NULL,
  `indemnite_logement` double DEFAULT NULL,
  `indemnite_risque` double DEFAULT NULL,
  `indemnite_transport` double DEFAULT NULL,
  `prime_ancien` double DEFAULT NULL,
  `prime_lait` double DEFAULT NULL,
  `prime_nourriture` double DEFAULT NULL,
  `prime_panier` double DEFAULT NULL,
  `prime_quart` double DEFAULT NULL,
  `type_paiement_id` bigint(20) DEFAULT NULL,
  `augementation_special_pourcentage` double NOT NULL,
  `augmentation_octobre_2019` double NOT NULL,
  `sursalaire` double NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Déchargement des données de la table `employe_paiement`
--

INSERT INTO `employe_paiement` (`id`, `salaire_net`, `salaire_brut`, `salaire_base`, `cotitsation_cnss`, `cnss_patronal`, `iuts`, `surplus_salaire`, `relicat_salaire`, `payer`, `created_at`, `updated_at`, `contrat_id`, `tpa`, `annee_id`, `mois_id`, `effort_paix`, `indemnite_fonction`, `indemnite_logement`, `indemnite_risque`, `indemnite_transport`, `prime_ancien`, `prime_lait`, `prime_nourriture`, `prime_panier`, `prime_quart`, `type_paiement_id`, `augementation_special_pourcentage`, `augmentation_octobre_2019`, `sursalaire`) VALUES
(25, 436175, 548827, 217119, 30185, 87812, 78060, 0, 0, 1, NULL, '2024-03-29 08:33:15.368514', 8, 16465, 1, 1, 4405.81, 0, 30000, 10000, 0, 0, 7500, 0, 0, 0, 1, 25000, 10000, 15000),
(26, 347528, 425321, 217119, 23393, 68051, 50890, 0, 0, 0, NULL, '2024-03-29 13:38:07.222022', 8, 12760, 1, 2, 3510.38, 0, 30000, 10000, 0, 0, 7500, 0, 0, 0, 1, 25000, 10000, 15000),
(27, 111435, 124873, 72373, 6868, 19980, 5444, 0, 0, 0, NULL, '2024-03-29 14:13:21.280586', 8, 3746, 1, 3, 1125.6100000000001, 0, 30000, 10000, 0, 0, 7500, 0, 0, 0, 1, 25000, 10000, 15000),
(28, 622316, 812073, 260000, 44664, 129932, 138807, 0, 0, 0, NULL, '2024-03-29 18:19:53.260186', 9, 24362, 1, 3, 6286.02, 0, 30000, 10000, 0, 18200, 10000, 20000, 16554, 72320, 1, 12000, 15000, 103000);

-- --------------------------------------------------------

--
-- Structure de la table `employe_pointage`
--

CREATE TABLE `employe_pointage` (
  `id` bigint(20) NOT NULL,
  `nb_h_normal` int(11) DEFAULT NULL,
  `nb_h_15` int(11) DEFAULT NULL,
  `nb_h_35` int(11) DEFAULT NULL,
  `nb_h_50` int(11) DEFAULT NULL,
  `nb_h_60` int(11) DEFAULT NULL,
  `nb_h_120` int(11) DEFAULT NULL,
  `nb_quart` int(11) DEFAULT NULL,
  `nb_jour` int(11) DEFAULT NULL,
  `paiement_id` bigint(20) DEFAULT NULL,
  `nb_jour_travail_normal` int(11) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Déchargement des données de la table `employe_pointage`
--

INSERT INTO `employe_pointage` (`id`, `nb_h_normal`, `nb_h_15`, `nb_h_35`, `nb_h_50`, `nb_h_60`, `nb_h_120`, `nb_quart`, `nb_jour`, `paiement_id`, `nb_jour_travail_normal`) VALUES
(25, 150, 16, 34, 40, 0, 0, 2, 20, 26, NULL),
(24, 150, 16, 34, 40, 0, 0, 2, 20, 25, NULL),
(26, 0, 0, 0, 0, 0, 0, 0, 0, 27, 10),
(27, 152, 12, 20, 32, 0, 0, 2, 18, 28, 30);

-- --------------------------------------------------------

--
-- Structure de la table `employe_situationmatrimoniale`
--

CREATE TABLE `employe_situationmatrimoniale` (
  `id` bigint(20) NOT NULL,
  `situation_matrimoniale` varchar(50) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Déchargement des données de la table `employe_situationmatrimoniale`
--

INSERT INTO `employe_situationmatrimoniale` (`id`, `situation_matrimoniale`) VALUES
(1, 'Marié'),
(2, 'Célibataire'),
(3, 'Veuf');

-- --------------------------------------------------------

--
-- Structure de la table `employe_specialite`
--

CREATE TABLE `employe_specialite` (
  `id` bigint(20) NOT NULL,
  `specialite` varchar(50) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Déchargement des données de la table `employe_specialite`
--

INSERT INTO `employe_specialite` (`id`, `specialite`) VALUES
(1, 'Gestion Commerciale'),
(2, 'Chimie'),
(3, 'Informatique');

-- --------------------------------------------------------

--
-- Structure de la table `employe_structure`
--

CREATE TABLE `employe_structure` (
  `id` bigint(20) NOT NULL,
  `denomination` varchar(255) NOT NULL,
  `description_structure` longtext DEFAULT NULL,
  `telephone` varchar(128) DEFAULT NULL,
  `email` varchar(254) DEFAULT NULL,
  `adresse` varchar(255) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Déchargement des données de la table `employe_structure`
--

INSERT INTO `employe_structure` (`id`, `denomination`, `description_structure`, `telephone`, `email`, `adresse`) VALUES
(1, 'ESACAN', 'Exploitation minier', '+226 77889900', 'esacan@gmail.com', 'Dori'),
(2, 'Humane Project Group', 'kjhiunerkke', '+22677882233', 'humaine@gmail.com', 'Ouaga'),
(3, 'Baradji', 'fnrkjbvijkrbfkejlisoheiobgbvvrjhkposlkm,xklncocejkndcnbvgk', '+22654678909', 'baradji@gmail.com', 'Gnagna'),
(4, 'Afriklonnya', 'Production de V', '+22678907645', 'afriklonnya@gmail.com', 'Koupela'),
(5, 'Axel', NULL, NULL, NULL, ''),
(6, 'SFTP', 'SOCIETE DE FORAGE ET DE TRAVAUX PUBLICS', '+22677777777', 'sftp@gmail.com', 'OUAGADOUGOU');

-- --------------------------------------------------------

--
-- Structure de la table `employe_typecontrat`
--

CREATE TABLE `employe_typecontrat` (
  `id` bigint(20) NOT NULL,
  `file` varchar(100) DEFAULT NULL,
  `libelle` varchar(50) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Déchargement des données de la table `employe_typecontrat`
--

INSERT INTO `employe_typecontrat` (`id`, `file`, `libelle`) VALUES
(1, 'contrats/Contrat_travail_cdd.docx', 'CDD'),
(2, 'contrats/Contrat_travail_cdi.docx', 'CDI');

-- --------------------------------------------------------

--
-- Structure de la table `employe_type_paiement`
--

CREATE TABLE `employe_type_paiement` (
  `id` bigint(20) NOT NULL,
  `libelle` varchar(100) DEFAULT NULL,
  `code` varchar(10) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Déchargement des données de la table `employe_type_paiement`
--

INSERT INTO `employe_type_paiement` (`id`, `libelle`, `code`) VALUES
(1, 'SALAIRE MENSUEL', 'SALAIRE'),
(2, 'INDEMNITE DE CONGES PAYES', 'ICP'),
(3, 'INDEMNITE DE FIN DE CONTRAT', 'IFC');

-- --------------------------------------------------------

--
-- Structure de la table `jour_ferier`
--

CREATE TABLE `jour_ferier` (
  `id` bigint(20) NOT NULL,
  `libelle` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `description` longtext NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Structure de la table `nuit_table`
--

CREATE TABLE `nuit_table` (
  `id` bigint(20) NOT NULL,
  `est_nuit` tinyint(1) NOT NULL,
  `min` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Structure de la table `tarif_heure_sup`
--

CREATE TABLE `tarif_heure_sup` (
  `id` bigint(20) NOT NULL,
  `taux` decimal(5,2) NOT NULL,
  `jourFerie` tinyint(1) NOT NULL,
  `nuit` tinyint(1) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Structure de la table `taxe_table`
--

CREATE TABLE `taxe_table` (
  `id` bigint(20) NOT NULL,
  `libelle` varchar(100) NOT NULL,
  `description` longtext NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Index pour la table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  ADD KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`);

--
-- Index pour la table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  ADD KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`);

--
-- Index pour la table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Index pour la table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  ADD KEY `auth_user_groups_group_id_97559544` (`group_id`);

--
-- Index pour la table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  ADD KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`);

--
-- Index pour la table `calcul_constante_calcule`
--
ALTER TABLE `calcul_constante_calcule`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `calcul_parametre_calcul`
--
ALTER TABLE `calcul_parametre_calcul`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `calcul_parametre_ifc`
--
ALTER TABLE `calcul_parametre_ifc`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `calcul_tranche_charge`
--
ALTER TABLE `calcul_tranche_charge`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `calcul_tranche_revenu`
--
ALTER TABLE `calcul_tranche_revenu`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6` (`user_id`);

--
-- Index pour la table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Index pour la table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Index pour la table `elementsal`
--
ALTER TABLE `elementsal`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `employe_annee`
--
ALTER TABLE `employe_annee`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `employe_categorie`
--
ALTER TABLE `employe_categorie`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `categorie` (`categorie`);

--
-- Index pour la table `employe_contrat`
--
ALTER TABLE `employe_contrat`
  ADD PRIMARY KEY (`id`),
  ADD KEY `employe_contrat_diplome_requis_id_49eefda6` (`diplome_requis_id`),
  ADD KEY `employe_contrat_employe_id_3ceece55` (`employe_id`),
  ADD KEY `employe_contrat_mode_calcul_id_5c6d11c8` (`mode_calcul_id`),
  ADD KEY `employe_contrat_structure_id_6a722025` (`structure_id`),
  ADD KEY `employe_contrat_type_contrat_id_bc44215d` (`type_contrat_id`);

--
-- Index pour la table `employe_diplome`
--
ALTER TABLE `employe_diplome`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `diplome` (`diplome`);

--
-- Index pour la table `employe_dossiers`
--
ALTER TABLE `employe_dossiers`
  ADD PRIMARY KEY (`id`),
  ADD KEY `employe_dossiers_employe_id_e4d7539f` (`employe_id`);

--
-- Index pour la table `employe_employe`
--
ALTER TABLE `employe_employe`
  ADD PRIMARY KEY (`id`),
  ADD KEY `employe_employe_categorie_id_9d4cdaff` (`categorie_id`),
  ADD KEY `employe_employe_dernier_diplome_id_00928144` (`dernier_diplome_id`),
  ADD KEY `employe_employe_situation_matrimoniale_id_2a1e7d60` (`situation_matrimoniale_id`),
  ADD KEY `employe_employe_specialite_id_876c946f` (`specialite_id`);

--
-- Index pour la table `employe_modecalcule`
--
ALTER TABLE `employe_modecalcule`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `mode_calcul` (`mode_calcul`);

--
-- Index pour la table `employe_mois`
--
ALTER TABLE `employe_mois`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `employe_paiement`
--
ALTER TABLE `employe_paiement`
  ADD PRIMARY KEY (`id`),
  ADD KEY `employe_paiement_contrat_id_ee072fc6` (`contrat_id`),
  ADD KEY `employe_paiement_annee_id_6cf631d4` (`annee_id`),
  ADD KEY `employe_paiement_mois_id_eaacb740` (`mois_id`),
  ADD KEY `employe_paiement_type_paiement_id_b6b9c0f1` (`type_paiement_id`);

--
-- Index pour la table `employe_pointage`
--
ALTER TABLE `employe_pointage`
  ADD PRIMARY KEY (`id`),
  ADD KEY `employe_pointage_paiement_id_cf5f0c53` (`paiement_id`);

--
-- Index pour la table `employe_situationmatrimoniale`
--
ALTER TABLE `employe_situationmatrimoniale`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `situation_matrimoniale` (`situation_matrimoniale`);

--
-- Index pour la table `employe_specialite`
--
ALTER TABLE `employe_specialite`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `specialite` (`specialite`);

--
-- Index pour la table `employe_structure`
--
ALTER TABLE `employe_structure`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `employe_typecontrat`
--
ALTER TABLE `employe_typecontrat`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `employe_type_paiement`
--
ALTER TABLE `employe_type_paiement`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `jour_ferier`
--
ALTER TABLE `jour_ferier`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `nuit_table`
--
ALTER TABLE `nuit_table`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `tarif_heure_sup`
--
ALTER TABLE `tarif_heure_sup`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `taxe_table`
--
ALTER TABLE `taxe_table`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT pour la table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=133;

--
-- AUTO_INCREMENT pour la table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT pour la table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT pour la table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `calcul_constante_calcule`
--
ALTER TABLE `calcul_constante_calcule`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT pour la table `calcul_parametre_calcul`
--
ALTER TABLE `calcul_parametre_calcul`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT pour la table `calcul_parametre_ifc`
--
ALTER TABLE `calcul_parametre_ifc`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT pour la table `calcul_tranche_charge`
--
ALTER TABLE `calcul_tranche_charge`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8031079444060971120;

--
-- AUTO_INCREMENT pour la table `calcul_tranche_revenu`
--
ALTER TABLE `calcul_tranche_revenu`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT pour la table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT pour la table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=62;

--
-- AUTO_INCREMENT pour la table `elementsal`
--
ALTER TABLE `elementsal`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT pour la table `employe_annee`
--
ALTER TABLE `employe_annee`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT pour la table `employe_categorie`
--
ALTER TABLE `employe_categorie`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT pour la table `employe_contrat`
--
ALTER TABLE `employe_contrat`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT pour la table `employe_diplome`
--
ALTER TABLE `employe_diplome`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT pour la table `employe_dossiers`
--
ALTER TABLE `employe_dossiers`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT pour la table `employe_employe`
--
ALTER TABLE `employe_employe`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT pour la table `employe_modecalcule`
--
ALTER TABLE `employe_modecalcule`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT pour la table `employe_mois`
--
ALTER TABLE `employe_mois`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT pour la table `employe_paiement`
--
ALTER TABLE `employe_paiement`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT pour la table `employe_pointage`
--
ALTER TABLE `employe_pointage`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT pour la table `employe_situationmatrimoniale`
--
ALTER TABLE `employe_situationmatrimoniale`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT pour la table `employe_specialite`
--
ALTER TABLE `employe_specialite`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT pour la table `employe_structure`
--
ALTER TABLE `employe_structure`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT pour la table `employe_typecontrat`
--
ALTER TABLE `employe_typecontrat`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT pour la table `employe_type_paiement`
--
ALTER TABLE `employe_type_paiement`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT pour la table `jour_ferier`
--
ALTER TABLE `jour_ferier`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `nuit_table`
--
ALTER TABLE `nuit_table`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `tarif_heure_sup`
--
ALTER TABLE `tarif_heure_sup`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `taxe_table`
--
ALTER TABLE `taxe_table`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
