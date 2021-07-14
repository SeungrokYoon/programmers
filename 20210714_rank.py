# 코딩테스트연습/그래프/순위

"""
해답을 찾는데 많은 시간이 걸렸던 문제이다.
이 문제를 처음 보고 내가 든 생각.->보통 이런 직관이 풀이법을 선택하는데 영향을 많이 주니까...
1)어...BFS인가?
2)그럼....DFS인가?
3) 그래프 알고리즘을 공부할 때 배웠던건 다익스트라, 플로이드 워셜인데 그 중 하나인가?
....아아아......너무 머리가 아팠다. 손으로 그림을 그리면 으흥...이러면 순위가 정해지네

1) 한 노드에 대해서 승리, 패배되하는 노드의 개수가 n-1 라면 확실하게 순위가 정해진다.
2) a->b, b->c, c>d이면 a는 d를 이긴 판정이 된다.

아니 그래서 뭐 어쩌라는건가!

모든 노드들에 대해서 모든 다른 노드들에 대한 승패 판정을 알아내야 한다.
모든 - 모든 -> 플로이드 워셜 사용하면 될 것 같았다.


선수가 총 n명이 존재할 때, 다른 n-1명의 선수들과의 승패를 확실하게 알 수만 있으면 순위가 정해집니다.

예를 들어, 총 5명의 선수가 있을 때, 1번 선수의 순위가 확실시 되는지를 알고 싶다면, 나머지 2번부터 5번까지 선수와의 경기 승패결과가 모두 있어야 합니다.

그렇지만 주어진 간선정보만으로는 충분하지 않습니다. 가령 results= [[1,2],[2,3]] 의 경우, 우리는 직관적으로는 '1번 선수가 3번 선수도 이겼네' 라고 알 수 있지만, [1,2] 간선은 results에서는 주어지지 않았고, 이 점이 우리가 그래프를 만들 때 난관으로 작용합니다.

그리고 이 부분이 우리가 이제껏 배운 알고리즘 개념이 적용되는 부분입니다.

우리가 배웠던 그래프, 최단거리 알고리즘 중에서 특정 정점에서 모든 정점을 거쳐 다른 정점까지의 최단거리를 구했던 알고리즘이 있습니다. 바로 플로이드-워셜 알고리즘이지요. 그렇지만 이 문제는 최단거리를 구하는 문제는 아닙니다.

이 문제에서 위 알고리즘이 적용되는 부분은, 2차원 배열 그래프에 모든 선수들 끼리의 '승리와 패배를 동시에 기록'하는 것입니다. 즉, a->b,b->c이면 table[a][c] 와 table[c][a] 의 값이 승패 기록을 위해 같이 기록되어야 한다는 것입니다.

그리고 a->b이지만 b<-c인 경우에 a와 c의 승패는 알 수 없다는 점도 기억해야 합니다.

그럼 다들 화이팅 하십쇼!
"""

def solution(n, results):
    """플로이드 워셜 """
    answer = 0

    dp_table = [[0] * (n+1) for _ in range(n+1)]

    # 그래프 입력
    for a, b in results:
        # 포인트는 이긴 녀석은 1로 진 녀석은 -1로 초기화 하는 것 0 은 아직 모르는 것.
        dp_table[a][b] = 1
        dp_table[b][a] = -1

    # 플로이드 워셜 알고리즘 적용
    for k in range(1,n+1):
        for a in range(1,n+1):
            for b in range(1,n+1):
                if dp_table[a][b] ==0:
                    if dp_table[a][k] == 1 and dp_table[k][b] == 1:
                        dp_table[a][b] = 1
                        dp_table[b][a] = -1
                    elif dp_table[a][k] == -1 and dp_table[k][b] == -1:
                        dp_table[a][b] = -1
                        dp_table[b][a] = 1

    # 결과 출력
    for i in range(1,n+1):
        print(dp_table[i][1:])
        if dp_table[i][1:].count(0) == 1:
            answer += 1

    return answer
"""
틀렸다! 왜 틀렸을까.....고민을 해보자......
"""

