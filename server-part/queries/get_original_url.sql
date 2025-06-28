SELECT original_url
FROM url_storage
WHERE is_active = 1 AND short_token = ?;