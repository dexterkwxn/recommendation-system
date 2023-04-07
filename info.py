from constants import *
data = {
    hall1: {
        name: hall1,
        location: [100, 200],
        rooms: [[single, 800], [singleAC, 900]],
        facilities: [canteen, gym],
    },
    hall2: {
        name: hall2,
        location: 'somewhere'
    },
    hall3: {
        name: hall3,
        location: 'somewhere'
    },
    hall4:
      {
        name: hall4,
        location: 'somewhere'
    },
    hall5: {
        name: hall5,
        location: 'somewhere'
    },
    hall6: {
        name: hall6,
        location: 'somewhere'
    },
    hall7: {
        name: hall7,
        location: 'somewhere'
    },
    hall8: {
        name: hall8,
        location: 'somewhere'
    },
    hall9: {
        name: hall9,
        location: 'somewhere'
    },
    hall10: {
        name: hall10,
        location: 'somewhere'
    },
    hall11: {
        name: hall11,
        location: 'somewhere'
    },
    hall12: {
        name: hall12,
        location: 'somewhere'
    },
    hall13: {
        name: hall13,
        location: 'somewhere'
    },
    hall14: {
        name: hall14,
        location: 'somewhere'
    },
    hall15: {
        name: hall15,
        location: 'somewhere'
    },
    hall16: {
        name: hall16,
        location: 'somewhere'
    },
    hall17: {
        name: hall17,
        location: 'somewhere'
    },
    hall18: {
        name: hall18,
        location: 'somewhere'
    },
    hall19: {
        name: hall19,
        location: 'somewhere'
    },
    hall20: {
        name: hall20,
        location: 'somewhere'
    },
    hall21: {
        name: hall21,
        location: 'somewhere'
    },
    hall22: {
        name: hall22,
        location: 'somewhere'
    },
    hall23: {
        name: hall23,
        location: 'somewhere'
    },
}

# 1000 x 1000 grid
school_locations = {
    nbs: [437, 758], 
    cceb: [206, 664], 
    eee: [362, 835],
    cee: [325, 641], 
    mse: [481, 600],
    scse: [400, 623],
    mae: [387, 576], 
    soh: [556, 758],
    adm: [600, 435],
    wkwsci: [293, 864],
    sss: [556, 758],
    spms: [418, 894],
    sbs: [225, 711],
    ase: [275, 594],
    lkc: [175, 705],
    nie: [212, 470],
    rsis: [525, 670]
}

# 1000 x 1000 grid
hall_locations = {
    hall1: [800, 630],
    hall2: [640, 540],
    hall3: [380, 350],
    hall4: [710, 740],
    hall5: [800, 700],
    hall6: [810, 550],
    hall7: [550, 160],
    hall8: [630, 360],
    hall9: [650, 280],
    hall10:[680, 200],
    hall11:[750, 120],
    hall12:[430, 260],
    hall13:[500, 260],
    hall14:[480, 210],
    hall15:[540, 210],
    hall16:[370, 280],
    hall17:[883, 623], 
    hall18:[941, 623], 
    hall19:[858, 213], 
    hall20:[900, 213], 
    hall21:[858, 176], 
    hall22:[625, 123], 
    hall23:[675, 117], 
}

hall_mapping = [
    [1, hall1],
    [2, hall2],
    [3, hall3],
    [4, hall4],
    [5, hall5],
    [6, hall6],
    [7, hall7],
    [8, hall8],
    [9, hall9],
    [10, hall10],
    [11, hall11],
    [12, hall12],
    [13, hall13],
    [14, hall14],
    [15, hall15],
    [16, hall16],
    [17, hall17],
    [18, hall18],
    [19, hall19],
    [20, hall20],
    [21, hall21],
    [22, hall22],
    [23, hall23],
]

school_mapping = [
    [1, nbs],
    [2, cceb],
    [3, eee],
    [4, cee],
    [5, mse],
    [6, scse],
    [7, mae],
    [8, soh],
    [9, adm],
    [10, wkwsci],
    [11, sss],
    [12, spms],
    [13, sbs],
    [14, ase],
    [15, lkc],
    [16, nie],
    [17, rsis],
]

room_mapping = [
    [1, single],
    [2, singleToilet],
    [3, singleAC],
    [4, singleACToilet],
    [5, double],
    [6, doubleToilet],
    [7, doubleAC],
    [8, doubleACToilet],
]
