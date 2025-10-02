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
- **Example**: `1986-akalura-river-chinook.json`
- **Location Slug**: Lowercase, hyphenated location name
- **Species Slug**: Lowercase, hyphenated species name

## Location Directory

This dataset contains **45 locations** across Alaska with commercial fishing data. Each location is organized by AFCA Location Codes Framework (1000-1999 range).

### Complete Location List (45 Locations)

| Location ID | Location Name | Species Available | GitHub Folder |
|-------------|---------------|-------------------|---------------|
| 1001 | Akalura River | chinook |  [Commercial](http://localhost:8000/) |
| 1025 | Akiak Creek (Upper) | pink, coho, chinook | [Commercial](http://localhost:8000/) |
| 1026 | Akulurak River (Upper) | chinook | [Commercial](http://localhost:8000/) |
| 1033 | Takotna River Weir | chinook, sockeye, coho, chum, other | [Commercial](http://localhost:8000/) |
| 1034 | Telaquana River | chinook, sockeye, coho, chum | [Commercial](http://localhost:8000/) |
| 1035 | Tuluksak River | chinook, sockeye, coho, pink, chum | [Commercial](http://localhost:8000/) |
| 1036 | Tatlawiksuk River | chinook, sockeye, coho, chum | [Commercial](http://localhost:8000/) |
| 1037 | Eldorado River | chinook, sockeye, coho, pink, chum | [Commercial](http://localhost:8000/) |
| 1038 | Bonanza River | chinook, sockeye, coho, pink, chum | [Commercial](http://localhost:8000/) |
| 1039 | Commercial Location 1039 | other | [Commercial](http://localhost:8000/) |
| 1040 | Commercial Location 1040 | other | [Commercial](http://localhost:8000/) |
| 1041 | Commercial Location 1041 | other | [Commercial](http://localhost:8000/) |
| 1042 | Commercial Location 1042 | other | [Commercial](http://localhost:8000/) |
| 1043 | Commercial Location 1043 | other | [Commercial](http://localhost:8000/) |
| 1044 | Commercial Location 1044 | other | [Commercial](http://localhost:8000/) |
| 1046 | Commercial Location 1046 | other | [Commercial](http://localhost:8000/) |
| 1047 | Commercial Location 1047 | other | [Commercial](http://localhost:8000/) |
| 1048 | Commercial Location 1048 | other | [Commercial](http://localhost:8000/) |
| 1049 | Commercial Location 1049 | other | [Commercial](http://localhost:8000/) |
| 1050 | Commercial Location 1050 | other | [Commercial](http://localhost:8000/) |
| 1051 | Commercial Location 1051 | chinook, sockeye, coho, pink, chum, other | [Commercial](http://localhost:8000/) |
| 1052 | Commercial Location 1052 | chinook, sockeye, coho, pink, chum, other | [Commercial](http://localhost:8000/) |
| 1053 | Commercial Location 1053 | other | [Commercial](http://localhost:8000/) |
| 1054 | Commercial Location 1054 | other | [Commercial](http://localhost:8000/) |
| 1055 | Commercial Location 1055 | other | [Commercial](http://localhost:8000/) |
| 1056 | Commercial Location 1056 | other | [Commercial](http://localhost:8000/) |
| 1057 | Commercial Location 1057 | other | [Commercial](http://localhost:8000/) |
| 1058 | Commercial Location 1058 | other | [Commercial](http://localhost:8000/) |
| 1059 | Commercial Location 1059 | other | [Commercial](http://localhost:8000/) |
| 1060 | Commercial Location 1060 | other | [Commercial](http://localhost:8000/) |
| 1061 | Commercial Location 1061 | other | [Commercial](http://localhost:8000/) |
| 1062 | Commercial Location 1062 | other | [Commercial](http://localhost:8000/) |
| 1063 | Commercial Location 1063 | other | [Commercial](http://localhost:8000/) |
| 1065 | Commercial Location 1065 | other | [Commercial](http://localhost:8000/) |
| 1066 | Commercial Location 1066 | other | [Commercial](http://localhost:8000/) |
| 1068 | Commercial Location 1068 | other | [Commercial](http://localhost:8000/) |
| 1069 | Commercial Location 1069 | other | [Commercial](http://localhost:8000/) |
| 1070 | Commercial Location 1070 | other | [Commercial](http://localhost:8000/) |
| 1071 | Commercial Location 1071 | other | [Commercial](http://localhost:8000/) |
| 1072 | Commercial Location 1072 | other | [Commercial](http://localhost:8000/) |
| 1101 | Bristol Bay Location | other | [Commercial](http://localhost:8000/) |
| 1201 | Cook Inlet Location | chinook, sockeye, coho, pink, chum | [Commercial](http://localhost:8000/) |
| 1501 | Prince William Sound Location | chinook, sockeye, coho, pink, chum | [Commercial](http://localhost:8000/) |

*Note: This table shows all 45 locations in the commercial dataset. Each location folder contains species-specific subdirectories with commercial fishing data following AFCA Location Codes Framework.*

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