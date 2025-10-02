# ADFG Commercial Dataset

## AFCA Location Codes Framework - Commercial Dataset (1000-1999)

This dataset contains commercial fishing data organized according to the official AFCA Location Codes Framework.

### Dataset Statistics
- **Total Files**: 502
- **Total Locations**: 45
- **ID Range**: 1000-1999
- **Year Range**: 1981-2024
- **Framework**: AFCA Location Codes Framework

### Management Area Blocks

#### 1000-1099: Arctic-Yukon-Kuskokwim (AYK) Region
- **1000-1024**: Yukon River Area
- **1025-1049**: Kuskokwim Area  
- **1050-1074**: Norton Sound & Kotzebue
- **1075-1099**: Arctic Coast

#### 1100-1199: Bristol Bay Area
- Dedicated block for Bristol Bay region

#### 1200 of-1299: Cook Inlet Area
- Full block covering Upper and Lower Cook Inlet

#### 1300-1399: Westward Minor Areas
- **1300-1324**: Chignik Area
- **1325-1349**: Alaska Peninsula & Aleutian Islands
- **1350-1374**: Reserved/Expandable
- **1375-1399**: Reserved

#### 1400-1499: Kodiak Island Area
- Full 100-code block for Kodiak Island

#### 1500-1599: Prince William Sound & Copper River
- Dedicated block for PWS Area

#### 1600-1699: Southeastern Alaska Area
- Full block for Southeast Alaska

#### 1700-1999: Reserved for Expansion
- Buffer for future expansion

### Species Coverage
- **sockeye** (ID: 420): Commercial salmon counts
- **pink** (ID: 440): Commercial salmon counts  
- **coho** (ID: 430): Commercial salmon counts
- **chinook** (ID: 410): Commercial salmon counts
- **chum** (ID: 450): Commercial salmon counts

### Data Structure
```
adfg-commercial-dataset/
├── [location-id]/           # AFCA framework location ID (1000-1999)
│   ├── [species-id]/        # Species ID (410, 420, 430, etc.)
│   │   ├── [year]-[location-slug]-[species-slug].json
│   │   └── ...
│   └── ...
├── manifest.json            # Dataset manifest with AFCA framework
└── README.md               # This file
```

### Framework Compliance
This dataset follows the official AFCA Location Codes Framework:
- ✅ Commercial dataset uses 1000-1999 range
- ✅ Management area blocks properly assigned
- ✅ Geographic organization maintained
- ✅ Reserved ranges for future expansion
- ✅ Compatible with AFCA app data loading

### Data Format
All files follow the ADFG standard format with consistent column structure:

```json
{
  "COLUMNS": [
    "YEAR",
    "COUNTDATE",
    "FISHCOUNT",
    "SPECIESID",
    "COUNTLOCATIONID",
    "COUNTLOCATION",
    "SPECIES"
  ],
  "DATA": [
    [
      1939,
      "May, 26 1939 00:00:00",
      3,
      410,
      1001,
      "Akalura Creek",
      "Chinook"
    ]
  ],
  "metadata": {
    "location_id": 1001,
    "location_name": "Akalura Creek",
    "species_id": 410,
    "species_name": "Chinook Salmon",
    "year": 1939,
    "last_updated": "2025-10-02T18:30:39Z",
    "data_source": "ADF&G Commercial"
  }
}
```

### AFCA Location Codes Framework
This dataset follows the official AFCA Location Codes Framework for commercial fishing locations:

#### Location ID Range: 1000-1999
- **1000-1099**: Arctic-Yukon-Kuskokwim (AYK) Region
  - 1000-1024: Yukon River Area
  - 1025-1049: Kuskokwim Area
  - 1050-1074: Norton Sound & Kotzebue
  - 1075-1099: Arctic Coast
- **1100-1199**: Bristol Bay Area
- **1200-1299**: Cook Inlet Area
- **1300-1399**: Westward Minor Areas
  - 1300-1324: Chignik Area
  - 1325-1349: Alaska Peninsula & Aleutian Islands
  - 1350-1374: Reserved/Expandable
  - 1375-1399: Reserved
