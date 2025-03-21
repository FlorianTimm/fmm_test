DROP TABLE IF EXISTS netz_pgr;
DROP TABLE IF EXISTS netz_pgr_vertices_pgr;

CREATE TABLE IF NOT EXISTS netz_pgr
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

CREATE INDEX ON netz_pgr USING gist (geom);
CREATE INDEX ON netz_pgr USING btree (source);
CREATE INDEX ON netz_pgr USING btree (target);

INSERT INTO netz_pgr (geom)
SELECT (g).geom FROM (
SELECT st_dump(st_node(st_collect(geom))) g FROM netz
) t;

INSERT INTO netz_pgr (geom)
SELECT ST_REVERSE(geom) FROM netz_pgr;
	
SELECT pgr_createTopology('netz_pgr', 0.5, 'geom', clean := TRUE);

UPDATE netz_pgr SET 
	cost = ST_LENGTH(geom),
	x1 = ST_X(ST_StartPoint(geom)),
	y1 = ST_Y(ST_StartPoint(geom)),
	x2 = ST_X(ST_EndPoint(geom)),
	y2 = ST_Y(ST_EndPoint(geom));


