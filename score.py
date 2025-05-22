import os
import pickle
from platformdirs import user_data_path

APP_NAME = "FlappyBird"
HIGH_SCORE_FILE = os.path.join(user_data_path(APP_NAME), "high_score.dat")

def load_high_score(game_mode):
    if not os.path.exists(HIGH_SCORE_FILE):
        return 0
    with open(HIGH_SCORE_FILE, "rb") as f:
        data = pickle.load(f)
    return data.get(game_mode, 0)

def save_high_score(game_mode, score):
    os.makedirs(os.path.dirname(HIGH_SCORE_FILE), exist_ok=True)
    data = {}
    if os.path.exists(HIGH_SCORE_FILE):
        with open(HIGH_SCORE_FILE, "rb") as f:
            data = pickle.load(f)
    if score > data.get(game_mode, 0):
        data[game_mode] = score
        with open(HIGH_SCORE_FILE, "wb") as f:
            pickle.dump(data, f)
