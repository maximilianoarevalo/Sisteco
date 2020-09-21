Funcionamiento del cifrado Playfair implementado en Python:

- Al ejecutar el script se desplegará un menu en el que se debe ingresar un número para realizar la opción deseada
- En caso de presionar 1 se solicitará ingresar la llave para la encriptación y luego el mensaje a encriptar
- En caso de presionar 2 se solicitará ingresar la llave para la desencriptación y luego el mensaje a desencriptar
- En caso de presionar 3 se terminará con la ejecución del programa
- En caso de querer realizar otra acción luego de haber terminado una, es necesario ejecutar nuevamente el script
- Es importante señalar que luego de encriptar o desencriptar, se mostrará por consola el mensaje ingresado junto con la encriptación
Playfair utilizando la llave indicada
- Además, se muestra el tiempo de encriptación o desencriptación en segundos junto con el throughput de la acción realizada
- También se desplega un gráfico que muestra el throughput v/s el tamaño del bloque de encriptación

Nota: 
- Debido a la naturaleza del cifrado Playfair, se solicita no ingresar números ni caracteres especiales para la llave ni para el mensaje
- El bloque es de tamaño 16, ya que agrupa de a pares de caracteres por lo que no es posible modificar este valor ya que afectaría el proceso
de encriptación y desencriptación. El cual está basado en el cifrado Playfair original.