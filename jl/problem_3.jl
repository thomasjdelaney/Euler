#= The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ? =#

using Primes

ans = maximum(Primes.factor(Vector, 600851475143))
@info "The answer is " ans
