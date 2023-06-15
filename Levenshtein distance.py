def calculate_levenshtein_distance(str_a, str_b):
    m = len(str_a)
    n = len(str_b)

    
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Calculate the distances
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str_a[i - 1] == str_b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(
                    dp[i - 1][j] + 1,  
                    dp[i][j - 1] + 1,  
                    dp[i - 1][j - 1] + 1  
                )

  
    return dp[m][n]



string_a = "76nk3a4n72nt"
string_b = "76z0t3sufc5u"
distance = calculate_levenshtein_distance(string_a, string_b)
print("Levenshtein distance:", distance)
