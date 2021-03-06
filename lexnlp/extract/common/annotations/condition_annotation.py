from typing import Tuple, List
from lexnlp.extract.common.annotations.text_annotation import TextAnnotation

__author__ = "ContraxSuite, LLC; LexPredict, LLC"
__copyright__ = "Copyright 2015-2020, ContraxSuite, LLC"
__license__ = "https://github.com/LexPredict/lexpredict-lexnlp/blob/master/LICENSE"
__version__ = "1.6.0"
__maintainer__ = "LexPredict, LLC"
__email__ = "support@contraxsuite.com"


class ConditionAnnotation(TextAnnotation):
    record_type = 'condition'
    """
    create an object of ConditionAnnotation like
    cp = ConditionAnnotation(name='name', coords=(0, 100), text='text text')
    """
    def __init__(self,
                 coords: Tuple[int, int],
                 locale: str = 'en',
                 text: str = None,
                 condition: str = None,
                 pre: str = None,
                 post: str = None):
        super().__init__(
            name='',
            locale=locale,
            coords=coords,
            text=text)
        self.condition = condition
        self.pre = pre
        self.post = post

    def get_cite_value_parts(self) -> List[str]:
        parts = [self.condition or '',
                 self.pre or '',
                 self.post or '']
        return parts

    def get_dictionary_values(self) -> dict:
        df = {
            "tags": {
                'Extracted Entity Condition': self.condition,
                'Extracted Entity Pre': self.pre,
                'Extracted Entity Post': self.post
            }
        }
        return df
