import time

def mesurer_temps_execution(fonction, *args, **kwargs):
    debut = time.time()
    resultat = fonction(*args, **kwargs)
    fin = time.time()
    temps_execution = (fin - debut) * 1000  # Convertir en millisecondes
    return resultat, temps_execution