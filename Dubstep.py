'''
Input
The input consists of a single non-empty string, consisting only of uppercase English letters, the string's length doesn't exceed 200 characters

Output
Return the words of the initial song that Polycarpus used to make a dubsteb remix. Separate the words with a space.

Examples
song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")
  # =>  WE ARE THE CHAMPIONS MY FRIEND
'''
def song_decoder(song):
    res = song.split('WUB')
    # for i in res:
    #     if i == '':
    #         res.remove(i)
    # 没有办法删除所有的空元素
    # for循环居然不能删除列表中所有空值！
    # for的计数器是依次递增的，但列表的内容已通过remove更改，i迭代的值为a ‘’ ‘’ ‘’然后越界，所以，只能删除前三个空元素。
    #第一种：
    while '' in res:
        res.remove('')
    #第二种：
    res = [i for i in res if i != '']
    print(' '.join(res))

song_decoder("AWUBWUBWUBBWUBWUBWUBC")