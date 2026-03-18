"""Copyright (c) 2025 DFlexy"""
"""https://github.com/DFlexy"""

from cache.redis_client import get_redis_client
from .service import TrackerService

_tracker_service = TrackerService(
    redis_client=get_redis_client(),
    scrape_timeout=1.0,   # era 1.5s — falha mais rápido por tracker
    scrape_retries=1,     # era 3 — 1 tentativa basta no free tier
    max_trackers=6,       # era 10 — 3 HTTP + 3 UDP
    cache_ttl=24 * 3600,
)

def get_tracker_service() -> TrackerService:
    return _tracker_service
