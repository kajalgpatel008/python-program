def title_case(s):
    words=s.split()
    return " ".join (w[0].upper()+w[1:].lower() if w else "" for w in words)
print(title_case("hello WORLD"))


