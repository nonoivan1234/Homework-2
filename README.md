# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> Solution  
path: tokenB->tokenA->tokenD->tokenC->tokenB, tokenB balance=113.383266  
1. tokenB -> tokenA balance=192.175027
2. tokenA -> tokenD balance=114.960136
3. tokenD -> tokenC balance=286.540717
4. tokenC -> tokenB balance=2571.152995

## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

> Solution  
### What is Slippage in AMM?

Slippage in Automated Market Makers (AMMs) refers to the difference between the expected price of a trade and the actual price at which the trade is executed. This discrepancy typically occurs in highly volatile markets or when executing large trades due to the constant updating of token prices based on the automated pricing algorithm of the AMM.

### How Uniswap V2 Addresses Slippage

Uniswap V2 addresses slippage by implementing a constant product market maker formula. In Uniswap V2, the product of the number of tokens in two pools remains constant, which means that as the supply of one token decreases during a trade, the supply of the other token increases proportionally to maintain the product.

#### The Uniswap V2 Formula

The Uniswap V2 formula is:

\[ $x \cdot y = k$ \]

Where:
- \( x \) is the amount of one token in the pool
- \( y \) is the amount of the other token in the pool
- \( k \) is the constant product of \( x \) and \( y \)

### Illustration with an Example

To illustrate how Uniswap V2 addresses slippage, let's consider a simple example:

Suppose we have a Uniswap V2 pool with ETH and DAI tokens, initially with 10 ETH and 5000 DAI, so the initial value of \( k \) is \( $10 \times 5000 = 50000$ \).

Now, let's say a trader wants to swap 1 ETH for DAI from this pool. Before the trade, the pool looks like this:

- \( $x_1 = 10$ \) ETH
- \( $y_1 = 5000$ \) DAI

After the trade, the trader will receive some DAI while the pool adjusts. Let's denote \( \Delta x \) as the change in ETH and \( \Delta y \) as the change in DAI. The new amounts will be:

- \( $x_2 = 10 - \Delta x$ \) ETH
- \( $y_2 = 5000 + \Delta y$ \) DAI

According to the constant product formula:

\[ $(10 - \Delta x) \times (5000 + \Delta y) = 50000$ \]

When executing the trade, Uniswap V2 ensures that:

\[ $\text{Slippage} = \frac{\text{Actual price} - \text{Expected price}}{\text{Expected price}}$ \]

By maintaining the constant product, Uniswap V2 minimizes slippage, providing traders with more predictable and fairer trades.


## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> Solution

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> Solution

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> Solution

