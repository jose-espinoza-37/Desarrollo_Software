# Actividad_1_ Jose Espinoza Rivadeneira
Tiempo Invertido: 3 horas, desde 29/08/2025
Contexto del tema: 

## Estructura de actividad 1 
1. DevOps vs. cascada tradicional
2. Ciclo tradicional de dos pasos y silos
3. d
4. d

## Entrega actividad 1
### DevOps vs. cascada tradicional
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

### Ciclo tradicional de dos pasos y silos
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

### Principios y beneficios de DevOps

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


       














