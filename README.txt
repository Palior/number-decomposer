Code Description
This Python script creates a graphical interface to break down a number into its units, tens, and hundreds. The user enters a number of up to three digits in a text box, and upon pressing the "Show" button, the corresponding value of each part (units, tens, and hundreds) is displayed.

Library used: Tkinter, for creating the GUI.

Main functionality: Decomposes a number with three digits or fewer, displaying its units, tens, and hundreds in labels within the window.

Program Structure
Data Entry: An Entry widget allows the user to input a number.

Calculation Functions:

calcularUnidad(): Retrieves the units part of the entered number.
calcularDecena(): Calculates the tens by subtracting the hundreds previously calculated.
calcularCentena(): Extracts the hundreds of the number.
Display Results: The function mostrar() uses the above functions to show the units, tens, and hundreds in the interface.

Validation: If the entered number is not within the range of 1 to 999, the program does not display valid results.

Requirements
Tkinter library must be installed.