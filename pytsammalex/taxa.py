"""
collect data from external sources into species.json
"""
from __future__ import print_function, unicode_literals, absolute_import, division
from collections import OrderedDict

from purl import URL

from pytsammalex.util import JsonData, REPOS


def wikipedia_url(s):  # pragma: no cover
    url = URL(s)
    if url.scheme() in ['http', 'https'] and 'wikipedia.' in url.host():
        return s


class TaxaData(JsonData):
    def __init__(self, repos=REPOS):
        JsonData.__init__(
            self, 'taxa.json', repos=repos, container_cls=list, json_opts=dict(indent=4))
        self._ids = set(spec['id'] for spec in self.items)

    def __contains__(self, item):
        return item in self._ids

    def add(self, index, item):
        """
        Add a taxon item as read from taxa.csv to the catalog, if it is not already in.

        :param index: Position in the list
        :param item: models.Taxa item
        """
        if item.id not in self:
            self.items.insert(
                index,
                OrderedDict([
                    ('id', item.id),
                    ('name', item.scientific_name),
                    ('kingdom', item.kingdom.capitalize() or None),
                    ('order', item.order.capitalize() or None),
                    ('family', item.family.capitalize() or None),
                    ('genus', item.genus.capitalize() or None),
                    ('ecoregions', []),
                    ('countries', item.countries__ids),
                    ('wikipedia_url', None),
                    ('eol_id', None),
                    ('gbif_id', None),
                    ('catalogueoflife_id', None),
                ]))
            self._ids.add(item.id)
