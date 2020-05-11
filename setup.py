chart_colors = {
    "red"   : '#FF0613FF',
    "purple": '#AA0061FF',
    "blue"  : '#020A85FF',
    "cyan"  : '#469DDDFF',
    "cyan5" : '#469DDD7F',
    "cyan2" : '#469DDD33',
}

chart_config = {
    "scale_for_highest_element_ring" : False,
    "start_angle" : 270,
    "color_by_ring" : True,
    "show_labels": False,

    "sections" : [
        {
            "name": "Section 1",
            "weight" : 1,
            "layers": [
                { "elements": [ "eSDK" ] },
                { "elements": [ "HW Module", "HW Blueprint", "SDK Integration Support" ] },
                { "elements": [ "HW Development", "SW Development" ] },
                { "elements": [ "Embedded Product Development" ] },
            ]
        },
        {
            "name": "Section 2",
            "weight" : 1,
            "layers": [
                { "elements": [ "mSDK" ] },
                { "elements": [ "Whitelabel App", "SDK Integration Support" ] },
                { "elements": [ "Mobile\nApp\nDevelopment" ] },
            ]
        },
        {
            "name": "Section 3",
            "weight" : 1,
            "layers": [
                { "elements": [ "Commision\nAPI" ] },
                { "elements": [ "Integration Support", "Asset Management Database" ] },
                { "elements": [ "Whitelabel Asset\nManagement App/web" ] },
                { "elements": [ "Permission Management Development" ] },
            ]
        },
        {
            "name": "Section 4",
            "weight" : 1,
            "layers": [
                { "elements": [ "Service API" ] },
                { "elements": [ "Integration Support", "ID Management" ] },
                { "elements": [ "Whitelabel User\nManagement App/Web" ] },
                { "elements": [ "Permission Management Development" ] },
            ]
        }
    ]
}
