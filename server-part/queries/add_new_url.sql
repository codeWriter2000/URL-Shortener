INSERT INTO url_storage (
    original_url,
    short_token,
    created,
    is_active
)
VALUES (
    ?, -- original_url
    ?, -- short_token
    ?, -- created
    1 -- is_active
);