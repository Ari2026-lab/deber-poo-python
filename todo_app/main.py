"""Programa principal - Interfaz del Gestor de Tareas."""

from gestor_tareas import GestorTareas
import os
import sys
from datetime import datetime

class InterfazTareas:
    """Clase que proporciona la interfaz de usuario para el gestor de tareas."""
    
    def __init__(self):
        """Inicializa la interfaz."""
        self.gestor = GestorTareas("data/tareas.json")
        self.ejecutando = True
    
    def limpiar_pantalla(self):
        """Limpia la pantalla de la consola."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def mostrar_encabezado(self):
        """Muestra el encabezado de la aplicación."""
        print("\n" + "="*50)
        print("║  GESTOR DE TAREAS - TO-DO LIST  ║")
        print("="*50)
    
    def mostrar_menu(self):
        """Muestra el menú principal."""
        self.mostrar_encabezado()
        stats = self.gestor.obtener_estadisticas()
        print(f"\n📊 Estadísticas: {stats['completadas']}/{stats['total']} completadas ")
        print(f"   Progreso: {stats['porcentaje_completado']}%")
        print("\n" + "-"*50)
        print("1.  Ver todas las tareas")
        print("2.  Ver tareas pendientes")
        print("3.  Ver tareas completadas")
        print("4.  Crear nueva tarea")
        print("5.  Marcar tarea como completada")
        print("6.  Editar tarea")
        print("7.  Eliminar tarea")
        print("8.  Limpiar pantalla")
        print("9.  Salir")
        print("-"*50)
    
    def mostrar_tareas(self, tareas, titulo=""):
        """Muestra una lista de tareas en formato tabular.
        
        Args:
            tareas: Lista de tareas a mostrar
            titulo: Título de la sección
        """
        if titulo:
            print(f"\n{titulo}")
            print("-"*60)
        
        if not tareas:
            print("❌ No hay tareas para mostrar\n")
            return
        
        # Encabezados
        print(f"{'ID':<5} {'Estado':<12} {'Título':<25} {'Vencimiento':<15}")
        print("-"*60)
        
        # Tareas
        for tarea in tareas:
            estado = "✓ Completada" if tarea.completada else "○ Pendiente"
            vencimiento = tarea.fecha_vencimiento if tarea.fecha_vencimiento else "Sin fecha"
            titulo_corto = tarea.titulo[:22] + "..." if len(tarea.titulo) > 25 else tarea.titulo
            print(f"{tarea.id:<5} {estado:<12} {titulo_corto:<25} {vencimiento:<15}")
        
        print("-"*60)
        if titulo == "":
            print(f"Total: {len(tareas)} tareas\n")
    
    def ver_tareas(self):
        """Muestra todas las tareas."""
        self.limpiar_pantalla()
        self.mostrar_encabezado()
        tareas = self.gestor.obtener_tareas()
        self.mostrar_tareas(tareas, "\n📋 TODAS LAS TAREAS")
    
    def ver_tareas_pendientes(self):
        """Muestra solo las tareas pendientes."""
        self.limpiar_pantalla()
        self.mostrar_encabezado()
        tareas = self.gestor.obtener_tareas_pendientes()
        self.mostrar_tareas(tareas, "\n⏳ TAREAS PENDIENTES")
    
    def ver_tareas_completadas(self):
        """Muestra solo las tareas completadas."""
        self.limpiar_pantalla()
        self.mostrar_encabezado()
        tareas = self.gestor.obtener_tareas_completadas()
        self.mostrar_tareas(tareas, "\n✅ TAREAS COMPLETADAS")
    
    def crear_tarea(self):
        """Crea una nueva tarea."""
        self.limpiar_pantalla()
        self.mostrar_encabezado()
        print("\n➕ CREAR NUEVA TAREA")
        print("-"*50)
        
        try:
            titulo = input("Título de la tarea: ").strip()
            if not titulo:
                print("❌ El título no puede estar vacío")
                return
            
            descripcion = input("Descripción (opcional): ").strip()
            vencimiento = input("Fecha de vencimiento (YYYY-MM-DD, opcional): ").strip()
            
            # Validar formato de fecha si se proporciona
            if vencimiento:
                try:
                    datetime.strptime(vencimiento, "%Y-%m-%d")
                except ValueError:
                    print("❌ Formato de fecha inválido. Use YYYY-MM-DD")
                    return
            
            tarea = self.gestor.agregar_tarea(titulo, descripcion, vencimiento)
            print(f"\n✅ Tarea creada exitosamente")
            print(f"   ID: {tarea.id}")
            print(f"   Título: {tarea.titulo}")
            if descripcion:
                print(f"   Descripción: {descripcion}")
            if vencimiento:
                print(f"   Vencimiento: {vencimiento}")
        
        except Exception as e:
            print(f"❌ Error al crear tarea: {e}")
    
    def marcar_completada(self):
        """Marca una tarea como completada."""
        self.limpiar_pantalla()
        self.mostrar_encabezado()
        print("\n✓ MARCAR TAREA COMO COMPLETADA")
        print("-"*50)
        
        try:
            id_tarea = int(input("ID de la tarea: "))
            tarea = self.gestor.obtener_tarea_por_id(id_tarea)
            
            if not tarea:
                print("❌ Tarea no encontrada")
                return
            
            if self.gestor.togglear_estado(id_tarea):
                estado = "✓ Completada" if tarea.completada else "○ Pendiente"
                print(f"✅ Estado actualizado a: {estado}")
            else:
                print("❌ Error al actualizar la tarea")
        
        except ValueError:
            print("❌ ID inválido")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def editar_tarea(self):
        """Edita una tarea existente."""
        self.limpiar_pantalla()
        self.mostrar_encabezado()
        print("\n✏️  EDITAR TAREA")
        print("-"*50)
        
        try:
            id_tarea = int(input("ID de la tarea a editar: "))
            tarea = self.gestor.obtener_tarea_por_id(id_tarea)
            
            if not tarea:
                print("❌ Tarea no encontrada")
                return
            
            print(f"\nTarea actual: {tarea.titulo}")
            print(f"Descripción: {tarea.descripcion}")
            
            nuevo_titulo = input("\nNuevo título (Enter para mantener): ").strip()
            nueva_descripcion = input("Nueva descripción (Enter para mantener): ").strip()
            nueva_fecha = input("Nueva fecha de vencimiento (Enter para mantener): ").strip()
            
            # Validar fecha si se proporciona
            if nueva_fecha:
                try:
                    datetime.strptime(nueva_fecha, "%Y-%m-%d")
                except ValueError:
                    print("❌ Formato de fecha inválido. Use YYYY-MM-DD")
                    return
            
            if self.gestor.actualizar_tarea(
                id_tarea,
                nuevo_titulo if nuevo_titulo else None,
                nueva_descripcion if nueva_descripcion else None,
                nueva_fecha if nueva_fecha else None
            ):
                print("\n✅ Tarea actualizada exitosamente")
            else:
                print("❌ Error al actualizar la tarea")
        
        except ValueError:
            print("❌ ID inválido")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def eliminar_tarea(self):
        """Elimina una tarea."""
        self.limpiar_pantalla()
        self.mostrar_encabezado()
        print("\n🗑️  ELIMINAR TAREA")
        print("-"*50)
        
        try:
            id_tarea = int(input("ID de la tarea a eliminar: "))
            tarea = self.gestor.obtener_tarea_por_id(id_tarea)
            
            if not tarea:
                print("❌ Tarea no encontrada")
                return
            
            print(f"\nTarea a eliminar: {tarea.titulo}")
            confirmacion = input("¿Estás seguro? (s/n): ").lower().strip()
            
            if confirmacion == 's':
                if self.gestor.eliminar_tarea(id_tarea):
                    print("✅ Tarea eliminada exitosamente")
                else:
                    print("❌ Error al eliminar la tarea")
            else:
                print("❌ Operación cancelada")
        
        except ValueError:
            print("❌ ID inválido")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def ejecutar(self):
        """Ejecuta la interfaz principal."""
        while self.ejecutando:
            self.mostrar_menu()
            
            try:
                opcion = input("\nSelecciona una opción (1-9): ").strip()
                
                if opcion == '1':
                    self.ver_tareas()
                elif opcion == '2':
                    self.ver_tareas_pendientes()
                elif opcion == '3':
                    self.ver_tareas_completadas()
                elif opcion == '4':
                    self.crear_tarea()
                elif opcion == '5':
                    self.marcar_completada()
                elif opcion == '6':
                    self.editar_tarea()
                elif opcion == '7':
                    self.eliminar_tarea()
                elif opcion == '8':
                    self.limpiar_pantalla()
                elif opcion == '9':
                    print("\n👋 ¡Hasta luego! Tareas guardadas automáticamente.")
                    self.ejecutando = False
                else:
                    print("❌ Opción inválida. Intenta de nuevo.")
                
                if self.ejecutando and opcion in ['1', '2', '3', '4', '5', '6', '7']:
                    input("\n✋ Presiona Enter para continuar...")
            
            except KeyboardInterrupt:
                print("\n\n⚠️  Programa interrumpido por el usuario")
                self.ejecutando = False
            except Exception as e:
                print(f"❌ Error inesperado: {e}")
                input("\n✋ Presiona Enter para continuar...")


if __name__ == "__main__":
    interfaz = InterfazTareas()
    interfaz.ejecutar()