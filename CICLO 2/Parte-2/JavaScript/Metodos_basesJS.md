# Funciones para la consola

Las funciones de consola en JavaScript son útiles para mostrar información en la consola. Aquí hay algunas de las más comunes:

- `console.log()`: Muestra la información proporcionada en la consola JavaScript[^1^][1].
- `console.info()`: Similar a `console.log()`, se utiliza para mensajes de información[^2^][2].
- `console.warn()`: Muestra información de advertencia en la consola. Los mensajes aparecen en amarillo.
- `console.error()`: Muestra información de error en la consola[^3^][3]. Los mensajes aparecen en rojo.
- `console.clear()`: Limpia la consola[^4^][4]. Es equivalente a pulsar Ctrl + L o escribir `clear()`.
- `console.time()` y `console.timeEnd()`: Estas funciones se utilizan juntas para medir el tiempo que tarda en completarse una operación[^5^][5].
- `console.table(data, columns)`: Muestra los datos como una tabla en la consola. El argumento `data` debe ser un array o un objeto, y `columns` es un parámetro adicional opcional.
- `console.log("%c¡Hola Manz!", "background:linear-gradient(#000, #555); color:#fff; padding: 5px 10px;")`: Permite aplicar estilos CSS en la consola JavaScript utilizando `%c`[^6^][6].

# Métodos numéricos

Los métodos numéricos en JavaScript permiten convertir un número a diferentes formatos. Aquí hay algunos ejemplos:

- `.toExponential(digits)`: Convierte el número a notación exponencial con `digits` decimales.
- `.toFixed(digits)`: Convierte el número a notación de punto fijo con `digits` decimales.
- `.toPrecision(size)`: Utiliza `size` dígitos de precisión en el número.

En todos los casos, el número se convierte a tipo de dato String[^7^][7].

## Notación exponencial

- `(1.25).toExponential(0)`: "1e+0"
- `(1.25).toExponential(1)`: "1.3e+0"
- `(1.25).toExponential(2)`: "1.25e+0"
- `(1.25).toExponential(3)`: "1.250e+0"

## Notación punto fijo

- `(1.25).toFixed(0)`: "1"
- `(1.25).toFixed(1)`: "1.3"
- `(1.25).toFixed(2)`: "1.25"
- `(1.25).toFixed(3)`: "1.250"

## Cambiando precisión

- `(523.75).toPrecision(1)`: "5e+2"
- `(523.75).toPrecision(2)`: "5.2e+2"
- `(523.75).toPrecision(3)`: "524"
- `(523.75).toPrecision(4)`: "523.8"
- `(523.75).toPrecision(5)`: "523.75"

## Funciones matemáticas

Las funciones matemáticas en JavaScript permiten realizar operaciones matemáticas con los números. Aquí hay algunos ejemplos:

- `Math.abs(x)`: Devuelve el valor absoluto de `x`. |x|
- `Math.sign(x)`: Devuelve el signo del número: 1 si es positivo, -1 si es negativo.
- `Math.max(a, b, c...)`: Devuelve el número más grande de los indicados por parámetro.
- `Math.min(a, b, c...)`: Devuelve el número más pequeño de los indicados por parámetro.
- `Math.pow(base, exp)`: Potenciación. Devuelve el número `base` elevado a `exp`.
- `Math.sqrt(x)`: Devuelve la raíz cuadrada de `x`. √x
- `Math.cbrt(x)`: Devuelve la raíz cúbica de `x`. √3x

# Métodos de cadena

Los métodos de cadena en JavaScript permiten manipular y procesar cadenas de texto. Aquí hay algunos ejemplos:

## Búsqueda y reemplazo

- `.charAt(pos)`: Devuelve el carácter de la posición `pos`. Es similar al operador `[]`.
- `.indexOf(text)`: Devuelve la primera posición del texto `text`.
- `.indexOf(text, from)`: Similar al anterior, pero comienza la búsqueda desde la posición `from`.
- `.lastIndexOf(text)`: Devuelve la última posición del texto `text`.
- `.lastIndexOf(text, from)`: Similar al anterior, pero comienza la búsqueda desde la posición `from` y se mueve hacia el inicio.
- `.repeat(num)`: Devuelve el texto repetido `num` veces.
- `.substring(start, end)`: Devuelve el substring desde la posición `start` hasta `end`.
- `.substr(start, size)`: Devuelve el substring desde la posición `start` hasta `start + size`.
- `.slice(start, end)`: Similar a `.substr()`, pero con algunas diferencias leves.

## Ejemplo

```javascript

text.substring(3); // 'marino' (desde el 3 en adelante)
text.substring(3, 5); // 'ma'     (desde el 3, hasta el 5)
text.substr(3); // 'marino' (desde el 3 en adelante)
text.substr(3, 5); // 'marin'  (desde el 3, hasta el 3+5)[^8^][8]
text.substr(-3); // 'ino'    (desde la posición 3 desde el final, en adelante)
text.substr(-3, 2); // 'in'     (desde la posición 3 desde el final, hasta 2 posiciones más)
.startsWith(text, from) // Comprueba si el texto comienza por `text`.
.endsWith(text, to) // Comprueba si el texto termina por `text`.
.includes(text, from) // Comprueba si el texto contiene el subtexto `text`.
```

