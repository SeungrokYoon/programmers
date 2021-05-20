#위
def solution(clothes):
    answer = 0
    temp=1
    hash_map={'1':0}
    for clothe in clothes:
        if clothe[1] not in hash_map.keys():
            hash_map[clothe[1]]=0
            hash_map[clothe[1]]+=1
        else:
            hash_map[clothe[1]]+=1
    for key in hash_map.keys():
        temp *= (hash_map[key]+1)
    answer =temp-1
    return a장nswer

#베스트 앨
def solution(genres, plays):
    answer = []
    music_map = {}
    genre_map = {}
    new_list = []

    for i in range(len(genres)):
        if genres[i] not in genre_map:
            genre_map[genres[i]] = 0
            music_map[genres[i]] = []
        genre_map[genres[i]] += plays[i]
        music_map[genres[i]].append([i, plays[i], genres[i]])

    for value in music_map.values():
        for subvalue in value:
            subvalue[2] = genre_map[subvalue[2]]

    for key in music_map.keys():
        music_map[key].sort(key=lambda x: (x[1], -x[0]), reverse=True)
        if len(music_map[key]) == 1:
            new_list += music_map[key]
        else:
            new_list += music_map[key][:2]
    new_list.sort(key=lambda x: (x[2], x[1], -x[0]), reverse=True)
    for v in new_list:
        answer.append(v[0])
    return answer