# Cronos Price Bot
## A Discord Bot for tracking price of DEX tokens

### Setting Up
You will need to replace `config/config.yaml` with the required settings.

#### Liquidity Pool
```
liquidity_pools:
  <liquidity_pool_contract_address 0xdeadbeef>:
    - <pool_token_one 0xdeadbeef>
    - <pool_token_two 0xdeadbeef>
```
You can get these variables through DexScreener, or using a cronos chain explorer.

#### Starting and Ending tokens
```
price_unit: 0xc21223249CA28397B4B6541dfFaEcC539BfF0c59  # USDC <token that is being used as the price standard>
token: 0x10C9284E6094b71D3CE4E38B8bFfc668199da677  # MIMAS <token you are getting the price of>
```
You can once again get these variables through DexScreener or a cronos chain explorer.
These contract addresses must be in the `liquidity_pools` section of the config, and must be able to be routed to each other using the liquidity pools. Please use pools with high liquidity where possible to ensure accurate prices.

#### Discord Token
```
discord_token: xxxxx
```
You can create a bot application [here](https://discord.com/developers/applications/) and invite it to your server. Make sure the bot has the permission to change nicknames on your server.
#### JSON RPC URL
```
json_rpc_url: https://rpc.vvs.finance/
```
You can use any rpc url here.

### Installation

#### Running it in a virtual environment
```sh
screen
python3 -m venv venv
source venv/bin/activate
pip install -e .
python3 cro_price_bot/main.py -c config/config.yaml
```

### Running it using docker
```sh
docker build . --tag cro_price_bot:latest
docker run -v $PWD/config/config.yaml:/config.yaml cro_price_bot:latest
```

## Donate

Donations are appreciated.

Cronos Address: 0x7C807e32573d5E80737F25113003F496efafF3A4

Feel free to contact me on discord 12Ghast#4326 if you would like custom work done, help with hosting, or anything in between.