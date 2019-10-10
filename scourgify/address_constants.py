#!/usr/bin/env python
# encoding: utf-8
"""
copyright (c) 2016-2017 Earth Advantage.
All rights reserved
..codeauthor::Fable Turas <fable@raintechpdx.com>

"""
# Imports from Third Party Modules
from frozendict import frozendict
from yamlconf import Config, ConfigError

KNOWN_ODDITIES = frozendict({})
ABNORMAL_OCCUPANCY_ABBRVS = frozendict({})

PROBLEM_ST_TYPE_ABBRVS = frozendict({
    'CT': 'COURT'
})

DIRECTIONAL_REPLACEMENTS = frozendict({
    'EAST': 'E',
    'WEST': 'W',
    'NORTH': 'N',
    'SOUTH': 'S',
    'NORTHEAST': 'NE',
    'NORTHWEST': 'NW',
    'SOUTHEAST': 'SE',
    'SOUTHWEST': 'SW'
})

STREET_TYPE_ABBREVIATIONS = frozendict({
    'ALLEE': 'ALY',
    'ALLEY': 'ALY',
    'ALLY': 'ALY',
    'ALY': 'ALY',
    'ANEX': 'ANX',
    'ANNEX': 'ANX',
    'ANNX': 'ANX',
    'ANX': 'ANX',
    'ARC': 'ARC',
    'ARCADE': 'ARC',
    'AV': 'AVE',
    'AVE': 'AVE',
    'AVEN': 'AVE',
    'AVENU': 'AVE',
    'AVENUE': 'AVE',
    'AVN': 'AVE',
    'AVNUE': 'AVE',
    'BAYOO': 'BYU',
    'BAYOU': 'BYU',
    'BCH': 'BCH',
    'BEACH': 'BCH',
    'BEND': 'BND',
    'BND': 'BND',
    'BLF': 'BLF',
    'BLUF': 'BLF',
    'BLUFF': 'BLF',
    'BLUFFS': 'BLFS',
    'BOT': 'BTM',
    'BOTTM': 'BTM',
    'BOTTOM': 'BTM',
    'BTM': 'BTM',
    'BLVD': 'BLVD',
    'BOUL': 'BLVD',
    'BOULEVARD': 'BLVD',
    'BOULV': 'BLVD',
    'BR': 'BR',
    'BRANCH': 'BR',
    'BRNCH': 'BR',
    'BRDGE': 'BRG',
    'BRG': 'BRG',
    'BRIDGE': 'BRG',
    'BRK': 'BRK',
    'BROOK': 'BRK',
    'BROOKS': 'BRKS',
    'BURG': 'BG',
    'BURGS': 'BGS',
    'BYP': 'BYP',
    'BYPA': 'BYP',
    'BYPAS': 'BYP',
    'BYPASS': 'BYP',
    'BYPS': 'BYP',
    'CAMP': 'CP',
    'CMP': 'CP',
    'CP': 'CP',
    'CANYN': 'CYN',
    'CANYON': 'CYN',
    'CNYN': 'CYN',
    'CYN': 'CYN',
    'CAPE': 'CPE',
    'CPE': 'CPE',
    'CAUSEWAY': 'CSWY',
    'CAUSWAY': 'CSWY',
    'CSWY': 'CSWY',
    'CEN': 'CTR',
    'CENT': 'CTR',
    'CENTER': 'CTR',
    'CENTR': 'CTR',
    'CENTRE': 'CTR',
    'CNTER': 'CTR',
    'CNTR': 'CTR',
    'CTR': 'CTR',
    'CENTERS': 'CTRS',
    'CIR': 'CIR',
    'CIRC': 'CIR',
    'CIRCL': 'CIR',
    'CIRCLE': 'CIR',
    'CRCL': 'CIR',
    'CRCLE': 'CIR',
    'CIRCLES': 'CIRS',
    'CLF': 'CLF',
    'CLIFF': 'CLF',
    'CLFS': 'CLFS',
    'CLIFFS': 'CLFS',
    'CLB': 'CLB',
    'CLUB': 'CLB',
    'COMMON': 'CMN',
    'COR': 'COR',
    'CORNER': 'COR',
    'CORNERS': 'CORS',
    'CORS': 'CORS',
    'COURSE': 'CRSE',
    'CRSE': 'CRSE',
    'COURT': 'CT',
    'CRT': 'CT',
    'CT': 'CT',
    'COURTS': 'CTS',
    'COVE': 'CV',
    'CV': 'CV',
    'COVES': 'CVS',
    'CK': 'CRK',
    'CR': 'CRK',
    'CREEK': 'CRK',
    'CRK': 'CRK',
    'CRECENT': 'CRES',
    'CRES': 'CRES',
    'CRESCENT': 'CRES',
    'CRESENT': 'CRES',
    'CRSCNT': 'CRES',
    'CRSENT': 'CRES',
    'CRSNT': 'CRES',
    'CREST': 'CRST',
    'CROSSING': 'XING',
    'CRSSING': 'XING',
    'CRSSNG': 'XING',
    'XING': 'XING',
    'CROSSROAD': 'XRD',
    'CURVE': 'CURV',
    'DALE': 'DL',
    'DL': 'DL',
    'DAM': 'DM',
    'DM': 'DM',
    'DIV': 'DV',
    'DIVIDE': 'DV',
    'DV': 'DV',
    'DVD': 'DV',
    'DR': 'DR',
    'DRIV': 'DR',
    'DRIVE': 'DR',
    'DRV': 'DR',
    'DRIVES': 'DRS',
    'EST': 'EST',
    'ESTATE': 'EST',
    'ESTATES': 'ESTS',
    'ESTS': 'ESTS',
    'EXP': 'EXPY',
    'EXPR': 'EXPY',
    'EXPRESS': 'EXPY',
    'EXPRESSWAY': 'EXPY',
    'EXPW': 'EXPY',
    'EXPY': 'EXPY',
    'EXT': 'EXT',
    'EXTENSION': 'EXT',
    'EXTN': 'EXT',
    'EXTNSN': 'EXT',
    'EXTENSIONS': 'EXTS',
    'EXTS': 'EXTS',
    'FALL': 'FALL',
    'FALLS': 'FLS',
    'FLS': 'FLS',
    'FERRY': 'FRY',
    'FRRY': 'FRY',
    'FRY': 'FRY',
    'FIELD': 'FLD',
    'FLD': 'FLD',
    'FIELDS': 'FLDS',
    'FLDS': 'FLDS',
    'FLAT': 'FLT',
    'FLT': 'FLT',
    'FLATS': 'FLTS',
    'FLTS': 'FLTS',
    'FORD': 'FRD',
    'FRD': 'FRD',
    'FORDS': 'FRDS',
    'FOREST': 'FRST',
    'FORESTS': 'FRST',
    'FRST': 'FRST',
    'FORG': 'FRG',
    'FORGE': 'FRG',
    'FRG': 'FRG',
    'FORGES': 'FRGS',
    'FORK': 'FRK',
    'FRK': 'FRK',
    'FORKS': 'FRKS',
    'FRKS': 'FRKS',
    'FORT': 'FT',
    'FRT': 'FT',
    'FT': 'FT',
    'FREEWAY': 'FWY',
    'FREEWY': 'FWY',
    'FRWAY': 'FWY',
    'FRWY': 'FWY',
    'FWY': 'FWY',
    'GARDEN': 'GDN',
    'GARDN': 'GDN',
    'GDN': 'GDN',
    'GRDEN': 'GDN',
    'GRDN': 'GDN',
    'GARDENS': 'GDNS',
    'GDNS': 'GDNS',
    'GRDNS': 'GDNS',
    'GATEWAY': 'GTWY',
    'GATEWY': 'GTWY',
    'GATWAY': 'GTWY',
    'GTWAY': 'GTWY',
    'GTWY': 'GTWY',
    'GLEN': 'GLN',
    'GLN': 'GLN',
    'GLENS': 'GLNS',
    'GREEN': 'GRN',
    'GRN': 'GRN',
    'GREENS': 'GRNS',
    'GROV': 'GRV',
    'GROVE': 'GRV',
    'GRV': 'GRV',
    'GROVES': 'GRVS',
    'HARB': 'HBR',
    'HARBOR': 'HBR',
    'HARBR': 'HBR',
    'HBR': 'HBR',
    'HRBOR': 'HBR',
    'HARBORS': 'HBRS',
    'HAVEN': 'HVN',
    'HAVN': 'HVN',
    'HVN': 'HVN',
    'HEIGHT': 'HTS',
    'HEIGHTS': 'HTS',
    'HGTS': 'HTS',
    'HT': 'HTS',
    'HTS': 'HTS',
    'HIGHWAY': 'HWY',
    'HIGHWY': 'HWY',
    'HIWAY': 'HWY',
    'HIWY': 'HWY',
    'HWAY': 'HWY',
    'HWY': 'HWY',
    'HILL': 'HL',
    'HL': 'HL',
    'HILLS': 'HLS',
    'HLS': 'HLS',
    'HLLW': 'HOLW',
    'HOLLOW': 'HOLW',
    'HOLLOWS': 'HOLW',
    'HOLW': 'HOLW',
    'HOLWS': 'HOLW',
    'INLET': 'INLT',
    'INLT': 'INLT',
    'IS': 'IS',
    'ISLAND': 'IS',
    'ISLND': 'IS',
    'ISLANDS': 'ISS',
    'ISLNDS': 'ISS',
    'ISS': 'ISS',
    'ISLE': 'ISLE',
    'ISLES': 'ISLE',
    'JCT': 'JCT',
    'JCTION': 'JCT',
    'JCTN': 'JCT',
    'JUNCTION': 'JCT',
    'JUNCTN': 'JCT',
    'JUNCTON': 'JCT',
    'JCTNS': 'JCTS',
    'JCTS': 'JCTS',
    'JUNCTIONS': 'JCTS',
    'KEY': 'KY',
    'KY': 'KY',
    'KEYS': 'KYS',
    'KYS': 'KYS',
    'KNL': 'KNL',
    'KNOL': 'KNL',
    'KNOLL': 'KNL',
    'KNLS': 'KNLS',
    'KNOLLS': 'KNLS',
    'LAKE': 'LK',
    'LK': 'LK',
    'LAKES': 'LKS',
    'LKS': 'LKS',
    'LAND': 'LAND',
    'LANDING': 'LNDG',
    'LNDG': 'LNDG',
    'LNDNG': 'LNDG',
    'LA': 'LN',
    'LANE': 'LN',
    'LANES': 'LN',
    'LN': 'LN',
    'LGT': 'LGT',
    'LIGHT': 'LGT',
    'LIGHTS': 'LGTS',
    'LF': 'LF',
    'LOAF': 'LF',
    'LCK': 'LCK',
    'LOCK': 'LCK',
    'LCKS': 'LCKS',
    'LOCKS': 'LCKS',
    'LDG': 'LDG',
    'LDGE': 'LDG',
    'LODG': 'LDG',
    'LODGE': 'LDG',
    'LOOP': 'LOOP',
    'LOOPS': 'LOOP',
    'MALL': 'MALL',
    'MANOR': 'MNR',
    'MNR': 'MNR',
    'MANORS': 'MNRS',
    'MNRS': 'MNRS',
    'MDW': 'MDW',
    'MEADOW': 'MDW',
    'MDWS': 'MDWS',
    'MEADOWS': 'MDWS',
    'MEDOWS': 'MDWS',
    'MEWS': 'MEWS',
    'MILL': 'ML',
    'ML': 'ML',
    'MILLS': 'MLS',
    'MLS': 'MLS',
    'MISSION': 'MSN',
    'MISSN': 'MSN',
    'MSN': 'MSN',
    'MSSN': 'MSN',
    'MOTORWAY': 'MTWY',
    'MNT': 'MT',
    'MOUNT': 'MT',
    'MT': 'MT',
    'MNTAIN': 'MTN',
    'MNTN': 'MTN',
    'MOUNTAIN': 'MTN',
    'MOUNTIN': 'MTN',
    'MTIN': 'MTN',
    'MTN': 'MTN',
    'MNTNS': 'MTNS',
    'MOUNTAINS': 'MTNS',
    'NCK': 'NCK',
    'NECK': 'NCK',
    'ORCH': 'ORCH',
    'ORCHARD': 'ORCH',
    'ORCHRD': 'ORCH',
    'OVAL': 'OVAL',
    'OVL': 'OVAL',
    'OVERPASS': 'OPAS',
    'PARK': 'PARK',
    'PK': 'PARK',
    'PRK': 'PARK',
    'PARKS': 'PARK',
    'PARKWAY': 'PKWY',
    'PARKWY': 'PKWY',
    'PKWAY': 'PKWY',
    'PKWY': 'PKWY',
    'PKY': 'PKWY',
    'PARKWAYS': 'PKWY',
    'PKWYS': 'PKWY',
    'PASS': 'PASS',
    'PASSAGE': 'PSGE',
    'PATH': 'PATH',
    'PATHS': 'PATH',
    'PIKE': 'PIKE',
    'PIKES': 'PIKE',
    'PINE': 'PNE',
    'PINES': 'PNES',
    'PNES': 'PNES',
    'PL': 'PL',
    'PLACE': 'PL',
    'PLAIN': 'PLN',
    'PLN': 'PLN',
    'PLAINES': 'PLNS',
    'PLAINS': 'PLNS',
    'PLNS': 'PLNS',
    'PLAZA': 'PLZ',
    'PLZ': 'PLZ',
    'PLZA': 'PLZ',
    'POINT': 'PT',
    'PT': 'PT',
    'POINTS': 'PTS',
    'PTS': 'PTS',
    'PORT': 'PRT',
    'PRT': 'PRT',
    'PORTS': 'PRTS',
    'PRTS': 'PRTS',
    'PR': 'PR',
    'PRAIRIE': 'PR',
    'PRARIE': 'PR',
    'PRR': 'PR',
    'RAD': 'RADL',
    'RADIAL': 'RADL',
    'RADIEL': 'RADL',
    'RADL': 'RADL',
    'RAMP': 'RAMP',
    'RANCH': 'RNCH',
    'RANCHES': 'RNCH',
    'RNCH': 'RNCH',
    'RNCHS': 'RNCH',
    'RAPID': 'RPD',
    'RPD': 'RPD',
    'RAPIDS': 'RPDS',
    'RPDS': 'RPDS',
    'REST': 'RST',
    'RST': 'RST',
    'RDG': 'RDG',
    'RDGE': 'RDG',
    'RIDGE': 'RDG',
    'RDGS': 'RDGS',
    'RIDGES': 'RDGS',
    'RIV': 'RIV',
    'RIVER': 'RIV',
    'RIVR': 'RIV',
    'RVR': 'RIV',
    'RD': 'RD',
    'ROAD': 'RD',
    'RDS': 'RDS',
    'ROADS': 'RDS',
    'ROUTE': 'RTE',
    'ROW': 'ROW',
    'RUE': 'RUE',
    'RUN': 'RUN',
    'SHL': 'SHL',
    'SHOAL': 'SHL',
    'SHLS': 'SHLS',
    'SHOALS': 'SHLS',
    'SHOAR': 'SHR',
    'SHORE': 'SHR',
    'SHR': 'SHR',
    'SHOARS': 'SHRS',
    'SHORES': 'SHRS',
    'SHRS': 'SHRS',
    'SKYWAY': 'SKWY',
    'SPG': 'SPG',
    'SPNG': 'SPG',
    'SPRING': 'SPG',
    'SPRNG': 'SPG',
    'SPGS': 'SPGS',
    'SPNGS': 'SPGS',
    'SPRINGS': 'SPGS',
    'SPRNGS': 'SPGS',
    'SPUR': 'SPUR',
    'SPURS': 'SPUR',
    'SQ': 'SQ',
    'SQR': 'SQ',
    'SQRE': 'SQ',
    'SQU': 'SQ',
    'SQUARE': 'SQ',
    'SQRS': 'SQS',
    'SQUARES': 'SQS',
    'STA': 'STA',
    'STATION': 'STA',
    'STATN': 'STA',
    'STN': 'STA',
    'STRA': 'STRA',
    'STRAV': 'STRA',
    'STRAVE': 'STRA',
    'STRAVEN': 'STRA',
    'STRAVENUE': 'STRA',
    'STRAVN': 'STRA',
    'STRVN': 'STRA',
    'STRVNUE': 'STRA',
    'STREAM': 'STRM',
    'STREME': 'STRM',
    'STRM': 'STRM',
    'ST': 'ST',
    'STR': 'ST',
    'STREET': 'ST',
    'STRT': 'ST',
    'STREETS': 'STS',
    'SMT': 'SMT',
    'SUMIT': 'SMT',
    'SUMITT': 'SMT',
    'SUMMIT': 'SMT',
    'TER': 'TER',
    'TERR': 'TER',
    'TERRACE': 'TER',
    'THROUGHWAY': 'TRWY',
    'TRACE': 'TRCE',
    'TRACES': 'TRCE',
    'TRCE': 'TRCE',
    'TRACK': 'TRAK',
    'TRACKS': 'TRAK',
    'TRAK': 'TRAK',
    'TRK': 'TRAK',
    'TRKS': 'TRAK',
    'TRAFFICWAY': 'TRFY',
    'TRFY': 'TRFY',
    'TR': 'TRL',
    'TRAIL': 'TRL',
    'TRAILS': 'TRL',
    'TRL': 'TRL',
    'TRLS': 'TRL',
    'TUNEL': 'TUNL',
    'TUNL': 'TUNL',
    'TUNLS': 'TUNL',
    'TUNNEL': 'TUNL',
    'TUNNELS': 'TUNL',
    'TUNNL': 'TUNL',
    'TPK': 'TPKE',
    'TPKE': 'TPKE',
    'TRNPK': 'TPKE',
    'TRPK': 'TPKE',
    'TURNPIKE': 'TPKE',
    'TURNPK': 'TPKE',
    'UNDERPASS': 'UPAS',
    'UN': 'UN',
    'UNION': 'UN',
    'UNIONS': 'UNS',
    'VALLEY': 'VLY',
    'VALLY': 'VLY',
    'VLLY': 'VLY',
    'VLY': 'VLY',
    'VALLEYS': 'VLYS',
    'VLYS': 'VLYS',
    'VDCT': 'VIA',
    'VIA': 'VIA',
    'VIADCT': 'VIA',
    'VIADUCT': 'VIA',
    'VIEW': 'VW',
    'VW': 'VW',
    'VIEWS': 'VWS',
    'VWS': 'VWS',
    'VILL': 'VLG',
    'VILLAG': 'VLG',
    'VILLAGE': 'VLG',
    'VILLG': 'VLG',
    'VILLIAGE': 'VLG',
    'VLG': 'VLG',
    'VILLAGES': 'VLGS',
    'VLGS': 'VLGS',
    'VILLE': 'VL',
    'VL': 'VL',
    'VIS': 'VIS',
    'VIST': 'VIS',
    'VISTA': 'VIS',
    'VST': 'VIS',
    'VSTA': 'VIS',
    'WALK': 'WALK',
    'WALKS': 'WALK',
    'WALL': 'WALL',
    'WAY': 'WAY',
    'WY': 'WAY',
    'WAYS': 'WAYS',
    'WELL': 'WL',
    'WELLS': 'WLS',
    'WLS': 'WLS'
})

