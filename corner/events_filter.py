__all__ = ['accept_event', 'reject_event', 'filter_events']


_IGNORE_EVENTS = {
     21310, # Check manually
     21310, # The Titchborne Claimant (Not on TMDb, http://www.imdb.com/title/tt0127933/)
     21330, # Check manually
     21360, # Check manually
     21365, # Check manually
     21375,
     21386,
     21438, # Check manually
     21439, # Check manually
     21443,
     21444,
     21474,
     21502,
     21503,
     21553, # Check manually
     21573, # Check manually
     21585,
     21589,
     21590, # Check manually
     21592,
     21593,
     21594, # Check manually
     21597,
     21599,
     21600, # Check manually
     21602, # Check manually
     21621, # Check manually
     21650,
     21651,
     21652,
     21653,
     21656, # Check manually
     21689, # Check manually
     21693, # Check manually
     21697, # Check manually
     21726, # Check manually
     21741, # Check manually
     21754,
     21778, # Check manually
     21780,
     21783,
     21784,
     21785,
     21794,
     21798, # Check manually
     21809, # Check manually
     21827,
     21832,
     21833, # Check manually
     21841, # Check manually
     21842, # Check manually
     21843, # Check manually
     21844, # Check manually
     21849,
     21850, # Check manually
     21865, # Check manually
     21879, # Check manually
     21881, # Check manually
     21882, # Check manually
     21885, # Check manually
     21886, # Check manually
     21887, # Check manually
     21888,
     21889,
     21911,
     21912,
     21913,
     21914,
     21915,
     21916,
     21917,
     21918,
     21919,
     21940,
     21941,
     21942,
     21943,
     21965,
     21966,
     21967,
     21968,
     21988, # Check manually
     22008, # Check manually
     22009, # Check manually
     22016, # Check manually
     22025, # Check manually
     22034, # Check manually
     22043,
     22044,
     22045,
     22058, # Check manually
     22070,
     22086,
     22087,
     22098, # Check manually
     22107,
     22128,
     22142,
     22147, # Check manually
     22149, # Check manually
     22164, # Check manually
     22165, # Check manually
     22166, # Check manually
     22167, # Check manually
     22173,
     22197,
     22198,
     22199,
     22200,
     22204,
     22205,
     22213, # Check manually
     22226, # Check manually
     22236,
     22247, # Check manually
     22266,
     22267,
     22268,
     22295,
     22297,
     22302,
     22303, # Check manually
     22309, # Check manually
     22313, # Check manually
     22316,
     22352, # Check manually
     22372,
     22381,
     22386, # Check manually
     22401, # Check manually
     22405, # Check manually
     22413, # Check manually
     22414, # Check manually
     22421,
     22423,
     22424,
     22425, # Check manually
     22426, # Check manually
     22428, # Check manually
     22429, # Check manually
     22446,
     22453,
     22454,
     22455,
     22456,
     22478, # Check manually
     22479, # Check manually
     22481, # Check manually
     22482, # Check manually
     22483, # Check manually
     22484, # Check manually
     22485, # Check manually
     22486,
     22487,
     22488, # Check manually
     22489,
     22490,
     22491,
     22492,
     22501,
     22502, # Check manually
     22523,
     22534, # Check manually
     22535, # Check manually
     22568,
     22575, # Check manually
     22586, # Check manually
     22595, # Check manually
     22596, # Check manually
     22597, # Check manually
     22615,
     22616,
     22617,
     22618,
     22619,
     22620,
     22621,
     22622,
     22623,
     22624,
     22625,
     22626,
     22627,
     22628,
     22629,
     22631,
     22634, # Check manually
     22635, # Check manually
     22657, # Check manually
     22661, # Check manually
     22663, # Check manually
     22666, # Check manually
     22679, # Check manually
     22700, # Check manually
     22701, # Check manually
     22716, # Check manually
     22719,
     22720,
     22721,
     22742, # Check manually
     22748, # Check manually
     22751, # Check manually
     22770, # Check manually
     22776,
     22778,
     22803, # Check manually
     22806,
     22826,
     22827,
     22854,
     22856, # Check manually
     22861, # Check manually
     22868, # Check manually
     22897,
     22913, # Check manually
     22915, # Check manually
     22916, # Check manually
     22918, # Check manually
     22921, # Check manually
     22922, # Check manually
     22932,
     22935,
     22936,
     22937,
     22938,
     22939,
     22940,
     22941,
     22943,
     22944,
     22945,
     22946,
     22948, # Check manually
     22960, # Check manually
     22961,
     22963, # Check manually
     22972,
     22990, # Check manually
     23025, # Check manually
     23034, # Check manually
     23039,
     23040, # Check manually
     23042, # Check manually
     23058,
     23063,
     23065, # Check manually
     23067, # Check manually
     23069, # Check manually
     23070, # Check manually
     23080,
     23081,
     23082,
     23089, # Check manually
     23098, # Check manually
     23101,
     23119, # Check manually
     23125,
     23126,
     23134, # Check manually
     23135, # Check manually
     23144,
     23145, # Check manually
     23156, # Check manually
     23204, # Check manually
     23205,
     23206,
     23218,
     23240, # Check manually
     23254,
     23265,
     23266,
     23279,
     23283,
     23295,
     23296,
     23311,
     23314, # Check manually
     23318,
     23319,
     23321,
     23322,
     23323, # Check manually
     23324,
     23325,
     23326,
     23327,
     23328,
     23329,
     23330,
     23342, # Check manually
     23353, # Check manually
     23354, # Check manually
     23368, # Check manually
     23369, # Check manually
     23385,
     23386,
     23391,
     23398,
     23404, # Check manually
     23414, # Check manually
     23423, # Check manually
     23427,
     23491, # Check manually
     23493,
     23530, # Check manually
     23555, # Check manually
     23556, # Check manually
     23568, # Check manually
     23606, # Check manually
     23614, # Check manually
     23632,
     23633,
     23634,
     23635, # Check manually
     23655, # Check manually
     23665, # Check manually
     23672, # Check manually
     23703, # Check manually
     23714, # Check manually
     23715,
     23716,
     23717, # Check manually
     23718, # Check manually
     23720,
     23723,
     23725, # Check manually
     23726,
     23728, # Check manually
     23729,
     23731, # Check manually
     23734, # Check manually
     23741, # Check manually
     23745,
     23747, # Check manually
     23752, # Check manually
     23775, # Check manually
     23796, # Check manually
     23821,
     23826, # Check manually
     23856,
     23885,
     23915,
     23949, # Check manually
     24040, # Check manually
     24141, # Check manually
     24143, # Check manually
     24163,
     24190, # Check manually
     24207,
     24247, # Check manually
     24324,
     24334, # Check manually
     24419, # Check manually
     24420, # Check manually
     24425,
     24426, # Check manually
     24429,
     24432,
     24436,
     24439, # Check manually
     24442, # Check manually
     24445, # Check manually
     24447,
     24450,
     24453,
     24456,
     24464,
     24468,
     24472,
     24473,
     24489, # Check manually
     24521, # Check manually
     24554, # Check manually
     24558, # Check manually
     24560, # Check manually
     24591, # Check manually
     24642, # Check manually
     24671,
     24892, # Check manually
     24894, # Check manually
     24898, # Check manually
     24901, # Check manually
     24903, # Check manually
     24904,
     24906, # Check manually
     24986, # Check manually
     25059,
     25073, # Check manually
     25100, # Check manually
     25102, # Check manually
     25123, # Check manually
     25131, # Check manually
     25146,
     25151,
     25153,
     25233, # Check manually
     25253, # Check manually
     25285, # Check manually
     25317,
     25320, # Check manually
     25322, # Check manually
     25325,
     25354,
     25368,
     25370, # Check manually
     25372, # Check manually
     25380, # Check manually
     25386,
     25395, # Check manually
     25440,
     25442,
     25444,
     25447, # Check manually
     25449,
     25451,
     25453,
     25455,
     25457,
     25459,
     25488, # Check manually
     25530, # Check manually
     25571, # Check manually
     25577,
     25585, # Check manually
     25589,
     25595, # Check manually
     25599, # Check manually
     25603,
     25613,
     25620, # Check manually
     25634, # Check manually
     25705,
     25713, # Check manually
     25724, # Check manually
     25731, # Check manually
     25732, # Check manually
     25733, # Check manually
     25735, # Check manually
     25738, # Check manually
     25805, # Check manually
     25807, # Check manually
     25811, # Check manually
     25817, # Check manually
     25837, # Check manually
     25864, # Check manually
     25872, # Check manually
     25930, # Check manually
     25932,
     25951, # Check manually
     25966, # Check manually
     25974, # Check manually
     26026, # Check manually
     26061, # Check manually
     26103, # Check manually
     26118, # Check manually
     26119, # Check manually
     26121, # Check manually
     26125, # Check manually
     26150, # Check manually
     26161, # Check manually
     26181, # Check manually
     26191, # Check manually
     26195, # Check manually
     26198, # Check manually
     26203, # Check manually
     26209, # Check manually
     26216, # Check manually
     26368, # Check manually
     26386, # Check manually
     26393, # Check manually
     26404, # Check manually
     26463, # Check manually
     26474, # Check manually
     26478, # Check manually
     26487, # Check manually
     26611, # Check manually
     26620, # Check manually
     26624, # Check manually
     26630, # Check manually
     26631, # Check manually
     26633, # Check manually
     26639, # Check manually
     26641, # Check manually
     26643, # Check manually
     26647, # Check manually
     26711,
     26747,
     26753,
     26761,
     26767,
     26773,
     26809, # Check manually
     26852,
     26854,
     26858, # Check manually
     26861, # Check manually
     27076, # Check manually
     27081, # Check manually
     27085, # Check manually
     27086, # Check manually
     27090, # Check manually
     27096, # Check manually
     27117, # Check manually
     27123, # Check manually
     27129, # Check manually
     27131, # Check manually
     27134, # Check manually
     27253, # Check manually
     27257, # Check manually
     27282, # Check manually
     27289, # Check manually
     27293, # Check manually
     27407,
     27415,
     27422,
     27427,
     27436,
     27444,
     27454,
     27466,
     27550,
     27651, # Check manually
     27766,
     27768,
     27770,
     27843, # Check manually
     27851, # Check manually
     27855, # Check manually
     27870, # Check manually
     27889, # Check manually
     27893, # Check manually
     27898, # Check manually
     27907, # Check manually
     27917, # Check manually
     27932,
     27939,
     27952, # Check manually
     28034, # Check manually
     28040,
     28041, # Check manually
     28043,
     28264, # Check manually
     28274, # Check manually
     28484,
     28621,
     28623, # Check manually
     28625, # Check manually
     28700, # Check manually
     28705, # Check manually
     28709, # Check manually
     28787, # Check manually
     28791, # Check manually
     28793,
     28803, # Check manually
     28816,
     28818,
     28820,
     28822,
     28824,
     28826,
     28828,
     28833,
     28842, # Check manually
     29000, # Check manually
     29112, # Check manually
     29156, # Check manually
     29255, # Check manually
     29256, # Check manually
     29258,
     29266, # Check manually
     29322, # Check manually
     29329, # Check manually
     29337, # Check manually
     43547, # Check manually
     43550, # Check manually
     45755, # Check manually
     45759, # Check manually
     54873,
     55622,
     55649,
     57807,
     57815, # Check manually
     58041,
     59727, # Check manually
     59736, # Check manually
     60709, # Check manually
     60802,
     62688,
     62703,
     63589, # Check manually
     63720, # Check manually
     65444,
     65490,
     65505,
     67782,
     67808,
     67817,
     67839,
     67849,
     67859,
     67936,
     70500,
     70547, # Check manually
     70828, # Check manually
     70961, # Check manually
     71030, # Check manually
     71249, # Check manually
     74506,
     74525,
     74558,
     75144, # Check manually
     75220,
     76365, # Check manually
     76529,
     76983,
     76986,
     78523,
     78719, # Check manually
     78741, # Check manually
     79259,
     81028, # Check manually
     82570, # Check manually
     82954,
     84296, # Check manually
     84647, # Check manually
     84966, # Check manually
     84972, # Check manually
     86853, # Check manually
     86977, # Check manually
     87479,
     87485,
     91233,
     91250, # Check manually
     91700, # Check manually
     92629,
     93522, # Check manually
     94556, # Check manually
     94617, # Check manually
     95180, # Check manually
     95266, # Check manually
     95284,
     95767, # Check manually
     95908,
     95911,
     95947,
     98053, # Check manually
     98061, # Check manually
     98069, # Check manually
     98335, # Check manually
     98377, # Check manually
     98708,
     99637,
     99775,
     99777,
     99831,
     99911,
     99922,
     99943,
    100059, # Check manually
    100265, # Check manually
    100295, # Check manually
    100377, # Check manually
    100387, # Check manually
    100405, # Check manually
    100405, # Mar de Plata (not in TMDb, http://www.imdb.com/title/tt2207022/)
    100480,
    101944,
    101949,
    101957,
    101966,
    101982,
    102005, # Movement, Magic and Mirrors: Five short films by Maya Deren (Not on TMDb)
    103008, # NT Live: Medea (Not a film)
    103869, # Matisse Live (Not a film)
    104004, # Monty Python Live (Mostly) (Not a film)
    104437, # NT Live: Skylight (Not a film)
    105088, # Art Party (Not on TMDb)
}


def accept_event(event):
    return event.id not in _IGNORE_EVENTS


def reject_event(event):
    return event.id in _IGNORE_EVENTS


def filter_events(events):
    return filter(accept_event, events)

