# Ejercicio 2: Diagrama de Flujo - Proceso de Aprobación de Facturas
## Diagrama de Flujo

![Diagrama de Flujo de Aprobación de Facturas](https://github.com/corpasdev/DesarrolloPruebaJuniorIA/blob/main/imagen-diagrama-flujo2/diagram-flujo2.jpeg)

## Descripción del Proceso

Este diagrama representa el flujo de trabajo para la aprobación de facturas, que incluye los siguientes pasos:

1. **Recepción**: Llega un email con factura adjunta
2. **Extracción y Validación**: Se extrae el adjunto y se valida el formato
3. **Verificación de Formato**:
   - Si el formato NO es válido → Se notifica al remitente y termina el proceso
   - Si el formato SÍ es válido → Continúa el proceso
4. **Primera Aprobación**: Se envía al "Aprobador 1"
   - Si rechaza → Se notifica al remitente y termina el proceso
   - Si aprueba → Continúa el proceso
5. **Segunda Aprobación**: Se envía al "Aprobador 2"
   - Si rechaza → Se notifica al solicitante y termina el proceso
   - Si aprueba → Factura aprobada y finaliza el proceso

## Componentes del Diagrama

El diagrama utiliza símbolos estándar de diagramas de flujo:
- **Óvalos**: Representan el inicio y fin del proceso
- **Rectángulos**: Representan acciones o actividades
- **Rombos**: Representan decisiones con múltiples caminos posibles
- **Flechas**: Indican la dirección del flujo y conectan los diferentes elementos



## Notas Adicionales

- El proceso incluye múltiples puntos de verificación para garantizar la validez y aprobación de las facturas
- Existen tres posibles puntos de finalización del proceso:
  1. Rechazo por formato inválido
  2. Rechazo por el Aprobador 1
  3. Rechazo por el Aprobador 2
  4. Aprobación completa (éxito del proceso)

# Ejercicio 3: Aplicación práctica de IA

## a) Aprendizaje Supervisado vs No Supervisado

**Aprendizaje Supervisado:**
- **Definición:** Entrena modelos usando datos etiquetados donde se conoce la respuesta correcta.
- **Ejemplo:** Filtro de spam en email, donde el modelo aprende de emails previamente clasificados como "spam" o "no spam".

**Aprendizaje No Supervisado:**
- **Definición:** Entrena modelos con datos sin etiquetar para encontrar patrones o estructuras ocultas.
- **Ejemplo:** Segmentación de clientes por comportamiento de compra, agrupando perfiles similares sin categorías predefinidas.

## b) Pasos para entrenar un Clasificador de Sentimiento

```python
# 1. Recolectar y limpiar datos
datos = cargar_reseñas("dataset.csv")
datos_limpios = eliminar_stopwords(normalizar_texto(datos))

# 2. Extraer características
vectorizador = TF_IDF_Vectorizer()
X = vectorizador.transformar(datos_limpios.texto)
y = datos_limpios.sentimiento  # positivo/negativo/neutral

# 3. Entrenar modelo
modelo = RegresionLogistica()
modelo.entrenar(X_entrenamiento, y_entrenamiento)

# 4. Evaluar modelo
predicciones = modelo.predecir(X_prueba)
precision = calcular_metricas(y_prueba, predicciones)

# 5. Desplegar
guardar_modelo(modelo, "modelo_sentimiento.pkl")
```

## c) Llamada a API de IA para extraer sentimiento

```json
// Solicitud a API de análisis de sentimiento (ej. Azure Text Analytics)
{
  "method": "POST",
  "url": "https://api.cognitive.microsoft.com/text/analytics/v3.0/sentiment",
  "headers": {
    "Content-Type": "application/json",
    "Ocp-Apim-Subscription-Key": "tu_clave_api"
  },
  "body": {
    "documents": [
      {
        "id": "1",
        "language": "es",
        "text": "La entrega llegó tarde, pero el servicio al cliente fue excelente."
      }
    ]
  }
}

// Respuesta
{
  "documents": [
    {
      "id": "1",
      "sentiment": "mixed",
      "confidenceScores": {
        "positive": 0.65,
        "neutral": 0.20,
        "negative": 0.15
      },
      "sentences": [
        {
          "text": "La entrega llegó tarde",
          "sentiment": "negative",
          "confidenceScores": {
            "positive": 0.05,
            "neutral": 0.25,
            "negative": 0.70
          }
        },
        {
          "text": "pero el servicio al cliente fue excelente",
          "sentiment": "positive",
          "confidenceScores": {
            "positive": 0.90,
            "neutral": 0.08,
            "negative": 0.02
          }
        }
      ]
    }
  ]
}
```