## Búsqueda y coincidencias

- `.search(regexp)`: Busca un patrón que encaje con `regexp` y devuelve la posición encontrada^9^.
- `.match(regexp)`: Similar al anterior, pero devuelve las coincidencias encontradas.
- `.matchAll(regexp)`: Similar al anterior, pero devuelve un iterador para iterar por cada coincidencia, devuelve un array con las coincidencias encontradas.

```javascript
const textito = "El gato, el perro y el pato.";
const regexp = /.a.o/g;

textito.search(regexp); // 3, porque la primera coincidencia ocurre en la posición 3 (gato)[^9^][9]
textito.match(regexp); // ["gato", "pato"], las dos coincidencias encontradas
const iterator = textito.matchAll(regexp);
for (let ocurrence of iterator) {
	console.log(ocurrence);
}
// ['gato', index: 3, input: 'El gato, el perro y el pato.', groups: undefined]
// ['pato', index: 23, input: 'El gato, el perro y el pato.', groups: undefined]
```

## Reemplazo de texto

- `.replace(text, newText)`: Reemplaza la primera aparición del `text` por `newText`.
- `.replace(regexp, newText)`: Similar al anterior, pero busca a partir de una `regexp` en lugar de un string.
- `.replaceAll(text, newText)`: Reemplaza todas las apariciones del texto `text` por `newText`.
- `.replaceAll(regexp, newText)`: Similar al anterior, pero busca a partir de una `regexp` en lugar de un string.

```javascript
const text = "Hola gato, ¿eres un perro o eres un pato?";[^13^][13]

// Reemplazar la primera ocurrencia
text.replace("g", "p"); // "Hola pato, ¿eres un perro o eres un pato?"[^13^][13][^12^][12]
text.replace("g", "p").replace("o", "a"); // "Hala pato, ¿eres un perro o eres un pato?"

// Reemplazar todas las ocurrencias
text.replaceAll("e", "i"); // "Hola gato, ¿iris un pirro o iris un pato?"[^10^][10][^11^][11]
text.replace(/e/g, "i"); // "Hola gato, ¿iris un pirro o iris un pato?"

const daenerys = "Javascript es un gran lenguaje";[^14^][14]

daenerys.replace(/[aeou]/g, "i"); // 'Jiviscript is in grin lingiiji'
```

# Expresiones regulares

Las expresiones regulares son secuencias de caracteres que forman un patrón de búsqueda o reemplazo de texto^15^. Se pueden crear con dos sintaxis: usando barras /…/ o usando el constructor `new RegExp("patrón", "banderas")`^16^. Por ejemplo, `/abc/` y `new RegExp("abc")` son dos formas de crear una expresión regular que coincide con la cadena “abc”^17^.

## Banderas

Las banderas modifican el comportamiento de las expresiones regulares. Aquí están las banderas más comunes en JavaScript:

- `i`: Ignora las mayúsculas y minúsculas. Por ejemplo, `/abc/i` coincide con “abc”, “ABC”, “Abc”, etc.
- `g`: Busca todas las coincidencias en lugar de detenerse en la primera. Por ejemplo, `/a/g` en “banana” coincide con las dos “a”.
- `m`: Trata a los caracteres de inicio y fin (`^` y `$`) como el inicio y el fin de cada línea en lugar de toda la cadena.
- `s`: Hace que el carácter `.` coincida con los caracteres de nueva línea.
- `u`: Trata a la cadena como Unicode.
- `y`: Realiza una búsqueda desde la última coincidencia en lugar de desde el principio.

## Métodos de cadena

Los métodos de cadena que admiten expresiones regulares son: `match`, `replace`, `search` y `split`. Por ejemplo, `"abc".match(/a/)` devuelve un array con la primera coincidencia de “a” en “abc”.

## Métodos de RegExp

Los métodos de RegExp que se pueden usar con las expresiones regulares son: `test` y `exec`. Por ejemplo, `/a/.test("abc")` devuelve `true` porque “a” se encuentra en “abc”.

## Caracteres especiales

Los caracteres especiales son símbolos que tienen un significado especial en las expresiones regulares. Algunos ejemplos son:

