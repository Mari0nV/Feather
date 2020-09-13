mapping = {
    "get up": {
        ("laying"): {
            "msg": ["You get up and remove the leafs hung up on your clothes. Man you're dirty. You better go back quicky to your dorm room to clean up."],
            "update": {"laying": False},
            },
        (): {
            "msg": ["You are already standing up."],
            }
    },
    "go to university": {
        ("forest", "dark"): {
            "msg": ["You wish you could, but it's so dark out here. You have no idea which direction to go."],
        },
        ("university"): {
            "msg": ["You are already on the university campus."],
        },
        ("forest", "gps"): {
            "msg": ["You follow the indication of the GPS to go back to the university campus. Luckily it's not that far."],
            "update": {"university": True, "forest": False}
        }
    },
}
