# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> Solution  
path: tokenB->tokenA->tokenD->tokenC->tokenB, tokenB balance=113.383266  
1. tokenB -> tokenA balance=192.175027(tokenA)
2. tokenA -> tokenD balance=114.960136(tokenD)
3. tokenD -> tokenC balance=286.540717(tokenC)
4. tokenC -> tokenB balance=2571.152995(tokenB)

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
- To prevent small liquidity adds.  
By subtracting a minimum liquidity amount, the protocol discourages users from adding very small amounts of liquidity. Small liquidity additions can lead to inefficient price discovery and can potentially be exploited by arbitrageurs, resulting in impermanent losses for liquidity providers.

- Efficient Price Discovery  
Uniswap's automated market maker (AMM) mechanism relies on liquidity providers to provide balanced liquidity across the trading pair. By setting a minimum liquidity requirement, the protocol encourages liquidity providers to add a sufficient amount of liquidity to facilitate efficient price discovery and smooth trading.

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> Solution  
In Uniswap V2, when depositing tokens into a liquidity pool (not for the first time), the liquidity minting process follows a specific formula to determine the amount of liquidity tokens (LP tokens) to be minted. This formula is designed with several intentions in mind:

1. **Balancing Liquidity:** The formula ensures that liquidity providers receive a fair share of LP tokens relative to the amount of tokens they are depositing. This helps in maintaining a balanced and proportionate distribution of liquidity in the pool, which is crucial for efficient trading and price discovery.

2. **Protection Against Front-Running:** Front-running refers to the practice of exploiting transactions by placing orders ahead of them in anticipation of benefiting from the subsequent price movement. By using a formula to calculate the amount of LP tokens minted, the process becomes deterministic and prevents front-runners from manipulating the liquidity provisioning process to their advantage.

3. **Prevention of Manipulation:** By having a transparent and deterministic formula, the system guards against potential manipulation of liquidity provision. This enhances the integrity and fairness of the Uniswap protocol, making it more resistant to market manipulation tactics.

4. **Incentivizing Efficient Provisioning:** The formula may also incorporate elements that incentivize efficient liquidity provision, such as providing higher LP token rewards for depositing tokens into pools with lower liquidity or incentivizing depositing tokens that rebalance existing pools in favor of more stable trading pairs.

5. **Ensuring Consistency:** Utilizing a specific formula for determining LP token issuance ensures consistency across different liquidity providers and transactions. This consistency helps in maintaining predictability and trust in the Uniswap protocol, which is essential for its widespread adoption and usage.

Overall, the intention behind using a specific formula for determining the amount of liquidity tokens minted when depositing tokens into a Uniswap V2 liquidity pool is to promote fairness, transparency, efficiency, and integrity within the protocol while discouraging potential manipulation and front-running tactics.


## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> Solution  
A sandwich attack is a type of exploit that targets decentralized exchanges (DEXs) or automated market makers (AMMs) like Uniswap. In a sandwich attack, the attacker aims to manipulate the price of a particular asset by strategically placing buy and sell orders around the target transaction.

Here's how a sandwich attack typically works:

1. **Monitoring Transactions:** The attacker monitors the blockchain for pending transactions involving a specific token pair on the targeted DEX.

2. **Placing Orders:** Before the target transaction is confirmed, the attacker quickly places two transactions on either side of the target transaction. They place a large buy order immediately before the target transaction and a large sell order immediately after it.

3. **Impact on Price:** The large buy order inflates the price of the token, causing the target transaction to execute at a higher price. Then, the large sell order immediately after the target transaction further depresses the price, resulting in the attacker profiting from the price difference.

4. **Profit for the Attacker:** By exploiting the price movement caused by their own buy and sell orders, the attacker can profit at the expense of the trader executing the target transaction.

When initiating a swap on a DEX like Uniswap, you might be impacted by a sandwich attack if your transaction falls between the attacker's strategically placed buy and sell orders. This could result in:

- **Higher Costs:** If you're buying tokens, you might end up paying a higher price than expected due to the inflated price caused by the attacker's buy order.
- **Lower Returns:** If you're selling tokens, you might receive a lower amount of proceeds than anticipated due to the depressed price caused by the attacker's sell order.
- **Slippage:** The price impact caused by the sandwich attack can lead to slippage, where the executed price of your transaction differs significantly from the expected price at the time of transaction initiation.

To mitigate the risk of sandwich attacks, traders can:

- **Use Limit Orders:** Some DEXs support limit orders, which allow traders to specify the maximum price they're willing to pay (for buys) or the minimum price they're willing to accept (for sells). Limit orders can help protect against sudden price movements caused by sandwich attacks.
- **Monitor Transactions:** Traders can monitor pending transactions and blockchain activity to identify potential sandwich attacks. However, this requires vigilance and may not always be practical.

DEX protocols and developers also work on implementing various strategies and safeguards to mitigate the impact of sandwich attacks on their platforms.


