from pathlib import Path

from amilib.file_lib import FileLib
from climate.un import IPCC


class TestSearch:

    def test_search_all_chapters_with_query_words(self, outfile=None):
        """
        read chapter, search for words and return list of paragraphs/ids in which they occur
        simple, but requires no server
        """

        query = "south_asia"
        indir = Path(Path(__file__).parent.parent, "ar6", "test")
        outfile = Path(indir, f"{query}.html")
        debug = False
        globstr = f"{str(indir)}/**/{HTML_WITH_IDS_HTML}"
        infiles = FileLib.posix_glob(globstr, recursive=True)
        print(f"{len(infiles)} {infiles[:2]}")
        phrases = [
            "bananas",
            "South Asia",
        ]
        html1 = IPCC.create_hit_html(infiles, phrases=phrases, outfile=outfile, debug=debug)
        assert html1 is not None
        assert len(html1.xpath("//p")) > 0

