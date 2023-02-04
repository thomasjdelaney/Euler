ans = sum(i -> i % 5 == 0 || i % 3 == 0 ? i : 0, 1:999)
@info "The answer is " ans

