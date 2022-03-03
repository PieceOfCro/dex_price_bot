from typing import Dict

from strictyaml import Map, MapPattern, Seq, Str, load

schema = Map(
    {
        "liquidity_pools": MapPattern(Str(), Seq(Str())),
        "price_unit": Str(),
        "token": Str(),
        "discord_token": Str(),
        "json_rpc_url": Str(),
        "display_format": Str(),
    }
)


def load_config(file_path: str) -> Dict:
    with open(file_path, "r") as fp:
        _cfg = fp.read()
    cfg = load(_cfg, schema).data
    return cfg
