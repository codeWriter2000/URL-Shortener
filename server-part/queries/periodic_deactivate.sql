UPDATE url_storage
SET is_active = 0
WHERE replace(created, 'T', ' ') < DATETIME('now', '-7 days')
    AND is_active = 1;
