import numpy as np

def select_warm_rounds(readings: np.ndarray, threshold: float = 27.0) -> np.ndarray:
    if not np.isfinite(threshold):
        raise ValueError(f"El umbral debe de ser un numero finito valido. Threshold: {threshold}")

    if not isinstance(readings, np.ndarray) or readings.ndim !=2 or readings.shape[1] !=3:
        raise ValueError ("El arreglo debe de ser una matriz bidimensional con 3 columnas")
    
    if not np.all(np.isfinite(readings)):
        raise ValueError("El arreglo de entrada contiene valores no finitos (NaN o Inf).")


    north_temperatures = readings[:, 0]
    warm_mask = north_temperatures >= threshold

    # 5. Devuelve una copia para no compartir memoria ni modificar el arreglo original
    return readings[warm_mask].copy()