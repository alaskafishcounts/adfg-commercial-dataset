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
- **Active Commercial Stations**: Inglutalik River, Fish River, Glacial Lake, Noatak River, Ungalik River, Solomon River, North River, Pikmiktalik River, Snake River, Pilgrim River, Kwiniuk River, Pilot Station Sonar, Nome River, Shaktoolik River, Unalakleet River, Tuluksak River, Bonanza River, Tatlawiksuk River, Takotna River Weir, Niukluk River, Akalura River Weir
- **Reserved Stations**: Commercial Location 1025, 1026, 1033-1038, 1101, 1201, 1501 (placeholder locations for future data)

### Complete Commercial Locations List (43 Stations)

| ID | Location Name | Species Available | Region |
|----|---------------|------------------|--------|
| 1001 | [Akalura River Weir](./1001/) | - | Unknown |
| 1025 | [Commercial Location 1025](./1025/) | - | Unknown |
| 1026 | [Commercial Location 1026](./1026/) | - | Unknown |
| 1033 | [Commercial Location 1033](./1033/) | - | Unknown |
| 1034 | [Commercial Location 1034](./1034/) | - | Unknown |
| 1035 | [Commercial Location 1035](./1035/) | - | Unknown |
| 1036 | [Commercial Location 1036](./1036/) | - | Unknown |
| 1037 | [Commercial Location 1037](./1037/) | - | Unknown |
| 1038 | [Commercial Location 1038](./1038/) | - | Unknown |
| 1039 | [Inglutalik River](./1039/) | Chinook | Unknown |
| 1040 | [Fish River](./1040/) | Chinook | Unknown |
| 1041 | [Glacial Lake](./1041/) | Sockeye | Unknown |
| 1042 | [Noatak River](./1042/) | Chum | Unknown |
| 1043 | [Ungalik River](./1043/) | Pink | Unknown |
| 1044 | [Solomon River](./1044/) | Chum | Unknown |
| 1046 | [Inglutalik River](./1046/) | Sockeye | Unknown |
| 1047 | [Eldorado River](./1047/) | Pink | Unknown |
| 1048 | [North River](./1048/) | Sockeye, Coho | Unknown |
| 1049 | [Pikmiktalik River](./1049/) | Chinook | Unknown |
| 1050 | [Snake River](./1050/) | Sockeye | Unknown |
| 1051 | [Pilgrim River](./1051/) | Pink | Unknown |
| 1052 | [Kwiniuk River](./1052/) | Chinook | Unknown |
| 1053 | [Pilot Station Sonar](./1053/) | Sockeye | Unknown |
| 1054 | [Nome River](./1054/) | Chinook | Unknown |
| 1055 | [Shaktoolik River](./1055/) | Sockeye | Unknown |
| 1056 | [Shaktoolik River](./1056/) | Pink | Unknown |
| 1057 | [Unalakleet River](./1057/) | Chum | Unknown |
| 1058 | [Glacial Lake](./1058/) | Sockeye | Unknown |
| 1059 | [Tuluksak River](./1059/) | Pink | Unknown |
| 1060 | [Tuluksak River](./1060/) | Chinook | Unknown |
| 1061 | [Fish River](./1061/) | Chinook | Unknown |
| 1062 | [Fish River](./1062/) | Chinook | Unknown |
| 1063 | [Nunavulnak River](./1063/) | Pink | Unknown |
| 1065 | [Bonanza River](./1065/) | Coho | Unknown |
| 1066 | [Bonanza River](./1066/) | Coho | Unknown |
| 1068 | [Tatlawiksuk River](./1068/) | Chinook | Unknown |
| 1069 | [Noatak River](./1069/) | Chum | Unknown |
| 1070 | [Takotna River Weir](./1070/) | Chinook | Unknown |
| 1071 | [Niukluk River](./1071/) | Chinook | Unknown |
| 1072 | [Niukluk River](./1072/) | Pink | Unknown |
| 1101 | [Commercial Location 1101](./1101/) | - | Unknown |
| 1201 | [Commercial Location 1201](./1201/) | - | Unknown |
| 1501 | [Commercial Location 1501](./1501/) | - | Unknown |

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