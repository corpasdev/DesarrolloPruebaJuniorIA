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
