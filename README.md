# Calculadora 

Una API REST desarrollada con FastAPI que proporciona funcionalidades básicas de calculadora.

## Estructura del Proyecto

calculator/
│
├── app/
│   ├── __init__.py
│   ├── main.py           # Aplicación FastAPI (endpoints)
│   ├── schemas.py        # Modelos Pydantic (antes models.py)
│   ├── services/
│   │   ├── calculator.py # Lógica de operaciones (antes operations.py)
│   ├── utils/
│   │   ├── validators.py
│   │   ├── errors.py
│
├── tests/                # Directorio para pruebas
│   ├── test_operations.py
│
├── requirements.txt
├── README.md
└── .gitignore

## Requisitos

- Python 3.8+
- Dependencias listadas en `requirements.txt`

## Instalación

1. Clonar el repositorio 

2. Crear un entorno virtual (opcional pero recomendado)
```bash
python -m venv venv
```

3. Activar el entorno virtual, ejecuta en la consola lo siguiente 
```bash
.\venv\Scripts\activate
```

4. Instalar las dependencias
```bash
pip install -r requirements.txt
```

## Ejecución

Para iniciar la aplicación, ejecuta:
```bash
uvicorn main:app --reload
```

O también puedes usar:
```bash
python main.py
```

La API estará disponible en `http://localhost:8000`

## Documentación de la API

FastAPI genera automáticamente la documentación de la API. Puedes acceder a:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Endpoints

### 1. Suma de números

**Endpoint:** `/api/sum`  
**Método:** `POST`  
**Descripción:** Suma dos o más números.

**Ejemplo de solicitud:**
```json
{
  "numbers": [10, 15, 25, 30]
}
```

**Ejemplo de respuesta:**
```json
{
  "result": 80,
  "operation": "sum"
}
```

### 2. Operaciones avanzadas

**Endpoint:** `/api/calculate`  
**Método:** `POST`  
**Descripción:** Realiza operaciones avanzadas entre dos números.

**Operaciones disponibles:**
- `multiplication`: Multiplicación
- `division`: División (validación para evitar división por cero)
- `power`: Potencia

**Ejemplo de solicitud (Potencia):**
```json
{
  "num1": 5,
  "num2": 2,
  "operation": "power"
}
```

**Ejemplo de respuesta:**
```json
{
  "result": 25,
  "operation": "power"
}
```

**Ejemplo de solicitud (Multiplicación):**
```json
{
  "num1": 7,
  "num2": 3,
  "operation": "multiplication"
}
```

**Ejemplo de respuesta:**
```json
{
  "result": 21,
  "operation": "multiplication"
}
```

**Ejemplo de solicitud (División):**
```json
{
  "num1": 10,
  "num2": 2,
  "operation": "division"
}
```

**Ejemplo de respuesta:**
```json
{
  "result": 5,
  "operation": "division"
}
```
