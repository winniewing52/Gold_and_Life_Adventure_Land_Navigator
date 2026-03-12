# Copy and paste your code for mode2.py here
from landsites import Land
from data_structures.heap import MaxHeap
from typing import List, Union, Tuple

class Mode2Navigator:
    """
    This class is used to navigate through a list of land sites and select the most profitable ones for teams of adventurers.

    Attributes:
    - n_teams (int): The number of teams.
    - sites (list[Land]): A list of land sites.
    - scores (MaxHeap): A max heap data structure to store the scores of the sites.
    """

    def __init__(self, n_teams: int) -> None:
        """
        Initializes the Mode2Navigator with the specified number of teams.

        Parameters:
            n_teams (int): The number of teams.

        Time Complexity:
            The best case and worst case time complexity is O(1). This occurs when initializing the variables.
        """
        self.n_teams = n_teams
        self.sites = []
        self.scores = None

    def add_sites(self, sites: list[Land]) -> None:
        """
        This method adds the given sites to the list of sites.

        Parameters:
            sites (list[Land]): A list of land sites.

        Time Complexity:
            Best Case: O(1), this occurs when the sites list is empty.
            Worst Case: O(n), where n is the number of land sites. This occurs when the sites list is not empty.
        """
        self.sites.extend(sites)

    def simulate_day(self, adventurer_size: int) -> List[Tuple[Union[Land, None], int]]:
        """
        This method simulates a day of adventuring by sending teams to the sites and updating the sites and scores accordingly.
        Parameters:
            adventurer_size (int): The number of adventurers in a team.

        Time Complexity:
            Best Case: O(n), where n is the number of teams. This occurs when the scores list is empty.
            Worst Case: O(n log n), where n is the number of teams. This occurs when the scores list is not empty.
        """
        self.construct_score_data_structure(adventurer_size)
        result = []
        teams = 0
        while teams < self.n_teams:
            if len(self.scores) > 0:
                team_score, site, adventurers_remaining = self.scores.get_max()
                adventurers_sent = adventurer_size - adventurers_remaining
                reward = team_score - (2.5*adventurers_remaining)
                site.gold -= reward
                site.guardians -= adventurers_sent
                new_score, new_adventurers_remaining = self.compute_score(site, adventurer_size)
                result.append((site, adventurers_sent))
                if site.guardians != 0:
                    self.scores.add((new_score, site, new_adventurers_remaining))
                if site.guardians == 0:
                    self.sites.remove(site)
            else:
                result.append((None, 0))
            teams += 1
        return result

    def compute_score(self, site: Land, adventurer_size: int):
        """
        This method computes the score for a site given the number of adventurers in a team.

        Parameters:
            site (Land): The land site.
            adventurer_size (int): The number of adventurers in a team.
        """
        default_reward = adventurer_size * 2.5
        score = default_reward
        adventurers_remaining = adventurer_size

        if site.get_guardians() > 0 and site.get_gold() > 0:
            adventurers_sent = min(adventurer_size, site.get_guardians())
            reward = min(adventurers_sent * site.get_gold() / site.get_guardians(), site.get_gold())
            adventurers_remaining = adventurer_size - adventurers_sent
            score = 2.5 * adventurers_remaining + reward

        return (default_reward if default_reward >= score else score, adventurers_remaining)

    def construct_score_data_structure(self, adventurer_size):
        """
        This method constructs the score data structure (a max heap) for the sites.

        Parameters:
            adventurer_size (int): The number of adventurers in a team.
        """
        scores_arr = []
        i = 0
        while i < len(self.sites):
            score, adventurers_remaining = self.compute_score(self.sites[i], adventurer_size)
            if score != 2.5 * adventurer_size:
                scores_arr.append((score, self.sites[i], adventurers_remaining))
            i += 1
        self.scores = MaxHeap.heapify(scores_arr, len(scores_arr))