OCCUPANCY_TYPE_ABBREVIATIONS = frozendict({
    'APARTMENT': 'APT',
    'BUILDING': 'BLDG',
    'BASEMENT': 'BSMT',
    'DEPARTMENT': 'DEPT',
    'FLOOR': 'FL',
    'FRONT': 'FRNT',
    'HANGER': 'HNGR',
    'KEY': 'KEY',
    'LOBBY': 'LBBY',
    'LOT': 'LOT',
    'LOWER': 'LOWR',
    'OFFICE': 'OFC',
    'PENTHOUSE': 'PH',
    'PIER': 'PIER',
    'REAR': 'REAR',
    'ROOM': 'RM',
    'SIDE': 'SIDE',
    'SLIP': 'SLIP',
    'SPACE': 'SPC',
    'STOP': 'STOP',
    'SUITE': 'STE',
    'TRAILER': 'TRLR',
    'UNIT': 'UNIT',
    'UPPER': 'UPPER'
})

STATE_ABBREVIATIONS = frozendict({
    'ALABAMA': 'AL',
    'ALA': 'AL',
    'ALASKA': 'AK',
    'ALAS': 'AK',
    'ARIZONA': 'AZ',
    'ARIZ': 'AZ',
    'ARKANSAS': 'AR',
    'ARK': 'AR',
    'CALIFORNIA': 'CA',
    'CALIF': 'CA',
    'CAL': 'CA',
    'COLORADO': 'CO',
    'COLO': 'CO',
    'COL': 'CO',
    'CONNECTICUT': 'CT',
    'CONN': 'CT',
    'DELAWARE': 'DE',
    'DEL': 'DE',
    'DISTRICT OF COLUMBIA': 'DC',
    'FLORIDA': 'FL',
    'FLA': 'FL',
    'FLOR': 'FL',
    'GEORGIA': 'GA',
    'GA': 'GA',
    'HAWAII': 'HI',
    'IDAHO': 'ID',
    'IDA': 'ID',
    'ILLINOIS': 'IL',
    'ILL': 'IL',
    'INDIANA': 'IN',
    'IND': 'IN',
    'IOWA': 'IA',
    'KANSAS': 'KS',
    'KANS': 'KS',
    'KAN': 'KS',
    'KENTUCKY': 'KY',
    'KEN': 'KY',
    'KENT': 'KY',
    'LOUISIANA': 'LA',
    'MAINE': 'ME',
    'MARYLAND': 'MD',
    'MASSACHUSETTS': 'MA',
    'MASS': 'MA',
    'MICHIGAN': 'MI',
    'MICH': 'MI',
    'MINNESOTA': 'MN',
    'MINN': 'MN',
    'MISSISSIPPI': 'MS',
    'MISS': 'MS',
    'MISSOURI': 'MO',
    'MONTANA': 'MT',
    'MONT': 'MT',
    'NEBRASKA': 'NE',
    'NEBR': 'NE',
    'NEB': 'NE',
    'NEVADA': 'NV',
    'NEV': 'NV',
    'NEW HAMPSHIRE': 'NH',
    'NEW JERSEY': 'NJ',
    'NEW MEXICO': 'NM',
    'N MEX': 'NM',
    'NEW M': 'NM',
    'NEW YORK': 'NY',
    'NORTH CAROLINA': 'NC',
    'NORTH DAKOTA': 'ND',
    'N DAK': 'ND',
    'OHIO': 'OH',
    'OKLAHOMA': 'OK',
    'OKLA': 'OK',
    'OREGON': 'OR',
    'OREG': 'OR',
    'ORE': 'OR',
    'PENNSYLVANIA': 'PA',
    'PENN': 'PA',
    'RHODE ISLAND': 'RI',
    'SOUTH CAROLINA': 'SC',
    'SOUTH DAKOTA': 'SD',
    'S DAK': 'SD',
    'TENNESSEE': 'TN',
    'TENN': 'TN',
    'TEXAS': 'TX',
    'TEX': 'TX',
    'UTAH': 'UT',
    'VERMONT': 'VT',
    'VIRGINIA': 'VA',
    'WASHINGTON': 'WA',
    'WASH': 'WA',
    'WEST VIRGINIA': 'WV',
    'W VA': 'WV',
    'WISCONSIN': 'WI',
    'WIS': 'WI',
    'WISC': 'WI',
    'WYOMING': 'WY',
    'WYO': 'WY'
})

