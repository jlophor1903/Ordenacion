# Ordenación. Algoritmos básicos 
Repositorio para profundizar en python estudiando cón ordenar un lista
Autor; Yo mismo
Fecha: Hoy
Organización: IES José de Mora

## Algoritmos:
Para cambiar de orden dos datos se usa una variable auxiliar, de modo que almacenamos
el primer dato de la lista en ella, y luego el segundo dato en el espacio del 
primero, para terminar volcando la variable auxiliar en el segundo dato. Esto se 
conoce como "intercambio" o "swap"

Para tres datos hay q hacer ```swap()``` con el primer y segundo dato, después con
el segundo y tercero, y finalmente otra vez con el primero y segundo

Existen varios algoritmos para ordenar. Los más sencillos son los de **burbuja** 
(es el que hemos hecho) y los de **insercción**. Pero se suele usar más el de 
**dividir y mexclar**, por ser habitualmente más rápido.

## Otros aprendizajes
1. Introducir datos con el terminal
Todos los aprendizajes de programación van introduciendo dificultades de manera
 progresiva. Primero se aprende a sacar datos por pantalla, y después a introducirlos
  mediante un teclado, desde el programa de consola (*Terminal*). Después se utilizan
 otros mecanismos más difíciles(*Interfaces de usuario*).
1. Documentar los proyectos
Hay al menos dos sistemas básicos: documentación *inline*, que explica cada fragmento 
del código y encabeza fragmentos dentro de los archivos, y encabeza fragmentos dentro
de los archivos de texto específicos para ello (como este que nos ocupa).
1. Manejar una GUI básica (pygame-widgets y ipywidgets).
Hay múltiples bibliotecas de funciones para casi cualquier lenguaje, que nos permiten
crear una interfaz de usuario para introducir y visualizar datos.