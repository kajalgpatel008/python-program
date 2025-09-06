def max_min(s):
    words=s.split()
    return " ".join(w[0].upper()+w[1:].lower() if w else "" for w in words)
print(max_min("kajal M patel "))
 
