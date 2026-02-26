# Documentation_quality_validator
Built a Python tool to validate documentation metadata (in csv): detects duplicates and missing and outdated version.

### Install guide: 
#### Prerequisites
- Python 3.8+ installed
- Run from terminal or PowerShell, no IDE required
- Files: main.py, documentValidator.py and docs.csv in the same folder

#### Run the tool:
- Open PowerShell (or terminal) in the folder with your files

#### Basic usage:
python main.py <csv_file> <delimiter> <lower_bound>
<csv_file> -> path to your CSV
<delimiter> -> CSV separator
<lower_bound> -> lower bound for checking document' update times 
-- help -> usage instructions


#### Example CSV format your validator expects:
doc_id,title,version,status,last_updated
M001,Motor Manual,1.0,approved,2023-01-01
M002,Installation Guide,,draft,2021-03-12
C201,Cable Guide,2.1,review,2019-05-01
