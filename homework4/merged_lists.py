def merge_and_sort(list1, list2):
    merged_list = list1 + list2
    merged_list.sort()
    return merged_list

if __name__ == "__main__":
    list1 = [(1, "apple"), (3, "orange"), (5, "banana")]
    list2 = [(2, "grape"), (4, "kiwi"), (6, "melon")]

    result = merge_and_sort(list1, list2)
    print(result)