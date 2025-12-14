from src import favorites

def deploy_favorites():
    print("Deploying the application...")
    favorites_contract = favorites.deploy()
    starting_number = favorites_contract.retrieve()
    print(f"Favorites contract deployed at {favorites_contract.address} with starting number {starting_number}.")
    print("Deployment complete.")
    return favorites_contract

def moccasin_main():
    return deploy_favorites()