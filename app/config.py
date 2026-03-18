"""Copyright (c) 2025 DFlexy"""
"""https://github.com/DFlexy"""

import os
from typing import Optional


def _parse_duration(duration_str: str) -> int:
    duration_str = duration_str.strip().lower()
    if duration_str.endswith('s'):
        return int(duration_str[:-1])
    elif duration_str.endswith('m'):
        return int(duration_str[:-1]) * 60
    elif duration_str.endswith('h'):
        return int(duration_str[:-1]) * 3600
    elif duration_str.endswith('d'):
        return int(duration_str[:-1]) * 86400
    else:
        return int(duration_str)


class Config:
    # Servidor
    PORT: int = int(os.getenv('PORT', '7006'))
    METRICS_PORT: int = int(os.getenv('METRICS_PORT', '8081'))

    # Redis
    REDIS_HOST: Optional[str] = os.getenv('REDIS_HOST', None)
    REDIS_PORT: int = int(os.getenv('REDIS_PORT', '6379'))
    REDIS_DB: int = int(os.getenv('REDIS_DB', '0'))

    # Cache
    HTML_CACHE_TTL_SHORT: int = _parse_duration(os.getenv('HTML_CACHE_TTL_SHORT', '10m'))
    HTML_CACHE_TTL_LONG: int  = _parse_duration(os.getenv('HTML_CACHE_TTL_LONG',  '12h'))
    FLARESOLVERR_SESSION_TTL: int = _parse_duration(os.getenv('FLARESOLVERR_SESSION_TTL', '8h'))

    # Logging
    LOG_LEVEL: int  = int(os.getenv('LOG_LEVEL', '1'))
    LOG_FORMAT: str = os.getenv('LOG_FORMAT', 'console')

    # FlareSolverr
    FLARESOLVERR_ADDRESS: Optional[str] = os.getenv('FLARESOLVERR_ADDRESS', None)

    EMPTY_QUERY_MAX_LINKS: int = int(os.getenv('EMPTY_QUERY_MAX_LINKS', '16'))

    # ---------------------------------------------------------------
    # PERFORMANCE — valores ajustados para free tier (512 MB, 0.1 CPU)
    # ---------------------------------------------------------------

    # Trackers: menos workers e retries para não travar no free tier
    TRACKER_MAX_WORKERS: int    = int(os.getenv('TRACKER_MAX_WORKERS',    '10'))   # era 30
    TRACKER_SCRAPING_ENABLED: bool = os.getenv('TRACKER_SCRAPING_ENABLED', 'true').lower() == 'true'

    # Metadata: menos requisições simultâneas para não estourar rate-limit do iTorrents
    METADATA_MAX_CONCURRENT: int = int(os.getenv('METADATA_MAX_CONCURRENT', '16'))  # era 128

    # Scraper: menos workers paralelos de links
    SCRAPER_MAX_WORKERS: int = int(os.getenv('SCRAPER_MAX_WORKERS', '8'))  # era 16

    # HTTP: timeout menor para falhar rápido em vez de acumular requisições travadas
    HTTP_REQUEST_TIMEOUT: int = int(os.getenv('HTTP_REQUEST_TIMEOUT', '20'))  # era 45

    # Retry: menos tentativas e backoff menor
    HTTP_RETRY_MAX_ATTEMPTS: int   = int(os.getenv('HTTP_RETRY_MAX_ATTEMPTS', '1'))    # era 3
    HTTP_RETRY_BACKOFF_BASE: float = float(os.getenv('HTTP_RETRY_BACKOFF_BASE', '0.5')) # era 1.0

    # Connection Pool: menor para economizar memória no free tier
    HTTP_POOL_CONNECTIONS: int = int(os.getenv('HTTP_POOL_CONNECTIONS', '20'))  # era 50
    HTTP_POOL_MAXSIZE: int     = int(os.getenv('HTTP_POOL_MAXSIZE',     '40'))  # era 100

    # Cache local em memória
    LOCAL_CACHE_ENABLED: bool = True
    LOCAL_CACHE_TTL: int      = 30

    # FlareSolverr
    FLARESOLVERR_MAX_SESSIONS: int = 5  # era 15

    # Text / parsing
    MAX_QUERY_LENGTH: int        = int(os.getenv('MAX_QUERY_LENGTH', '200'))
    MAX_EPISODE_NUMBER: int      = 99
    MAX_EPISODE_DIFF: int        = 20
    INFO_HASH_LENGTH: int        = 40
    RELEASE_TITLE_CACHE_TTL: int = 7 * 24 * 3600

    # Proxy
    PROXY_TYPE: str           = os.getenv('PROXY_TYPE', 'http').lower().strip()
    PROXY_HOST: Optional[str] = os.getenv('PROXY_HOST', None)
    PROXY_PORT: Optional[str] = os.getenv('PROXY_PORT', None)
    PROXY_USER: Optional[str] = os.getenv('PROXY_USER', None)
    PROXY_PASS: Optional[str] = os.getenv('PROXY_PASS', None)
