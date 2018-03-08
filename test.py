list1 = ['a','b','c']
list2 = ['1','2','3','4','5','6','7','8','9','10']
list3 = ['i','ii','iii','iv','v','vi']

lists = [list1, list2, list3]

# all_lists -> blendedlist
# take all lists and returns a blended list
# NOTE RECURSIVE
# def merge_lists(all_lists):
#     if len(all_lists) == 1:
#         return all_lists[0]
#     if len(all_lists[0]) == 0:
#         return merge_lists(all_lists[1:])
#     return [all_lists[0][0]] + merge_lists(all_lists[1:] + [all_lists[0][1:]])

# all_lists -> blendedlist
# take all lists and returns a blended list, initialize wsf with empty list
# NOTE TAIL RECURSIVE
# def merge_lists(all_lists, wsf):
#     if len(all_lists) == 1:
#         return wsf + all_lists[0]
#     if len(all_lists[0]) == 0:
#         return merge_lists(all_lists[1:], wsf)
#     return merge_lists(all_lists[1:] + [all_lists[0][1:]], wsf + [all_lists[0][0]])

# all_lists -> blendedlist
# take all lists and returns a blended list
# NOTE ITTERATIVE
def merge_lists(all_lists):
    result = []
    counter = 0
    empty_counter = True
    while empty_counter:
        empty_counter = False
        for single_list in all_lists:
            try:
                result.append(single_list[counter])
                empty_counter = True or empty_counter
            except:
                empty_counter = False or empty_counter
        counter = counter + 1
    return result


# channel url -> channel uploads playlist id
def get_channel_playlist(channel_url):
    start = channel_url.find('/channel/')
    if start > -1:
        start = start + 9
        print(channel_url[start:])
    start = channel_url.find('/user/')
    if start > -1:
        start = start + 6
        print(channel_url[start:])

get_channel_playlist('https://www.youtube.com/user/HGTV')
