# Actividad_1_ Jose Espinoza Rivadeneira
Tiempo Invertido: 5 horas, desde 29/08/2025

Contexto del tema: Conocer más sobre el funcionamiento y obstáculos en el desarrollo de una aplicación. 

## 1. Estructura de actividad 1 
1. DevOps vs. cascada tradicional
2. Ciclo tradicional de dos pasos y silos
3. Principios y beneficios de DevOps
4. Evolución a DevSecOps
5. CI/CD y estrategias de despliegue
6. Fundamentos prácticos sin comandos

## 2. Entrega actividad 1
### 2.1 DevOps vs. cascada tradicional
1. Funcionamiento de cada modelo
* Modelo tradicional cascada
  * Un enfoque secuencial del desarrollo. En cada fase(desarrollo, QA, operaciones) debe terminar antes de pasar a la siguiente. 
  * El feedback llega tardio, usualmente cuando ya se ha pasado por las 3 etapas.
  * Maneja menos flexibilidad para hacer cambios, ya que implica a volver a pasar por las 3 fases de manera unidireccional.
    
* DevOps
  * Tiene la buena práctica de unir el proceso de las 3 fases, desde desarrollo(Dev) hasta operaciones(Ops). 
  * Busca una colaboraación conjunta con los 3 equipos, por lo que el feedback no es tardado. Y logra tener pequeños, pero frecuentes cambios.
  * Está basado en las metodologías ágiles CI/CD.
    
2. ¿Por qué DevOps tiene un menor riesgo frente a cascada?
* Feedback realizado:
  * En DevOps cada cambio realizado primero se prueba, valida y despliega, razón por la cual si hubiera un error se podría detectar en que actualización se dio.
  * Por otro lado cascada tiene grandes cambios, y al encontrarse una falla habría que investigar un largo proceso.

* Lotes de entrega: 
  * DevOps libera funcionalidades en iteraciones cortas y manejables. Lo que reduce la complejidad y ayuda a poder revertir cambios.
  * En cascada se entrega un gran lote, lo que hace más pesado el trabajo.

* Automatización
  * El uso de los pipelines en DevOps hace que se trabeje de forma automatizada ya sea para pruebas, despliegue o monitoreos. Lo que conlleva a reducir el error humano.
  * La forma manual es como trabaja cascada, por lo que se invierte tiempo haciendo una tarea muy repetitiva y aumenta la probabilidad del error por causa humana.

3. Caso reales de los modelos
* Juegos Indie
  * En este tipos de proyectos, donde en cliente es el mismo desarrollador. Se tiene claro los requisitos desde el inicio.
  * No tanta necesidad de hacer cambios bruscos en los requisitos.
  * El mismo creador hace los testeos, el desarrollo y despliegue. Por lo que el feedback es inmediato y no hay barreras entre comunicación. 
* Juegos AAA
  * Para estos proyectos grandes, un grupo reducido no es viable. Tardaría demasiado en finalizar, por lo que se divide el trabajo en varios departamentos.
  * Aun que los objetivos son claros desde un inicio, es necesario saber como están yendo en otro departamento, por lo que las reuniones frecuentes son fundamental.
     
* Mientras que se ve casada tiene menos flexibilidad, lo hace bien para proyectos medianos-pequeños.
* DevOps destaca en cuanto a la complejidad. Hace mas fluido al avance en conjunto con los demás departamentos. 

### 2.2 Ciclo tradicional de dos pasos y silos
Los ciclos de dos pasos, se refiere a la parte del proyecto que le corresponde a los de operación. Las cuales constan de 2 fases: Construcción y Operación.
* **Construcción(build)**: Parte del software que se desarrolla en un entorno aislado.
* **Operación(run)**: Encargados de ejecutar, monitoriar y si hubiera incidentes responder ante ellos.  

En cuanto a que son los silos. Se pueden decir que son estructuras **asiladas** en la organización, en donde cada equipo (desarrollo, QA, operaciones) trabaja con un objetivo particular. Además, escasea la comunicación.

