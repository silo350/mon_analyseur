import logging

import pandas as pd
import requests

from config import API_GEO_URL

logger = logging.getLogger(__name__)


def get_regions() -> pd.DataFrame:
    """Récupère la liste des régions françaises depuis l'API Géo."""
    url = f"{API_GEO_URL}/regions"
    try:
        reponse = requests.get(url, timeout=10)
        reponse.raise_for_status()
    except requests.RequestException as erreur:
        logger.error("Échec de l'appel à l'API Géo : %s", erreur)
        raise
    df = pd.DataFrame(reponse.json())
    logger.info("%d régions récupérées", len(df))
    return df