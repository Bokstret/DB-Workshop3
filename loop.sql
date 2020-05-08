DECLARE
    TYPE INTS IS VARRAY(15) OF collection.goal%TYPE;
    TYPE CHARS IS VARRAY(15) OF collection.currency%TYPE;
   
    
    Projectid INTS;
    Collected INTS;
    Goal INTS;
    Currency CHARS;
    
BEGIN
    Projectid := INTS(1000002330,1000004038,1000007540,100004721,1000014025,1000232288,1000256760,1000335422,1000190427,1000115172,1000104953,1000071625,1000320473,1000542390,1000567557);
    Collected := INTS(0, 220,1283,0,52375,37199,700,4944,8105,21,112,1781,10410,5,260);
    Goal := INTS(1000, 45000,19500,2500,50000,25000,15000,4000,3000,3500,100,5000,29700,500,3000);
    Currency := CHARS('GBP','USD','USD','CAD','USD','USD','CAD','CAD','USD','GBP','GBP','USD','USD','GBP','USD');
    
    FOR i IN 1 .. Projectid.count
    LOOP
        INSERT INTO collection (projectid,collected,goal,currency) VALUES (Projectid(i), Collected(i), Goal(i), Currency(i));
        COMMIT;
    END LOOP;
END;
