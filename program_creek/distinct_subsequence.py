def distinct(S, T):
    dp = [[0] * (len(T) + 1) for _ in range(0, len(S) + 1)]
    
    for i in range(0, len(S)):
        dp[i][0] = 1
        
    for i in range(1, len(S) + 1):
        for j in range(1, len(T) + 1):
            if S[i-1] == T[j-1]:
                dp[i][j] += dp[i-1][j] + dp[i-1][j-1]
            else:
                dp[i][j] += dp[i-1][j]
    
    return dp[len(S)][len(T)]
    
def main():
    print(distinct("rabbbit", "rabbit"))

if __name__ == "__main__":
    main()