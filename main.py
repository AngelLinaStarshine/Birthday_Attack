import random
from sympy import isprime

def num_gen(n, prime=True):
    return [p for p in range(2, n) if isprime(p)] if prime else [x for x in range(4, n) if not isprime(x)]

def hash(p1, p2, p3):
    return p1 ^ p2 ^ p3

def hash_gen(prime_numbers):
    hash_set = {}
    print("16 valid messages:")
    for _ in range(16): 
        p_num1, p_num2, p_num3 = random.sample(prime_numbers, 3) 
        hash_value = hash(p_num1, p_num2, p_num3)
        hash_set[hash_value] = (p_num1, p_num2, p_num3) 
        print(f"({p_num1} {p_num2} {p_num3}) || {hash_value}")
    return hash_set

def collision(hash_set, composite_numbers):
    print("\nLooking for a fraudulent message that matches a valid message's hash...")
    attempts = 0
    collision_found = False

    while not collision_found:
        c1, c2, c3 = random.sample(composite_numbers, 3) #3 unique random composites are selected
        composite_hash = hash(c1, c2, c3)
        attempts += 1

        if composite_hash in hash_set: 
            collision_found = True
            print(f"Collision found after {attempts} attempts:")
            print(f"({c1} {c2} {c3}) || {composite_hash}")
            print(f"({hash_set[composite_hash][0]} {hash_set[composite_hash][1]} {hash_set[composite_hash][2]}) || {composite_hash}")

    input("Press any key to continue...")

def main():
    n = 256 
    prime_numbers = num_gen(n, prime=True)
    composite_numbers = num_gen(n, prime=False)
    hash_set = hash_gen(prime_numbers)
    collision(hash_set, composite_numbers)

if __name__ == "__main__":
    main()
