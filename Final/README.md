
# 🚀 Práctica Final: Mini-CRM de Eventos
### Gestión completa con CSV, Clases y Datetime

---

## 🎯 Objetivo del Proyecto

Desarrollar una **aplicación de consola en Python** que gestione clientes, eventos y ventas a partir de **ficheros CSV**. La app debe:

* Incluir un **menú de ejecución en bucle**.
* Leer y escribir **CSV** (módulo `csv`).
* Usar **tipos de datos básicos** (`str`, `int`, `float`, `bool`) y **colecciones** (`list`, `dict`, `set`, `tuple`).
* Definir al menos **una clase propia** (recomendadas: `Cliente`, `Evento`, `Venta`).
* Utilizar **datetime** para parsear fechas y calcular rangos/diferencias.

---

## 📋 Requisitos Funcionales Mínimos

| No. | Requisito | Descripción |
| :---: | :--- | :--- |
| **1.** | **Menú Principal** | Opciones: cargar CSV, listar tablas, alta de cliente, filtro de ventas por rango de fechas, métricas, exportar informe, salir. |
| **2.** | **Archivos CSV** | `clientes.csv`, `eventos.csv`, `ventas.csv` (ver formato en *starter*). |
| **3.** | **POO** | Implementar clases y métodos de utilidad (p. ej., `dias_hasta_evento()`). |
| **4.** | **Fechas** | Parsear fechas con `datetime.strptime`, calcular diferencias con `date.today()`. |
| **5.** | **Colecciones** | **Listas** para tablas, **diccionarios** índice por ID, **set** de categorías, **tuplas** para devolver resúmenes. |
| **6.** | **Gestión de Archivos** | Lectura robusta, guardado incremental y exportación de informe CSV. |

---

## ✅ Tareas Pendientes (`TODO`)

### Mínimos (Obligatorios)

* [ ] Implementar **`cargar_datos()`** para leer `clientes.csv`, `eventos.csv`, `ventas.csv`.
* [ ] Completar **`listar(tabla)`** con salidas formateadas.
* [ ] **`alta_cliente()`**: pedir datos por `input`, validar fecha (`YYYY-MM-DD`), actualizar colecciones y **guardar incrementalmente** `data/clientes.csv`.
* [ ] **`filtrar_ventas_por_rango()`**: leer dos fechas, validar, devolver/imprimir ventas entre el rango.
* [ ] **`estadisticas()`**:
    * [ ] Ingresos totales
    * [ ] Ingresos por evento (`dict`)
    * [ ] `set` de categorías existentes
    * [ ] Días hasta el evento más próximo
    * [ ] `tupla` (`min`, `max`, `media`) de precios
* [ ] **`exportar_informe()`**: crear `data/informe_resumen.csv` con totales por evento.

### Clases (Añadir Métodos)

* [ ] `Cliente.antiguedad_dias()` -> `int`
* [ ] `Evento.dias_hasta_evento()` -> `int`
* [ ] `__str__`/`__repr__` en las clases para salidas legibles

### Validaciones

* [ ] Manejo de `FileNotFoundError` en lectura.
* [ ] Validación simple de *email*.
* [ ] Evitar colisión de IDs (o generarlos automáticamente).

---

## 📦 Entregables

1.  **Código fuente** (*starter* adaptado).
2.  Carpeta `data/` con **CSV de prueba**.
3.  **`informe_resumen.csv`** generado.

---

## 📊 Evaluación (Orientativa)

| Criterio | Peso |
| :--- | :---: |
| **Menú / UX** | **15 %** |
| **Lectura/escritura CSV** | **20 %** |
| **Programación Orientada a Objetos (POO)** | **20 %** |
| **Uso de `datetime`** | **15 %** |
| **Colecciones y métricas** | **15 %** |
| **Calidad del código** | **15 %** |

---

## ✨ Sugerencias

* Implementa primero el **menú** y la **carga de datos**.
* **Aísla la E/S CSV** en funciones.
* **Documenta** con comentarios breves y nombres claros.
* *Opcional (para subir nota):* Modulariza y añade *tests* con `pytest`.
