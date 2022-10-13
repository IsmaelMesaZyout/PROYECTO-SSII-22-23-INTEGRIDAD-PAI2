import aperturaBaseDatos

def run_query(query=''):    
    cursor = aperturaBaseDatos.conexion.cursor()
    cursor.execute(query)          # Ejecutar una consulta 
    if query.upper().startswith('SELECT'): 
        data = cursor.fetchall()   # Traer los resultados de un select 
    else:               # Hacer efectiva la escritura de datos 
        data = None
    return data

def sel():
    val1 = "SELECT * FROM tablepai2"
    val1 = run_query(val1) 
    return val1