
from scrapers.example_scraper import MatchScraper
from services.analytics import Analytics

scraper = MatchScraper()
matches = scraper.fetch()

engine = Analytics()
ranking = engine.team_form(matches)

print("TEAM RANKINGS")
for t,p in ranking:
    print(t, p)
