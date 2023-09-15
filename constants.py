from enum import Enum


ALL_STOCKS = {
    "Infosys": "INFY",
    "Tata Consultancy Services": "TCS",
    "Wipro": "WIPRO",
    "HCL Technologies": "HCLTECH",
    "Tech Mahindra": "TECHM",
    "Oracle Financial Services Software": "OFSS",
    "Mphasis": "MPHASIS",
}

class TRADER_TYPES(Enum):
    Low = "Low"
    Medium = "Medium"
    Aggressive = "Aggressive"

class INVESTMENT_TYPES(Enum):
    SHORT_TERM = "Short Term"
    LONG_TERM = "Long Term"

def get_duration(term):
    if term == INVESTMENT_TYPES.SHORT_TERM.value:
        return 90
    elif term == INVESTMENT_TYPES.LONG_TERM.value:
        return 360
    else:
        # No term selected
        return 720