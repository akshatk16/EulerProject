# Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit num_strings. What is the maximum 16-digit num_string for a "magic" 5-gon ring?


from time import time


start = time()

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # available nums


def join_digits(a, b, c, d, e, f, g, h, i, j):
    num = {a: 0, d: 1, f: 2, h: 3, j: 4}
    num_div = num[min(num.keys())]
    nums = [(a, b, c), (d, c, e), (f, e, g), (h, g, i), (j, i, b)]
    nums = nums[num_div:]+nums[:num_div]
    num_string = ''
    for num_tup in nums:
        for num in num_tup:
            num_string += str(num)
    return num_string


possible_perms = []

for a in nums:
    nums_b = nums[:]
    nums_b.remove(a)
    for b in nums_b:
        nums_c = nums_b[:]
        nums_c.remove(b)
        for c in nums_c:
            line_sum = a + b + c
            nums_d = nums_c[:]
            nums_d.remove(c)
            for d in nums_d:
                nums_e = nums_d[:]
                nums_e.remove(d)
                e = line_sum - c - d
                if e in nums_e:
                    nums_f = nums_e[:]
                    nums_f.remove(e)
                    for f in nums_f:
                        nums_g = nums_f[:]
                        nums_g.remove(f)
                        g = line_sum - e - f
                        if g in nums_g:
                            nums_h = nums_g[:]
                            nums_h.remove(g)
                            for h in nums_h:
                                nums_i = nums_h[:]
                                nums_i.remove(h)
                                i = line_sum - g - h
                                if i in nums_i:
                                    j = line_sum - i - b
                                    nums_j = nums_i[:]
                                    nums_j.remove(i)
                                    if j in nums_j:
                                        possible_perms.append(join_digits(a, b, c, d, e, f, g, h, i, j))

# check for largest solution out of all generated solution with 16 digits
sol = max([int(x) if len(x) == 16 else 0 for x in possible_perms])

print(sol)
end = time()
print(int((end-start)*1000), "ms")
