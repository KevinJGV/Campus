# INTRODUCCIÓN A HTML5

### ¿Qué es HTML?

- **HTML** (HyperText Markup Language) es un lenguaje de marcado utilizado en el desarrollo web para crear la estructura y el contenido de una página web.
- Permite definir la presentación y la organización de los elementos en una página.

### Código HTML y sus etiquetas

- El código HTML se compone de **etiquetas** que indican cómo se debe mostrar el contenido.
- Las etiquetas están encerradas entre **comillas angulares** (`<` y `>`).

---

## ETIQUETAS DE CABECERA

### ¿Qué son las etiquetas head?

- Las etiquetas `<head>` contienen metadatos e información sobre el documento HTML.
- No se muestra en la página web, pero es crucial para su funcionamiento.

### La etiqueta HTML `<meta>`

- Proporciona **metadatos** sobre el documento, como el juego de caracteres, la descripción y palabras clave.
- Ayuda a los motores de búsqueda y navegadores a interpretar correctamente la página.

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8" />
		<meta name="description" content="Página de ejemplo" />
		<meta name="keywords" content="HTML, tutorial, web" />
		<title>Mi Página Web</title>
	</head>
	<body>
		<!-- Contenido de la página -->
	</body>
</html>
```

### La etiqueta HTML `<link>`

- Establece **relaciones con otros documentos**, como hojas de estilo CSS o íconos.
- Se utiliza para vincular archivos externos.

```html
<!DOCTYPE html>
<html>
	<head>
		<link rel="stylesheet" href="styles.css" />
		<link rel="icon" href="favicon.ico" />
	</head>
	<body>
		<!-- Contenido de la página -->
	</body>
</html>
```

### Etiquetas para redes sociales

- Permiten **previsualizaciones en enlaces** cuando se comparte la página en redes sociales.

```html
<!DOCTYPE html>
<html>
	<head>
		<meta property="og:title" content="Mi Página Web" />
		<meta property="og:image" content="imagen.jpg" />
	</head>
	<body>
		<!-- Contenido de la página -->
	</body>
</html>
```

### Etiquetas HTML de precarga

- Utilizadas para **precargar anticipadamente enlaces**.

```html
<!DOCTYPE html>
<html>
	<head>
		<link rel="preload" href="archivo.js" as="script" />
		<link rel="preload" href="imagen.jpg" as="image" />
	</head>
	<body>
		<!-- Contenido de la página -->
	</body>
