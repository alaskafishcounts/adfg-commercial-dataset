# ADFG Commercial Dataset

## AFCA Location Codes Framework - Commercial Dataset (1000-1999)

This dataset contains commercial fishing data organized according to the official AFCA Location Codes Framework.

### Dataset Statistics
- **Total Files**: 584
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

#### 1200-1299: Cook Inlet Area
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
- **sockeye** (ID: 420): 94 files
- **pink** (ID: 440): 136 files
- **coho** (ID: 430): 216 files
- **chinook** (ID: 410): 138 files

### Data Structure
```
adfg-commercial-dataset/
├── [location-id]/           # AFCA framework location ID (1000-1999)
│   ├── [species-id]/        # Species ID (410, 420, 430, etc.)
│   │   ├── [year]-[location-slug]-[species-id]-[species-name].json
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
      1000,
      "Akalura Creek",
      "Chinook"
    ]
  ],
  "metadata": {
    "location_id": 1000,
    "location_name": "Commercial Location",
    "species_id": 410,
    "species_name": "Chinook Salmon",
    "year": 2025,
    "last_updated": "2025-01-28T10:00:00Z",
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
- **Example**: `2025-bristol-bay-sockeye.json`
- **Location Slug**: Lowercase, hyphenated location name
- **Species Slug**: Lowercase, hyphenated species name

## Location Directory

This dataset contains **45 locations** across Alaska with commercial fishing data. Each location is organized by AFCA Location Codes Framework (1000-1999 range).

### Complete Location List (45 Locations)

| Location ID | Location Name | Species Available | GitHub Folder |
|-------------|---------------|-------------------|---------------|
| 1001 | [Location 1001](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1001) | chinook, sockeye, coho, pink, chum | [1001](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1001) |
| 1025 | [Location 1025](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1025) | chinook, sockeye, coho, pink, chum | [1025](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1025) |
| 1026 | [Location 1026](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1026) | chinook | [1026](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1026) |
| 1033 | [Location 1033](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1033) | chinook, sockeye, coho, chum | [1033](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1033) |
| 1034 | [Location 1034](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1034) | chinook, sockeye, coho, chum | [1034](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1034) |
| 1035 | [Location 1035](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1035) | chinook, sockeye, coho, pink, chum | [1035](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1035) |
| 1036 | [Location 1036](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1036) | chinook, sockeye, coho, chum | [1036](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1036) |
| 1037 | [Location 1037](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1037) | chinook, sockeye, coho, pink, chum | [1037](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1037) |
| 1038 | [Location 1038](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1038) | chinook, sockeye, coho, pink, chum | [1038](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1038) |
| 1039 | [Location 1039](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1039) | other | [1039](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1039) |
| 1040 | [Location 1040](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1040) | other | [1040](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1040) |
| 1041 | [Location 1041](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1041) | other | [1041](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1041) |
| 1042 | [Location 1042](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1042) | other | [1042](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1042) |
| 1043 | [Location 1043](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1043) | other | [1043](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1043) |
| 1044 | [Location 1044](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1044) | other | [1044](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1044) |
| 1046 | [Location 1046](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1046) | other | [1046](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1046) |
| 1047 | [Location 1047](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1047) | other | [1047](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1047) |
| 1048 | [Location 1048](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1048) | other | [1048](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1048) |
| 1049 | [Location 1049](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1049) | other | [1049](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1049) |
| 1050 | [Location 1050](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1050) | other | [1050](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1050) |

*Note: This table shows the first 20 locations. The complete dataset contains 45 locations total. Each location folder contains species-specific subdirectories with commercial fishing data.*

### Regional Organization

The locations are organized by management areas:

- **Arctic-Yukon-Kuskokwim Region (1000-1099)**: Yukon River, Kuskokwim, Norton Sound, Kotzebue
- **Bristol Bay Area (1100-1199)**: Bristol Bay commercial fisheries
- **Cook Inlet Area (1200-1299)**: Upper and Lower Cook Inlet
- **Westward Minor Areas (1300-1399)**: Chignik, Alaska Peninsula, Aleutian Islands
- **Kodiak Island Area (1400-1499)**: Kodiak Island commercial fisheries
- **Prince William Sound & Copper River (1500-1599)**: PWS Area commercial fisheries
- **Southeastern Alaska Area (1600-1699)**: Southeast Alaska commercial fisheries
- **Future Expansion (1700-1999)**: Reserved for additional locations

### Data Sources
Commercial fishing data from Alaska Department of Fish & Game (ADFG) management regions.

### Last Updated
2025-01-28T10:00:00Z


### Complete Location List

| Location ID | Location Name | Species Available | GitHub Folder |
|-------------|---------------|-------------------|---------------|
| 1001 | Location 1001 | 5 | [1001](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1001) |
| 1025 | Location 1025 | 4 | [1025](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1025) |
| 1026 | Location 1026 | 1 | [1026](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1026) |
| 1027 | Location 1027 | 0 | [1027](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1027) |
| 1032 | Location 1032 | 0 | [1032](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1032) |
| 1033 | Takotna River Weir | 4 | [1033](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1033) |
| 1034 | Telaquana River | 4 | [1034](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1034) |
| 1035 | Tuluksak River | 5 | [1035](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1035) |
| 1036 | Tatlawiksuk River | 4 | [1036](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1036) |
| 1037 | Eldorado River | 5 | [1037](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1037) |
| 1038 | Bonanza River | 5 | [1038](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1038) |
| 1039 | Location 1039 | 1 | [1039](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1039) |
| 1040 | Location 1040 | 1 | [1040](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1040) |
| 1041 | Location 1041 | 1 | [1041](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1041) |
| 1042 | Location 1042 | 1 | [1042](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1042) |
| 1043 | Location 1043 | 1 | [1043](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1043) |
| 1044 | Location 1044 | 1 | [1044](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1044) |
| 1046 | Location 1046 | 1 | [1046](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1046) |
| 1047 | Location 1047 | 1 | [1047](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1047) |
| 1048 | Location 1048 | 1 | [1048](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1048) |
| 1049 | Location 1049 | 1 | [1049](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1049) |
| 1050 | Location 1050 | 1 | [1050](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1050) |
| 1051 | Location 1051 | 6 | [1051](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1051) |
| 1052 | Location 1052 | 6 | [1052](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1052) |
| 1053 | Location 1053 | 1 | [1053](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1053) |
| 1054 | Location 1054 | 1 | [1054](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1054) |
| 1055 | Location 1055 | 1 | [1055](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1055) |
| 1056 | Location 1056 | 1 | [1056](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1056) |
| 1057 | Location 1057 | 1 | [1057](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1057) |
| 1058 | Location 1058 | 1 | [1058](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1058) |
| 1059 | Location 1059 | 1 | [1059](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1059) |
| 1060 | Location 1060 | 1 | [1060](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1060) |
| 1061 | Location 1061 | 1 | [1061](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1061) |
| 1062 | Location 1062 | 1 | [1062](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1062) |
| 1063 | Location 1063 | 1 | [1063](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1063) |
| 1065 | Location 1065 | 1 | [1065](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1065) |
| 1066 | Location 1066 | 1 | [1066](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1066) |
| 1068 | Location 1068 | 1 | [1068](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1068) |
| 1069 | Location 1069 | 1 | [1069](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1069) |
| 1070 | Location 1070 | 1 | [1070](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1070) |
| 1071 | Location 1071 | 1 | [1071](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1071) |
| 1072 | Location 1072 | 1 | [1072](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1072) |
| 1101 | Location 1101 | 1 | [1101](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1101) |
| 1201 | Location 1201 | 5 | [1201](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1201) |
| 1501 | Location 1501 | 5 | [1501](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/1501) |