Por lo que surge una barrera, pero también consigo trae nuevas formas de sortearlas. Como es el caso de "handoffs" (transferencias formales de trabajo) que es una forma de comunicación entre el equipo global.


1. Limitaciones del ciclo tradicional sin CI
* Grandes lotes de cambios
  * Al acomular nuevas funcionalidades y correcciones pasadas los costes de integración aumentan.
  * En caso de fallar algo, no estará claro en donde se originó el error.
* Colas de defectos y tiempos muertos
  * Los errores detectados son naturalmente reportados, pero el tiempo en llegar al equipo de desarrollo para su correción aumenta.
  * Genera los **handoffs con asimetría de información**, lo que significa que una de las partes tiene menos o nula información con respecto a la otra parte. 
   
2. Anti-patrones del ciclo en silos

* Anti-patrón 1:"Throw over the wall" (lanzar sobre la pared)

  * Lo que significa es que el equipo de desarrollo entrega el software al equipo de operaciones por entregar, ej. Dar solo el código sin ningún tipo de comentarios, instrucciones de como es el funcionamiento de los algoritmos.

  * El efecto que genera esta práctica es crear una *"caja negra"*, por lo que operaciones tarda en investigar las funciones para un diagnóstico.

* Anti-patrón 2: "Seguridad como auditoría tardía"
  * Es pensar que la seguridad se implementa y revisa al final del desarrollo en lugar de integrarla desde un inicio.
  * Causando que al detectar vulnerabilidades se tenga que reabrir fases ya cerradas. 

### 2.3 Principios y beneficios de DevOps

1. Integración continua CI
  * Hacer cambios en el código de forma frecuente y a la vez ligeras(diariamente).
  * Reduce el costo de integración tardía.

2. Entrega continua CD
  * Se asegura que el software siempre esté en estado "deployable"(listo para lanzamiento)
  * Incluye pruebas más amplias como: integración, seguridad, etc.
  * Hace que los despliegues sean menos riezgosos, teniendo en cuenta que son reversibles.
 
3. **Agile** precursor de DevOps
  * Las prácticas de este método siguen siendo utilizadas como "daily stand-up"(reuniones diarias). Permite identificar y solucionar los bloqueos encontrados.
    * Con esto se puede saber también que "branchs"(ramas) se les dará prioridad.
  * Usando retrospectiva nos permite aprender los incidentes o despliegues fallidos.
    * Se puede llegar a redifinir políticas en la producción.
    * Evita recaer en episodios no deseados.
4. Indicador observable de colaboración Dev–Ops
Los **PR**(pull resques) son solicitudes para fucionar ramas a otras ramas.
  * Se refleja con ello si los equipos están en sincronía.
  * Hay un notorio cambio entre PR, si el tiempo baja es buen indicativo.
  * No es de paga, ya que los repositorios tienen un registro del tiempo en donde se hacen cada PR.  

### 2.4 Evolución a DevSecOps

1. Diferencia SAST vs. DAST
* SAST (Static Application Security Testing):
  * Es un método el cual analisa el código fuente, código bytes o código binario para poder detectar vulnerabilidades antes de ejecutar el software.
  * Las vulnerabilidades que detectan son: inyecciones, malas prácticas de criptografía, librerías no seguras.
  * Se ubica en las primeras fases del pipeline(etapa build). 

* DAST (Dynamic Application Security Testing):
  * Evalua la aplicación cuando está siendo ejecutada. Simulando ataques reales en un entorgo seguro de staging.
  * Está puesta en la fase posterior al deslpiegue, en los entornos de prueba.
    
2. Gate puertas de cobertura de prueba
* Se centran en la integridad junto con la eficacia de las pruebas del software.
* Miden el porcentaje del código cubierto por las pruebas, así mismo, evaluan la calidad de estas.
* Depende de lo que se mida, pueden estar por encima del 60%, pero no llegan al 100%. 

