Descripción General del Chatbot
El chatbot está diseñado con una matriz de 8 estados que transita entre distintas categorías como greetings (saludos), menu_inquiry (consulta de menú), menu_items (artículos del menú), entre otros. Este sistema permite una interacción fluida y natural con los usuarios.

Funcionamiento
Matriz de Transición:
- La matriz de transición define cómo el chatbot se mueve entre diferentes estados en función de la entrada del usuario. Cada estado está relacionado con una categoría específica y puede tener varias respuestas asociadas.
- Los estados son
  - Inicial (Funcional)
  - Greetings (Funcional)
  - Menu Inquiry (Funcional)
      - Mostrar el Menu
      - Que contiene x producto
      - Cuanto cuesta x producto
  - Place Order
  - Order Confirmation
  - Order Review
  - Finalize Order
  - Exit conversation

Triggers y Pesos:
- Cada categoría tiene una serie de triggers (palabras clave) que activan respuestas específicas. Cada trigger tiene un peso asignado, lo que permite que el chatbot evalúe la relevancia de la entrada del usuario. Por ejemplo, palabras como "hola" pueden tener un peso alto (100), mientras que otras como "buenos" tienen un peso menor (50).
Respuestas Dinámicas:
- Para cada conjunto de triggers, hay múltiples respuestas posibles. Esto añade un nivel de dinamismo al chatbot, haciendo que las interacciones sean menos predecibles y más conversacionales.

Consulta de Menú:
- Cuando la entrada del usuario está relacionada con el menú, el chatbot puede transitar a un estado especial. En este estado, puede extraer artículos del JSON correspondiente y ofrecer descripciones detalladas, gracias a su capacidad de buscar en múltiples archivos JSON.
Flexibilidad:
- La combinación de pesos en los triggers y la búsqueda en varios JSON permite que el chatbot se adapte a diferentes contextos de conversación, respondiendo de manera adecuada a una amplia gama de consultas.

Ejemplo de Interacción
>> Hola
Encantado de verte.

>> muestrame el menu
Estos son nuestros platos disponibles:
Big Mac - $3.99
Cuarto de Libra con Queso - $4.79
McNuggets de Pollo - $4.49
Papas Fritas Famosas - $2.29
McFlurry - $3.49
Pastelito de Manzana - $1.29

>> que venden aqui
Estos son nuestros platos disponibles:
Big Mac - $3.99
Cuarto de Libra con Queso - $4.79
McNuggets de Pollo - $4.49
Papas Fritas Famosas - $2.29
McFlurry - $3.49
Pastelito de Manzana - $1.29

>> Que ingredientes tiene la big mac
El producto contiene...
Dos hamburguesas de carne 100% pura, salsa especial, lechuga, queso, pepinillos y cebolla en un pan de sésamo.

>> que contiene el mcflurry
El producto contiene...
Una deliciosa mezcla de suave helado de vainilla con tu elección de Oreo o M&M's.

>> adios
