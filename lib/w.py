import os
from webfonts.conf import (
    _WEBFONT_ATTRIBUTES,
    WEBFONT_FORMAT,
    FONT_FILE,
    FONT_VARIABLES_FORMAT,
)


class WriteWebFont(object):
    """ Class that will generate the web font
        file.
    """
    def __init__(self, *args, **kwargs):
        self.src_format = {
            '.eot': self.f_eot,
            '.woff': self.f_woff,
            '.woff2': self.f_woff2,
            '.ttf': self.f_tff,
            '.otf': self.f_otf
        }

        return super(WriteWebFont, self).__init__()

    def write(self, location_url, fontfiles, dest_path=None):
        # write the @font-face
        for name, extensions in fontfiles.items():

            _format = _WEBFONT_ATTRIBUTES.format(
                fontfamily="\'{name}\'".format(name=name),
                src=self.font_src(os.path.join("/", location_url, name), extensions),
                fontstyle="normal"
            )

            self.write_to_file(WEBFONT_FORMAT.format(attributes=_format), dest_path)

        # add variables
        for name, extensions in fontfiles.items():
            _format = FONT_VARIABLES_FORMAT.format(fontname=name)

            self.write_to_file(_format, dest_path)


    def write_to_file(self, font_str, dest_path=None):

        # set the destination path. If not provided, generate
        # the file in the user desktop.
        dest_path = dest_path or os.path.expanduser("~/Desktop")

        with open("{path}/{file}".format(path=dest_path, file=FONT_FILE), "a") as f:
            f.write(font_str)

    def font_src(self, name, extensions):
        """ returns the concatenated src strings
        """
        def _generate_src():
            """ generate the src strings
            """
            for ext in extensions:
                yield self.src_format[ext](f="{}{}".format(name, ext))

        return ",".join([i for i in _generate_src()])


    def f_eot(self, **f):
        return "url({f}?iefix) format(\'embedded-opentype\')".format(**f)

    def f_woff(self, **f):
        return "url({f}) format(\'woff\')".format(**f)

    def f_woff2(self, **f):
        return "url({f}) format(\'woff2\')".format(**f)

    def f_tff(self, **f):
        return "url({f}) format(\'truetype\')".format(**f)

    def f_otf(self, **f):
        return "url({f})".format(**f)