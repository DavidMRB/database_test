# 🗄️ Database Test

Este proyecto en Python simula la interacción con una base de datos, permitiendo realizar pruebas de manera local sin necesidad de una conexión real. Es ideal para desarrollar y probar funcionalidades que requieren acceso a datos, sin depender de una base de datos activa.

## 📁 Estructura del Proyecto

```
database_test/
├── db.py             # Conexión a la base de datos (simulada)
├── db_query.py       # Funciones para obtener usuarios desde la DB
├── db_simulation.py  # Datos simulados de usuarios
├── print_users.py    # Lógica para convertir datos a JSON
└── test_function.py  # Pruebas automatizadas con pytest
```

## ⚙️ Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/DavidMRB/database_test.git
   cd database_test
   ```

2. Crea un entorno virtual (opcional pero recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instala las dependencias necesarias:

   ```bash
   pip install pytest
   ```

## 🧪 Uso

### Generar JSON con datos simulados

```bash
python print_users.py
```

Este comando generará un archivo `users.json` con los datos de usuarios simulados.

### Ejecutar pruebas automatizadas

```bash
pytest test_function.py
```

Esto ejecutará las pruebas definidas en `test_function.py`, verificando el correcto funcionamiento de las funciones.

## 🧪 Pruebas con pytest

El archivo `test_function.py` contiene pruebas automatizadas utilizando `pytest`. Estas pruebas incluyen:

* Verificar que la función `returnData()` devuelve un JSON válido.
* Comprobar que los datos convertidos coinciden con los esperados.

## 📝 Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar este proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva funcionalidad'`).
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Crea un pull request describiendo tus cambios.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.
