from script.deploy import deploy_favorites

def test_starting_values():
    favorites_contract = deploy_favorites()

    assert favorites_contract.retrieve() == 7

def test_update_favorites():
    # Arrange
    favorites_contract = deploy_favorites()
    # Act
    favorites_contract.store(15)
    # Assert
    assert favorites_contract.retrieve() == 15

def test_can_add_people():
    new_person = "Myk"
    new_favorite_number = 33
    favorites_contract = deploy_favorites()

    favorites_contract.add_person(new_person, new_favorite_number)

    assert favorites_contract.list_of_people(0) == (new_favorite_number, new_person)