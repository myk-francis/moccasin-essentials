from src import favorites
from moccasin.boa_tools import VyperContract
from moccasin.config import get_active_account

def deploy_favorites() -> VyperContract:
    print("Deploying the application...")
    favorites_contract: VyperContract = favorites.deploy()
    starting_number: int = favorites_contract.retrieve()
    print(f"Favorites contract deployed at {favorites_contract.address} with starting number {starting_number}.")
    print("Deployment complete.")

    active_network = get_active_account()
    if active_network.has_explorer:
        print("Verifying contract on explorer...")
        result = active_network.moccasin_veriry(favorites_contract)
        result.wait_for_verification()
        print("Verification complete.")

    return favorites_contract

def moccasin_main():
    return deploy_favorites()