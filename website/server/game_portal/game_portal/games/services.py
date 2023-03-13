from django.conf import settings

import requests
import logging

def get_leaderboard(product_id):
    logging.info(f"Requesting top ten for product: {product_id}")
    
    try:
        response = requests.get(
            f"{settings.STATS_TRACKER_CONFIG['url']}/leaderboards/top_ten/{product_id}"
        )
        response.raise_for_status()
        return response.json()
        
    except (requests.exceptions.RequestException, ValueError):
        logging.exception("Error occurred while requesting leaderboard")
        return {"error": "An error occurred while requesting the leaderboard."}

def get_player_stats_for_game(product_id, user_id):
    logging.info(f"Requesting stats for user: {user_id}, product: {product_id}")

    try:
        response = requests.get(
            f"{settings.STATS_TRACKER_CONFIG['url']}/" f"stats/{product_id}/{user_id}"
        )
        response.raise_for_status()
        return response.json()
    except (requests.exceptions.RequestException, ValueError)
        logging.exception("Error occurred while requesting leaderboard")
        return {"error": "An error occurred while requesting the leaderboard."}
    
