Para la solución de tener seguridad segun  OWASP Top 10 se buscaria:
1. Validar la falsificación de las solicitudes del lado del servidor, verificando que no se puede acceder al segmento que no necesitan, validando reglas de firewall.
2. Verificar la autenticación y sesiones en la aplicación movil, interfaz web y backend, asegurandose que las contraseñas esten codificadas con un algoritmo hash.
3. Asegurar que los empleados tengan los permisos adecuados dependiendo al rol que tienen, no darles acceso de edición, creación, eliminación y actualización de tablas de base de datos a roles que no lo requieren, poner solo permisos de lectura.
4. Evitar la exposición de datos confidenciales asegurandose que la información del cliente y los detalles de los pedidos esten protegidos adecuadamente, usando tecnicas para proteger información confidencial en el transito de la información.
5. Verificar las fallas en el software y en la integridad de los datos, mirando que las librerias tengan una gran comunidad respaldada.
6. Evaluar que la seguridad de los contenedores y la configuración de kubernetes garantice que no existan vulnerabilidades.
7. Realizar pruebas de penetración para identificar posibles vulnerabilidades que puedan realizarse por fuerza bruta.
8. El login de cada uno de los aplicativos tenga un numero de intentos maximo, para asi evitar que ingresen al perfil haciendo uso de forma bruta.
9. Por ultimo tener actualizado a cada uno de los empleados, sobre buenas practicas de seguridad y las nuevas amenazas
