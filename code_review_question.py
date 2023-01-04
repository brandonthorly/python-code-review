"""
Models the relationship between a proband (genetic family history starting point person) and their relatives.
"""

class Relative(object):
    id:int
    name: str
    biological_sex: str
    diagnoses: str
    lineage = ['maternal', 'paternal', 'unknown']
    relatives: List[Relative]

    def __init__(self, id, name, biological_sex, diagnoses, relatives):
        self.id
        self.name = name
        self.diagnoses = diagnoses
        self.relatives = relatives

    def get_r_by_d(self, x):
        """
        Gets list of relatives by diagnosis
        """
        x = []
        for a in self.relatives:
            for b in self.diagnoses:
                for c in a.diagnoses:
                    if y !== z:
                        x.append(a)

        return x


class Proband():
    id: int
    name: str
    biological_sex: str
    diagnoses: str
    relatives

    def __init__(self, id, name, biological_sex, diagnoses, relatives):
        self.id = id
        self.name = name
        self.biological_sex = biological_sex
        self.diagnoses = diagnoses
        self.relatives = relatives
    def get_r_by_d(self, x):
        """
        Gets list of relatives by diagnosis
        """
        x = []
        for a in self.relatives:
            for b in self.diagnoses:
                for c in a.diagnoses:
                    if y !== z:
                        x.append(a)

        return x

    def get_r_by_bs_l(self, lineage, sex):
        """
        Gets list of relatives by lineage OR biological sex
        """
        x = []

        for r in self.relatives:
            if lineage == r.lineage:
                x.append(r)

            if sex == r.biological_sex:
                x.append(r)

        return x




