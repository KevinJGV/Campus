<!-- Crear una tabla HTML -->
<table>
  <!-- Crear una fila para los encabezados -->
  <tr>
    <!-- Iterar sobre las llaves del mapa -->
    <% for (let key of map.keys()) { %>
      <!-- Crear una celda de encabezado con la llave -->
      <th><%= key %></th>
    <% } %>
  </tr>
  <!-- Crear una fila para los valores -->
  <tr>
    <!-- Iterar sobre los valores del mapa -->
    <% for (let value of map.values()) { %>
      <!-- Crear una celda con el valor -->
      <td><%= value %></td>
    <% } %>
  </tr>
</table>
