CREATE TABLE IF NOT EXISTS radnetz.netz_pgr_neu
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

CREATE INDEX ON radnetz.netz_pgr_neu USING gist (geom);
CREATE INDEX ON radnetz.netz_pgr_neu USING btree (source);
CREATE INDEX ON radnetz.netz_pgr_neu USING btree (target);


INSERT INTO radnetz.netz_pgr_neu (id, geom, source, target)
SELECT id, geom, source, target FROM radnetz.netz_pgr_noded;

INSERT INTO radnetz.netz_pgr (id, geom, source, target)
SELECT -id, ST_REVERSE(geom), target, source FROM radnetz.netz_pgr_noded;


UPDATE radnetz.netz_pgr_neu SET 
	cost = ST_LENGTH(geom),
	x1 = ST_X(ST_StartPoint(geom)),
	y1 = ST_Y(ST_StartPoint(geom)),
	x2 = ST_X(ST_EndPoint(geom)),
	y2 = ST_Y(ST_EndPoint(geom));
