def beauty(n, beauty1, beauty2):
    if n == 1:
        return max(beauty1[0], beauty2[0])
    
    dp1 = [beauty1[0]]
    dp2 = [beauty2[0]]
    
    if n > 1:
        dp1.append(dp2[0] + beauty1[1])
        dp2.append(dp1[0] + beauty2[1])
    
    for i in range(2, n):
        dp1.append(beauty1[i] + max(dp2[i-1], dp2[i-2]))
        dp2.append(beauty2[i] + max(dp1[i-1], dp1[i-2]))
    
    return max(dp1[n-1], dp2[n-1])


if __name__ == "__main__":
    t = int(input())  # Read number of test cases
    for _ in range(t):
        n = int(input())  # Read the value of n
        list1 = list(map(int, input().split()))  # Read first list of beauty values
        list2 = list(map(int, input().split()))  # Read second list of beauty values
        
        result = beauty(n, list1, list2)
        print(result)
