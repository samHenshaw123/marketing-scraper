# marketing-scraper

A web scraper designed for collating tyre specifications using Python and MongoDB for marketing solutions.

---

## Project Overview

This project is a Python-based web scraper tailored for extracting tyre specifications from various sources and storing them in a MongoDB database. The extracted data is useful for marketing analytics and solutions in the tyre industry.

---

## Features

- Scrapes tyre specification data from selected websites
- Stores data in a MongoDB database
- Exports data to a CSV file for easy analysis and sharing
- Configurable and extensible scraper logic

---

## Getting Started

### Prerequisites

- Python 3.8+
- MongoDB (local or remote instance)
- Git

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/samHenshaw123/marketing-scraper.git
   cd marketing-scraper
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

### Configuration

- Update your MongoDB connection string in `config.py` or as an environment variable, depending on your project setup.
- Adjust scraping URLs and parameters in the sites script as needed.

### Running the Scraper

```sh
python main.py
```

The script will fetch tyre specification data and save it to your MongoDB database. After scraping, it will export the data to a CSV file with a unique timestamp.

---

## Database Structure

The scraper stores data in a MongoDB collection named `tyres`. You can find the exported MongoDB structure in [`schema-marketing_scraper-tyres-mongoDBJSON.json`](schema-marketing_scraper-tyres-mongoDBJSON.json).

---

### CSV File

You can find the CSV export in [`tyres_export.csv`](tyres_export.csv).

---

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for more information.

---

## Public Project Location

Repository: [https://github.com/samHenshaw123/marketing-scraper](https://github.com/samHenshaw123/marketing-scraper)

Exports:
- [schema-marketing_scraper-tyres-mongoDBJSON.json](schema-marketing_scraper-tyres-mongoDBJSON.json)
- [tyres_export.csv](tyres_export.csv)

---
