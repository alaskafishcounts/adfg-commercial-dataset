# ADFG Commercial Fish Count Dataset

## Overview
This repository contains fish count data from the Alaska Department of Fish and Game (ADFG) Commercial Fisheries division, organized by the four management regions and their respective commercial monitoring stations.

## ADFG Commercial Fisheries Management Regions

Alaska's fisheries are managed at a local area level through four regions, each containing multiple area offices:

### 1. Arctic-Yukon-Kuskokwim Region
The Arctic-Yukon-Kuskokwim (AYK) Region encompasses the coastal waters of Alaska and includes the rivers and streams that drain into the Bering, Chukchi, and Beaufort Seas. It stretches from its boundary at Cape Newenham with the Bristol Bay area to the border with Canada on the Arctic Ocean. The Yukon River, with the fifth largest drainage in North America, lies within this management region, as do many other major rivers; the Kuskokwim being second in size next to the Yukon.

**Management Areas:**
- Yukon Management Area
- Arctic Management Area  
- Norton Sound & Kotzebue Management Areas
- Kuskokwim Management Area

**Commercial Monitoring Locations:**
- **5001-kuskokwim-river-sonar** - Kuskokwim River Commercial (Sonar)
- **5002-george-river-weir** - George River Commercial (Weir)
- **5007-norton-river-escapement** - Norton River Escapement (Weir)
- **5008-north-river-weir** - North River Commercial (Weir)
- **5009-nunakogak-river-weir** - Nunakogak River Commercial (Weir)
- **5010-yukon-river-sonar** - Yukon River Commercial (Sonar)

### 2. Central Region
Central Region Alaska commercial fisheries are composed of four distinct management areas that include Bristol Bay, Prince William Sound and Copper River, Upper Cook Inlet, and Lower Cook Inlet. Although all 5 species of salmon are harvested in each area, sockeye and pink salmon are the most abundant and most valuable. This area encompasses some of the largest and most valuable salmon fisheries in the world. From Bristol Bay, home of the largest sockeye salmon fishery in the world, to the Copper River where sockeye and Chinook salmon fetch some of the highest prices per pound paid to commercial fishermen.

**Management Areas:**
- Bristol Bay Management Area
- Cook Inlet Management Area
- Upper Cook Inlet Management Area
- Lower Cook Inlet Management Area
- Prince William Sound Management Area
- Copper River Management Area

**Commercial Monitoring Locations:**
- *Additional locations to be added as data becomes available*

### 3. Southeast Alaska & Yakutat Region
The Southeast Alaska/Yakutat Region (Region I) consists of Alaska waters between Cape Suckling on the north and Dixon Entrance on the south. Salmon are commercially harvested in Southeast Alaska with purse seines and drift gillnets; in Yakutat with set gillnets; and in both areas with hand and power troll gear. Herring are harvested in winter bait, sac roe, spawn-on-kelp, and bait pound fisheries. Miscellaneous shellfish (sea cucumber, sea urchins, and geoduck clams) are harvested in dive fisheries in the region.

**Commercial Monitoring Locations:**
- *Additional locations to be added as data becomes available*

### 4. Westward Region
Westward Region includes the Kodiak Archipelago, the north and south sides of the Alaska Peninsula (including Chignik, the Shumagin Islands, and Port Moller), and the Aleutian Islands. Dutch Harbor, the number one fishing port in the nation, in pounds landed, is situated in the Aleutian Islands. This region encompasses all Pacific Ocean waters extending south from the Kodiak Archipelago and west of the longitude of the eastern side of Cook Inlet, as well as Bering Sea waters east of the maritime boundary between Russia and the United States.

**Management Areas:**
- Kodiak Management Area
- Chignik Management Area
- Alaska Peninsula Management Area
- Bering Sea/Aleutians Islands Area

**Commercial Monitoring Locations:**
- **6001-bear-river-weir** - Bear River Weir (Sockeye)
- **6002-ilnik-river-weir** - Ilnik River Weir (Sockeye)
- **6003-mclees-lake-weir** - McLees Lake Weir (Sockeye)
- **6004-nelson-river-weir** - Nelson River Weir (Sockeye)
- **6005-orzinski-lake-weir** - Orzinski Lake Weir (Sockeye)
- **6006-sandy-river-weir** - Sandy River Weir (Sockeye)

