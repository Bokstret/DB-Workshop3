--------------------------------
-- Populate projectcountry table
--------------------------------
INSERT INTO projectcountry(country)
VALUES('US');

INSERT INTO projectcountry(country)
VALUES('GB');

INSERT INTO projectcountry(country)
VALUES('CA');

INSERT INTO projectcountry(country)
VALUES('AU');

INSERT INTO projectcountry(country)
VALUES('NO');

---------------------------------
-- Populate projectcategory table
---------------------------------
INSERT INTO projectcategory(main_category)
VALUES('Publishing');

INSERT INTO projectcategory(main_category)
VALUES('Film and Video');

INSERT INTO projectcategory(main_category)
VALUES('Music');

INSERT INTO projectcategory(main_category)
VALUES('Food');

INSERT INTO projectcategory(main_category)
VALUES('Design');

INSERT INTO projectcategory(main_category)
VALUES('Games');

-------------------------
-- Populate project table
-------------------------
INSERT INTO Project(projectid,title,country,main_category)
VALUES(1000002330, 'The Songs of Adelaide and Abullah', 'GB', 'Publishing');

INSERT INTO Project(projectid,title,country,main_category)
VALUES(1000004038, 'Where is Hank?', 'US', 'Film and Video');

INSERT INTO Project(projectid,title,country,main_category)
VALUES(1000007540, 'ToshiCapital Needs Help to Complete Album', 'US', 'Music');

INSERT INTO Project(projectid,title,country,main_category)
VALUES(100004721, 'Of Jesus and Madmen', 'CA', 'Publishing');

INSERT INTO Project(projectid,title,country,main_category)
VALUES(1000014025, 'Monarch Espresso Bar', 'US', 'Food');

INSERT INTO Project(projectid,title,country,main_category)
VALUES(1000232288, 'Empires at Sea', 'US', 'Games');

INSERT INTO Project(projectid,title,country,main_category)
VALUES(1000256760, 'Raise the Woof, expanding the love', 'CA', 'Design');

INSERT INTO Project(projectid,title,country,main_category)
VALUES(1000335422, 'Where is Home? Anthology', 'CA', 'Publishing');

INSERT INTO Project(projectid,title,country,main_category)
VALUES(1000190427, 'Seas of Iron', 'US', 'Games');

INSERT INTO Project(projectid,title,country,main_category)
VALUES(1000115172, 'Daily Brew Coffee', 'GB', 'Food');

INSERT INTO Project(projectid,title,country,main_category)
VALUES(1000104953, 'Rebel Army: The Story Of Major Gripes', 'GB', 'Publishing');

INSERT INTO Project(projectid,title,country,main_category)
VALUES(1000071625, 'Boco Tea', 'US', 'Food');

INSERT INTO Project(projectid,title,country,main_category)
VALUES(1000320473, 'Uncommon Rhythm Season One	', 'US', 'Film and Video');

INSERT INTO Project(projectid,title,country,main_category)
VALUES(1000542390, 'Spirits Asunder', 'GB', 'Film and Video');

INSERT INTO Project(projectid,title,country,main_category)
VALUES(1000567557, 'The Seven Rays', 'US', 'Music');
