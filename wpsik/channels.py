
frequencies_dict = {
    # 2.4 GHZ channels
    2412: 1, 2417: 2, 2422: 3,
    2427: 4, 2432: 5, 2437: 6,
    2442: 7, 2447: 8, 2452: 9,
    2457: 10, 2462: 11, 2467: 12,
    2472: 13, 2484: 14,
    # 5GHz channelshandler
    5170: 34, 5180: 36, 5190: 38,
    5200: 40, 5210: 42, 5220: 44,
    5230: 46, 5240: 48, 5260: 52,
    5280: 56, 5300: 58, 5320: 60,
    5500: 100, 5520: 104, 5540: 108,
    5560: 112, 5580: 116, 5600: 120,
    5620: 124, 5640: 128, 5660: 132,
    5680: 136, 5700: 140, 5745: 149,
    5765: 153, 5785: 157, 5805: 161,
    5825: 165
}
frequencies_list = [k for k in frequencies_dict.keys()]

channels_dict = dict((v, k) for k, v in frequencies_dict.iteritems())
channels_list = [k for k in channels_dict.keys()]

# channels = {
#     # 2.4ghz channel list
#     '2.4GHz': [x for x in xrange(1, 15)],
#     # 5ghz channel list
#     '5GHz': [34, 36, 38,
#              40, 42, 44, 46, 52, 56,
#              58, 60, 100, 104, 108, 112,
#              116, 120, 124, 128, 132, 136,
#              140, 149, 153, 157, 161, 165]}

channel_hop_list = [1, 6, 11, 13, 2, 7, 3, 8, 4, 9, 5, 10]


# channel_hop_list_full = [1, 6, 11, 14, 2, 7, 3, 8, 4, 9, 5, 10,
#                          36, 38, 40, 42, 44, 46, 52, 56, 58, 60, 100, 104, 108, 112,
#                          116, 120, 124, 128, 132, 136, 140, 149, 153, 157, 161, 165]
