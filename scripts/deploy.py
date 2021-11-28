from brownie import FundMe, MockV3Aggregator, network, config
from .utils import deploy_mocks, get_account, LOCAL_BLOCKCHAIN_ENV


def deploy_fund_me():
    account = get_account()

    # if on test networks, use associated address, otherwise deploy mocks
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENV:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract Deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
