SELECT 'CREATE DATABASE http_quest_test'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'http_quest_test')\gexec

SELECT 'CREATE DATABASE http_quest'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'http_quest')\gexec
