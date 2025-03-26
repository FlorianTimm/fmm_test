# Versuch FastMapMatching

GitHub: [https://github.com/cyang-kth/fmm/tree/master]()

Ziel: Nutzung von MapMatching um Fachdaten mit anderer Netzgrundlage auf ein bestehendes Netz zu matchen

## Daten aufbereiten

### Netz

- Daten in Postgres importieren als Tabelle `netz` mit Attribut `geom`
- Aufbereitung zu einem Netz mittels netz.sql
- Export zu netz.shp

### Routen

- Falls keine realen GPS-Tracks
  - QGIS: Stützpunkte alle 50m (Punkte entlang einer Geometrie)
  - Punkte zu Weg
- Linien dürfen keine Unterbrechungen haben (LineString)

## MapMatching

### Dockerimage

```
docker build -f Dockerfile . -t fmm_test
```

### Terminal in Docker öffnen

Weiterleiten des aktuellen Ordners und des Port 8888 (ggf. Jupyter)

```
docker run -i -p 8888:8888 -v ./:/folder -t fmm_test /bin/bash
```

## Visualisierung im GIS

- `netz.shp` zu QGIS hinzufügen
- `candidates.csv` einladen
- Netz mit candidates.csv verknüpfen (id = eid)
- Filter erstellen (virtueller Layer) auf `"candidates_source" IS NOT NULL`

## ToDo

- [ ] Automatisierung der Datenaufbereitung
- [ ] Python 3 nutzen
- [ ] Jupyter-Server
