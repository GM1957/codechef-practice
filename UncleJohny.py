testcase = int(input())
for test in range (testcase):
    num = int(input())
    songs = list(map(int, input().split(' ')))
    jonycurr = songs[int(input()) - 1]
    songs.sort()
    yo = songs.index(jonycurr)
    print(yo + 1)