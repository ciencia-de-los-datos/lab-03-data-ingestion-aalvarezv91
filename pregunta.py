import pandas as pd
import re

def ingest_data():
    with open('clusters_report.txt', 'r') as file:
        content = file.read()

    cluster_blocks = re.split(r'\n\s*\d+\s+\d+\s+[\d,]+,\d+ %', content)
    header = re.findall(r'\n\s*(\d+)\s+(\d+)\s+([\d,]+),(\d+) %', content)

    clusters = []
    cantidades = []
    porcentajes = []
    keywords = []

    for i, block in enumerate(cluster_blocks[1:]):
        cluster, cantidad, porcentaje_c, porcentaje_d = header[i]
        clusters.append(int(cluster))
        cantidades.append(int(cantidad))
        porcentajes.append(float(f"{porcentaje_c}.{porcentaje_d}"))
        keyword_text = block.strip().replace('\n', ' ')
        keywords.append(' '.join(keyword_text.split()).replace('.', ''))

    df = pd.DataFrame({
        'cluster': clusters,
        'cantidad_de_palabras_clave': cantidades,
        'porcentaje_de_palabras_clave': porcentajes,
        'principales_palabras_clave': keywords
    })

    return df
