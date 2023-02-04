#= A palindromic number reads the same both ways. The largest palindrome made from 
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers. =#

using Primes
using Combinatorics

"For getting the largest palindromic number less than or equal to the given limit.
# Arguments
- limit::Integer: the limit.
# Returns
- the large palindromic number less than the limit"
function get_largest_palindromic_number_below_limit(limit::Integer)::Integer
    str_limit = string(limit)
    num_digits = length(str_limit)
    half_num_digits = Int(ceil(num_digits / 2))
    str_prefix = str_limit[1:half_num_digits]
    prefix_reversed_str = parse(Int, reverse(str_prefix))
    suffix_int = parse(Int, str_limit[end-half_num_digits+1:end])
    is_suffix_lt_reversed_prefix = suffix_int <= prefix_reversed_str
    if num_digits % 2 == 1
        if is_suffix_lt_reversed_prefix
            centre_digit = parse(Int, str_limit[half_num_digits])-1
        else
            centre_digit = parse(Int, str_limit[half_num_digits])
        end
        prefix = str_prefix[1:end-1]
        suffix = reverse(prefix)
        palindromic_str = "$prefix$centre_digit$suffix"
        palindromic_number = parse(Int, palindromic_str)
    else
        if is_suffix_lt_reversed_prefix
            str_prefix = string(parse(Int, str_prefix) - 1)
            palindromic_number = parse(Int, "$str_prefix$(reverse(str_prefix))")
        else
            palindromic_number = parse(Int, "$str_prefix$(reverse(str_prefix))")
        end
    end
    return palindromic_number
end

"Try to make an n digit int from a combination of the largest factor in factors and next largest possible.
Return 0 if this is not possible.
# Arguments
- factors: a list of ints
- n: the number of digits allowed
# Returns
- either the factor itself or 0"
function try_make_n_digit_product_from_factors(
    factors::Vector{<:Integer}, n::Integer)::Tuple{Integer, Tuple{Integer, Integer}}
    max_product = 0
    max_product_pair = (0, 0)
    for pair in combinations(factors, 2)
        product = np.prod(pair)
        if product > max_product & len(str(product)) <= n
            max_product = product
            max_product_pair = pair
        end
    end
    return max_product, max_product_pair
end

"For checking if the given integer is a product of m integers of n digits
# Arguments
- to_check: the int to check
- m: the number of products
- n: the number of digits allowed in the products
# Returns
- bool"
function is_product_of_m_n_digit_int(to_check::Integer; m::Integer, n::Integer)::Bool
    is_product = false
    prime_factors = Primes.factor(Vector, to_check)
    has_long_factors = any(x -> length(string(x)) > n, prime_factors)
    if has_long_factors
        return false
    end
    factors = prime_factors
    largest_n_digit_product = 0
    max_product = 0
    while max_product != 0
        largest_n_digit_product = max_product
        max_product, used_pair = try_make_n_digit_product_from_factors(factors, n)
        if max_product == 0
            continue
        end
        map(u -> factors.remove(u), used_pair)
        push!(factors, max_product)
    end
    if length(factors) == m
        is_product = true
    end
    return is_product
end

"Counts down from limit testing each palindromic number
# Arguments
- starting_limit: int
# Returns
- res"
function get_largest_palindromic_number_with_three_digit_prime_factor(starting_limit:: Integer)::Integer
    is_product_of_three_digit_pair = false
    limit = starting_limit
    while !is_product_of_three_digit_pair
        palindromic_number = get_largest_palindromic_number_below_limit(limit)
        is_product_of_three_digit_pair = is_product_of_m_n_digit_int(palindromic_number, m=2, n=3)
        limit = palindromic_number
        @info "The number is " limit
    end
    return limit
end

three_digit_palindrome_limit = 999*999
ans = get_largest_palindromic_number_with_three_digit_prime_factor(three_digit_palindrome_limit)
@info "The answer is " ans