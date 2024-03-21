from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):

    def __init__(self,name):
        super().__init__(name,150)

    def can_climb(self):

        if self.strength >= 75:
            return True
        return False

    def climb(self, peak: BasePeak):

        if peak.difficulty_level == 'Advanced':
            self.strength -= 1.3 * 30
        else:
            self.strength -= 2.5 * 30

        self.conquered_peaks.append(peak)