</html>
```

## ETIQUETAS SEMÁNTICAS DE TEXTO

### Enlaces o hipervínculos

- La etiqueta `<a>` se utiliza para **referenciar otros documentos o recursos** .
- Puede enlazar a otras páginas web, archivos descargables, direcciones de correo electrónico, etc.
- Ejemplo:
  ```html
  <a href="https://www.ejemplo.com">Visita nuestro sitio web</a>
  ```

### La etiqueta HTML `<strong>`

- Marca un texto como **importante o prioritario** .
- Visualmente, suele mostrarse en negrita.
- Ejemplo:
  ```html
  <p>Este es un <strong>mensaje importante</strong> para todos los usuarios.</p>
  ```

### La etiqueta HTML `<em>`

- Sirve para **enfatizar un fragmento de texto** .
- Visualmente, suele mostrarse en cursiva.
- Ejemplo:
  ```html
  <p>El <em>arte</em> es una expresión única de la creatividad humana.</p>
  ```

### La etiqueta HTML `<mark>`

- Se utiliza para **destacar textos y dirigir la atención** .
- Visualmente, suele mostrar el texto resaltado.
- Ejemplo:
  ```html
  <p>Este es un <mark>dato relevante</mark> que debes recordar.</p>
  ```

### La etiqueta HTML `<s>`

- Marca contenidos **imprecisos o irrelevantes** .
- Visualmente, suele mostrar el texto tachado.
- Ejemplo:
  ```html
  <p>El precio original era $100, pero ahora está en <s>$120</s>.</p>
  ```

### La etiqueta HTML `<span>`

- Sirve para **delimitar o agrupar fragmentos de texto** .
- No tiene significado semántico específico.
- Ejemplo:
  ```html
  <p>Este es un <span>texto especial</span> dentro de un párrafo.</p>
  ```

### La etiqueta HTML `<q>` y `<cite>`

- `<q>` se utiliza para **citar mensajes o frases cortas** .
- `<cite>` se usa para citar **títulos de obras** (libros, películas, etc.).
- Ejemplo:
  ```html
  <p>
  	Según <cite>El Principito</cite>, "Lo esencial es invisible a los ojos".
  </p>
  ```

### La etiqueta HTML `<sup>` y `<sub>`

- `<sup>` establece **superíndices** (como exponentes).
- `<sub>` define **subíndices** (como en fórmulas químicas).
- Ejemplo:
  ```html
  <p>H<sub>2</sub>O es la fórmula del agua.</p>
  ```

### La etiqueta HTML `<small>`

- Se utiliza para hacer **pequeñas aclaraciones o advertencias** .
- Visualmente, suele mostrar el texto en un tamaño más reducido.
- Ejemplo:
  ```html
  <p><small>Nota: Los precios pueden variar según la ubicación.</small></p>
  ```

### La etiqueta HTML `<abbr>` y `<dfn>`

- `<abbr>` muestra **abreviaturas** .
- `<dfn>` define **términos o conceptos** .
- Ejemplo:
  ```html
  <p>
  	<abbr title="World Wide Web">WWW</abbr> es la red global de información.
  </p>
  <p><dfn>HTML</dfn> es el lenguaje de marcado utilizado en la web.</p>
  ```

### La etiqueta HTML `<br>` y `<wbr>`

- `<br>` define **saltos de línea** .
- `<wbr>` indica **puntos de posible separación** en palabras largas.
- Ejemplo:
  ```html
  <p>Línea 1<br />Línea 2</p>
  <p>
  	Esta es una palabra muy larga que puede romperse así: su<wbr />percalifragilis<wbr />ticexpialidoso.
  </p>
  ```

### La etiqueta HTML `<kbd>` y `<samp>`

- `<kbd>` representa **entrada de teclado** (como atajos).
- `<samp>` muestra **salida de información** (como resultados de comandos).
- Ejemplo:
  ```html
  <p>Pulsa <kbd></kbd></p>
  ```

### La etiqueta HTML `<time>` y `<data>`

- `<time>` se utiliza para representar **fechas y horas** .
- `<data>` se emplea para representar **datos para máquinas** .
- Ejemplo:
  ```html
  <p>
  	La fecha de lanzamiento es
  	<time datetime="2023-12-31">31 de diciembre de 2023</time>.
  </p>
  <p><data value="42">Respuesta universal</data></p>
  ```

### La etiqueta HTML `<code>`

- Establece fragmentos de **código en línea** .
- Útil para mostrar comandos o sintaxis.
- Ejemplo:
  ```html
  <p>
  	Para instalar un paquete, ejecuta el comando
  	<code>npm install nombre-del-paquete</code>.
  </p>
  ```

### La etiqueta HTML `<ins>` y `<del>`

- `<ins>` indica información **añadida** o insertada.
- `<del>` señala información **eliminada** o tachada.
- Ejemplo:
  ```html
  <p>
  	El precio original era $100, pero ahora está en <del>$120</del>
  	<ins>$90</ins>.
  </p>
  ```

## ETIQUETAS SEMÁNTICAS

### La etiqueta HTML `<article>`

- Sirve para definir **entidades importantes** o secciones independientes de contenido.
- Puede contener títulos, párrafos, imágenes, etc.
- Ejemplo:
  ```html
  <article>
  	<h1>Artículo sobre la biodiversidad</h1>
  	<p>La biodiversidad es esencial para...</p>
  	<img src="biodiversidad.jpg" alt="Imagen de biodiversidad" />
  </article>
  ```

### La etiqueta HTML `<nav>`

- Define una **sección de navegación** dentro del documento.
- Contiene enlaces a otras páginas o recursos.
- Ejemplo:
  ```html
  <nav>
  	<a href="/">Inicio</a>
  	<a href="/productos">Productos</a>
  	<a href="/contacto">Contacto</a>
  </nav>
  ```

### Las etiquetas `<header>` y `<footer>`

- `<header>` representa el **encabezado** de una sección o del documento completo.
- `<footer>` se utiliza para el **pie de página** de una sección o del documento.
- Ejemplo:
  ```html
  <header>
  	<h1>Mi Blog</h1>
  	<p>Explorando el mundo digital</p>
  </header>
  ...
  <footer>
  	<p>Derechos reservados © 2023</p>
  </footer>
  ```

### La etiqueta HTML `<section>`

- Define **secciones concretas** de la página.
- Puede contener contenido relacionado.
- Ejemplo:
  ```html
  <section>
  	<h2>Noticias</h2>
  	<article>...</article>
  	<article>...</article>
  </section>
  ```

### Las etiquetas HTML `<h1>` … `<h6>`

- Son etiquetas para **títulos o encabezados** .
- `<h1>` es el más importante, `<h6>` el menos importante.
- Ejemplo:
  ```html
  <h1>Título principal</h1>
  <h2>Subtítulo</h2>
  ...
  <h6>Subtítulo de menor importancia</h6>
  ```

### La etiqueta HTML `<address>`

- Proporciona información de **contacto** .
- Puede incluir direcciones, números de teléfono, etc.
- Ejemplo:
  ```html
  <address>
  	<p>Dirección: Calle Principal, 123</p>
  	<p>Teléfono: 555-123-4567</p>
  </address>
  ```

### La etiqueta HTML `<article>`

- Sirve para definir **entidades importantes** o secciones independientes de contenido.
- Puede contener títulos, párrafos, imágenes, etc.
- Ejemplo:
  ```html
  <article>
  	<h1>Artículo sobre la biodiversidad</h1>
  	<p>La biodiversidad es esencial para...</p>
  	<img src="biodiversidad.jpg" alt="Imagen de biodiversidad" />
  </article>
  ```

### La etiqueta HTML `<nav>`

- Define una **sección de navegación** dentro del documento.
- Contiene enlaces a otras páginas o recursos.
- Ejemplo:
  ```html
  <nav>
  	<a href="/">Inicio</a>
  	<a href="/productos">Productos</a>
  	<a href="/contacto">Contacto</a>
  </nav>
  ```

### Las etiquetas `<header>` y `<footer>`

- `<header>` representa el **encabezado** de una sección o del documento completo.
- `<footer>` se utiliza para el **pie de página** de una sección o del documento.
- Ejemplo:
  ```html
  <header>
  	<h1>Mi Blog</h1>
  	<p>Explorando el mundo digital</p>
  </header>
  ...
  <footer>
  	<p>Derechos reservados © 2023</p>
  </footer>
  ```

### La etiqueta HTML `<section>`

- Define **secciones concretas** de la página.
- Puede contener contenido relacionado.
- Ejemplo:
  ```html
  <section>
  	<h2>Noticias</h2>
  	<article>...</article>
  	<article>...</article>
  </section>
  ```

### Las etiquetas HTML `<h1>` … `<h6>`

- Son etiquetas para **títulos o encabezados** .
- `<h1>` es el más importante, `<h6>` el menos importante.
- Ejemplo:
  ```html
  <h1>Título principal</h1>
  <h2>Subtítulo</h2>
  ...
  <h6>Subtítulo de menor importancia</h6>
  ```

### La etiqueta HTML `<address>`

- Proporciona información de **contacto** .
- Puede incluir direcciones, números de teléfono, etc.
- Ejemplo:

```html
<address>
	<p>Dirección: Calle Principal, 123</p>
	<p>Teléfono: 555-123-4567</p>
