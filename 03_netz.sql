SELECT pgr_createTopology('radnetz.netz_pgr_noded', 10, 'geom', clean := TRUE);
SELECT pgr_analyzeGraph('radnetz.netz_pgr_noded',10,'geom');


UPDATE radnetz.netz_pgr_noded SET geom = ST_ADDPOINT(geom, (SELECT the_geom FROM radnetz.netz_pgr_noded_vertices_pgr p WHERE source = p.id), 0);
UPDATE radnetz.netz_pgr_noded SET geom = ST_ADDPOINT(geom, (SELECT the_geom FROM radnetz.netz_pgr_noded_vertices_pgr p WHERE target = p.id), -1);


UPDATE radnetz.netz_pgr_noded SET geom = ST_SimplifyPreserveTopology(geom, 1);