from typing import List

from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:

    DIVER_TYPES = "FreeDiver", "ScubaDiver"
    FISH_TYPES = "PredatoryFish", "DeepSeaFish"

    def __init__(self):

        self.divers = []
        self.fish_list = []

    def dive_into_competition(self,diver_type: str, diver_name: str):

        if diver_type not in self.DIVER_TYPES:
            return f"{diver_type} is not allowed in our competition."

        current_diver = self.get_diver(diver_name)
        if current_diver is not None:
            return f"{diver_name} is already a participant."

        diver = eval(f'{diver_type}(diver_name)')
        self.divers.append(diver)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self,fish_type: str, fish_name: str, points: float):

        if fish_type not in self.FISH_TYPES:
            return f"{fish_type} is forbidden for chasing in our competition."

        current_fish = self.get_fish(fish_name)
        if current_fish is not None:
            return f"{fish_name} is already permitted."

        fish = eval(f'{fish_type}(fish_name,points)')
        self.fish_list.append(fish)
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):

        diver = self.get_diver(diver_name)
        if not diver:
            return f"{diver_name} is not registered for the competition."

        fish = self.get_fish(fish_name)
        if not fish:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            if diver.oxygen_level == 0:
                diver.update_health_status()
            return f"{diver_name} missed a good {fish_name}."

        elif diver.oxygen_level == fish.time_to_catch:

            if is_lucky:
                diver.hit(fish)
                if diver.oxygen_level == 0:
                    diver.update_health_status()
                return f"{diver_name} hits a {fish.points:.1f}pt. {fish_name}."
            else:
                diver.miss(fish.time_to_catch)
                if diver.oxygen_level == 0:
                    diver.update_health_status()
                return f"{diver_name} missed a good {fish_name}."
        else:
            diver.hit(fish)
            if diver.oxygen_level == 0:
                diver.update_health_status()
            return f"{diver_name} hits a {fish.points:.1f}pt. {fish_name}."

    def health_recovery(self):

        counter = 0

        for diver in self.divers:
            if diver.has_health_issue:
                counter += 1
                diver.update_health_status()
                diver.renew_oxy()

        return f"Divers recovered: {counter}"

    def diver_catch_report(self, diver_name: str):
        diver = self.get_diver(diver_name)
        fish_details = [fish.fish_details() for fish in diver.catch]

        catch_report = '\n'.join(fish_details)
        return f"**{diver_name} Catch Report**\n{catch_report}"

    def competition_statistics(self):

        divers = [diver for diver in self.divers if not diver.has_health_issue]

        sorted_divers = sorted(
            divers,
            key=lambda x: (-x.competition_points, -len(x.catch),x.name)
        )

        result = "**Nautical Catch Challenge Statistics**\n"
        result += "\n".join(str(d) for d in sorted_divers)
        return result

    def get_diver(self, diver_name: str):
        diver_name = [c for c in self.divers if c.name == diver_name]
        return diver_name[0] if diver_name else None

    def get_fish(self, fish_name: str):
        fish_name = [c for c in self.fish_list if c.name == fish_name]
        return fish_name[0] if fish_name else None


