from taipy.gui import Gui
import taipy as tp

from pages.home.home import home_md
from pages.country.country import country_md
from pages.company.company import company_md
# from pages.world.world import world_md
# from pages.map.map import map_md
# from pages.predictions.predictions import predictions_md, selected_scenario
from pages.root import root
from pages.country.country import selected_country, selector_country
from pages.company.company import selected_company, selector_company

from config.config import Config

pages = {
    '/': root,
    'Home': home_md,
    'Company': company_md,
    'Country': country_md
    # "Country": country_md,
    # "World": world_md,
    # "Map": map_md,
    # "Predictions": predictions_md
}

gui_multi_pages = Gui(pages=pages)

if __name__ == '__main__':
    tp.Core().run()

    gui_multi_pages.run(title="My first Dashboard")