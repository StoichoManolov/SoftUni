from typing import List

from project.climbers.arctic_climber import ArcticClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:

    def __init__(self):

        self.climbers = []
        self.peaks = []

    def register_climber(self,climber_type: str,climber_name: str):

        if climber_type == 'ArcticClimber' or climber_type == 'SummitClimber':

            try:
                climber = next(filter(lambda x: x.name == climber_name, self.climbers))
                return f"{climber_name} has been already registered."
            except StopIteration:
                pass

            climber = eval(f'{climber_type}(climber_name)')
            self.climbers.append(climber)
            return f"{climber_name} is successfully registered as a {climber_type}."
        else:
            return f"{climber_type} doesn't exist in our register."

    def peak_wish_list(self,peak_type: str, peak_name: str, peak_elevation: int):

        if peak_type == 'ArcticPeak' or peak_type == 'SummitPeak':
            peak = eval(f'{peak_type}(peak_name,peak_elevation)')
            self.peaks.append(peak)
            return f"{peak_name} is successfully added to the wish list as a {peak_type}."

        return f"{peak_type} is an unknown type of peak."

    def check_gear(self,climber_name: str, peak_name: str, gear: List[str]):

        climber = next(filter(lambda x: x.name == climber_name,self.climbers))
        peak = next(filter(lambda x: x.name == peak_name, self.peaks))
        needed_gear = peak.get_recommended_gear()

        if gear == needed_gear:
            climber.is_prepared = True
            return f"{climber_name} is prepared to climb {peak_name}."

        climber.is_prepared = False
        diff = sorted([x for x in needed_gear if x not in gear])
        return f"{climber_name} is not prepared to climb {peak_name}. " \
               f"Missing gear: {', '.join(diff)}."

    def perform_climbing(self,climber_name: str, peak_name: str):

        try:
            climber = next(filter(lambda x: x.name == climber_name,self.climbers))
        except StopIteration:
            return f"Climber {climber_name} is not registered yet."

        try:
            peak = next(filter(lambda x: x.name == peak_name, self.peaks))
        except StopIteration:
            return f"Peak {peak_name} is not part of the wish list."

        if climber.is_prepared and climber.can_climb():
            climber.climb(peak)
            return f"{climber.name} conquered {peak.name} whose difficulty level is {peak.difficulty_level}."

        if not climber.is_prepared:
            return f"{climber.name} will need to be better prepared next time."

        climber.rest()
        return f"{climber.name} needs more strength to climb {peak.name} and is therefore taking some rest."

    def get_statistics(self):

        peaks_climbed = set([peak.name for peak in self.peaks])

        result = f"Total climbed peaks: {len(peaks_climbed)}\n"
        result += "**Climber's statistics:**\n"

        sorted_climbers = sorted(self.climbers, key=lambda x: (-len(x.conquered_peaks),x.name))

        for climber in sorted_climbers:
            if len(climber.conquered_peaks) > 0:
                result += str(climber) + '\n'

        return result