- **1400-1499**: Kodiak Island Area
- **1500-1599**: Prince William Sound & Copper River
- **1600-1699**: Southeastern Alaska Area
- **1700-1999**: Reserved for Expansion

#### File Naming Convention
- **Format**: `YEAR-location-slug-species-slug.json`
- **Example**: `1986-akalura-river-chinook.json`
- **Location Slug**: Lowercase, hyphenated location name
- **Species Slug**: Lowercase, hyphenated species name

## Location Directory

This dataset contains **45 locations** across Alaska with commercial fishing data. Each location is organized by AFCA Location Codes Framework (1000-1999 range).

### Complete Location List

| Location ID | Location Name | Species Available | GitHub Folder |
|-------------|---------------|-------------------|---------------|
| 1001 | Akalura River Weir | chinook, sockeye, coho, pink, chum | [1001](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1001) |
| 1025 | Situk Lower | chinook, sockeye, coho, chum | [1025](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1025) |
| 1026 | Ford Arm | chinook | [1026](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1026) |
| 1027 | Ilnik River | - | [1027](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1027) |
| 1032 | Hetta Lake | - | [1032](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1032) |
| 1033 | Speel Lake | chinook, sockeye, coho, chum | [1033](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1033) |
| 1034 | Sashin Creek | chinook, sockeye, coho, chum | [1034](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1034) |
| 1035 | Tahltan Lake | chinook, sockeye, coho, pink, chum | [1035](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1035) |
| 1036 | Salmon River (Aniak) | chinook, sockeye, coho, chum | [1036](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1036) |
| 1037 | Salmon Lake Stream | chinook, sockeye, coho, pink, chum | [1037](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1037) |
| 1038 | Kanektok River | chinook, sockeye, coho, pink, chum | [1038](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1038) |
| 1039 | Karta River | 999 | [1039](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1039) |
| 1040 | Uganik River | 999 | [1040](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1040) |
| 1041 | Neva Creek | 999 | [1041](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1041) |
| 1042 | Warm Chuck Lake | 999 | [1042](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1042) |
| 1043 | Sitkoh Lake Creek | 999 | [1043](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1043) |
| 1044 | Big Bay Creek | 999 | [1044](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1044) |
| 1046 | Klag Lake | 999 | [1046](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1046) |
| 1047 | Lake Eva | 999 | [1047](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1047) |
| 1048 | Little Waterfall | 999 | [1048](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1048) |
| 1049 | Little Kitoi | 999 | [1049](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1049) |
| 1050 | Location 1050 | 999 | [1050](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1050) |
| 1051 | Location 1051 | chinook, sockeye, coho, pink, chum, 999 | [1051](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1051) |
| 1052 | Location 1052 | chinook, sockeye, coho, pink, chum, 999 | [1052](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1052) |
| 1053 | Location 1053 | 999 | [1053](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1053) |
| 1054 | Location 1054 | 999 | [1054](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1054) |
| 1055 | Location 1055 | 999 | [1055](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1055) |
| 1056 | Location 1056 | 999 | [1056](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1056) |
| 1057 | Location 1057 | 999 | [1057](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1057) |
| 1058 | Location 1058 | 999 | [1058](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1058) |
| 1059 | Location 1059 | 999 | [1059](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1059) |
| 1060 | Location 1060 | 999 | [1060](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1060) |
| 1061 | Location 1061 | 999 | [1061](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1061) |
| 1062 | Location 1062 | 999 | [1062](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1062) |
| 1063 | Location 1063 | 999 | [1063](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1063) |
| 1065 | Location 1065 | 999 | [1065](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1065) |
| 1066 | Location 1066 | 999 | [1066](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1066) |
| 1068 | Location 1068 | 999 | [1068](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1068) |
| 1069 | Location 1069 | 999 | [1069](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1069) |
| 1070 | Location 1070 | 999 | [1070](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1070) |
| 1071 | Location 1071 | 999 | [1071](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1071) |
| 1072 | Location 1072 | 999 | [1072](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1072) |
| 1101 | Location 1101 | sockeye | [1101](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1101) |
| 1201 | Location 1201 | chinook, sockeye, coho, pink, chum | [1201](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1201) |
| 1501 | Location 1501 | chinook, sockeye, coho, pink, chum | [1501](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1501) |
