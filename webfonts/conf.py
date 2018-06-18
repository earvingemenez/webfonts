SUPPORTED_FONTS = ['.eot', '.woff', '.woff2', '.ttf', '.otf']


ANTIALIASED = "antialiased"
GRAYSCALE = "grayscale"

_WEBFONT_ATTRIBUTES = ";\n".join([
    "  font-family: {fontfamily}",
    "  src: {src}",
    "  font-style: {fontstyle}".rjust(4),
    "  -webkit-font-smoothing: {}".format(ANTIALIASED),
    "  moz-osx-font-smoothing: {}".format(GRAYSCALE)
])

WEBFONT_FORMAT = "@font-face {{\n{attributes}\n}}\n\n"

FONT_VARIABLES_FORMAT = "${fontname}: \'{fontname}\';\n"

DEFAULT_LOCURL = "/static/fonts/"

FONT_FILE = "_typography.scss"