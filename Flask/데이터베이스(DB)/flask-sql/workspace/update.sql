-- UPDATE classmate
-- SET name='강 예 원', address='제주'
-- WHERE id=4;

-- UPDATE classmate
-- SET name='박 성 주', address='제주'
-- WHERE id=4 and id=6;
-- id는 유니크한 값이라서 and는 들어갈 수 없다.

UPDATE classmate
SET name='박 성 주', address='제주'
WHERE id=4 or id=6;