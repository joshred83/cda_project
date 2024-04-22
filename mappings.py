import pandas as pd

SECTOR_MAPPING = {
    "Accommodation and Food Services": "Food",
    "Administrative and Support and Waste Management and Remediation Services": "Waste",
    "Agriculture, Forestry, Fishing and Hunting": "Agriculture",
    "Arts, Entertainment, and Recreation": "Arts",
    "Construction": "Construction",
    "Educational Services": "Education",
    "Federal, State, and Local Government, excluding state and local schools and hospitals and the U.S. Postal Service (OES Designation)": "Government",
    "Finance and Insurance": "Finance",
    "Health Care and Social Assistance": "Health",
    "Information": "Information",
    "Management of Companies and Enterprises": "Management",
    "Manufacturing": "Manufacturing",
    "Mining, Quarrying, and Oil and Gas Extraction": "Mining",
    "Other Services (except Public Administration)": "Other Services",
    "Professional, Scientific, and Technical Services": "Professional",
    "Real Estate and Rental and Leasing": "Realty",
    "Retail Trade": "Retail",
    "Transportation and Warehousing": "Transportation",
    "Utilities": "Utilities",
    "Wholesale Trade": "Wholesale",
}


def shorten_sector_name(longnames: pd.Series):

    return longnames.replace(SECTOR_MAPPING)


def expand_sector_name(shortnames):
    return shortnames.replace({v: k for k, v in SECTOR_MAPPING.items()})


def state_replacer(states, in_fmt, out_fmt):
    assert in_fmt in ("long", "short", "fips")
    assert out_fmt in ("long", "short", "fips")
    long_short = {
        "Alabama": "AL",
        "Alaska": "AK",
        "Arizona": "AZ",
        "Arkansas": "AR",
        "California": "CA",
        "Colorado": "CO",
        "Connecticut": "CT",
        "Delaware": "DE",
        "Florida": "FL",
        "Georgia": "GA",
        "Hawaii": "HI",
        "Idaho": "ID",
        "Illinois": "IL",
        "Indiana": "IN",
        "Iowa": "IA",
        "Kansas": "KS",
        "Kentucky": "KY",
        "Louisiana": "LA",
        "Maine": "ME",
        "Maryland": "MD",
        "Massachusetts": "MA",
        "Michigan": "MI",
        "Minnesota": "MN",
        "Mississippi": "MS",
        "Missouri": "MO",
        "Montana": "MT",
        "Nebraska": "NE",
        "Nevada": "NV",
        "New Hampshire": "NH",
        "New Jersey": "NJ",
        "New Mexico": "NM",
        "New York": "NY",
        "North Carolina": "NC",
        "North Dakota": "ND",
        "Ohio": "OH",
        "Oklahoma": "OK",
        "Oregon": "OR",
        "Pennsylvania": "PA",
        "Rhode Island": "RI",
        "South Carolina": "SC",
        "South Dakota": "SD",
        "Tennessee": "TN",
        "Texas": "TX",
        "Utah": "UT",
        "Vermont": "VT",
        "Virginia": "VA",
        "Washington": "WA",
        "West Virginia": "WV",
        "Wisconsin": "WI",
        "Wyoming": "WY",
    }
    short_long = {v: k for k, v in long_short.items()}
    long_fips = {
        "Alabama": "01",
        "Alaska": "02",
        "Arizona": "04",
        "Arkansas": "05",
        "California": "06",
        "Colorado": "08",
        "Connecticut": "09",
        "Delaware": "10",
        "Florida": "12",
        "Georgia": "13",
        "Hawaii": "15",
        "Idaho": "16",
        "Illinois": "17",
        "Indiana": "18",
        "Iowa": "19",
        "Kansas": "20",
        "Kentucky": "21",
        "Louisiana": "22",
        "Maine": "23",
        "Maryland": "24",
        "Massachusetts": "25",
        "Michigan": "26",
        "Minnesota": "27",
        "Mississippi": "28",
        "Missouri": "29",
        "Montana": "30",
        "Nebraska": "31",
        "Nevada": "32",
        "New Hampshire": "33",
        "New Jersey": "34",
        "New Mexico": "35",
        "New York": "36",
        "North Carolina": "37",
        "North Dakota": "38",
        "Ohio": "39",
        "Oklahoma": "40",
        "Oregon": "41",
        "Pennsylvania": "42",
        "Rhode Island": "44",
        "South Carolina": "45",
        "South Dakota": "46",
        "Tennessee": "47",
        "Texas": "48",
        "Utah": "49",
        "Vermont": "50",
        "Virginia": "51",
        "Washington": "53",
        "West Virginia": "54",
        "Wisconsin": "55",
        "Wyoming": "56",
    }
    fips_long = {v: k for k, v in long_short.items()}
    short_fips = {k1: k2 for k1, k2 in zip(short_long.keys(), fips_long.keys())}
    fips_short = {v: k for k, v in short_fips.items()}

    if in_fmt == "short":
        if out_fmt == "fips":
            return states.replace(short_fips)
        elif out_fmt == "long":
            return states.replace(short_long)
    if in_fmt == "long":
        if out_fmt == "fips":
            return states.replace(long_fips)
        elif out_fmt == "short":
            return states.replace(long_short)
    if in_fmt == "fips":
        if out_fmt == "long":
            return states.replace(fips_long)
        elif out_fmt == "short":
            return states.replace(fips_short)
    else:
        raise ValueError
