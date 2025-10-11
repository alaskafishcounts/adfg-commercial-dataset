# ADF&G Commercial Fisheries Dataset

## Overview

This dataset contains commercial fish count data from ADF&G monitoring stations across Alaska. The dataset has been completely reorganized and deduplicated to include all available commercial fishing locations.

## Dataset Statistics

- **Total Locations**: 49
- **Total Files**: 1464
- **Total Records**: 142,949
- **Year Range**: 1965-2025
- **Last Updated**: 2025-10-10

## Location Directory Structure

```
adfg-commercial-dataset/
├── [location-name]/
│   ├── [species-id]/
│   │   ├── [year]-[location]-[species].json
│   │   └── ...
│   └── ...
└── ...
```

## Commercial Fishing Locations

| Location | Species | Years | Files | Available Species |
|----------|---------|-------|-------|-------------------|
| Andreafsky River East Fork | 5 | 1981-2024 | 135 | 430 Chum Salmon, 440 Coho Salmon, 410 Chinook Salmon, 420 Sockeye Salmon, 450 Pink Salmon |
| Anvik River Escapement | 3 | 1972-2025 | 77 | 430 Chum Salmon, 410 Chinook Salmon, 450 Pink Salmon |
| Barton Creek Escapement | 2 | 1994-1994 | 2 | 450 Chum Salmon, 430 Coho Salmon |
| Big Salmon River Escapement | 1 | 2024-2024 | 1 | 420 Sockeye |
| Blind Creek Escapement | 1 | 2024-2024 | 1 | 420 Sockeye |
| Bonanza River | 6 | 2018-2020 | 16 | Coho, Bonanza River Pink, Bonanza River Coho, Bonanza River Chinook, Bonanza River Sockeye, Bonanza River Chum |
| Bristol Bay Mariner | 1 | 2023-2025 | 6 | 420 Sockeye Salmon |
| Eagle Sonar Yukoncanadian Border | 1 | 1981-2024 | 37 | Andreafsky River East Fork Escapement |
| Egegik | 1 | 2023-2023 | 1 | Egegik |
| Eldorado River | 7 | 1995-2025 | 148 | Eldorado River Pink, Pink, Eldorado River Coho, Eldorado River Sockeye, Eldorado River Chinook, Sockeye, Eldorado River Chum |
| Fish River | 1 | 2014-2014 | 1 | Chinook |
| Fishing Branch River Escapement | 1 | 2024-2024 | 1 | 420 Sockeye |
| George River Weir | 2 | 1993-2025 | 93 | 410 Chinook Salmon, 410 Chinook |
| Gisasa River Escapement | 4 | 1994-2023 | 65 | 430 Chum Salmon, 410 Chinook Salmon, 420 Sockeye Salmon, 450 Pink Salmon |
| Glacial Lake | 3 | 2000-2014 | 4 | Chum, Pink, Sockeye |
| Goodnews River Middle Fork Escapement | 1 | 2024-2024 | 1 | 420 Sockeye |
| Goodpaster River Escapement | 1 | 2004-2018 | 15 | 410 Chinook Salmon |
| Henshaw Creek Escapement | 2 | 1999-2021 | 40 | 430 Chum Salmon, 410 Chinook Salmon |
| Inglutalik River | 2 | 2011-2020 | 2 | Chinook, Sockeye |
| Klondike River Escapement | 1 | 2024-2024 | 1 | 420 Sockeye |
| Kuskokwim River Sonar | 2 | 1981-2025 | 128 | 410 Chinook Salmon, 410 Chinook |
| Kwiniuk River | 3 | 1965-2005 | 3 | Coho, Chinook, Sockeye |
| Location 1025 | 1 | 2018-2025 | 8 | Kuskokwim River Sonar |
| Mclees Lake Weir | 1 | 2001-2014 | 15 | 420 Sockeye |
| Niukluk River | 2 | 1979-1995 | 2 | Chinook, Pink |
| Noatak River | 1 | 1981-1981 | 1 | Chum |
| Nome River | 2 | 1993-1999 | 2 | Chinook, Sockeye |
| North River | 3 | 1972-2016 | 3 | Chum, Coho, Sockeye |
| North River Weir | 1 | 1972-2025 | 72 | 410 Chinook |
| Norton River Escapement | 2 | 1965-2025 | 152 | 410 Chinook Salmon, 410 Chinook |
| Nunakogak River Weir | 1 | 1992-1992 | 2 | 410 Chinook |
| Nunavulnak River | 1 | 1992-1992 | 1 | Pink |
| Pikmiktalik River | 1 | 1992-1992 | 1 | Chinook |
| Pilgrim River | 2 | 1997-2000 | 2 | Chum, Pink |
| Pilot Station Escapement | 4 | 1995-2025 | 94 | 440 Coho Salmon, 410 Chinook Salmon, 420 Sockeye Salmon, 450 Pink Salmon |
| Pilot Station Sonar | 2 | 1995-2022 | 2 | Chinook, Sockeye |
| Salmon River Aniak Escapement | 1 | 2024-2024 | 1 | 420 Sockeye |
| Salmon River Pitka Fork Escapement | 1 | 2024-2024 | 1 | 420 Sockeye |
| Shaktoolik River | 2 | 1996-2019 | 2 | Pink, Sockeye |
| Snake River | 3 | 1995-2002 | 3 | Chinook, Pink, Sockeye |
| Solomon River | 2 | 2013-2015 | 2 | Chum, Chinook |
| Takotna River Weir | 5 | 2000-2025 | 5 | Chinook, Takotna River Weir Coho, Takotna River Weir Chinook, Takotna River Weir Chum, Takotna River Weir Sockeye |
| Tatlawiksuk River | 5 | 1999-2025 | 5 | Tatlawiksuk River Coho, Tatlawiksuk River Chum, Chinook, Tatlawiksuk River Chinook, Tatlawiksuk River Sockeye |
| Telaquana River | 6 | 2010-2025 | 6 | Coho, Telaquana River Chum, Telaquana River Sockeye, Sockeye, Telaquana River Coho, Telaquana River Chinook |
| Tuluksak River | 7 | 1991-2025 | 7 | Tuluksak River Chinook, Tuluksak River Coho, Tuluksak River Chum, Tuluksak River Sockeye, Chinook, Pink, Tuluksak River Pink |
| Unalakleet River | 1 | 2010-2010 | 1 | Chum |
| Ungalik River | 1 | 2020-2020 | 1 | Pink |
| Whitehorse Dam Fishway Escapement | 1 | 2024-2024 | 1 | 420 Sockeye |
| Yukon River Sonar | 1 | 1972-2025 | 294 | 410 Chinook |

## Data Format

Each JSON file contains fish count data in the following format:

```json
{
  "COLUMNS": ["YEAR", "MONTH", "DAY", "SPECIESID", "COUNTLOCATIONID", "COUNTLOCATION", "SPECIES", "COUNT"],
  "DATA": [
    [2024, 7, 1, 420, 1001, "Location Name", "Sockeye", 150]
  ]
}
```

## Species Codes

- **410**: Chinook Salmon
- **420**: Sockeye Salmon  
- **430**: Coho Salmon
- **440**: Pink Salmon
- **450**: Chum Salmon
- **460**: Steelhead Trout

## Usage

This dataset is designed for use with the Alaska Fish Count App (AFCA) and provides comprehensive commercial fishing data for analysis and visualization.

## Data Sources

- ADF&G Commercial Fisheries Division
- Historical Escapement Monitoring
- Sonar and Weir Counts
- Daily and Cumulative Passage Data

## License

This dataset is provided for research and educational purposes. Please cite ADF&G as the original data source.
