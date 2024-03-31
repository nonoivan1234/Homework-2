liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}

def return_money(orig, to, amount):
    if(orig == to):
        return amount
    try:
       return amount * liquidity[(orig, to)][1] * 0.997 / (liquidity[(orig, to)][0] + amount * 0.997)
    except:
        return amount * liquidity[(to, orig)][0] * 0.997 / (liquidity[(to, orig)][1] + amount * 0.997)

tokens = ["tokenA", "tokenB", "tokenC", "tokenD", "tokenE"]

max_length = 5

def find_profitable_path(start_token, initial_balance):
    stack = [(start_token, [start_token], initial_balance)]
    while stack:
        if len(stack[-1][1]) > max_length:
            stack.pop()
            continue
        token, path, balance = stack.pop()
        if balance > 20 and token == "tokenB":
            print(f"path: {'->'.join(path)}, tokenB balance={balance:.6f}")
            return path
        
        for next_token in tokens:
            if next_token == token:
                continue
            new_balance = return_money(token, next_token, balance)
            stack.append((next_token, path + [next_token], new_balance))

# Start the search with tokenB and an initial balance of 5
path = find_profitable_path("tokenB", 5)

# balance = 5
# for i in range(len(path) - 1):
#     balance = return_money(path[i], path[i + 1], balance)
#     print(f"  {path[i]} -> {path[i + 1]}: {balance:.6f}")