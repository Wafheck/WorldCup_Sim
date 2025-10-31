import os
import pycountry
import pygal
import cairosvg
from pygal.style import Style

def generate_map(countries):
    def country_name_to_iso2(name):
        try:
            if name in ["ENGLAND", "SCOTLAND", "WALES", "NORTHERN IRELAND"]:
                name = "UNITED KINGDOM"
            country = pycountry.countries.lookup(name)
            return country.alpha_2.lower()
        except LookupError:
            return None
    country_names = [*countries]
    iso_codes = [country_name_to_iso2(name) for name in country_names]
    iso_codes = [code for code in iso_codes if code is not None]

    # Define custom style with first color green
    custom_style = Style(
        colors=('#009900',) # tuple, first color is green
    )

    worldmap = pygal.maps.world.World(style=custom_style)
    worldmap.title = 'Qualified Teams (World Cup)'
    worldmap.add('Qualified', iso_codes)

    svg_string = worldmap.render(is_unicode=True)

    png_path = os.path.abspath('qualified.png')
    cairosvg.svg2png(bytestring=svg_string.encode('utf-8'), write_to=png_path)

    print(f"Map generated:\nPNG: {png_path}")
    return png_path
