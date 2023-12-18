# Crear elementos HTML

Crear elementos HTML es una tarea común en el desarrollo web. JavaScript proporciona varios métodos para crear eficientemente diferentes elementos HTML o nodos. Estos métodos facilitan la creación de estructuras dinámicas, ya sea mediante bucles o estructuras definidas.

## Métodos para crear elementos HTML

Aquí hay una lista de algunos métodos útiles para crear elementos HTML:

- `.createElement(tag, options)`: Este método crea y devuelve un elemento HTML definido por el `tag`. Por ejemplo, `document.createElement("div")` crea un elemento `<div></div>`.
- `.createComment(text)`: Este método crea y devuelve un nodo de comentarios HTML. Por ejemplo, `document.createComment("Hello World")` crea un comentario HTML `<!-- Hello World -->`.
- `.createTextNode(text)`: Este método crea y devuelve un nodo de texto HTML. Por ejemplo, `document.createTextNode("Hello World")` crea un nodo de texto `Hello World`.
- `.cloneNode(deep)`: Este método clona el nodo HTML y devuelve una copia. El parámetro `deep` es `false` por defecto. Si `deep` es `true`, el método clonará también los elementos hijos del nodo.
- `.isConnected`: Esta propiedad indica si el nodo HTML está insertado en el documento HTML.

## Creando elementos con `createElement()`

El método `.createElement()` se utiliza para crear un elemento HTML en la memoria (¡no estará insertado aún en nuestro documento HTML!). Con dicho elemento almacenado en una variable o constante, podemos modificar sus características o contenido, para posteriormente insertarlo en una posición determinada del DOM o documento HTML.

```javascript
const div = document.createElement("div"); // Creamos un <div></div>
const span = document.createElement("span"); // Creamos un <span></span>
const img = document.createElement("img"); // Creamos un <img>
```

En este punto, nos centraremos principalmente en el proceso de creación del elemento. Más adelante veremos diferentes formas de insertarlo en el DOM.

## El método `.cloneNode()`

Es importante tener cuidado al crear e intentar duplicar elementos HTML. Un error común es asignar un elemento que tenemos en otra variable, pensando que estamos creando una copia (cuando no es así). Para evitar que se cree una referencia, y duplicar el elemento, que es lo que realmente queremos, deberíamos usar el método `.cloneNode()`:

```javascript
const div = document.createElement("div");
div.textContent = "Elemento 1";

const div2 = div.cloneNode(); // Ahora SÍ estamos duplicando
div2.textContent = "Elemento 2";

div.textContent; // 'Elemento 1'
```

El método `cloneNode(deep)` acepta un parámetro `deep` opcional, a `false` por defecto, para indicar el tipo de clonación que se realizará:

- Si es `true`, clonará también elementos hijos. Se conoce como clonación profunda (Deep Clone).
- Si es `false`, no clonará elementos hijos. Se conoce como clonación superficial (Shallow Clone).

## La propiedad `.isConnected`

La propiedad `isConnected` nos indica si el elemento en cuestión está conectado al DOM, es decir, si está insertado en el documento HTML:

- Si devuelve `true`, significa que el elemento está conectado al DOM.
- Si devuelve `false`, significa que el elemento no está conectado al DOM.

Hasta ahora, hemos creado elementos que no lo están (permanecen sólo en memoria). En el capítulo Insertar elementos en el DOM veremos como insertarlos en el documento HTML para que aparezca visualmente en la página.

## Usando fragmentos

En algunas ocasiones, nos puede resultar muy interesante utilizar fragmentos. Los fragmentos son una especie de documento paralelo, aislado de la página con la que estamos trabajando, que tiene varias características:

- No tiene elemento padre. Está aislado de la página o documento.
- Es mucho más simple y ligero (mejor rendimiento).
- Si necesitamos hacer cambios consecutivos, no afecta al reflow (repintado de un documento).

Para crearlos, necesitaremos utilizar la siguiente función:

- `document.createDocumentFragment()`: Crea un fragmento aislado (sin padre).

Así pues, el objeto que devuelve el método `document.createDocumentFragment()` es un fragmento que podremos utilizar para almacenar en su interior un pequeño DOM temporal, que luego añadiremos en nuestro DOM principal.

