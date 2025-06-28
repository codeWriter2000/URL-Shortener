SELECT original_url, created
FROM url_storage
WHERE is_active = 1
ORDER BY created DESC
LIMIT ?;