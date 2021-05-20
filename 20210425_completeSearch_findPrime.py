"""
막혔던 부분
리스트의 원소들로 모든 subset을 찾는 알고리즘 구현
"""
#1. subset 알고리즘 찾기
def findSubsets(l):
    base=[]
    lists=[base]
    for i in range(len(l)):
        print(i)
        ori = lists[:]
        new = l[i]
        for j in range(len(lists)):
            lists[j] = lists[j]+[new]
        lists = ori+lists
    return lists

#2. subset이 아니라 모든 subset에 permutation을 구하면 어떻게 될까.
#위 알고리즘을 조금 변형하면 순서가 바뀌어 있는 것도 만들 수 있지 않을까

#조합을 만들어내는 itertools 공부하기
from itertools import permutations
def isPrime(n):
    if n ==1 or n==0:
        return False
    if n==2 or n==3:
        return True
    for a in range(2,n//2+1):
        if n%a ==0:
            return False
    return True




#############################################################

# 조합을 만들어내는 itertools 공부하기
# 조합을 만들어내는 itertools 공부하기
from itertools import permutations
import math


def findPermutations(l):
    maxLength = len(l)
    permus = []
    for currentLength in range(maxLength, 0, -1):
        tempList = permutations(l, currentLength)
        permus += tempList
    for i in range(len(permus)):
        permus[i] = int(''.join(permus[i]))

    return list(set(permus))

"""
https://wikidocs.net/1015
집합 자료형의 연산에서 합집합의 표시가 |였다. 이는 binary operator 가 아니기 때문에, 헷갈리지 않도록 하자. 
set에 대한 이해가 높은 풀이 방법이었다. 

"""

def findPermutationsFromOthers(l):
    a=set()
    for i in range(len(l)):
        a|= set(map(int, map("".join, permutations(list(l), i+1))))
    print(a)

def isPrime(n):
    if n == 1 or n == 0:
        return False
    for a in range(2, int(math.sqrt(n)) + 1):
        if n % a == 0:
            return False
    return True


def solution(l):
    answer = 0
    permuList = findPermutations(l)
    print(permuList)
    for n in permuList:
        if isPrime(n):
            answer += 1
    return answer



if __name__ =='__main__':
    l="123"
    print(solution(l))
    print(findPermutationsFromOthers(l))
##########################################################
    #java solution
    """
    import java.util.*;

class Solution {
    private static int cnt = 0;
    private static String[] map;
    private static String[] result;
    private static boolean[] visit;
    private static HashSet<Integer> list;

    public int solution(String numbers) {
        int answer = 0;

        visit = new boolean[numbers.length()];
        map = new String[numbers.length()];
        map = numbers.split("");

        list = new HashSet();

        for (int i=1; i<=numbers.length(); i++) {
            result = new String[i];
            cycle(0, i, numbers.length());
        }

        return list.size();
    }

    public void cycle(int start, int end, int length) {

        if (start == end) {
            findPrime();
        } else {

            for (int i=0; i<length; i++) {
                if (!visit[i]) {
                    visit[i] = true;
                    result[start] = map[i];
                    cycle(start+1, end, length);
                    visit[i] = false;
                }
            }

        }

    }

    public void findPrime() {

        // 숫자로 변환
        String str = "";
        for(int i=0; i<result.length; i++)
            str += result[i];
        int num = Integer.parseInt(str);

        // 예외 처리
        if(num == 1 || num == 0)
            return;

        // 소수 인지 검사
        boolean flag = false;
        for(int i=2; i<=Math.sqrt(num); i++){
            if(num % i == 0)
                flag = true;
        }

        if(!flag)
            list.add(num);
    }
}
    
    
    """