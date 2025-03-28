DROP TABLE IF EXISTS radnetz.netz_pgr;
DROP TABLE IF EXISTS radnetz.netz_pgr_vertices_pgr;

CREATE TABLE IF NOT EXISTS radnetz.netz_pgr
(
    id SERIAL NOT NULL PRIMARY KEY,
    geom geometry(LINESTRING, 25832) NOT NULL,
    status text,
    source integer,
    target integer,
	cost decimal,
	x1 decimal,
	y1 decimal,
	x2 decimal,
	y2 decimal
);

CREATE INDEX ON radnetz.netz_pgr USING gist (geom);
CREATE INDEX ON radnetz.netz_pgr USING btree (source);
CREATE INDEX ON radnetz.netz_pgr USING btree (target);

INSERT INTO radnetz.netz_pgr (geom)
SELECT (g).geom FROM (
select st_dump(st_node(st_collect(
--st_lineextend(
(g).geom
--,20,20)
))) g from (
SELECT st_dump(st_linemerge(st_collect(geom))) g FROM radnetz.radnetz
));
	
SELECT pgr_createTopology('radnetz.netz_pgr', 10, 'geom', clean := TRUE);


SELECT  pgr_nodeNetwork('radnetz.netz_pgr',10,the_geom=>'geom');

SELECT pgr_createTopology('radnetz.netz_pgr_noded', 10, 'geom');
SELECT  pgr_analyzeGraph('radnetz.netz_pgr_noded',10,'geom');


UPDATE radnetz.netz_pgr_noded SET geom = ST_ADDPOINT(geom, (SELECT the_geom FROM radnetz.netz_pgr_noded_vertices_pgr p WHERE source = p.id), 0);
UPDATE radnetz.netz_pgr_noded SET geom = ST_ADDPOINT(geom, (SELECT the_geom FROM radnetz.netz_pgr_noded_vertices_pgr p WHERE target = p.id), -1);







UPDATE radnetz.netz_pgr SET 
	cost = ST_LENGTH(geom),
	x1 = ST_X(ST_StartPoint(geom)),
	y1 = ST_Y(ST_StartPoint(geom)),
	x2 = ST_X(ST_EndPoint(geom)),
	y2 = ST_Y(ST_EndPoint(geom));

	
--INSERT INTO radnetz.netz_pgr (geom)
--SELECT ST_REVERSE(geom) FROM radnetz.netz_pgr;


