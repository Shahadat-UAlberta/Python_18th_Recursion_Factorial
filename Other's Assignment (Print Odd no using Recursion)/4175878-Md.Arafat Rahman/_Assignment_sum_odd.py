def odd_sums(n):
    if n == 0:
        return []
    else:
        odd_sum = odd_sums(n-1)
        if n % 2 == 1:
            odd_sum.append(n)
        return odd_sum
n = int(input("Enter a number:"))
odd_sums_list =odd_sums(n)
print("odd sums:",odd_sums_list)


