from collections import OrderedDict
from typing import Optional

from ..en import Provider as AddressProvider


class Provider(AddressProvider):
    counties = (
        "Cork",
        "Galway",
        "Mayo",
        "Donegal",
        "Kerry",
        "Tipperary",
        "Clare",
        "Tyrone",
        "Antrim",
        "Limerick",
        "Roscommon",
        "Down",
        "Meath",
        "Londonderry",
        "Wexford",
        "Kilkenny",
        "Offaly",
        "Cavan",
        "Wicklow",
        "Waterford",
        "Sligo",
        "Laois",
        "Westmeath",
        "Kildare",
        "Leitrim",
        "Armagh",
        "Fermanagh",
        "Monaghan",
        "Dublin",
        "Louth",
        "Longford",
        "Carlow",
    )

    _postcode_sets = OrderedDict(
        (
            (" ", [" ", ""]),
            ("N", [str(i) for i in range(0, 10)]),
            ("L", "ACDEFHKNPRTVWXY"),
            ("A", "ACDEFHKNPRTVWXY0123456789"),
        )
    )
    postcode_pattern: str = "LNN AAAA"

    def postcode(self) -> str:
        return "".join(
            self.random_element(self._postcode_sets[placeholder])
            for placeholder in self.postcode_pattern
        )

    def administrative_unit(self, min_length: Optional[int] = None, max_length: Optional[int] = None) -> str:
        return self.random_element(self.counties, min_length, max_length)

    county = administrative_unit
