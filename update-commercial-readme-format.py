#!/usr/bin/env python3
"""
Update Commercial README to Match Sport Format
==============================================

This script updates the Commercial README to match the Sport README format
with the same sections, structure, and styling.
"""

import json
import os
import re
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Set
from datetime import datetime

def extract_location_info_from_filenames(dataset_path: Path) -> Dict[str, Dict]:
    """Extract location information from JSON filenames."""
    location_info = defaultdict(lambda: {
        'name': '',
        'species': set(),
        'years': set(),
        'files': []
    })
    
    # Pattern to match: YEAR-location-name-species.json
    pattern = r'(\d{4})-(.+)-([^-]+)\.json'
    
    for json_file in dataset_path.rglob('*.json'):
        if json_file.name == 'manifest.json':
            continue
            
        filename = json_file.name
        match = re.match(pattern, filename)
        
        if match:
            year, location_name, species = match.groups()
            
            # Clean up location name (replace hyphens with spaces, title case)
            clean_location = location_name.replace('-', ' ').title()
            
            # Get location ID from directory structure
            location_id = json_file.parent.parent.name
            
            location_info[location_id]['name'] = clean_location
            location_info[location_id]['species'].add(species.title())
            location_info[location_id]['years'].add(year)
            location_info[location_id]['files'].append(json_file)
    
    return dict(location_info)

def get_species_id_mapping(species_name: str) -> str:
    """Convert species name to ID."""
    species_map = {
        'Chinook': '410',
        'Sockeye': '420', 
        'Coho': '430',
        'Pink': '440',
        'Chum': '450'
    }
    return species_map.get(species_name, '410')  # Default to Chinook if not found

def generate_readme_content(location_info: Dict[str, Dict]) -> str:
    """Generate README.md content matching Sport format."""
    
    # Sort locations by ID (only numeric IDs)
    sorted_locations = sorted([(k, v) for k, v in location_info.items() if k.isdigit()], key=lambda x: int(x[0]))
    
    # Calculate totals
    total_files = sum(len(info['files']) for info in location_info.values())
    all_years = set()
    for info in location_info.values():
        all_years.update(info['years'])
    year_range = f"{min(all_years)}-{max(all_years)}" if all_years else "Unknown"
    
    # Current date
    current_date = datetime.now().strftime("%B %d, %Y")
    
    readme_content = f"""# ADF&G Commercial Fisheries Dataset

## Overview

This dataset contains commercial fish count data from Alaska Department of Fish and Game (ADF&G) monitoring stations across Alaska. The data spans multiple years and includes various salmon species counts from commercial fishing operations.

## Geographic Areas

- **Active Commercial Stations:** {len(location_info)} monitoring stations across Alaska
- **Species Coverage:** Chinook, Sockeye, Coho, Pink, and Chum salmon
- **Temporal Coverage:** Historical data from commercial fishing operations

## Complete Commercial Locations List ({len(location_info)} Stations)

| Location ID | Location Name | Species Available |
|-------------|---------------|-------------------|
"""
    
    for location_id, info in sorted_locations:
        species_list = sorted(info['species'])
        species_links = []
        
        for species in species_list:
            species_id = get_species_id_mapping(species)
            species_link = f'[{species.lower()}](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/{location_id}/{species_id})'
            species_links.append(species_link)
        
        species_links_text = ', '.join(species_links)
        location_link = f'[{info["name"]}](https://github.com/alaskafishcounts/adfg-commercial-dataset/tree/master/{location_id})'
        
        readme_content += f"| {location_id} | {location_link} | {species_links_text} |\n"
    
    readme_content += f"""
_This table shows all {len(location_info)} locations in the commercial dataset following AFCA Location Codes Framework (1000-2999 range). Each location folder contains species-specific subdirectories with current commercial fishing data._

## 📊 Data Format

All files follow the ADFG standard format with consistent column structure:

```json
{{
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
      2002,
      "May, 26 2002 00:00:00",
      3,
      410,
      1001,
      "Akalura River",
      "Chinook"
    ]
  ],
  "metadata": {{
    "location_id": 1001,
    "location_name": "Akalura River",
    "species_id": 410,
    "species_name": "Chinook Salmon",
    "year": 2002,
    "last_updated": "{current_date}T10:00:00Z",
    "data_source": "ADF&G Commercial"
  }}
}}
```

## 🏔️ Regional Organization

All COMMERCIAL locations use AFCA IDs 1000–2999\. Regional grouping is not encoded in the ID range.

## 🔄 Related Datasets

* **Sport Dataset**: Current sport fishing data (0-100 range)
* **SASAP Dataset**: Historical escapement data (2000-2999 range)
* **Commercial Dataset**: Commercial fishing data (1000-1999 range) - _This dataset_

## 📄 License & Attribution

This data is in the **Public Domain** and available for unrestricted use.

When using this data, please attribute:

* **Data Source**: Alaska Department of Fish & Game (ADF&G)
* **Repository**: alaskafishcounts/adfg-commercial-dataset
* **Application**: Alaska Fish Count App
* **Framework**: AFCA Location Codes Framework

## 📞 Contact Support

* **GitHub Issues**: Report problems via repository Issues
* **Data Source**: Alaska Department of Fish & Game
* **Repository**: alaskafishcounts/adfg-commercial-dataset

---

**Last Updated**: {current_date}  
**Version**: AFCA v1.0.1  
**Data Source**: Alaska Department of Fish & Game (ADF&G)  
**Framework**: AFCA Location Codes Framework  
**Repository**: alaskafishcounts/adfg-commercial-dataset

## About

ADFG Commercial Fish Count Dataset - {len(all_years)} years of commercial fishing data ({year_range}) across {len(location_info)} locations and 5 species

### Resources

Readme 

Activity 

### Stars

**1** star 

### Watchers

**0** watching 

### Forks

**0** forks 

Report repository 

## Releases

No releases published

## Packages0

No packages published   

## Contributors3

## Footer

© 2025 GitHub, Inc. 

### Footer navigation

* Terms
* Privacy
* Security
* Status
* Community
* Docs
* Contact
* Manage cookies
* Do not share my personal information
"""
    
    return readme_content

def main():
    """Main function to update README.md with Sport format."""
    dataset_path = Path(".")
    
    if not dataset_path.exists():
        print(f"❌ Dataset path not found: {dataset_path}")
        return
    
    print(f"🔍 Extracting location information from {dataset_path}...")
    location_info = extract_location_info_from_filenames(dataset_path)
    
    print(f"📊 Found {len(location_info)} locations")
    
    print(f"📝 Generating updated README.md matching Sport format...")
    readme_content = generate_readme_content(location_info)
    
    readme_path = dataset_path / "README.md"
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print(f"✅ README.md updated with Sport format: {readme_path}")
    print(f"📄 File size: {len(readme_content)} characters")

if __name__ == "__main__":
    main()