```javascript
const fragment = document.createDocumentFragment();

for (let i = 0; i < 5000; i++) {
	const div = document.createElement("div");
	div.textContent = `Item número ${i}`;
	fragment.appendChild(div);
}

document.body.appendChild(fragment);
```

Como se puede ver, utilizamos el fragmento `fragment` generado como ubicación temporal donde hacer todos los cambios del DOM que necesitemos, sin que afecten al reflow del documento de forma independiente. Una vez terminemos nuestra lógica y tengamos el DOM definitivo, lo insertamos como hacemos siempre, por ejemplo, con un `appendChild` (ver más adelante).

Es entonces cuando se traslada todo el DOM del fragmento al lugar donde hemos indicado en el `appendChild` (en nuestro ejemplo, a la etiqueta `<body>`), dejando nuevamente el fragmento vacío. <|assistant to=assistant code|(

# Acceder a atributos HTML

Una vez que tenemos un elemento HTML y queremos crear algunos atributos para él, lo más sencillo es asignarle valores como propiedades de objetos:

```javascript
const element = document.querySelector("div"); // <div class="container"></div>

element.id = "page"; // <div id="page" class="container"></div>
element.style = "color: red"; // <div id="page" class="container" style="color: red"></div>
element.className = "data"; // <div id="page" class="data" style="color: red"></div>
```

## Obtener atributos HTML

Aunque la forma anterior es la más rápida, tenemos algunos métodos para obtener los atributos HTML de forma clara y literal, sin problemas como los de `className`:

- `hasAttributes()`: Indica si el elemento tiene atributos HTML.
- `hasAttribute(attr)`: Indica si el elemento tiene el atributo HTML `attr`.
- `getAttributeNames()`: Devuelve un array con los atributos del elemento.
- `getAttribute(attr)`: Devuelve el valor del atributo `attr` del elemento o `null` si no existe.

Consideremos el siguiente HTML:

```html
<div id="page" class="info data dark" data-number="5"></div>
```

Vamos a aplicar las siguientes lineas de Javascript, trabajando con ese elemento:

```javascript
const element = document.querySelector("#page");

element.hasAttributes(); // true (tiene 3 atributos)
element.hasAttribute("data-number"); // true (data-number existe)
element.hasAttribute("disabled"); // false (disabled no existe)

element.getAttributeNames(); // ["id", "data-number", "class"]
element.getAttribute("id"); // "page"
```

Como puedes ver, es muy sencillo de utilizar.

## Modificar o eliminar atributos HTML

Por otro lado, tenemos algunos métodos para modificar atributos HTML existentes, o directamente, eliminarlos:

- `setAttribute(attr, value)`: Añade o cambia el atributo `attr` al valor `value` del elemento HTML.
- `toggleAttribute(attr, force)`: Añade atributo `attr` si no existe, si existe lo elimina.
- `removeAttribute(attr)`: Elimina el atributo `attr` del elemento HTML.

Estos métodos son bastante autoexplicativos y fáciles de entender, aún así, vamos a ver unos ejemplos de uso donde podemos ver como funcionan. Continuamos con el ejemplo HTML anterior:

```html
<div id="page" class="info data dark" data-number="5"></div>
```

Ahora, vamos a modificar sus atributos HTML utilizando dichos métodos. Observa que `setAttribute()` puede servir tanto para añadir nuevos atributos que no existían como para modificar los que ya existen:

```javascript
const element = document.querySelector("#page");

element.setAttribute("data-number", "10"); // Cambiar data-number a 10
element.removeAttribute("id"); // Elimina el atributo id
element.setAttribute("id", "page"); // Vuelve a añadirlo
```

## Caso especial: Atributos booleanos

Hay un caso especial con los atributos HTML que son booleanos, es decir, que no tienen indicado ningún valor. Si intentamos establecer estos atributos con el método `setAttribute()` y le indicamos un booleano, no obtendremos exactamente lo que buscamos. Recuerda que los atributos HTML son siempre de tipo string:

```javascript
const button = document.querySelector("button");

button.setAttribute("disabled", true); // ❌ <button disabled="true">Clickme!</button>
button.disabled = true; // ✅ <button disabled>Clickme!</button>
button.setAttribute("disabled", ""); // ✅ <button disabled>Clickme!</button>
```

Normalmente, el método `.toggleAttribute(attr, force)` es más sencillo para estos casos. Añade el atributo que le pasas por parámetro si no existe, y lo elimina si ya existe.

## La propiedad `.className`

Javascript tiene a nuestra disposición una propiedad `.className` en todos los elementos HTML. Dicha propiedad contiene el valor del atributo HTML `class` como un string, y puede tanto leerse como reemplazarse:

- `.className`: Acceso directo al valor del atributo HTML `class`. También se puede asignar.
- `.classList`: Objeto especial para manejar clases CSS. Contiene métodos y propiedades de ayuda.

La propiedad `.className` viene a ser la modalidad directa y rápida de utilizar el getter `.getAttribute("class")` y el setter `.setAttribute("class", value)`.

Veamos un ejemplo utilizando estas propiedades y métodos y su equivalencia:

```javascript
const div = document.querySelector(".element");

// Obtener clases CSS
div.className; // "element shine dark-theme"
div.getAttribute("class"); // "element shine dark-theme"

// Modificar clases CSS
div.className = "element shine light-theme";
div.setAttribute("class", "element shine light-theme");
```

## La propiedad `.classList`

Para trabajar más cómodamente, existe un sistema muy interesante para trabajar con clases: la propiedad u objeto `.classList`. Se trata de un objeto especial que contiene una serie de ayudantes que permiten trabajar con las clases de forma más intuitiva y lógica.

Si accedemos a `.classList`, nos devolverá un array (no es exactamente un array, sino un DOMTokenList) de clases CSS de dicho elemento. Pero además, incorpora una serie de métodos ayudantes que nos harán muy sencillo trabajar con clases CSS:

- `.classList`: Devuelve la lista de clases del elemento HTML.
- `.classList.length`: Devuelve el número de clases del elemento HTML.
- `.classList.item(n)`: Devuelve la clase número `n` del elemento HTML. `null` si no existe.
- `.classList.contains(clase)`: Indica si la clase existe en el elemento HTML.
- `.classList.add(c1, c2, ...)`: Añade las clases `c1`, `c2`… al elemento HTML.
- `.classList.remove(c1, c2, ...)`: Elimina las clases `c1`, `c2`… del elemento HTML.
- `.classList.toggle(clase)`: Si la clase no existe, la añade. Si no, la elimina.
- `.classList.toggle(clase, expr)`: Si `expr` es `true`, añade la clase. Si es `false`, la elimina.
- `.classList.replace(old, new)`: Reemplaza la clase `old` por la clase `new`.

Veamos un ejemplo de uso de cada método de ayuda. Supongamos que tenemos el siguiente elemento HTML en nuestro documento. Vamos a acceder a él y a utilizar el objeto `.classList` con dicho elemento:

```html
<div id="page" class="info data dark" data-number="5"></div>
```

Observa que dicho elemento HTML tiene:

- Un atributo `id`
- Tres clases CSS: `info`, `data` y `dark`
- Un metadato HTML `data-number` (también es un atributo)

## Acceder a clases CSS

Al margen de acceder a la lista de clases mediante `.classList` y al número de clases del elemento con `.classList.length`, es posible acceder a la propiedad `.classList.values` para obtener un string como lo haría `.className`:

```javascript
const element = document.querySelector("#page");

// ¿Qué clases tiene?
element.classList;              // ["info", "data", "dark"] (DOMTokenList)
element.classList.value;        // "info data dark" (String)
element.classList.length;       // 3

// Convertirlas a array
Array.from(element.classList)   // ["info", "data", "dark"] (Array)
[...element.classList];         // ["info", "data", "dark"] (Array)

// Consultarlas
element.classList.item(0);      // "info"
element.classList.item(1);      // "data"
element.classList.item(3);      // null
```

El objeto `.classList` aunque parece que devuelve un array no es un array, sino un `DOMTokenList` que actúa de forma similar a un array, por lo que puede carecer de algunos métodos o propiedades concretos. Si quieres convertirlo a un array real, utiliza `Array.from()` o desestructuración con `[...div.classList]`.

Por último, observa que disponemos del método `.classList.item()` que nos devuelve un string con la clase específica en esa posición. Si no existe una clase en esa posición, nos devolverá `null`.

## Añadir y eliminar clases CSS

Los métodos `.classList.add()` y `.classList.remove()` permiten indicar una o múltiples clases CSS a añadir o eliminar. Observa el siguiente código donde se ilustra un ejemplo:

```javascript
const element = document.querySelector("#page");

element.classList.add("uno", "dos");
element.classList; // ["info", "data", "dark", "uno", "dos"]

element.classList.remove("uno", "dos");
element.classList; // ["info", "data", "dark"]
```

Al utilizar los métodos `.add()` o `.remove()`, en el caso de que se añada una clase CSS que ya existía previamente, o que se elimine una clase CSS que no existía, simplemente no ocurrirá nada.

## Comprobar si existen clases CSS

Con el método `.classList.contains()` podemos comprobar si existe una clase en un elemento HTML, ya que nos devuelve un booleano indicándonos si está presente o no:

```javascript
const element = document.querySelector("#page");

element.classList; // ["info", "data", "dark"]
element.classList.contains("info"); // Devuelve `true` (existe esa clase)
element.classList.contains("warning"); // Devuelve `false` (no existe esa clase)
```

Esto puede resultar interesante en algunas situaciones, donde queremos averiguar mediante Javascript si existe una clase.

## Conmutar o alternar clases CSS

Otro ayudante muy interesante es el del método `.classList.toggle()`, que lo que hace es añadir o eliminar la clase CSS dependiendo de si ya existía previamente. Es decir, añade la clase si no existía previamente o elimina la clase si existía previamente:

```javascript
const element = document.querySelector("#page");

element.classList; // ["info", "data", "dark"]

element.classList.toggle("info"); // Como "info" existe, lo elimina. Devuelve "false"
element.classList; // ["data", "dark"]

element.classList.toggle("info"); // Como "info" no existe, lo añade. Devuelve "true"
element.classList; // ["info", "data", "dark"]
```

Observa que `.toggle()` devuelve un booleano que será `true` o `false` dependiendo de si, tras la operación, la clase sigue existiendo o no. Ten en cuenta que en `.toggle()`, al contrario que `.add()` o `.remove()`, sólo se puede indicar una clase CSS por parámetro.

## Reemplazar una clase CSS

Por último, tenemos un método `.classList.replace()` que nos permite reemplazar la primera clase indicada por parámetro, por la segunda. Veamos este método en acción:

```javascript
const element = document.querySelector("#page");

element.classList; // ["info", "data", "dark"]

element.classList.replace("dark", "light"); // Devuelve `true` (se hizo el cambio)
element.classList.replace("warning", "error"); // Devuelve `false` (no existe warning)
```

Con todos estos métodos de ayuda, nos resultará mucho más sencillo manipular clases CSS desde Javascript en nuestro código.

# Contenido en el DOM

Antes de empezar, imaginemos que tenemos el siguiente código HTML:

```html
<div class="container">
	<div class="parent">
		<p>Hola a todos.</p>
		<p class="message">Mi nombre es <strong>Manz</strong>.</p>
	</div>
</div>
```

Vamos a seleccionar el elemento `<p>` con clase `.message` desde Javascript y a trabajar con él accediendo a varias de sus propiedades. Las propiedades a las que vamos a acceder son las siguientes:

- `.nodeName`: Devuelve el nombre del nodo (etiqueta si es un elemento HTML). Sólo lectura.
- `.textContent`: Devuelve el contenido de texto del elemento. Se puede asignar para modificar.
- `.innerText`: Versión no estándar de `.textContent` de Internet Explorer con diferencias. Evitar.
- `.outerText`: Versión no estándar de `.textContent/.outerHTML` de Internet Explorer. Evitar.
- `.innerHTML`: Devuelve el contenido HTML del elemento. Se puede usar asignar para modificar.
- `.outerHTML`: Idem a `.innerHTML` pero incluyendo el HTML del propio elemento HTML.
- `.setHTML(htmlCode, options)`: Método que inserta HTML, pero sanitizando la entrada de datos.

## La propiedad `nodeName`

La propiedad `nodeName` nos devuelve el nombre del nodo, que en elementos HTML es interesante puesto que nos devuelve el nombre de la etiqueta (en mayúsculas). Se trata de una propiedad de sólo lectura, por lo cuál no podemos modificarla, sólo acceder a ella.

## La propiedad `.textContent`

La propiedad `.textContent` nos devuelve el contenido de texto de un elemento HTML. Es útil para obtener (o modificar) sólo el texto dentro de un elemento, obviando el marcado o etiquetado HTML:

```javascript
const element = document.querySelector(".message");

element.textContent; // "Mi nombre es Manz."
element.textContent = "Hola a todos";
element.textContent; // "Hola a todos"
```

Como puedes ver, no sólo podemos utilizar la propiedad `.textContent` para acceder a la información de texto que contiene, sino también para reemplazar su contenido, simplemente asignándolo como si fuera una variable o constante.

Observa la etiqueta `<strong>`: En el caso de que el elemento tenga anidadas varias etiquetas HTML una dentro de otra, la propiedad `.textContent` se quedará sólo con el contenido textual.

## Las propiedades `.innerText` y `.outerText`

La propiedad `.innerText` es muy similar a `.textContent`, pero tiene una diferencia clave: accede al texto renderizado visualmente por el navegador. Por ejemplo, observa el siguiente fragmento de código:

```html
<div class="container">
	<p>Hola a todos.</p>
	<p>
		Me llamo <strong>Manz</strong>.
		<mark style="display: none">New message</mark>
	</p>
	<p hidden>Esto es un mensaje posterior oculto semánticamente.</p>
	<details>
		<summary>Más información</summary>
		<div>Esto es un desplegable que está colapsado.</div>
	</details>
</div>
```

Observa que:

- El contenido de la etiqueta `<mark>` está oculto mediante CSS.
- El contenido de la tercera etiqueta `<p>` está oculto semánticamente mediante el atributo `hidden`.
- El contenido de la etiqueta `<div>` dentro del `<details>` está oculto porque el acordeón está colapsado.

Si consultamos el contenido de texto del `.container` mediante la propiedad `.textContent` nos devolvería todo el contenido de texto de todas las etiquetas del interior del `.container`. Sin embargo, si lo hacemos mediante la propiedad `.innerText` nos devolvería lo siguiente:

```javascript
const element = document.querySelector(".container");
element.innerText;

// "Hola a todos.
//
// Me llamo Manz.
//
// Más información"
```

## La propiedad `.innerHTML`

Por otro lado, tenemos la propiedad `.innerHTML`, que nos permite acceder al contenido de un elemento, pero en lugar de devolver su contenido de texto, nos devuelve su contenido HTML, es decir, su marcado HTML. Esto tiene varias implicaciones que explicaremos más adelante.

Primero, un ejemplo con la diferencia entre `.textContent` y `.innerHTML`:

```javascript
const element = document.querySelector(".message");

element.innerHTML; // "Mi nombre es <strong>Manz</strong>."
element.textContent; // "Mi nombre es Manz."
```

De la misma forma que `.textContent`, también podemos usar `.innerHTML` para modificar el contenido. Ten en cuenta que el contenido HTML suministrado a `.innerHTML` se interpretará, mientras que el suministrado por `.textContent` se inserta literalmente como texto:

```javascript
element.innerHTML = "<strong>Importante</strong>"; // Se lee "Importante" (en negrita)
element.textContent = "<strong>Importante</strong>"; // Se lee "<strong>Importante</strong>"
```

## Parseo de marcado HTML

Ten en cuenta que la propiedad `.innerHTML` comprueba y parsea el marcado HTML escrito (corrigiendo si hay errores) antes de realizar la asignación. Por ejemplo, observa el siguiente código:

```javascript
const div = document.createElement("div");
div.innerHTML = "<strong>Manz";
div.innerHTML; // "<strong>Manz</strong>"
```

Aunque hemos insertado el HTML incompleto con `.innerHTML`, si examinamos el contenido, podemos ver que está completo. Esto ocurre porque el navegador parsea e intenta que el código HTML sea correcto en todo momento.

Esto puede provocar algunas incongruencias si el código es incorrecto o una disminución de rendimiento en porciones de código muy extensas o que hay que procesar múltiples veces.

## La propiedad `.outerHTML`

La propiedad `.outerHTML` es muy similar a la anterior. Mientras que `.innerHTML` devuelve el código HTML del interior de un elemento HTML, `.outerHTML` devuelve el código HTML desde el exterior, es decir, incluyendo al propio elemento implicado:

```javascript
const data = document.querySelector(".data");
data.innerHTML = "<h1>Tema 1</h1>";

data.textContent; // "Tema 1"
data.innerHTML; // "<h1>Tema 1</h1>"
data.outerHTML; // "<div class="data"><h1>Tema 1</h1></div>"
```

Al igual que hemos visto anteriormente, se puede utilizar `.outerHTML` asignando textos para modificar su contenido. Esto puede ser muy útil para reemplazar un elemento HTML, incluido el propio elemento HTML contenedor.

## El método `.setHTML()`

El método `.setHTML()` es muy interesante para insertar contenido HTML sin preocuparte excesivamente por temas de seguridad, como suele ocurrir con `.innerHTML`. Su utilización es muy sencilla, observa el siguiente fragmento de código:

```javascript
const container = document.querySelector(".container");
const unsafe_html = "<strong onmouseover='alert(\"hello\")'>Hello</strong>";

container.innerHTML = unsafe_html; // Introduce literalmente el código HTML
container.setHTML(unsafe_html); // Introduce "<strong>Hello</strong>"
```

Opcionalmente, se le puede pasar un segundo parámetro de opciones, donde se puede configurar un sanitizador.

# Insertar elementos en el DOM

Veamos 3 formas (de más tradicional a más moderna) de inserción o modificación de elementos:

1️⃣ La API de nodos 2️⃣ La API de elementos 3️⃣ La API de inserción adyacente

Puedes usar la que prefieras, que se adapte mejor a tus necesidades.

## API de nodos

La API de nodos de Javascript es la más tradicional y antigua, y aunque cumple bien determinados aspectos, suele ser más complicado llegar al objetivo porque no hay ciertos métodos explícitos para hacer determinadas cosas. No obstante, suele ser la más extendida que te encuentras, ya que `.appendChild()` está muy extendido al ser uno de los más usados:

- `.appendChild(node)`: Añade como hijo el nodo `node`. Devuelve el nodo insertado.
- `.removeChild(node)`: Elimina y devuelve el nodo hijo `node`.
- `.replaceChild(new, old)`: Reemplaza el nodo hijo `old` por `new`. Devuelve `old`.
- `.insertBefore(new, node)`: Inserta el nodo `new` antes de `node` y como hijo del nodo actual.
- `.insertBefore(new, )`: Inserta el nodo `new` después del último nodo hijo. Equivale a `.appendChild()`.

De ellos, probablemente el método más extendido y conocido es `.appendChild()`. Vamos a analizar cada uno de ellos y ver como podemos utilizarlos.

### El método `.appendChild()`

Uno de los métodos más comunes para añadir un elemento HTML creado con Javascript es `.appendChild()`. Como su propio nombre indica, este método añade o inserta un nuevo elemento, como si fuera un hijo al final de todos los hijos del elemento sobre el que se realiza.

```javascript
const container = document.querySelector(".container");

const img = document.createElement("img");
img.src = "https://lenguajejs.com/assets/logo.svg";
img.alt = "Logo Javascript";

container.appendChild(img);
```

En este ejemplo, creamos un elemento `<img>` que aún no está conectado al DOM de la página. Existe sólo en la constante `<img>`. Posteriormente, añadimos los atributos `src` y `alt` y lo conectamos al DOM el elemento usando el método `.appendChild()`.

Se insertará como último hijo del elemento `<body>`, ya que es su comportamiento predefinido.

### El método `.removeChild()`

En algunos casos, nos puede interesar eliminar un nodo hijo de un elemento. Para esas situaciones, podemos utilizar el método `.removeChild(node)` donde `node` es el nodo hijo que queremos eliminar:

```javascript
const container = document.querySelector(".container");
const secondItem = container.querySelector(".item:nth-child(2)");

container.removeChild(secondItem); // Desconecta el segundo .item
```

### El método `.replaceChild()`

De la misma forma, el método `replaceChild(new, old)` nos permite cambiar un nodo hijo `old` por un nuevo nodo hijo `new`. En ambos casos, el método nos devuelve el nodo reemplazado:

```javascript
const container = document.querySelector(".container");
const secondItem = container.querySelector(".item:nth-child(2)");

const newNode = document.createElement("div");
newNode.textContent = "DOS";

container.replaceChild(newNode, secondItem);
```

### El método `.insertBefore()`

Por último, el método `insertBefore(newnode, node)` es un método más específico y menos utilizado en el que se puede especificar exactamente el lugar a insertar un nodo. El primer parámetro es el nodo a insertar, mientras que el segundo parámetro puede ser:

- `null`: inserta `newnode` después del último nodo hijo. Equivale a `.appendChild()`.
- `node`: inserta `newnode` antes de dicho `node` de referencia.

```javascript
const container = document.querySelector(".container");
const secondItem = container.querySelector(".item:nth-child(2)");

const newNode = document.createElement("div");
newNode.textContent = "Nuevo elemento";

container.insertBefore(newNode, secondItem);
```

En este caso, el nuevo elemento aparecería justo antes del segundo item.

## API de elementos

Los métodos mencionados con anterioridad sirven en muchos casos, sin embargo, son poco específicos y puede que no cubran todas las posibles situaciones. Existe otra familia de métodos para añadir e insertar elementos que quizás sea mucho más versátil.

Todos los métodos permiten pasar por parámetro un elemento o una lista de elementos. También puedes pasar un `string` (para insertar un fragmento de texto). Echemos un vistazo a estos métodos:

- `.before()`: Añade el nuevo elemento justo antes.
- `.after()`: Añade el nuevo elemento justo después.
- `.prepend()`: Se añade el nuevo elemento antes del primer hijo.
- `.append()`: Se añade el nuevo elemento después del último hijo.
- `.replaceChildren()`: Elimina todos los hijos y los sustituye por el nuevo elemento.
- `.replaceWith()`: Se sustituye por el nuevo elemento.
- `.remove()`: Elimina el propio elemento.

Vamos a suponer que estos métodos los vamos a ejecutar en base al elemento `container`, por lo que todo se hará respecto a él. Por ejemplo, `container.before()`.

### El método `.before()` y `.after()`

Con el método `.before()` podemos insertar uno o varios elementos antes del elemento que llama al `before` (en el ejemplo, `container`). Con el método `.after()` ocurre exactamente lo mismo, pero después del elemento en lugar de antes:

```javascript
const element = document.createElement("div");
element.textContent = "Item insertado";

// A) Inserta antes de .container
container.before(element);

// B) Inserta después de .container
container.after(element);
```

### El método `.prepend()` y `.append()`

Con estos dos métodos podemos insertar elementos en sus elementos hijos, al principio o al final. El método `.prepend()` permite insertar uno o varios elementos antes del primer elemento hijo de nuestro elemento base. En el caso de `append()` ocurre lo mismo, pero después del último elemento hijo:

```javascript
const element = document.createElement("div");
element.textContent = "Item insertado";

// A) Inserta antes del primer hijo de .container
container.prepend(element);

// B) Inserta después del último hijo de .container
container.append(element);
```

El método `.append()` es equivalente al `.appendChild()` que vimos más atrás.

### El método `.replaceChildren()` y `.replaceWith()`

Por otro lado, también tenemos los métodos `.replaceChildren()` y `.replaceWith()`. El primero de ellos, `replaceChildren()` permite eliminar todos los elementos hijos del elemento base, y sustituirlos por uno o varios que indiques por parámetro.

El segundo método, `replaceWith()`, lo que permite es reemplazar el propio elemento base con uno o varios elementos que pasemos por parámetro, por lo que se realiza un reemplazo completo:

```javascript
const element = document.createElement("div");
element.textContent = "Nuevo Item hijo";

// A) Reemplaza por todos sus hijos
container.replaceChildren(element);

// B) El container es reemplazado por el nuevo item hijo
container.replaceWith(element);
```

### El método `.remove()`

Al igual que podemos insertar o reemplazar elementos, también podemos eliminarlos. Ten en cuenta que al «eliminar» un nodo o elemento HTML, lo que hacemos realmente no es borrarlo, sino desconectarlo del DOM o documento HTML, de modo que no están conectados, pero siguen existiendo.

El método `.remove()` se encarga de desconectarse del DOM a sí mismo,

```javascript
const div = document.querySelector(".deleteme");

div.isConnected; // true
div.remove();
div.isConnected; // false
```

En este caso, lo que hemos hecho es buscar el elemento HTML `<div class="deleteme">` en el documento HTML y desconectarlo de su elemento padre, de forma que dicho elemento pasa a no pertenecer al documento HTML, pero sigue existiendo en la constante `div`.


## API de inserción adyacente

Probablemente, una de las APIs de manejo del DOM más desconocidas y más interesantes, es la de Inserción de elementos adjacentes. Son una familia de 3 métodos que permiten hacer prácticamente cualquier operación posible en el DOM.

Son los métodos que tenemos a continuación:

* `.insertAdjacentElement(position, element)`: Inserta el `element` en la posición `position`. Si falla, `null`.
* `.insertAdjacentHTML(position, htmlCode)`: Inserta el código HTML de `htmlCode` en la posición `position`.
* `.insertAdjacentText(position, text)`: Inserta el texto `text` en la posición `position`.

Los métodos de la familia `insertAdjacent` son bastante más versátiles que `.appendChild()`, ya que permiten muchas más posibilidades. Tenemos tres versiones diferentes:

* `.insertAdjacentElement()` donde insertamos una etiqueta HTML
* `.insertAdjacentHTML()` donde insertamos código HTML directamente (similar a `innerHTML`)
* `.insertAdjacentText()` donde insertamos un texto directamente (similar a `textContent`)

Ten en cuenta que `position` es un `string` que puede tener uno de los siguientes valores:

* `beforebegin`: Inserta el elemento antes de la etiqueta HTML de apertura.
* `afterbegin`: Inserta el elemento dentro, antes de su primer hijo.
* `beforeend`: Inserta el elemento dentro, justo antes de la etiqueta HTML de cierre.
* `afterend`: Inserta el elemento después de la etiqueta HTML de cierre.

Veamos algunos ejemplo aplicando cada uno de ellos con el método `.insertAdjacentElement()`:

```javascript
const container = document.querySelector(".container");

// Creamos un nuevo <div>Ejemplo</div>
const div = document.createElement("div");
div.textContent = "Ejemplo";

container.insertAdjacentElement("beforebegin", div);
// A) <div>Ejemplo</div> <div class="container">container</div>

container.insertAdjacentElement("afterbegin", div);
// B) <div class="container"> <div>Ejemplo</div> container</div>

container.insertAdjacentElement("beforeend", div);
// C) <div class="container">container <div>Ejemplo</div> </div>

container.insertAdjacentElement("afterend", div);
// D) <div class="container">App</div> <div>Ejemplo</div>
```

Ten en cuenta que en el ejemplo muestro varias opciones alternativas, no lo que ocurriría tras ejecutar las cuatro opciones una detrás de otra.

Por otro lado, notar que tenemos tres versiones en esta familia de métodos, una que actua sobre elementos HTML (la que hemos visto), pero otras dos que actuan sobre código HTML y sobre nodos de texto. Veamos un ejemplo de cada una:

```javascript
container.insertAdjacentElement("beforebegin", div);
// A) <div>Ejemplo</div> <div class="container">App</div>

container.insertAdjacentHTML("beforebegin", "<p>Hola</p>");
// B) <p>Hola</p> <div class="container">App</div>

container.insertAdjacentText("beforebegin", "Hola a todos");
// C) Hola a todos <div class="container">App</div>
```