- `.`: Coincide con cualquier carácter excepto los de nueva línea.
- `*`: Coincide con cero o más repeticiones del carácter anterior.
- `+`: Coincide con una o más repeticiones del carácter anterior.
- `?`: Hace que el carácter anterior sea opcional.
- `^`: Coincide con el inicio de la cadena.
- `$`: Coincide con el final de la cadena.
- `\`: Se usa para escapar caracteres especiales.

## Grupos y retroreferencias

Los grupos son subexpresiones que se pueden capturar entre paréntesis. Se pueden usar para extraer partes de la cadena o para aplicar cuantificadores. Por ejemplo, en la expresión regular `(abc)`, "abc" es un grupo. Las retroreferencias son referencias a los grupos capturados que se pueden usar dentro de la misma expresión regular o en el método `replace`. Se indican con una barra invertida seguida del número del grupo (`\1`, `\2`, etc.).

## Clases de caracteres

Las clases de caracteres son conjuntos de caracteres que se pueden especificar entre corchetes. Se pueden usar para indicar un rango (por ejemplo, `[a-z]`), una negación (por ejemplo, `[^a-z]`), una clase predefinida (por ejemplo, `\d` para dígitos, `\w` para alfanuméricos, `\s` para espacios) o una clase personalizada (por ejemplo, `[aeiou]` para vocales).

## Cuantificadores

Los cuantificadores son símbolos que indican el número de repeticiones de un carácter, un grupo o una clase. Algunos ejemplos son: `{3}`, `{3,}`, `{,3}`, `{3,5}`, `?`, `+`, `*`.

## Anclas

Las anclas son símbolos que indican la posición relativa de una coincidencia. En las expresiones regulares, los caracteres `^` y `$` son anclas que coinciden con el inicio y el final de una cadena, respectivamente. Por ejemplo, `^abc` coincide con cualquier cadena que comienza con "abc", y `abc$` coincide con cualquier cadena que termina con "abc".

## Modos

Los modos son opciones que afectan al funcionamiento global de las expresiones regulares. Se pueden activar con las banderas que se colocan después del patrón. Los modos disponibles en JavaScript son: `i` (case-insensitive), `g` (global), `m` (multiline), `s` (dotall), `u` (Unicode) y `y` (sticky).

# Ejemplos

1. **Expresión regular simple**:

```javascript
let regex = /abc/;
```

En este ejemplo, `/abc/` es la expresión regular. `abc` es el patrón que estamos buscando en la cadena.

2. **Expresión regular con banderas** :

```javascript
let regex1 = /abc/gi;
```

Aquí, `g` y `i` son banderas. `g` significa “global”, lo que significa que buscará todas las coincidencias en la cadena, no solo la primera. `i` significa “insensible a mayúsculas y minúsculas”, lo que significa que tratará las letras mayúsculas y minúsculas como iguales.

3. **Expresión regular con grupos** :

```javascript
let regex2 = /(abc)/;
```

Aquí, `(abc)` es un grupo. Los grupos se utilizan para tratar múltiples caracteres como una sola unidad, y también se pueden utilizar para capturar partes de la cadena.

4. **Expresión regular con cuantificadores** :

```javascript
let regex3 = /a{3}/;
```

Aquí, `{3}` es un cuantificador. Significa que estamos buscando exactamente tres repeticiones del carácter `a`.

5. **Expresión regular con clases de caracteres** :

```javascript
let regex4 = /[a-z]/;
```

Aquí, `[a-z]` es una clase de caracteres. Significa que estamos buscando cualquier carácter que sea una letra minúscula.

## Expresión regular con anclas

```javascript
let regex5 = /^abc$/;
```

Aquí, `^` es una ancla que coincide con el inicio de la cadena, y `$` es una ancla que coincide con el final de la cadena. Por lo tanto, esta expresión regular coincide con una cadena que comienza y termina con “abc”.

## Modificación

Los métodos de modificación en JavaScript permiten transformar y ajustar cadenas de texto. Aquí hay algunos ejemplos:

- `.toLowerCase()`: Devuelve el string transformado a minúsculas[^1^][1].
- `.toUpperCase()`: Devuelve el string transformado a mayúsculas.
- `.toCapitalize()`, `.toCapitalizeEveryWord()`: Capitaliza el string.
- `.padStart(size, text)`: Devuelve el string rellenando el inicio con `text` hasta llegar al tamaño `size`[^2^][2][^1^][1]. Es especialmente útil para formatear horas.
- `.padEnd(size, text)`: Devuelve el string rellenando el final con `text` hasta llegar al tamaño `size`. Es especialmente útil para formatear horas.
- `.trimStart()`: Devuelve el string eliminando espacios a la izquierda del texto.
- `.trimEnd()`: Devuelve el string eliminando espacios a la derecha del texto.
- `.trim()`: Devuelve el string eliminando espacios a la izquierda y derecha del texto.
- `.concat(text1, text2...)`: Devuelve el string unido (concatenado) a las variables `text1`, `text2`…

```javascript
const name = "Manz";

// Utilizando método concat
name.concat("i", "to");     // "Manzito"
name.concat(4, 5);          // "Manz45"
name.concat((4 + 5));       // "Manz9"

// Utilizando operador +
name + "i" + "to";          // "Manzito"
name + 4 + 5;               // "Manz45"
name + (4 + 5);             // "Manz9"
```
