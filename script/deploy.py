from src import favorites
from moccasin.boa_tools import VyperContract

def deploy_favorites() -> VyperContract:
    print("Deploying the application...")
    favorites_contract: VyperContract = favorites.deploy()
    starting_number: int = favorites_contract.retrieve()
    print(f"Favorites contract deployed at {favorites_contract.address} with starting number {starting_number}.")
    print("Deployment complete.")
    return favorites_contract

def moccasin_main():
    return deploy_favorites()