chart_colors = (
    '#FF0613FF',
    '#AA0061FF',
    '#020A85FF',
    '#469DDDFF',
    '#469DDD7F',
    '#469DDD33',
)

chart_config = {
    "scale_for_highest_element_ring" : False,
    "start_angle" : 270,
    "color_by_ring" : True,
    "show_labels": False,

    "sections" : [
        {
            "name": "Embedded",
            "weight" : 1,
            "donuts": [
                { "elements": [ 1 ] },
                { "elements": [ 1, 1, 1 ] },
                { "elements": [ 1, 1 ] },
                { "elements": [ 1 ] },
            ]
        },
        {
            "name": "Mobile",
            "weight" : 1,
            "donuts": [
                { "elements": [ 1 ] },
                { "elements": [ 1, 1 ] },
                { "elements": [ 1 ] },
            ]
        },
        {
            "name": "Commissioning",
            "weight" : 1,
            "donuts": [
                { "elements": [ 1 ] },
                { "elements": [ 1, 1 ] },
                { "elements": [ 1 ] },
                { "elements": [ 1 ] },
            ]
        },
        {
            "name": "Service",
            "weight" : 1,
            "donuts": [
                { "elements": [ 1 ] },
                { "elements": [ 1, 1 ] },
                { "elements": [ 1 ] },
                { "elements": [ 1 ] },
            ]
        }
    ]
}
