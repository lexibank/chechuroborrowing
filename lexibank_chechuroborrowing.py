from pathlib import Path

from pylexibank.dataset import Dataset as BaseDataset
from pylexibank import progressbar
import attr
from clldutils.misc import slug
from pylexibank import Concept, Language, Lexeme, FormSpec
from pylexibank.dataset import Dataset as BaseDataset
from pylexibank.util import progressbar

@attr.s
class CustomConcept(Concept):
    Number = attr.ib(default=None)
    Russian_Gloss = attr.ib(default=None)


@attr.s
class CustomLanguage(Language):
    Source = attr.ib(default=None)
    District = attr.ib(default=None)
    Village = attr.ib(default=None)
    DataType = attr.ib(default=None)
    List_ID = attr.ib(default=None)
    SubGroup = attr.ib(default=None)

@attr.s
class CustomLexeme(Lexeme):
    Stem = attr.ib(default=None)
    EntryId = attr.ib(default=None)

class Dataset(BaseDataset):
    dir = Path(__file__).parent
    id = "chechuroborrowing"

    # add your personalized data types here
    concept_class = CustomConcept
    language_class = CustomLanguage

    # define the way in which forms should be handled
    #form_spec = FormSpec(
    #    brackets={"(": ")", "[": "]"},
    #    separators=";/,",
    #    missing_data=("?", "-"),
    #    strip_inside_brackets=True,
    #)

    def cmd_makecldf(self, args):
        """
        Convert the raw data to a CLDF dataset.
        """
        data = self.raw_dir.read_csv('words_IJB_submission.tsv', dicts=True, delimiter='\t')
        args.writer.add_sources()
        languages = args.writer.add_languages(lookup_factory="ID")
        sources = {l['ID']: l['Source'] for l in self.languages}
        concepts = {}
        for concept in self.concepts:
            idx = concept["NUMBER"].split("-")[-1] + "_" + slug(concept["ENGLISH"])
            args.writer.add_concept(
                    ID=idx,
                    Name=concept['ENGLISH'],
                    Concepticon_ID=concept['CONCEPTICON_ID'],
                    Concepticon_Gloss=concept['CONCEPTICON_GLOSS'],
                    Russian_Gloss=concept['RUSSIAN'],
                    Number=concept['NUMBER']
                    )
            concepts[concept['NUMBER']] = idx

        for row in progressbar(data, desc="cldfify"):
            lexeme = args.writer.add_form(
                    Language_ID=languages[row['Code']],
                    Parameter_ID=concepts[row['Concept nr.']],
                    Value=row['Standard Transcription'],
                    Form=row['Standard Transcription'],
                    Source=languages[row['Code']]
                    )
            args.writer.add_cognate(
                    lexeme=lexeme,
                    Cognateset_ID=row['Set'].replace(' ', ''),
                    Cognate_Detection_Method='expert',
                    Source='chechuro2021'
                    )

