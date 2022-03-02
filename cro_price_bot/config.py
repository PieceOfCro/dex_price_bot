from typing import Dict

from strictyaml import Map, MapPattern, Seq, Str, load

schema = Map(
    {
        "liquidity_pools": MapPattern(Str(), Seq(Str())),
        "price_unit": Str(),
        "token": Str(),
        "discord_token": Str(),
        "json_rpc_url": Str(),
    }
)


def load_config(file_path: str) -> Dict:
    with open(file_path, "r") as fp:
        _cfg = fp.read()
    cfg = load(_cfg, schema).data
    return cfg
    """
    assert cfg["token_contract"].startswith("0x") and len(cfg["token_contract"]) == 42
    if not cfg["discord"].get("ignore_users_with_roles"):
        cfg["discord"]["ignore_users_with_roles"] = set()
    else:
        cfg["discord"]["ignore_users_with_roles"] = set(
            cfg["discord"]["ignore_users_with_roles"]
        )
    return cfg
    """
