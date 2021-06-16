class Restaurant:
    """
    Restaurant information.
    """

    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialize restuarant name and cuisine type
        """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """
        Prints restaurant information.
        """
        print(f"\n{self.restaurant_name} serves {self.cuisine_type}")

    def open_restaurant(self):
        """
        Prints that the restaurant is open.
        """
        print(f"\n{self.restaurant_name} is open.")

    def set_number_served(self, number_served):
        """
        Set the number of customers served.
        """
        self.number_served = number_served

    def increment_number_served(self, number_served):
        """
        Increment the number of customers who have been served.
        """
        self.number_served += number_served

class IceCreamStand(Restaurant):
    """
    Ice cream stand information.
    """

    def __init__(self, restaurant_name, cuisine_type = 'Ice Cream'):
        """
        Initialize attributes of the parent class.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def display_flavors(self):
        """
        Displays flavors.
        """
        print(f"\nFlavors available at {self.restaurant_name}:")
        for flavor in self.flavors:
            print(flavor.title())