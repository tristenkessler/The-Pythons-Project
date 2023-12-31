import unittest
import Inventory_List_Class

class TestInventoryList(unittest.TestCase):
    
    def test_constructor(self):
        inventory = Inventory_List_Class.Inventory_List()
        self.assertEqual(len(inventory.inventory_list), 0)
        
    def test_get_inventory(self):
        inventory = Inventory_List_Class.Inventory_List()
        self.assertEqual(len(inventory.get_inventory()), 0)
        
    def test_add_video(self):
        inventory = Inventory_List_Class.Inventory_List()
        inventory.add_video("Test", 2020, "John Doe", 5, "Comedy", "Available")
        self.assertEqual(len(inventory.get_inventory()), 1)
        
    def test_remove_video(self):
        inventory = Inventory_List_Class.Inventory_List()
        inventory.add_video("Test", 2020, "John Doe", 5, "Comedy", "Available")
        inventory.remove_video("Test")
        self.assertEqual(len(inventory.get_inventory()), 0)
        
    def test_get_inventory_list_by_attribute(self):
        inventory = Inventory_List_Class.Inventory_List()
        inventory.add_video("Test", 2020, "John Doe", 5, "Comedy", "Available")
        inventory.add_video("Movie", 2018, "Jane Doe", 7, "Action", "Available")
        filteredList = inventory.get_inventory_list_by_attribute("Action")
        self.assertEqual(filteredList[0].name, "Movie")

        inventory = Inventory_List_Class.Inventory_List()
        inventory.add_video("Test", 2020, "John Doe", 5, "Comedy", "Available")
        inventory.add_video("Movie", 2018, "Jane Doe", 7, "Action", "Available")
        filteredList = inventory.get_inventory_list_by_attribute("5")
        self.assertEqual(filteredList[0].name, "Test")
        
    def test_sort_inventory(self):
        inventory = Inventory_List_Class.Inventory_List()
        inventory.add_video("Test", 2020, "John Doe", 5, "Comedy", "Available")
        inventory.add_video("Movie", 2018, "Jane Doe", 7, "Action", "Available")
        inventory.sort_inventory("name", "asc")
        self.assertEqual(inventory.inventory_list[0].name, "Movie")
        
        
if __name__ == '__main__':
    unittest.main()