3. Política de excepción 
* Es cuando un hallazgo no puede corregirse de forma inmediata.
* **Excepción temporal**: Cuando situaciones inesperadas cambian el flujo normal del trabajo, por lo que se da un tiempo para poder redirigir al correcto flujo.
* **Responsable**: Puede ser lider de un módulo, fundamentalmente asume la remediación.
* **Plan de corrección**: Se toma cuando se nota una vulnerabilidad o error, pero será omitida. Ya sea por falta de soporte para la aplicación u otros casos.
* **Caducidad automática**: En caso de que se termine el tiempo establecido y no hay correcciones, se bloqueará los pipelines con los despliegues relacionados. 

4. Evitar el teatro de seguridad
* Se le dice así cuando el equipo ponga como cumplido ciertos requisitos de seguridad, pero en verdad no se ha mejorado.
Dos señales de eficacia y cómo medirlas.

* Disminución de hallazgos repetidos:
  * Si las mismas vulnerabilidades no vuelven aparecer, como inyecciones en XXS.
  * Comparar reportes de SAST/DAST.
* Reducción de tiempo en remediación:
  * Cuando el tiempo entre la detección de una vulnerabilidad y su cierre efectivo amenora.
  * Se puede usar los ¨timestamps de detección y cierre en los issues¨.   
  
### 2.5 CI/CD y estrategias de despliegue
1. Microservicio: Autentificación
* La estrategía que usada será un "despliegue canary".
* Tiene como objetivo analizar si hay una mayor latencia, procesos de login.
* Podría ser una nueva forma de autentificar, como loguearse por medio de terceros(federado).

2. Tabla  de riesgos vs mitigaciones

 | Riesgo | Mitigación | 
 |-----------------|--------------------|
 | Regresión funcional(una función deja de responder como debería)| Validación de contratos de API en pipeline antes de seguir avanzando| 
 | El costo operativo de tener dos versiones| Límites de tiempo en que puedan haber versiones ejecutandose|
 | Usuarios que están autenticados en la versión antigua| Estrategia de draining de sesiones y compatibilidad de esquemas en tokens/cookies| 

3. KPI primario de gate
Es el indicativo de una empresa si está cumpliendo sus objetivos.
* KPI: Errores 5xx en autenticación
  * Los errores tipo 5xx son respuestas de error del servidor, o sea que no se pudo completar una solicitud.
* Umbral: < 0.5% de requests con error 5xx
* Ventana de observación: 15 minutos después de habilitar el canary
* Se puede actuar de la siguiente manera:
  * Si llego a superar el umbral: **rollback** automático.
  * Si se mantiene estable: Ampliar a más usuarios a seguir migrando.

### 2.6 Fundamentos prácticos sin comandos

1. HTTP – contrato observable
Se puede inferir el comportamiento del servidor con las respuestas que esta nos pueda dar.

* **Método**: Es lo que indique la intención de la petición. Puede ser `[POST]`, `[GET]`.
* **Código de estado**: Sería lo que refleja el resultado `[404 Not Found]`, `[500 Internal Server Error]`, `[200 OK]`.
* **Cabeceras clave**: Llegan a complementar la respuesta.



2. DNS – nombres y TTL
Cuando se consulta al DNS, se puede ver que tipo de registro apunta y por cuanto tiempo se mantiene válido(TTL).
* Cuando el TTL es bajo(60-300s):
  * Una propagación rápida, los clientes resfrescan la IP de forma frecuente.
  * Útil para los rollbacks: Si se cambia la IP de un servicio esencial, la red lo notará en minutos.
  * Dará una mayor latencia.
* Cuando el TTL es alto(24h):
  * Menos consultas al DNS, por lo que da buen rendimiento.
  * Se dará que algunos usuarios tienen la nueva IP, mientras que otros intentarán usar la IP anterior. Lo que crea ventanas de inconsistencias. 


3. TLS - seguridad en tránsito 







