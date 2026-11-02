"""
Conversor de Divisas (ARS a USD Oficial y Blue).

Este módulo permite pedir un monto en pesos argentinos (ARS) al usuario,
consultar la cotización en vivo desde la API pública de DolarApi
y renderizar los resultados en una tabla organizada por consola.
"""

from typing import Any, Dict, List, Optional
import requests
from tabulate import tabulate

API_URL: str = "https://dolarapi.com/v1/dolares"
CASAS_DE_INTERES: tuple[str, ...] = ("oficial", "blue")


def obtener_cotizaciones(url: str) -> List[Dict[str, Any]]:
    """
    Realiza una petición HTTP GET a la API enviada para obtener las cotizaciones.

    Args:
        url (str): Endpoint de la API pública.

    Returns:
        List[Dict[str, Any]]: Lista de diccionarios con la información
        de cada tipo de dólar.

    Raises:
        requests.exceptions.RequestException: Si ocurre un error de red o la API
        devuelve un código de estado fallido.
    """
    response = requests.get(url, timeout=10)
    response.raise_for_status()  # Lanza HTTPError si el status code no es 200
    datos: List[Dict[str, Any]] = response.json()
    return datos


def solicitar_monto_ars() -> float:
    """
    Solicita al usuario ingresar un monto en pesos argentinos mediante consola,
    validando que sea un número flotante mayor a cero.

    Returns:
        float: Monto válido ingresado en ARS.
    """
    while True:
        entrada = input("Ingrese el monto en Pesos Argentinos (ARS): ").strip()
        try:
            monto = float(entrada)
            if monto <= 0:
                print("❌ El monto debe ser un valor positivo mayor a cero.")
                continue
            return monto
        except ValueError:
            print("❌ Entrada inválida. Ingrese un número válido (ej: 15000 o 15000.50).")


def procesar_cotizaciones(
    cotizaciones: List[Dict[str, Any]], monto_ars: float
) -> List[List[Any]]:
    """
    Filtra las cotizaciones de interés (oficial y blue), calcula el monto
    convertido en base al precio de venta y formatea la estructura para la tabla.

    Args:
        cotizaciones (List[Dict[str, Any]]): Lista de cotizaciones obtenida de la API.
        monto_ars (float): Monto en pesos argentinos a convertir.

    Returns:
        List[List[Any]]: Filas preparadas para ser renderizadas por tabulate.
    """
    filas_tabla: List[List[Any]] = []

    for item in cotizaciones:
        casa = item.get("casa", "").lower()
        if casa in CASAS_DE_INTERES:
            nombre: str = item.get("nombre", casa.capitalize())
            compra: Optional[float] = item.get("compra")
            venta: Optional[float] = item.get("venta")

            if venta and venta > 0:
                total_usd = monto_ars / venta
                total_usd_fmt = f"USD {total_usd:,.2f}"
            else:
                total_usd_fmt = "N/D"

            compra_fmt = f"${compra:,.2f}" if compra else "N/D"
            venta_fmt = f"${venta:,.2f}" if venta else "N/D"

            filas_tabla.append([nombre, compra_fmt, venta_fmt, total_usd_fmt])

    return filas_tabla


def main() -> None:
    """
    Función principal que coordina el flujo de la aplicación.
    """
    print("============================================")
    print("   CONVERSOR DE DIVISAS (COTIZACIÓN EN VIVO)")
    print("============================================\n")

    monto_ars = solicitar_monto_ars()

    print("\n⏳ Consultando cotizaciones en vivo...")
    try:
        cotizaciones = obtener_cotizaciones(API_URL)
        filas = procesar_cotizaciones(cotizaciones, monto_ars)

        if not filas:
            print("⚠️ No se encontraron las cotizaciones requeridas (oficial/blue).")
            return

        encabezados = ["Cotización", "Compra", "Venta", "Total Convertido"]

        print(f"\n📊 Resultado para ${monto_ars:,.2f} ARS:\n")
        print(tabulate(filas, headers=encabezados, tablefmt="fancy_grid"))

    except requests.exceptions.ConnectionError:
        print("\n❌ Error de conexión: Comprobá tu acceso a internet.")
    except requests.exceptions.Timeout:
        print("\n❌ Error: La solicitud a la API expiró. Intentá nuevamente.")
    except requests.exceptions.HTTPError as err:
        print(f"\n❌ Error en la API (Respuesta del servidor): {err}")
    except Exception as err:
        print(f"\n❌ Ocurrió un error inesperado: {err}")


if __name__ == "__main__":
    main()