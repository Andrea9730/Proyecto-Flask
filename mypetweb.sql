-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 03-07-2024 a las 22:31:50
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `mypetweb`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estadoturno`
--

CREATE TABLE `estadoturno` (
  `idEstadoTurno` int(11) NOT NULL,
  `Estado` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mascotas`
--

CREATE TABLE `mascotas` (
  `idMascotas` int(11) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `raza` varchar(45) NOT NULL,
  `edad` int(11) DEFAULT NULL,
  `vacunas` varchar(45) DEFAULT NULL,
  `Usuarios_idUsuarios` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `profesionales`
--

CREATE TABLE `profesionales` (
  `idProfesionales` int(11) NOT NULL,
  `cuil` int(11) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `matricula` varchar(45) NOT NULL,
  `direccion` varchar(45) NOT NULL,
  `nivelAcc` int(11) NOT NULL,
  `especialidad` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `servicios`
--

CREATE TABLE `servicios` (
  `idServicios` int(11) NOT NULL,
  `Precio` decimal(10,2) DEFAULT NULL,
  `Profesionales_idProfesionales` int(11) NOT NULL,
  `Detalle` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `turnos`
--

CREATE TABLE `turnos` (
  `idTurnos` int(11) NOT NULL,
  `fecha` datetime NOT NULL,
  `Usuarios_idUsuarios` int(11) NOT NULL,
  `Mascotas_idMascotas` int(11) NOT NULL,
  `Profesionales_idProfesionales` int(11) NOT NULL,
  `Servicios_idServicios` int(11) NOT NULL,
  `EstadoTurno_idEstadoTurno` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `cuil` varchar(45) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `apellido` varchar(45) NOT NULL,
  `direccion` varchar(45) NOT NULL,
  `telefono` varchar(45) NOT NULL,
  `email` varchar(45) DEFAULT NULL,
  `nivelAcc` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `cuil`, `nombre`, `apellido`, `direccion`, `telefono`, `email`, `nivelAcc`) VALUES
(1, '2732502662', 'Andrea', 'Aguiar', 'ceibos 8432', '3764252400', 'andrea00aguiar@gmail.com', 0),
(5, '21781093', 'Marta', 'Santa Cruz', 'ceibos 8432', '001215454785', 'rey.laurad@gmail.com', NULL),
(6, '2732502888', 'Andrea', 'Santa Cruz', 'ceibos 8432', '111111111', 'gimenezselenaluana@gmail.com', NULL);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `estadoturno`
--
ALTER TABLE `estadoturno`
  ADD PRIMARY KEY (`idEstadoTurno`);

--
-- Indices de la tabla `mascotas`
--
ALTER TABLE `mascotas`
  ADD PRIMARY KEY (`idMascotas`),
  ADD KEY `fk_Mascotas_Usuarios_idx` (`Usuarios_idUsuarios`);

--
-- Indices de la tabla `profesionales`
--
ALTER TABLE `profesionales`
  ADD PRIMARY KEY (`idProfesionales`);

--
-- Indices de la tabla `servicios`
--
ALTER TABLE `servicios`
  ADD PRIMARY KEY (`idServicios`),
  ADD KEY `fk_Servicios_Profesionales1_idx` (`Profesionales_idProfesionales`);

--
-- Indices de la tabla `turnos`
--
ALTER TABLE `turnos`
  ADD PRIMARY KEY (`idTurnos`),
  ADD KEY `fk_Turnos_Usuarios1_idx` (`Usuarios_idUsuarios`),
  ADD KEY `fk_Turnos_Mascotas1_idx` (`Mascotas_idMascotas`),
  ADD KEY `fk_Turnos_Profesionales1_idx` (`Profesionales_idProfesionales`),
  ADD KEY `fk_Turnos_Servicios1_idx` (`Servicios_idServicios`),
  ADD KEY `fk_Turnos_EstadoTurno1_idx` (`EstadoTurno_idEstadoTurno`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `mascotas`
--
ALTER TABLE `mascotas`
  ADD CONSTRAINT `fk_Mascotas_Usuarios` FOREIGN KEY (`Usuarios_idUsuarios`) REFERENCES `usuarios` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `servicios`
--
ALTER TABLE `servicios`
  ADD CONSTRAINT `fk_Servicios_Profesionales1` FOREIGN KEY (`Profesionales_idProfesionales`) REFERENCES `profesionales` (`idProfesionales`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `turnos`
--
ALTER TABLE `turnos`
  ADD CONSTRAINT `fk_Turnos_EstadoTurno1` FOREIGN KEY (`EstadoTurno_idEstadoTurno`) REFERENCES `estadoturno` (`idEstadoTurno`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_Turnos_Mascotas1` FOREIGN KEY (`Mascotas_idMascotas`) REFERENCES `mascotas` (`idMascotas`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_Turnos_Profesionales1` FOREIGN KEY (`Profesionales_idProfesionales`) REFERENCES `profesionales` (`idProfesionales`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_Turnos_Servicios1` FOREIGN KEY (`Servicios_idServicios`) REFERENCES `servicios` (`idServicios`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_Turnos_Usuarios1` FOREIGN KEY (`Usuarios_idUsuarios`) REFERENCES `usuarios` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
