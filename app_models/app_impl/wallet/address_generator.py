from app_impl.wallet.address_generator_interface import AddressGeneratorInterface


class AddressGenerator(AddressGeneratorInterface):
    def __init__(self):
        self.address = 0

    def get_address(self, user_id) -> str:
        if self.address == 3:
            self.address = 1
        else:
            self.address += 1
        return str(user_id) + " " + str(self.address)
