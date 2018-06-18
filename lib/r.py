import os
from os import walk

from .w import WriteWebFont
from webfonts.conf import SUPPORTED_FONTS


class Inspect(WriteWebFont):
    """ Class that will read the font files located
        in a specific directory.
    """
    def __init__(self, *args, **kwargs):
        self.fonts_path = kwargs.get('fonts_path')
        return super(Inspect, self).__init__(*args, **kwargs)

    def read(self):
        for (dirpath, dirnames, filenames) in walk(self.fonts_path):
            # exclude hidden dir since we don't store
            # the fonts in a hidden directory
            if "." in self.get_dirname(dirpath): continue

            # exclude dir without font files
            fontfiles = self.filter_fontfiles(filenames)
            if not fontfiles: continue

            # modify the dirpath to dirurl
            dirurl = self.get_dirurl(dirpath)

            yield dirurl, fontfiles

    def get_dirname(self, dirpath):
        """ return the dir name
        """
        return dirpath.split('/')[-1]

    def get_dirurl(self, dirpath):
        """ return the dir url
        """
        paths = dirpath.split("/")

        return "/".join(paths[paths.index("static"):])

    def filter_fontfiles(self, filenames, d=dict()):
        """ filter to return font files only
        """
        for f in filenames:
            n, ext = os.path.splitext(f)
            # skip for the files that are not supported
            if not ext in SUPPORTED_FONTS: continue

            d[n] =  d[n] + [ext] if d.get(n) else [ext]
        return d