# proyectos-laboratorio
Proyectos desarrollados sobre scripts Python 

### Referencia
Se puede encontrar una explicación más completa de este material docente en el artículo **Introducción a la Programación con Python, Computación Interactiva y Aprendizaje Significativo**  ([PDF](http://www.aenui.net/ojs/index.php?journal=actas_jenui&page=article&op=view&path%5B%5D=430&path%5B%5D=632)), publicado en las _XXIV Jornadas sobre la Enseñanza Universitaria de la Informática_ ([JENUI18](http://jenui2018.uoc.edu/)). Para citar este trabajo:

```
@article{troyano2018introduccion,
  title={Introducción a la Programación con Python, Computación Interactiva y Aprendizaje Significativo},
  author={Troyano, José A. and Cruz, Fermín and González, Mariano and Vallejo, Carlos G. and Toro, Miguel},
  journal={Actas de XXIV Jornadas sobre la Enseñanza Universitaria de la Informática - JENUI'18},
  volume={3},
  pages={223--230},
  year={2018}
}
```

### Contenido

Cada carpeta contiene un proyecto implementado en un script Python. Estos proyectos permiten ir descubriendo distintos elementos del lenguaje Python mediante su aplicación en la resolución de un problema concreto. Se utilizará este material en las clases de laboratorio.

Los proyectos están parcialmente resueltos, incluyen:
- Un breve enunciado en pdf
- La organización del proyecto en funciones. Para cada función se definen los parámetros y se incluye un comentario explicativo de su funcionamiento.
- Un módulo de pruebas con una función de test para cada función del proyecto
- La decisión de las estructuras usadas para representar los datos del proyecto

No se incluye:
- La implementación de las funciones. El cuerpo de las funciones contiene solo una instrucción <code>pass</code> que deberá ser sustituida por una implementación que cubra lo que se indica en el comentario explicativo. 

Los proyectos disponibles son:

1. **Poblacion**: análisis de datos sobre la población mundial
2. **Normalidad**: test de normalidad para series de valores numéricos
3. **Minimos cuadrados**: cálculo de una recta de regresión mediante la técnica de mínimos cuadrados
4. **Cifrado**: cifrado y descifrado de textos mediante el código de desplazamiento de César
5. **D-Hondt**: análisis de datos electorales y cálculo de escaños mediante la ley D'Hondt
6. **Vecinos cercanos**: clasificación automática basada en el método de los vecinos más cercanos
7. **Imagenes**: funciones de manipulación de imágenes RGB (reflejo, rotación, transformaciones del color, ...)
8. **Clima**: análisis de datos históricos de clima y generación de climogramas

Para poder ejecutar los scripts es necesario instalar el intérprete de Python. Lo más recomendable es hacerlo a través de la distribución de Anaconda (https://conda.io/docs/user-guide/install/download.html) que incluye el intérprete de Python, y la mayoría de las librerías que usaremos a lo largo del curso.

Para editar los programas se puede usar cualquier editor de texto plano, aunque es recomendable usar algún IDE (_integrated development environment_) como, por ejemplo, Eclipse+PyDev (http://www.pydev.org/).