## Data Source
- **Primary Source**: [ADFG Commercial Fisheries](https://www.adfg.alaska.gov/index.cfm?adfg=fishingcommercialbyarea.interior)
- **Data Format**: CSV/Excel files from ADFG commercial archives
- **Coverage**: Historical fish count data from commercial monitoring stations across all four regions
- **Update Frequency**: Manual updates from ADFG commercial sites

## Project Description
The Kuskokwim River is the second largest drainage in Alaska, flowing west approximately 730 km from the confluence of its east and north forks to the Bering Sea. The glacially fed north fork originates northwest of Denali in the Kuskokwim Mountains and Alaska Range, bringing the total length to 1,130 km.

**Sonar Project Details:**
- Location: 130 river km upriver from confluence of Kuskokwim River and Church Slough (20 river km upriver from Bethel)
- River width: 450 m bankfull width at sonar site
- Technology: Combination of split-beam and imaging sonar
- Methodology: Drift gillnet fishing used to apportion counts
- Operation period: June 1 - August 26 (extended from July 26 since 2020)

## Repository Structure
```
adfg-commercial-dataset/
├── data/                           # Converted JSON data files
│   ├── manifest.json              # File organization index
│   ├── 01-master/                 # Master location and species data
│   └── ADFGC-REGION-LOCATION-METHOD/  # Location-based organization
│       ├── location-info.json     # Location metadata
│       └── SPECIES-NAME/          # Species-based organization
│           └── YEAR_filename.json # Individual year files
├── scripts/                       # Data processing scripts
│   ├── csv-to-afca.py            # CSV to AFCA JSON converter
│   ├── validate-data.py          # Data validation script
│   └── update-manifest.py        # Manifest update script
├── docs/                          # Documentation
│   ├── data-schema.md            # Data format documentation
│   └── conversion-log.md         # Conversion process log
├── workflows/                     # GitHub Actions workflows
│   └── data-sync.yml             # Automated data sync workflow
└── README.md                     # This file
```

## Naming Conventions

### Location IDs
- **Format**: `ADFGC-REGION-LOCATION-METHOD`
- **Examples**:
  - `ADFGC-NORTON-YUKON-RIVER` (Norton Sound region, Yukon River, Commercial)
  - `ADFGC-AP-MCLEES-LAKE-WEIR` (Alaska Peninsula region, McLees Lake, Weir)

### Species Folders
- **Format**: `SPECIES-NAME`
- **Examples**:
  - `Chinook-Salmon/` (instead of numeric IDs)
  - `Sockeye-Salmon/`

### File Names
- **Format**: `YEAR_location_species_type.json`
- **Examples**:
  - `2023_Location-ADFGC-1009_Chinook_escapement.json`
  - `2008_mclees-lake-weir-annual-summary.json`

## Data Format
All data follows the AFCA v1.0.1 JSON format:
```json
{
  "DATA": [
    {
      "date": "YYYY-MM-DD",
      "count": number,
      "species": "species_name",
      "location": "location_name",
      "method": "sonar|weir|visual",
      "notes": "additional_information"
    }
  ],
  "metadata": {
    "source": "ADFG Commercial Fisheries",
    "location": "location_details",
    "method": "monitoring_method",
    "period": "operation_period",
    "last_updated": "timestamp"
  }
}
```

## Usage
1. **Data Conversion**: Use `scripts/csv-to-afca.py` to convert CSV files to AFCA format
2. **Validation**: Run `scripts/validate-data.py` to check data quality
3. **Manifest Update**: Use `scripts/update-manifest.py` to update file organization
4. **Deployment**: Data is automatically synced via GitHub Actions

## Integration with AFCA
This dataset integrates with the Alaska Fish Count App (AFCA) v1.0.1:
- Follows same manifest-driven data loading system
- Compatible with existing AFCA components
- Uses same location and species ID system
- Maintains data consistency with main AFCA dataset

## License
Data sourced from Alaska Department of Fish and Game - Commercial Fisheries Division.
All data is public domain and available for research and educational purposes.

## Contributing
1. Download CSV files from ADFG commercial site
2. Convert using provided scripts
3. Validate data quality
4. Submit pull request with converted data
5. Update documentation as needed

## Contact
For questions about this dataset, please refer to the main AFCA project documentation.
