"""
Ejercicio 1: Pseudocódigo y lógica
Ordenar tickets de soporte por prioridad (Alta > Media > Baja) y fecha (más antiguo primero)
Incluye manejo de empates y explicación de la complejidad del algoritmo
"""

from enum import Enum
from datetime import datetime
from typing import List, Dict, Any


class Prioridad(Enum):
    """Enum para representar los niveles de prioridad de los tickets."""
    ALTA = 3
    MEDIA = 2
    BAJA = 1


class Ticket:
    """Clase para representar un ticket de soporte."""
    
    def __init__(self, id: int, titulo: str, prioridad: Prioridad, fecha: datetime):
        """
        Inicializa un nuevo ticket de soporte.
        
        Args:
            id: Identificador único del ticket
            titulo: Título descriptivo del ticket
            prioridad: Nivel de prioridad del ticket (ALTA, MEDIA, BAJA)
            fecha: Fecha de creación del ticket
        """
        self.id = id
        self.titulo = titulo
        self.prioridad = prioridad
        self.fecha = fecha
    
    def __str__(self) -> str:
        """Representación en string del ticket."""
        return f"Ticket #{self.id}: {self.titulo} - Prioridad: {self.prioridad.name}, Fecha: {self.fecha.strftime('%Y-%m-%d %H:%M')}"


def ordenar_tickets(tickets: List[Ticket]) -> List[Ticket]:
    """
    Ordena una lista de tickets por prioridad (Alta > Media > Baja) y fecha (más antiguo primero).
    
    Args:
        tickets: Lista de tickets a ordenar
    
    Returns:
        Lista ordenada de tickets
    
    Complejidad:
        - Tiempo: O(n log n) donde n es el número de tickets
        - Espacio: O(n) para almacenar la lista ordenada
    """
    # Utilizamos el método sort con una función lambda como clave de ordenamiento
    # El signo negativo en la prioridad.value es para ordenar de mayor a menor prioridad
    # La fecha se ordena de forma ascendente (más antiguo primero)
    tickets_ordenados = sorted(tickets, key=lambda t: (-t.prioridad.value, t.fecha))
    return tickets_ordenados


def mostrar_ejemplo():
    """Muestra un ejemplo de uso del algoritmo de ordenamiento."""
    # Crear algunos tickets de ejemplo
    tickets = [
        Ticket(1, "Error en la base de datos", Prioridad.ALTA, datetime(2023, 5, 10, 9, 30)),
        Ticket(2, "Problema de inicio de sesión", Prioridad.MEDIA, datetime(2023, 5, 9, 14, 15)),
        Ticket(3, "Actualización de documentación", Prioridad.BAJA, datetime(2023, 5, 8, 11, 0)),
        Ticket(4, "Servidor caído", Prioridad.ALTA, datetime(2023, 5, 11, 8, 45)),
        Ticket(5, "Error en formulario de contacto", Prioridad.MEDIA, datetime(2023, 5, 9, 10, 20)),
        # Ticket con la misma prioridad y fecha diferente para mostrar manejo de empates
        Ticket(6, "Problema de rendimiento", Prioridad.ALTA, datetime(2023, 5, 10, 10, 15)),
    ]
    
    print("Tickets originales:")
    for ticket in tickets:
        print(ticket)
    
    tickets_ordenados = ordenar_tickets(tickets)
    
    print("\nTickets ordenados por prioridad y fecha:")
    for ticket in tickets_ordenados:
        print(ticket)


"""
Explicación de la complejidad del algoritmo:

1. Complejidad temporal: O(n log n)
   - El algoritmo utiliza la función sorted() de Python, que implementa Timsort con complejidad O(n log n)
   - La comparación de cada elemento (función key) tiene complejidad O(1)
   - Por lo tanto, la complejidad total es O(n log n)

2. Complejidad espacial: O(n)
   - Se crea una nueva lista ordenada, que requiere O(n) espacio adicional
   - No se requiere espacio adicional significativo más allá de la lista de salida

3. Manejo de empates:
   - Los empates en prioridad se resuelven automáticamente comparando las fechas
   - Si dos tickets tienen la misma prioridad, se ordena por fecha (más antiguo primero)
   - Este comportamiento está garantizado por la tupla (-t.prioridad.value, t.fecha) en la clave de ordenamiento

4. Estabilidad:
   - El algoritmo es estable, lo que significa que mantiene el orden relativo de elementos con valores iguales
   - Esto es importante para garantizar que los tickets con la misma prioridad y fecha mantengan su orden original
"""


if __name__ == "__main__":
    mostrar_ejemplo()
