Descripción del código
Este script en Python crea una interfaz gráfica para descomponer un número en sus unidades, decenas y centenas. 
El usuario ingresa un número de hasta tres dígitos en un cuadro de texto, y al presionar el botón "Mostrar", se despliega el valor correspondiente de cada parte (unidad, decena y centena).

Librería utilizada: Tkinter, para la creación de la GUI.

Funcionalidad principal: Desglosa un número de tres dígitos o menos, mostrando su unidad, decena y centena en etiquetas dentro de la ventana.

Estructura del programa


	Entrada de datos: Se usa un Entry para que el usuario ingrese un número.

	Funciones de cálculo:

		calcularUnidad(): Obtiene la unidad del número ingresado.
		calcularDecena(): Calcula la decena restando la centena previamente calculada.
		calcularCentena(): Extrae la centena del número.

	Mostrar resultados: La función mostrar() utiliza las funciones anteriores para mostrar las unidades, decenas y centenas en la interfaz.

	Validación: Si el número ingresado no está en el rango de 1 a 999, el programa no muestra resultados válidos.

Requisitos
Tener instalada la librería Tkinter