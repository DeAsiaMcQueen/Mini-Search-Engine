# Mini-Search-Engine
## **Introduction**
The Mini Search Engine is a Python-based application that simplifies file and concept searches. It features a dual-function GUI that allows users to search their local device directories for specific files based on keywords and perform detailed concept or historical searches using Wikipedia API. This project showcases the power of Python's file-handling capabilities and API integration.
## **Features**
1.  Historical/Concept Search:
  - Fetch concise summaries of historical events, concepts, or figures.
  - Provides clickable links for in-depth exploration.
  - Recommends learning resources tailored to the topic.
2. Device File Search:
  - Search local device directories for `.txt,` `.docx,` `.pdf,` and `.xlsx` files.
  - Keyword-based file content matching.
  - Clickable links to open found files directly from the GUI.
3. User-Friendly GUI:
  - Simple tab-based navigation for different search modes.
  - Clear results display with interactive elements.
## **Requirements**
- Python 3.9 or later
- The following libraries (install via `requirements.txt`):
  - `requests`
  - `pandas`
  - `PyPDF2`
  - `python-docx`
- A Windows system with access to directories like Documents, Desktop, and Downloads.
- A working internet connection for concept/historical searches.
## **Installation**
1. Clone the Repository:
   ```bash
   git clone https://github.com/YourUsername/Mini-Search-Engine.git
   cd Mini-Search-Engine
2. Install dependiences
   - pip install -r requirements.txt
3. Run application
   -python mini-search-engine.py
## **Usage**
1. Launch the Application:
   - Run the script to open the GUI.
2. Historical/Concept Search:
   - Enter a topic or keyword in the provided field.
   - Click "Search" to view a detailed summary and recommended learning resources.
   - Click on links for further exploration.
3. Device File Search:
   - Select a directory from the dropdown (e.g., Documents, Downloads).
   - Choose the file type to search (e.g., `.txt`, `.docx`).
   - Enter a keyword to search within the selected file type.
   - View results with clickable links to open matching files.
## **Future Enhancements**
- Additional File Types:
  - Support for schematic files and 3D printed file formats.
- Cross-Platform Support:
  - Adapt for macOS and Linux systems.
- Enhanced Search Features:
  - Add advanced filtering (e.g., by file size or modification date).
- Learning Resources Integration:
  - Expand learning resources with more APIs or curated datasets.
## **License**
This project is licensed under the MIT License. 
You are free to use, modify, and distribute this project under the following conditions:
- Attribution: Include a copy of this license and attribution to the original author.
- No Liability: The software is provided "as is", without warranty of any kind.
Please look at this repository's [LICENSE](LICENSE) file for more details.
