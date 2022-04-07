PAIR_EVENT = {
    "0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925": {
        "signature": "0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925",
        "anonymous": False,
        "name": "Approval",
        "parameters": [
            {
                "parameter_name": "owner",
                "parameter_type": "address",
                "components": [],
                "indexed": True,
                "dynamic": False,
            },
            {
                "parameter_name": "spender",
                "parameter_type": "address",
                "components": [],
                "indexed": True,
                "dynamic": False,
            },
            {
                "parameter_name": "value",
                "parameter_type": "uint256",
                "components": [],
                "indexed": False,
                "dynamic": False,
            },
        ],
    },
    "0xdccd412f0b1252819cb1fd330b93224ca42612892bb3f4f789976e6d81936496": {
        "signature": "0xdccd412f0b1252819cb1fd330b93224ca42612892bb3f4f789976e6d81936496",
        "anonymous": False,
        "name": "Burn",
        "parameters": [
            {
                "parameter_name": "sender",
                "parameter_type": "address",
                "components": [],
                "indexed": True,
                "dynamic": False,
            },
            {
                "parameter_name": "amount0",
                "parameter_type": "uint256",
                "components": [],
                "indexed": False,
                "dynamic": False,
            },
            {
                "parameter_name": "amount1",
                "parameter_type": "uint256",
                "components": [],
                "indexed": False,
                "dynamic": False,
            },
            {
                "parameter_name": "to",
                "parameter_type": "address",
                "components": [],
                "indexed": True,
                "dynamic": False,
            },
        ],
    },
    "0x4c209b5fc8ad50758f13e2e1088ba56a560dff690a1c6fef26394f4c03821c4f": {
        "signature": "0x4c209b5fc8ad50758f13e2e1088ba56a560dff690a1c6fef26394f4c03821c4f",
        "anonymous": False,
        "name": "Mint",
        "parameters": [
            {
                "parameter_name": "sender",
                "parameter_type": "address",
                "components": [],
                "indexed": True,
                "dynamic": False,
            },
            {
                "parameter_name": "amount0",
                "parameter_type": "uint256",
                "components": [],
                "indexed": False,
                "dynamic": False,
            },
            {
                "parameter_name": "amount1",
                "parameter_type": "uint256",
                "components": [],
                "indexed": False,
                "dynamic": False,
            },
        ],
    },
    "0xd78ad95fa46c994b6551d0da85fc275fe613ce37657fb8d5e3d130840159d822": {
        "signature": "0xd78ad95fa46c994b6551d0da85fc275fe613ce37657fb8d5e3d130840159d822",
        "anonymous": False,
        "name": "Swap",
        "parameters": [
            {
                "parameter_name": "sender",
                "parameter_type": "address",
                "components": [],
                "indexed": True,
                "dynamic": False,
            },
            {
                "parameter_name": "amount0In",
                "parameter_type": "uint256",
                "components": [],
                "indexed": False,
                "dynamic": False,
            },
            {
                "parameter_name": "amount1In",
                "parameter_type": "uint256",
                "components": [],
                "indexed": False,
                "dynamic": False,
            },
            {
                "parameter_name": "amount0Out",
                "parameter_type": "uint256",
                "components": [],
                "indexed": False,
                "dynamic": False,
            },
            {
                "parameter_name": "amount1Out",
                "parameter_type": "uint256",
                "components": [],
                "indexed": False,
                "dynamic": False,
            },
            {
                "parameter_name": "to",
                "parameter_type": "address",
                "components": [],
                "indexed": True,
                "dynamic": False,
            },
        ],
    },
    "0x1c411e9a96e071241c2f21f7726b17ae89e3cab4c78be50e062b03a9fffbbad1": {
        "signature": "0x1c411e9a96e071241c2f21f7726b17ae89e3cab4c78be50e062b03a9fffbbad1",
        "anonymous": False,
        "name": "Sync",
        "parameters": [
            {
                "parameter_name": "reserve0",
                "parameter_type": "uint112",
                "components": [],
                "indexed": False,
                "dynamic": False,
            },
            {
                "parameter_name": "reserve1",
                "parameter_type": "uint112",
                "components": [],
                "indexed": False,
                "dynamic": False,
            },
        ],
    },
    "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef": {
        "signature": "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef",
        "anonymous": False,
        "name": "Transfer",
        "parameters": [
            {
                "parameter_name": "from",
                "parameter_type": "address",
                "components": [],
                "indexed": True,
                "dynamic": False,
            },
            {
                "parameter_name": "to",
                "parameter_type": "address",
                "components": [],
                "indexed": True,
                "dynamic": False,
            },
            {
                "parameter_name": "value",
                "parameter_type": "uint256",
                "components": [],
                "indexed": False,
                "dynamic": False,
            },
        ],
    },
}

