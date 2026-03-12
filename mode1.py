# Copy and paste your code for mode1.py here
from landsites import Land
from data_structures.bst import BinarySearchTree

class Mode1Navigator:
    """
    This class is used to navigate through a list of land sites and select the most profitable ones for adventurers.
    """

    def __init__(self, sites: list[Land], adventurers: int) -> None:
        """
        This method initializes the Mode1Navigator with a list of sites and the number of adventurers.
        It creates a Binary Search Tree and inserts each site into the BST with a key of -1 times the ratio of gold to guardians.

        Parameters:
            sites (list[Land]): A list of land sites.
            adventurers (int): The number of adventurers.
            
        Complexity:
            The best case and worst case complexity is O(N log N), where N is the number of land sites. This occurs when each inserting into the Binary Search Tree.
        """
        land_sites = BinarySearchTree()
        for site in sites:
            land_sites[-1 * site.get_gold()/site.get_guardians()] = site
        self.sites = land_sites
        self.adventurers = adventurers

    def select_sites(self) -> list[tuple[Land, int]]:
        """
        This method selects the most profitable sites for the adventurers.
        It iterates over the Binary Search Tree and for each site, it sends as many adventurers as possible.
        The number of adventurers sent to a site is the minimum of the number of guardians at the site and the remaining number of adventurers.

        Complexity:
            Best Case Complexity: O(log N), where N is the number of land sites. This occurs when the number of adventurers is less than the 
                                            number of guardians at the first site
            Worst Case Complexity: O(N), where N is the number of land sites. This occurs when the number of adventurers is greater than or 
                                        equal to the total number of guardians at all sites.
        """
        selected_sites = []
        remaining_adventurers = self.adventurers
        iterator = iter(self.sites)

        while remaining_adventurers > 0:
            try:
                node = next(iterator)
            except StopIteration:
                break

            site = node.item 

            if site.guardians > 0:
                ci = min(site.guardians, remaining_adventurers)
                selected_sites.append((site, ci))
                remaining_adventurers -= ci

        return selected_sites

    def select_sites_from_adventure_numbers(self, adventure_numbers: list[int]) -> list[float]:
        """
        This method calculates the total reward for a list of numbers of adventurers.
        For each number of adventurers, it calls the select_sites method to select the most profitable sites and then calculates the total reward.

        Parameters:
            adventure_numbers (list[int]): A list of numbers of adventurers.
        
        Returns:
            list[float]: A list of total rewards for each number of adventurers.
            
        Complexity:
            Best Case Complexity: O(A x log N), where N is the number of land sites. This occurs when the select_sites method returns a list in logarithmic time
            Worst Case Complexity: O(A x N), where A is the length of adventure_numbers and N is the number of land sites. This occurs when 
                                   the adventure_numbers list is not empty and the select_sites method returns a list.
        """
        reward_list = []
        i = 0

        while i < len(adventure_numbers):
            self.adventurers = adventure_numbers[i]
            reward = 0

            for site, adventurers_sent in self.select_sites():
                gold_per_adventurer = adventurers_sent*site.get_gold()/site.get_guardians()
                reward += min (gold_per_adventurer, site.get_gold())
            reward_list.append(reward)
            i+=1

        return reward_list

    def update_site(self, land: Land, new_reward: float, new_guardians: int) -> None:
        """
        This method update the reward and the number of guardians of a site.
        It first deletes the site from the BST and then inserts it back with the updated reward and number of guardians.

        Parameters:
            land (Land): The land site to be updated.
            new_reward (float): The new reward of the land site.
            new_guardians (int): The new number of guardians of the land site.

        Complexity:
            The best case and worst case complexity is O(log N), where N is the number of land sites. This occurs when the method involves deleting in self.sites.
        """
        del self.sites[-1 * land.get_gold()/land.get_guardians()]
        land.gold = new_reward
        land.guardians = new_guardians
        self.sites[-1 * new_reward / new_guardians] = land
