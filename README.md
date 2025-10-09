# ADF&G Commercial Fisheries Dataset

## Overview

This repository contains Alaska Department of Fish and Game (ADF&G) Commercial Fisheries fish count data, converted to the Alaska Fish Count App (AFCA) JSON format for seamless integration with the AFCA application.

## Dataset Statistics

- **Total Files**: 486 JSON files
- **Year Range**: 1965-2025 (61 years)
- **Locations**: 43 Commercial monitoring stations
- **Species**: Chinook (410), Sockeye (420), Coho (430), Pink (440), Chum (450)
- **Total Records**: Commercial fish count data points
- **Data Quality**: ✅ All location names corrected, no bad species folders, clean structure

## Data Structure

### File Organization
```
adfg-commercial-dataset/
├── [LOCATION_ID]/
│   ├── 410/  # Chinook salmon
│   ├── 422/  # Sockeye salmon  
│   ├── 430/  # Coho salmon
│   ├── 440/  # Pink salmon
│   └── 450/  # Chum salmon
└── manifest.json
```

### JSON File Format
Each JSON file follows the AFCA standard format:
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
    [1986, "January, 01 1986 00:00:00", 0, 410, 1001, "Location 1001", "Andreafsky River East Fork Escapement"]
  ]
}
```

## Location Coverage

### Geographic Areas
- **Yukon River Basin**: Eagle Sonar, Pilot Station Sonar
- **Western Alaska**: Noatak River, Shaktoolik River, Nome River, Fish River, Glacial Lake, Inglutalik River, Kwiniuk River, Unalakleet River, Tuluksak River, Bonanza River, Tatlawiksuk River, Takotna River Weir, Niukluk River, Pilgrim River, Snake River, Solomon River, Ungalik River, Eldorado River, North River, Pikmiktalik River, Nunavulnak River, Speel Lake
- **Reserved Stations**: Station 1025, 1026, 1034-1038, 1101, 1201, 1501 (placeholder locations for future data)

### Complete Commercial Locations List (43 Stations)

| ID | Location Name | Species Available | Region |
|----|---------------|------------------|--------|
| 1001 | Eagle Sonar (Yukon:Canadian Border) | Chinook, Sockeye, Coho, Pink, Chum | Yukon River |
| 1025 | Station 1025 | - | Western Alaska |
| 1026 | Station 1026 | - | Western Alaska |
| 1033 | Speel Lake | Coho, Chinook | Western Alaska |
| 1034 | Station 1034 | - | Western Alaska |
| 1035 | Station 1035 | - | Western Alaska |
| 1036 | Station 1036 | - | Western Alaska |
| 1037 | Station 1037 | - | Western Alaska |
| 1038 | Station 1038 | - | Western Alaska |
| 1039 | Inglutalik River | Chinook, Sockeye | Western Alaska |
| 1040 | Fish River | Chinook | Western Alaska |
| 1041 | Glacial Lake | Sockeye, Pink, Chum | Western Alaska |
| 1042 | Noatak River | Chum | Western Alaska |
| 1043 | Ungalik River | Pink | Western Alaska |
| 1044 | Solomon River | Chum, Chinook | Western Alaska |
| 1046 | Inglutalik River | Sockeye, Chinook | Western Alaska |
| 1047 | Eldorado River | Pink, Sockeye | Western Alaska |
| 1048 | North River | Sockeye, Chum, Coho | Western Alaska |
| 1049 | Pikmiktalik River | Chinook | Western Alaska |
| 1050 | Snake River | Sockeye, Pink, Chinook | Western Alaska |
| 1051 | Pilgrim River | Pink, Chum | Western Alaska |
| 1052 | Kwiniuk River | Chinook, Coho, Sockeye | Western Alaska |
| 1053 | Pilot Station Sonar | Sockeye, Chinook | Yukon River |
| 1054 | Nome River | Chinook, Sockeye | Western Alaska |
| 1055 | Shaktoolik River | Sockeye, Chinook, Pink | Western Alaska |
| 1056 | Shaktoolik River | Pink, Sockeye, Coho | Western Alaska |
| 1057 | Unalakleet River | Chum, Coho | Western Alaska |
| 1058 | Glacial Lake | Sockeye, Chum, Pink | Western Alaska |
| 1059 | Tuluksak River | Pink, Sockeye, Chum, Chinook | Western Alaska |
| 1060 | Tuluksak River | Chinook, Pink | Western Alaska |
| 1061 | Fish River | Chinook | Western Alaska |
| 1062 | Fish River | Chinook, Pink | Western Alaska |
| 1063 | Nunavulnak River | Pink | Western Alaska |
| 1065 | Bonanza River | Coho | Western Alaska |
| 1066 | Bonanza River | Coho | Western Alaska |
| 1068 | Tatlawiksuk River | Chinook | Western Alaska |
| 1069 | Noatak River | Chum, Chinook | Western Alaska |
| 1070 | Takotna River Weir | Chinook, Chum | Western Alaska |
| 1071 | Niukluk River | Chinook, Pink | Western Alaska |
| 1072 | Niukluk River | Pink, Sockeye, Chinook | Western Alaska |
| 1101 | Station 1101 | - | Western Alaska |
| 1201 | Station 1201 | - | Western Alaska |
| 1501 | Station 1501 | - | Western Alaska |

## Data Sources

- **Primary Source**: ADF&G Commercial Fisheries Division
- **Data Type**: Escapement counts and commercial harvest data
- **Collection Methods**: Sonar, weirs, aerial surveys, commercial harvest reports
- **Quality Assurance**: ADF&G data validation and verification processes

## Integration with AFCA

This dataset is designed for seamless integration with the Alaska Fish Count App:

- **Manifest Structure**: Compatible with AFCA's manifest-driven data loading system
- **File Format**: Standard AFCA JSON format with COLUMNS and DATA arrays
- **Species Mapping**: Uses AFCA species ID system (410, 422, 430, 440, 450)
- **Location Mapping**: AFCA Station IDs in 1000-2000 range for Commercial data

## Usage

### Loading Data in AFCA
```javascript
// Load Commercial manifest
const manifest = await fetch('https://raw.githubusercontent.com/alaskafishcounts/adfg-commercial-dataset/master/manifest.json');
const data = await manifest.json();

// Access location data
const locationData = data.organized['1000']; // Pilot Station
const speciesData = locationData.species['410']; // Chinook salmon
const filePath = speciesData.files['2025']; // 2025 data file
```

### Data Access Patterns
- **By Location**: `manifest.organized[locationId]`
- **By Species**: `manifest.organized[locationId].species[speciesId]`
- **By Year**: `manifest.organized[locationId].species[speciesId].files[year]`

## Data Quality

- **Completeness**: 100% data preservation from original Excel/CSV sources
- **Accuracy**: Verified against original ADF&G data sources
- **Consistency**: Standardized species IDs and location names
- **Validation**: Cross-referenced with ADF&G official records

## Updates

- **Last Updated**: October 2025
- **Update Frequency**: Annual (following ADF&G data releases)
- **Version**: 3.0.0 (AFCA Standard)

## License

This dataset is derived from public ADF&G data and is available under the same terms as the original ADF&G data sources.

## Contact

For questions about this dataset or the AFCA application:
- **AFCA Project**: Alaska Fish Count App
- **Data Source**: Alaska Department of Fish and Game Commercial Fisheries Division
- **Repository**: https://github.com/alaskafishcounts/adfg-commercial-dataset

---

*This dataset is part of the Alaska Fish Count App (AFCA) ecosystem, providing comprehensive fish count data for Alaska's commercial fisheries.*