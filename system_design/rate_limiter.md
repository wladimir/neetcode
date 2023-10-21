**DESIGN A RATE LIMITER**

Some of algorithsm: Token Bucket, Leaky Bucket, Fixed Window Counter, Sliding Window Counter.
Store in in-memory DB.
Decide on rules format.
Decide either to drop (HTTP 429 + other headers) or store and retry requests.