ADDRESS_KEYS = (
    'address_line_1', 'address_line_2', 'city', 'state', 'postal_code'
)


class NormalizationConfig(Config):
    """Config class for GBR"""
    # pylint: disable=too-few-public-methods
    default_file = 'address_constants.yaml'

    def __init__(self, config_file=None, config_dir=None, section=None):
        super(NormalizationConfig, self).__init__(
            config_file=config_file, config_dir=config_dir, section=section,
            env_prefix='ADDRESS_CONFIG'
        )


def set_address_constants():
    config = NormalizationConfig()
    if config:
        addr_constants = (
            'DIRECTIONAL_REPLACEMENTS',
            'OCCUPANCY_TYPE_ABBREVIATIONS',
            'STATE_ABBREVIATIONS',
            'STREET_TYPE_ABBREVIATIONS',
            'KNOWN_ODDITIES',
            'PROBLEM_ST_TYPE_ABBRVS',
        )
        insertion_method = config.get('insertion_method', default='update')
        update = ('update', 'insert')
        replace = ('replace', 'overwrite')
        if insertion_method not in update + replace:
            msg = "'{}' is not a valid option for 'insertion_method'".format(
                insertion_method
            )
            raise ConfigError(msg)
        globals()['ADDRESS_KEYS'] = config.get(
            'ADDRESS_KEYS', default=globals()['ADDRESS_KEYS']
        )
        for key in addr_constants:
            new_vals = config.get(key, default={})
            if key == 'OCCUPANCY_TYPE_ABBREVIATIONS' and new_vals:
                org_keys = OCCUPANCY_TYPE_ABBREVIATIONS.keys()
                new_keys = new_vals.keys()
                globals()['ABNORMAL_OCCUPANCY_ABBRVS'] = (
                    set(new_keys) - set(org_keys)
                )
            if new_vals and insertion_method in update:
                globals()[key] = globals()[key].copy(**new_vals)
            elif new_vals and insertion_method in replace:
                globals()[key] = new_vals


set_address_constants()
