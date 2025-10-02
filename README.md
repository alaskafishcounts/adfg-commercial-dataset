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

| Location ID | Location Name | Species Available |
|-------------|---------------|-------------------|
| 1001 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1001">Akalura River Weir</a> | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1001/440">pink</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1001/430">coho</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1001/410">chinook</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1001/420">sockeye</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1001/450">chum</a> |
| 1025 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1025">Situk Lower</a> | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1025/430">coho</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1025/410">chinook</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1025/420">sockeye</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1025/450">chum</a> |
| 1026 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1026">Ford Arm</a> | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1026/410">chinook</a> |
| 1027 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1027">Ilnik River</a> | - |
| 1032 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1032">Hetta Lake</a> | - |
| 1033 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1033">Speel Lake</a> | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1033/430">coho</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1033/410">chinook</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1033/420">sockeye</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1033/450">chum</a> |
| 1034 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1034">Sashin Creek</a> | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1034/430">coho</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1034/410">chinook</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1034/420">sockeye</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1034/450">chum</a> |
| 1035 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1035">Tahltan Lake</a> | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1035/440">pink</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1035/430">coho</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1035/410">chinook</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1035/420">sockeye</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1035/450">chum</a> |
| 1036 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1036">Salmon River (Aniak)</a> | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1036/430">coho</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1036/410">chinook</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1036/420">sockeye</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1036/450">chum</a> |
| 1037 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1037">Salmon Lake Stream</a> | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1037/440">pink</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1037/430">coho</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1037/410">chinook</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1037/420">sockeye</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1037/450">chum</a> |
| 1038 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1038">Kanektok River</a> | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1038/440">pink</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1038/430">coho</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1038/410">chinook</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1038/420">sockeye</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1038/450">chum</a> |
| 1039 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1039">Karta River</a> | - |
| 1040 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1040">Uganik River</a> | - |
| 1041 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1041">Neva Creek</a> | - |
| 1042 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1042">Warm Chuck Lake</a> | - |
| 1043 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1043">Sitkoh Lake Creek</a> | - |
| 1044 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1044">Big Bay Creek</a> | - |
| 1046 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1046">Klag Lake</a> | - |
| 1047 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1047">Lake Eva</a> | - |
| 1048 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1048">Little Waterfall</a> | - |
| 1049 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1049">Little Kitoi</a> | - |
| 1050 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1050">Commercial Location 1050</a> | - |
| 1051 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1051">Commercial Location 1051</a> | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1051/440">pink</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1051/430">coho</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1051/410">chinook</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1051/420">sockeye</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1051/450">chum</a> |
| 1052 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1052">Commercial Location 1052</a> | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1052/440">pink</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1052/430">coho</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1052/410">chinook</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1052/420">sockeye</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1052/450">chum</a> |
| 1053 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1053">Commercial Location 1053</a> | - |
| 1054 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1054">Commercial Location 1054</a> | - |
| 1055 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1055">Commercial Location 1055</a> | - |
| 1056 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1056">Commercial Location 1056</a> | - |
| 1057 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1057">Commercial Location 1057</a> | - |
| 1058 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1058">Commercial Location 1058</a> | - |
| 1059 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1059">Commercial Location 1059</a> | - |
| 1060 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1060">Commercial Location 1060</a> | - |
| 1061 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1061">Commercial Location 1061</a> | - |
| 1062 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1062">Commercial Location 1062</a> | - |
| 1063 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1063">Commercial Location 1063</a> | - |
| 1065 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1065">Commercial Location 1065</a> | - |
| 1066 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1066">Commercial Location 1066</a> | - |
| 1068 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1068">Commercial Location 1068</a> | - |
| 1069 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1069">Commercial Location 1069</a> | - |
| 1070 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1070">Commercial Location 1070</a> | - |
| 1071 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1071">Commercial Location 1071</a> | - |
| 1072 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1072">Commercial Location 1072</a> | - |
| 1101 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1101">Commercial Location 1101</a> | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1101/420">sockeye</a> |
| 1201 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1201">Commercial Location 1201</a> | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1201/440">pink</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1201/430">coho</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1201/410">chinook</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1201/420">sockeye</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1201/450">chum</a> |
| 1501 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1501">Commercial Location 1501</a> | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1501/440">pink</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1501/430">coho</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1501/410">chinook</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1501/420">sockeye</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1501/450">chum</a> |


