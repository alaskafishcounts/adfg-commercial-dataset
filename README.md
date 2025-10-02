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
| 1001 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1001">Location 1001</a> | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1001/440">pink</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1001/430">coho</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1001/410">chinook</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1001/420">sockeye</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1001/450">chum</a> |
| 1025 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1025">Location 1025</a> | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1025/430">coho</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1025/410">chinook</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1025/420">sockeye</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1025/450">chum</a> |
| 1026 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1026">Location 1026</a> | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1026/410">chinook</a> |
| 1027 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1027">Location 1027</a> | - |
| 1032 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1032">Location 1032</a> | - |
| 1033 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1033">Location 1033</a> | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1033/430">coho</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1033/410">chinook</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1033/420">sockeye</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1033/450">chum</a> |
| 1034 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1034">Location 1034</a> | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1034/430">coho</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1034/410">chinook</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1034/420">sockeye</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1034/450">chum</a> |
| 1035 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1035">Location 1035</a> | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1035/440">pink</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1035/430">coho</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1035/410">chinook</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1035/420">sockeye</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1035/450">chum</a> |
| 1036 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1036">Location 1036</a> | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1036/430">coho</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1036/410">chinook</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1036/420">sockeye</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1036/450">chum</a> |
| 1037 | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1037">Location 1037</a> | <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1037/440">pink</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1037/430">coho</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1037/410">chinook</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1037/420">sockeye</a>, <a href="https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1037/450">chum</a> |
*Note: Showing first 10 of 45 locations.*


## 🧩 AFCA App Integration

This repository is consumed by the Alaska Fish Count App (AFCA). Components load `manifest.json` first, then resolve data paths strictly via the manifest (no hardcoded URLs). The app selects the appropriate repo by location ID range:

- SPORT: 0–100 (200–999 reserved)
- COMMERCIAL: 1000–1999
- SASAP (Historical): 2000–2999

AFCA fetches JSON files directly from GitHub Raw/JSDelivr using the manifest paths and handles errors gracefully.

## 🗂️ Repository Roles

- `adfg-sport-dataset` (0–100 used; 200–999 reserved): Active ADF&G sport fish count data.
- `adfg-commercial-dataset` (1000–1999): Commercial fish count datasets organized by AFCA Location Codes Framework.
- `adfg-sasap-dataset` (2000–2999): Historical escapement counts (SASAP, 1922–2017).

Each repo is scoped to its range to avoid overlap and to keep the AFCA app loading logic simple and deterministic.