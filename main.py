from src import database, exporter, scraper, sites
 
database = database.Database()

def main():
    national_urls = sites.generate_national_urls(sites.TARGETS)
    black_circles_urls = sites.generate_black_circles_urls(sites.TARGETS)

    for url in national_urls:
        data = scraper.scrape_national_tyre_data(url)
        for entry in data:
            database.insert_tyre_data(entry)
    
    for url in black_circles_urls:
        data = scraper.scrape_black_circles_tyre_data(url)
        for entry in data:
            database.insert_tyre_data(entry)
    
    tyre_data = database.fetch_all_tyre_data()
    exporter.export_to_csv(tyre_data)

    database.close_connection()

if __name__ == "__main__":
    main()
