# https://www.hackerrank.com/challenges/one-week-preparation-kit-zig-zag-sequence/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=preparation-kits&playlist_slugs%5B%5D%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D%5B%5D=one-week-day-three
def findZigZagSequence(a, n):
        a.sort()
        mid = int((n + 1)/2) - 1 # 1st modification
        a[mid], a[n-1] = a[n-1], a[mid]

        st = mid + 1
        ed = n - 2 # 2nd modification
        while(st <= ed):
                a[st], a[ed] = a[ed], a[st]
                st = st + 1
                ed = ed - 1 # 3rd modification

        for i in range (n):
                if i == n-1:
                        print(a[i])
                else:
                        print(a[i], end = ' ')
        return

test_cases = int(input())
for cs in range (test_cases):
        n = int(input())
        a = list(map(int, input().split()))
        findZigZagSequence(a, n)