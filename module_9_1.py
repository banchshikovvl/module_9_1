def apply_all_func(int_list, *functions):
    results = {}
    for functions in functions:
        result = functions(int_list)
        results[functions.__name__] = result
    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