PAIR_FUNCTION = {
        "constructor" : {
            "signature" : "constructor",
            "name" : "constructor",
            "inputs" : [],
            "outputs" : []
        },
        "0x3644e515" : {
            "signature" : "0x3644e515",
            "name" : "DOMAIN_SEPARATOR",
            "inputs" : [],
            "outputs" : [ 
                {
                    "parameter_name" : "",
                    "parameter_type" : "bytes32",
                    "components" : [],
                    "indexed" : False,
                    "dynamic" : False
                }
            ]
        },
        "0xba9a7a56" : {
            "signature" : "0xba9a7a56",
            "name" : "MINIMUM_LIQUIDITY",
            "inputs" : [],
            "outputs" : [ 
                {
                    "parameter_name" : "",
                    "parameter_type" : "uint256",
                    "components" : [],
                    "indexed" : False,
                    "dynamic" : False
                }
            ]
        },
        "0x30adf81f" : {
            "signature" : "0x30adf81f",
            "name" : "PERMIT_TYPEHASH",
            "inputs" : [],
            "outputs" : [ 
                {
                    "parameter_name" : "",
                    "parameter_type" : "bytes32",
                    "components" : [],
                    "indexed" : False,
                    "dynamic" : False
                }
            ]
        },
        "0xdd62ed3e" : {
            "signature" : "0xdd62ed3e",
            "name" : "allowance",
            "inputs" : [ 
                {
                    "parameter_name" : "",
                    "parameter_type" : "address",
                    "components" : [],
                    "indexed" : False,
                    "dynamic" : False
                }, 
                {
                    "parameter_name" : "",
                    "parameter_type" : "address",
                    "components" : [],
                    "indexed" : False,
                    "dynamic" : False
                }
            ],
            "outputs" : [ 
                {
                    "parameter_name" : "",
                    "parameter_type" : "uint256",
                    "components" : [],
                    "indexed" : False,
                    "dynamic" : False
                }
            ]
        },
        "0x095ea7b3" : {
            "signature" : "0x095ea7b3",
            "name" : "approve",
            "inputs" : [ 
                {
                    "parameter_name" : "spender",
                    "parameter_type" : "address",
                    "components" : [],
                    "indexed" : False,
                    "dynamic" : False
                }, 
                {
                    "parameter_name" : "value",
                    "parameter_type" : "uint256",
                    "components" : [],
                    "indexed" : False,
                    "dynamic" : False
                }
            ],
            "outputs" : [ 
                {
                    "parameter_name" : "",
                    "parameter_type" : "bool",
                    "components" : [],
                    "indexed" : False,
                    "dynamic" : False
                }
            ]
        },
        "0x70a08231" : {
            "signature" : "0x70a08231",
            "name" : "balanceOf",
            "inputs" : [ 
                {
                    "parameter_name" : "",
                    "parameter_type" : "address",
                    "components" : [],
                    "indexed" : False,
                    "dynamic" : False
                }
            ],
            "outputs" : [ 
                {
                    "parameter_name" : "",
                    "parameter_type" : "uint256",
                    "components" : [],
                    "indexed" : False,
                    "dynamic" : False
                }
            ]
        },
        "0x89afcb44" : {
            "signature" : "0x89afcb44",
            "name" : "burn",
            "inputs" : [ 
                {
                    "parameter_name" : "to",
                    "parameter_type" : "address",
                    "components" : [],
                    "indexed" : False,
                    "dynamic" : False
                }
            ],
            "outputs" : [ 
                {
                    "parameter_name" : "amount0",
                    "parameter_type" : "uint256",
                    "components" : [],
                    "indexed" : False,
                    "dynamic" : False
                }, 
                {
                    "parameter_name" : "amount1",
                    "parameter_type" : "uint256",
                    "components" : [],
                    "indexed" : False,
                    "dynamic" : False
                }
            ]
        },
        "0x313ce567" : {
            "signature" : "0x313ce567",
            "name" : "decimals",
            "inputs" : [],
            "outputs" : [ 
                {
                    "parameter_name" : "",
                    "parameter_type" : "uint8",
                    "components" : [],
                    "indexed" : False,
                    "dynamic" : False
                }
            ]
        },
        "0xc45a0155" : {
            "signature" : "0xc45a0155",
            "name" : "factory",
            "inputs" : [],
            "outputs" : [ 
                {
                    "parameter_name" : "",
                    "parameter_type" : "address",
                    "components" : [],
                    "indexed" : False,
                    "dynamic" : False
                }
            ]
        },
        "0x0902f1ac" : {
            "signature" : "0x0902f1ac",
            "name" : "getReserves",
            "inputs" : [],
            "outputs" : [ 
                {
                    "parameter_name" : "_reserve0",
                    "parameter_type" : "uint112",
                    "components" : [],
                    "indexed" : False,
                    "dynamic" : False
                }, 
                {
                    "parameter_name" : "_reserve1",
                    "parameter_type" : "uint112",
                    "components" : [],
                    "indexed" : False,
                    "dynamic" : False
                }, 
                {
                    "parameter_name" : "_blockTimestampLast",
                    "parameter_type" : "uint32",
                    "components" : [],
                    "indexed" : False,
                    "dynamic" : False
                }
            ]
        },
        "0x485cc955" : {
            "signature" : "0x485cc955",
            "name" : "initialize",
            "inputs" : [ 
                {
                    "parameter_name" : "_token0",
                    "parameter_type" : "address",
                    "components" : [],
                    "indexed" : False,
                    "dynamic" : False
                }, 
                {
                    "parameter_name" : "_token1",
                    "parameter_type" : "address",
                    "components" : [],
                    "indexed" : False,
                    "dynamic" : False
                }
            ],
            "outputs" : []
        },
        "0x7464fc3d" : {
            "signature" : "0x7464fc3d",
            "name" : "kLast",
            "inputs" : [],
            "outputs" : [ 
                {
                    "parameter_name" : "",
                    "parameter_type" : "uint256",
                    "components" : [],
                    "indexed" : False,
                    "dynamic" : False
                }
            ]
        },
        "0x6a627842" : {
            "signature" : "0x6a627842",
            "name" : "mint",
            "inputs" : [ 
                {
                    "parameter_name" : "to",
                    "parameter_type" : "address",
                    "components" : [],
                    "indexed" : False,
                    "dynamic" : False
                }
            ],
            "outputs" : [ 
                {
                    "parameter_name" : "liquidity",
                    "parameter_type" : "uint256",
                    "components" : [],
                    "indexed" : False,
                    "dynamic" : False
                }
            ]
        },
        "0x06fdde03" : {
            "signature" : "0x06fdde03",
            "name" : "name",
            "inputs" : [],
            "outputs" : [ 
                {
                    "parameter_name" : "",
                    "parameter_type" : "string",
                    "components" : [],
                    "indexed" : False,
                    "dynamic" : True
                }
            ]
        },
        "0x7ecebe00" : {
            "signature" : "0x7ecebe00",
            "name" : "nonces",
            "inputs" : [ 
                {
                    "parameter_name" : "",
                    "parameter_type" : "address",
                    "components" : [],
                    "indexed" : False,
                    "dynamic" : False
                }
            ],
            "outputs" : [ 
                {
                    "parameter_name" : "",
                    "parameter_type" : "uint256",
                    "components" : [],
                    "indexed" : False,
                    "dynamic" : False
                }
            ]
        },
        "0xd505accf" : {
            "signature" : "0xd505accf",
            "name" : "permit",
            "inputs" : [ 
                {
                    "parameter_name" : "owner",
                    "parameter_type" : "address",
                    "components" : [],
                    "indexed" : False,
                    "dynamic" : False
                }, 
                {
                    "parameter_name" : "spender",
                    "parameter_type" : "address",
                    "components" : [],
                    "indexed" : False,
                    "dynamic" : False
                }, 
                {
                    "parameter_name" : "value",
                    "parameter_type" : "uint256",
                    "components" : [],
                    "indexed" : False,
                    "dynamic" : False
                }, 
                {
                    "parameter_name" : "deadline",
                    "parameter_type" : "uint256",
                    "components" : [],
                    "indexed" : False,
                    "dynamic" : False
                }, 
                {
                    "parameter_name" : "v",
                    "parameter_type" : "uint8",
                    "components" : [],
                    "indexed" : False,
                    "dynamic" : False
                }, 
                {
                    "parameter_name" : "r",
                    "parameter_type" : "bytes32",
                    "components" : [],
                    "indexed" : False,
                    "dynamic" : False
                }, 
                {
                    "parameter_name" : "s",
                    "parameter_type" : "bytes32",
                    "components" : [],
                    "indexed" : False,
                    "dynamic" : False
                }
            ],
            "outputs" : []
        },
        "0x5909c0d5" : {
            "signature" : "0x5909c0d5",
            "name" : "price0CumulativeLast",
            "inputs" : [],
            "outputs" : [ 
                {
                    "parameter_name" : "",
                    "parameter_type" : "uint256",
                    "components" : [],
                    "indexed" : False,
                    "dynamic" : False
                }
            ]
        },
        "0x5a3d5493" : {
            "signature" : "0x5a3d5493",
            "name" : "price1CumulativeLast",
            "inputs" : [],
            "outputs" : [ 
                {
                    "parameter_name" : "",
                    "parameter_type" : "uint256",
                    "components" : [],
                    "indexed" : False,
                    "dynamic" : False
                }
            ]
        },
        "0xbc25cf77" : {
            "signature" : "0xbc25cf77",
            "name" : "skim",
            "inputs" : [ 
                {
                    "parameter_name" : "to",
                    "parameter_type" : "address",
                    "components" : [],
                    "indexed" : False,
                    "dynamic" : False
                }
            ],
            "outputs" : []
        },
        "0x022c0d9f" : {
            "signature" : "0x022c0d9f",
            "name" : "swap",
            "inputs" : [ 
                {
                    "parameter_name" : "amount0Out",
                    "parameter_type" : "uint256",
                    "components" : [],
                    "indexed" : False,
                    "dynamic" : False
                }, 
                {
                    "parameter_name" : "amount1Out",
                    "parameter_type" : "uint256",
                    "components" : [],
                    "indexed" : False,
                    "dynamic" : False
                }, 
                {
                    "parameter_name" : "to",
                    "parameter_type" : "address",
                    "components" : [],
                    "indexed" : False,
                    "dynamic" : False
                }, 
                {
                    "parameter_name" : "data",
                    "parameter_type" : "bytes",
                    "components" : [],
                    "indexed" : False,
                    "dynamic" : True
                }
            ],
            "outputs" : []
        },
        "0x95d89b41" : {
            "signature" : "0x95d89b41",
            "name" : "symbol",
            "inputs" : [],
            "outputs" : [ 
                {
                    "parameter_name" : "",
                    "parameter_type" : "string",
                    "components" : [],
                    "indexed" : False,
                    "dynamic" : True
                }
            ]
        },
        "0xfff6cae9" : {
            "signature" : "0xfff6cae9",
            "name" : "sync",
            "inputs" : [],
            "outputs" : []
        },
        "0x0dfe1681" : {
            "signature" : "0x0dfe1681",
            "name" : "token0",
            "inputs" : [],
            "outputs" : [ 
                {
                    "parameter_name" : "",
                    "parameter_type" : "address",
                    "components" : [],
                    "indexed" : False,
                    "dynamic" : False
                }
            ]
        },
        "0xd21220a7" : {
            "signature" : "0xd21220a7",
            "name" : "token1",
            "inputs" : [],
            "outputs" : [ 
                {
                    "parameter_name" : "",
                    "parameter_type" : "address",
                    "components" : [],
                    "indexed" : False,
                    "dynamic" : False
                }
            ]
        },
        "0x18160ddd" : {
            "signature" : "0x18160ddd",
            "name" : "totalSupply",
            "inputs" : [],
            "outputs" : [ 
                {
                    "parameter_name" : "",
                    "parameter_type" : "uint256",
                    "components" : [],
                    "indexed" : False,
                    "dynamic" : False
                }
            ]
        },
        "0xa9059cbb" : {
            "signature" : "0xa9059cbb",
            "name" : "transfer",
            "inputs" : [ 
                {
                    "parameter_name" : "to",
                    "parameter_type" : "address",
                    "components" : [],
                    "indexed" : False,
                    "dynamic" : False
                }, 
                {
                    "parameter_name" : "value",
                    "parameter_type" : "uint256",
                    "components" : [],
                    "indexed" : False,
                    "dynamic" : False
                }
            ],
            "outputs" : [ 
                {
                    "parameter_name" : "",
                    "parameter_type" : "bool",
                    "components" : [],
                    "indexed" : False,
                    "dynamic" : False
                }
            ]
        },
        "0x23b872dd" : {
            "signature" : "0x23b872dd",
            "name" : "transferFrom",
            "inputs" : [ 
                {
                    "parameter_name" : "from",
                    "parameter_type" : "address",
                    "components" : [],
                    "indexed" : False,
                    "dynamic" : False
                }, 
                {
                    "parameter_name" : "to",
                    "parameter_type" : "address",
                    "components" : [],
                    "indexed" : False,
                    "dynamic" : False
                }, 
                {
                    "parameter_name" : "value",
                    "parameter_type" : "uint256",
                    "components" : [],
                    "indexed" : False,
                    "dynamic" : False
                }
            ],
            "outputs" : [ 
                {
                    "parameter_name" : "",
                    "parameter_type" : "bool",
                    "components" : [],
                    "indexed" : False,
                    "dynamic" : False
                }
            ]
        }
    }