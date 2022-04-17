CREATE TABLE articles (
  title TEXT NOT NULL,
  content TEXT NOT NULL
);

INSERT INTO articles 
VALUES ('1번제목', '1번내용');

-- 테이블 이름 변경
ALTER TABLE articles
RENAME TO news;

-- 새로운 컬럼 추가
ALTER TABLE news
ADD COLUMN created_at TEXT NOT NULL;

-- 1. NOT NULL 설정 없이 추가하기
ALTER TABLE news 
ADD COLUMN created_at TEXT;

INSERT INTO news 
VALUES ('제목', '내용', datetime('now'));

-- 2. 기본 값 설정해서 추가하기
ALTER TABLE news
ADD COLUMN subtitle TEXT NOT NULL
DEFAULT '소제목';

-- new in 3.25
ALTER TABLE news
RENAME COLUMN title TO main_title;

-- new in 3.35
ALTER TABLE news
DROP COLUMN subtitle;