</address>
```

## ETIQUETAS DE TABLAS

### La etiqueta HTML `<table>`

* Se utiliza para  **mostrar datos tabulares** .
* Contiene filas (`<tr>`) y celdas (`<td>` o `<th>`).
* Ejemplo:
  ```html
  <table>
      <tr>
          <th>Nombre</th>
          <th>Edad</th>
      </tr>
      <tr>
          <td>Juan</td>
          <td>30</td>
      </tr>
  </table>
  ```

### Tablas con celdas irregulares

* Se pueden **combinar celdas** en una tabla HTML.
* Utilizando los atributos `rowspan` y `colspan`.
* Ejemplo:
  ```html
  <table>
      <tr>
          <td rowspan="2">Juan</td>
          <td>30</td>
      </tr>
      <tr>
          <td>Programador</td>
      </tr>
  </table>
  ```

### Organización de tablas HTML

* Etiquetas semánticas para  **organizar partes de la tabla** .
* `<thead>`: Encabezado de la tabla.
* `<tbody>`: Cuerpo de la tabla.
* `<tfoot>`: Pie de la tabla.
* Ejemplo:
  ```html
  <table>
      <thead>
          <tr>
              <th>Nombre</th>
              <th>Edad</th>
          </tr>
      </thead>
      <tbody>
          <tr>
              <td>Juan</td>
              <td>30</td>
          </tr>
      </tbody>
      <tfoot>
          <tr>
              <td colspan="2">Total: 1 persona</td>
          </tr>
      </tfoot>
  </table>
  ```

### Columnas en tablas HTML

* Modificar características de  **columnas en tablas** .
* Atributos como `colspan`, `colgroup`, etc.

---

## ETIQUETAS DE FORMULARIOS

### La etiqueta `<form>`

* Permite la **creación de formularios HTML** para su envío.
* Define el principio y final del formulario.
* Ejemplo:
  ```html
  <form action="/procesar-formulario" method="POST">
      <!-- Campos del formulario -->
  </form>
  ```

### La etiqueta HTML `<input>`

* Controles para  **campos de entrada de texto** .
* Ejemplo:
  ```html
  <input type="text" id="nombre" name="nombre" placeholder="Nombre" required>
  ```

### La etiqueta HTML `<textarea>`

* Controles para  **campos de entrada de texto extensos** .
* Ejemplo:
  ```html
  <textarea id="comentario" name="comentario" rows="4" cols="50"></textarea>
  ```

### La etiqueta `<input>` con números

* Controles para  **campos de entrada numéricos** .
* Ejemplo:
  ```html
  <input type="number" id="edad" name="edad" min="18" max="99">
  ```

### La etiqueta `<input>` con fechas

* Controles para  **campos de entrada con fechas** .
* Ejemplo:
  ```html
  <input type="date" id="fecha" name="fecha">
  ```

### La etiqueta `<input>` con casillas

* Controles para  **casillas de verificación y radio** .
* Ejemplo:
  ```html
  <input type="checkbox" id="suscripcion" name="suscripcion" value="1">
  <input type="radio" id="genero-m" name="genero" value="M">
  ```

### La etiqueta `<input>` con colores

* Controles para  **campos para elegir colores** .
* Ejemplo:
  ```html
  <input type="color" id="color" name="color">
  ```

### La etiqueta HTML `<select>`

* Crea  **listas de opciones desplegables** .
* Ejemplo:
  ```html
  <select id="pais" name="pais">
      <option value="es">España</option>
      <option value="ar">Argentina</option>
  </select>
  ```

### La etiqueta HTML `<datalist>`

* Crea  **listas de opciones autocompletables** .
* Ejemplo:
  ```html
  <input list="frutas" id="fruta" name="fr
  ```

## ORGANIZACIÓN DE CAMPOS EN FORMULARIOS

### Etiqueta `<fieldset>`

* Utilizada para **agrupar visualmente** campos relacionados en un formulario.
* Permite establecer una **leyenda** para describir el grupo de campos.
* Ejemplo:
  ```html
  <form>
      <fieldset>
          <legend>Datos personales</legend>
          <label for="nombre">Nombre:</label>
          <input type="text" id="nombre">
          <!-- Otros campos relacionados -->
      </fieldset>
  </form>
  ```

### Etiqueta `<label>`

* Representa el **título o etiqueta** de un elemento de control en un formulario.
* Mejora la **semántica y usabilidad** del formulario.
* Ejemplo:
  ```html
  <label for="email">Email:</label>
  <input type="email" id="email" required>
  ```

### Atributo `tabindex`

* Permite personalizar el **orden de navegación** entre los campos del formulario.
* Asigna un número para indicar el orden deseado.
* Ejemplo:
  ```html
  <input type="text" id="nombre" tabindex="1">
  <input type="email" id="email" tabindex="2">
  ```

### Etiqueta `<progress>`

* Crea **barras de progreso** para mostrar el avance en una tarea.
* Útil para formularios con múltiples pasos.
* Ejemplo:
  ```html
  <progress value="50" max="100"></progress>
  ```

### Etiqueta `<meter>`

* Representa  **medidores, umbrales y valores óptimos** .
* Puede utilizarse para mostrar el progreso o nivel de cumplimiento.
* Ejemplo:
  ```html
  <meter value="75" min="0" max="100">75%</meter>
  ```

### Etiqueta `<input>` tipo `submit`

* Crea **botones de envío** para enviar el formulario.
* Ejemplo:
  ```html
  <input type="submit" value="Enviar">
  ```

---

Espero que esta información te sea útil. Si tienes más preguntas o necesitas detalles adicionales, no dudes en preguntar. 😊.

## VALIDACIONES DE FORMULARIOS

### ¿Qué son las validaciones?

- Las **validaciones** son procesos para verificar la corrección y coherencia de los datos ingresados en formularios web.
- Son esenciales para garantizar que los datos sean válidos y seguros.

### Validaciones básicas con HTML5

- HTML5 proporciona **atributos de validación** para campos de entrada.
- Ejemplos:
  - `required`: Campo obligatorio.
  - `min` y `max`: Rango de valores numéricos.
  - `pattern`: Validación mediante expresiones regulares.

### El atributo `pattern` (RegExp)

- Permite realizar **validaciones avanzadas** utilizando expresiones regulares.
- Ejemplo:
  ```html
  <input type="text" pattern="[A-Za-z]+" title="Solo letras" />
  ```

---

## ETIQUETAS DE SCRIPTING

### Etiqueta HTML `<script>`

- Ejecuta **código Javascript** en una página web.
- Se coloca en la sección `<head>` o al final del `<body>`.
- Ejemplo:
  ```html
  <script>
  	alert("¡Hola, mundo!");
  </script>
  ```

### Atributos `defer` y `async`

- Controlan los **modos de carga** de las etiquetas `<script>`.
- `defer`: Carga el script después de que se renderice la página.
- `async`: Carga el script sin bloquear la renderización.

### Los módulos Javascript (ESM)

- Etiqueta `<script>` con el atributo `type="module"`.
- Permite usar **módulos de ES6** para organizar el código.

### Bloque de datos desconocido

- Etiqueta `<script>` con información **desconocida** .
- Ejemplo:
  ```html
  <script type="text/unknown">
  	// Código desconocido
  </script>
  ```

---

## ETIQUETAS INTERACTIVAS

### Etiqueta HTML `<details>`

- Crea **elementos desplegables** (Acordeón HTML).
- Permite mostrar u ocultar contenido.
- Ejemplo:
  ```html
  <details>
  	<summary>Ver más</summary>
  	<p>Contenido oculto aquí.</p>
  </details>
  ```

### Popovers: Elementos emergentes

- Contenido emergente con atributo `popover`.
- Ejemplo:
  ```html
  <a href="#" popover="Información adicional">Enlace</a>
  ```

### La etiqueta `<dialog>`

- Crea **ventanas de diálogo nativas** y ventanas modales.
- Ejemplo:
  ```html
  <dialog open>
  	<p>¿Estás seguro de eliminar este elemento?</p>
  	<button>Eliminar</button>
  </dialog>
  ```

### Eventos en HTML

- Conectar una **acción de usuario** con Javascript.
- Ejemplo:
  ```html
  <button onclick="saludar()">Saludar</button>
  <script>
  	function saludar() {
  		alert("¡Hola!");
  	}
  </script>
  ```

### El atributo `contenteditable`

- Convierte el texto de una etiqueta en **editable** .
- Ejemplo:
  ```html
  <p contenteditable>Texto editable</p>
  ```

### El atributo `hidden`

- Marca secciones como **ocultas** .
- Ejemplo:
  ```html
  <div hidden>Contenido oculto</div>
  ```
