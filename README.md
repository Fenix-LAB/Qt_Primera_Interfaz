## Primera Interfaz de Usuario con PyQt5
#### Paso 1:
Crear un nuevo proyecto

#### Paso 2:
Diseñar la interfaz en Qt Designer
- Seleccionamos la plantilla main window
- Se colocan los widgets necesarios
- Definir los IDs de los widgets
- Guardamos el diseño dentro de nuestro proyecto

#### Paso 3:
Instalar el modulo de PyQt5 desde la terminal
```python
pip install PyQt5
```

#### Paso 4:
Correr el siguiente comando para convertir el archivo .ui a .py
```python
pyuic5 -x 'name'.ui -o 'name'.py
pyuic5 -x GUI.ui -o gui_design.py
```