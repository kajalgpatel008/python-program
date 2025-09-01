def remove_duplicate(s):
    seen=[]
    result=[]
    for ch in s:
        if ch not in seen:
            seen.append(ch)
            result.append(ch)
    return "".join(result)
print(remove_duplicate("kaajajlmpatel"))
