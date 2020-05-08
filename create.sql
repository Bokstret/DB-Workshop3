CREATE TABLE collection (
    projectid   INTEGER NOT NULL,
    collected   INTEGER,
    goal        INTEGER,
    currency    VARCHAR2(15 CHAR),
    launched    TIMESTAMP
);

ALTER TABLE collection ADD CONSTRAINT collection_pk PRIMARY KEY ( projectid );

CREATE TABLE project (
    projectid        INTEGER NOT NULL,
    title            VARCHAR2(50 CHAR),
    country          VARCHAR2(50 CHAR) NOT NULL,
    main_category   VARCHAR2(50 CHAR) NOT NULL
);

ALTER TABLE project ADD CONSTRAINT project_pk PRIMARY KEY ( projectid );

CREATE TABLE projectcategory (
    main_category VARCHAR2(50 CHAR) NOT NULL
);

ALTER TABLE projectcategory ADD CONSTRAINT projectcategory_pk PRIMARY KEY ( main_category );

CREATE TABLE projectcountry (
    country VARCHAR2(50 CHAR) NOT NULL
);

ALTER TABLE projectcountry ADD CONSTRAINT projectcountry_pk PRIMARY KEY ( country );

ALTER TABLE project
    ADD CONSTRAINT category_project FOREIGN KEY ( main_category )
        REFERENCES projectcategory ( main_category );

ALTER TABLE project
    ADD CONSTRAINT country_project FOREIGN KEY ( country )
        REFERENCES projectcountry ( country );

ALTER TABLE collection
    ADD CONSTRAINT project_collection FOREIGN KEY ( projectid )
        REFERENCES project ( projectid );
