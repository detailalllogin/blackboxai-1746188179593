import swisseph as swe
from datetime import datetime
from typing import Dict, Any

# Constants for Nakshatra and Pada names in English and Hindi
NAKSHATRA_NAMES = {
    "en": [
        "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashirsha", "Ardra",
        "Punarvasu", "Pushya", "Ashlesha", "Magha", "Purva Phalguni", "Uttara Phalguni",
        "Hasta", "Chitra", "Swati", "Vishakha", "Anuradha", "Jyeshtha",
        "Mula", "Purva Ashadha", "Uttara Ashadha", "Shravana", "Dhanishta", "Shatabhisha",
        "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"
    ],
    "hi": [
        "अश्विनी", "भरणी", "कृत्तिका", "रोहिणी", "मृगशिरा", "आर्द्रा",
        "पुनर्वसु", "पुष्य", "अश्लेषा", "मघा", "पूर्व फाल्गुनी", "उत्तर फाल्गुनी",
        "हस्त", "चित्रा", "स्वाती", "विशाखा", "अनुराधा", "ज्येष्ठा",
        "मूल", "पूर्वाषाढा", "उत्तराषाढा", "श्रवण", "धनिष्ठा", "शतभिषा",
        "पूर्व भाद्रपद", "उत्तर भाद्रपद", "रेवती"
    ]
}

def calculate_planetary_positions(jd_ut: float) -> Dict[str, Any]:
    """
    Calculate planetary positions using Swiss Ephemeris for given Julian Day UT.
    Returns a dictionary with planet names and their longitudes.
    """
    planets = {
        "Sun": swe.SUN,
        "Moon": swe.MOON,
        "Mars": swe.MARS,
        "Mercury": swe.MERCURY,
        "Jupiter": swe.JUPITER,
        "Venus": swe.VENUS,
        "Saturn": swe.SATURN,
        "Rahu": swe.MEAN_NODE,  # North Node
        "Ketu": swe.MEAN_NODE   # South Node (180 degrees opposite Rahu)
    }
    positions = {}
    for name, planet in planets.items():
        lon, lat, dist = swe.calc_ut(jd_ut, planet)[0:3]
        if name == "Ketu":
            lon = (positions["Rahu"] + 180) % 360 if "Rahu" in positions else (lon + 180) % 360
        positions[name] = lon
    return positions

def get_nakshatra(p_longitude: float, lang: str = "en") -> Dict[str, Any]:
    """
    Calculate Nakshatra and Pada from planetary longitude.
    """
    nakshatra_index = int(p_longitude / (360 / 27))
    pada = int((p_longitude % (360 / 27)) / (360 / 27 / 4)) + 1
    nakshatra_name = NAKSHATRA_NAMES.get(lang, NAKSHATRA_NAMES["en"])[nakshatra_index]
    return {"nakshatra": nakshatra_name, "pada": pada}

def datetime_to_julian_day(dt: datetime) -> float:
    """
    Convert datetime to Julian Day UT using Swiss Ephemeris.
    """
    return swe.julday(dt.year, dt.month, dt.day, dt.hour + dt.minute / 60 + dt.second / 3600)

# Additional functions for Lagna, Chandra Rashi, Vimshottari Dasha, etc. to be implemented
