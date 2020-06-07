Tracking file by folder pattern:  migrations
BEGIN;
--
-- Create model EnvExposure
--
CREATE TABLE "fdn_participant_envexposure" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "exposure_name" varchar(1000) NOT NULL);
--
-- Create model GeneMutation
--
CREATE TABLE "fdn_participant_genemutation" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "gene_name" varchar(1000) NOT NULL);
--
-- Create model Participant
--
CREATE TABLE "fdn_participant_participant" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(255) NOT NULL, "age" integer unsigned NOT NULL CHECK ("age" >= 0), "has_siblings" bool NOT NULL, "reviewed_status" varchar(255) NOT NULL);
CREATE TABLE "fdn_participant_participant_env_exposures" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "participant_id" integer NOT NULL REFERENCES "fdn_participant_participant" ("id") DEFERRABLE INITIALLY DEFERRED, "envexposure_id" integer NOT NULL REFERENCES "fdn_participant_envexposure" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE "fdn_participant_participant_gene_mutations" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "participant_id" integer NOT NULL REFERENCES "fdn_participant_participant" ("id") DEFERRABLE INITIALLY DEFERRED, "genemutation_id" integer NOT NULL REFERENCES "fdn_participant_genemutation" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE UNIQUE INDEX "fdn_participant_participant_env_exposures_participant_id_envexposure_id_6c79421d_uniq" ON "fdn_participant_participant_env_exposures" ("participant_id", "envexposure_id");
CREATE INDEX "fdn_participant_participant_env_exposures_participant_id_0395d428" ON "fdn_participant_participant_env_exposures" ("participant_id");
CREATE INDEX "fdn_participant_participant_env_exposures_envexposure_id_1a488346" ON "fdn_participant_participant_env_exposures" ("envexposure_id");
CREATE UNIQUE INDEX "fdn_participant_participant_gene_mutations_participant_id_genemutation_id_ed69adbb_uniq" ON "fdn_participant_participant_gene_mutations" ("participant_id", "genemutation_id");
CREATE INDEX "fdn_participant_participant_gene_mutations_participant_id_f2e76286" ON "fdn_participant_participant_gene_mutations" ("participant_id");
CREATE INDEX "fdn_participant_participant_gene_mutations_genemutation_id_740363b2" ON "fdn_participant_participant_gene_mutations" ("genemutation_id");
COMMIT;