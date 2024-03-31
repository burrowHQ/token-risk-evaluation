# token-risk-evaluation
### Token Rating
|Rate|Collateral Factor|Comment|
|--|--|--|
|A+|95%|Stable Coins|
|A|90%|Algorithm Stable coins|
|A-|85%||
|B+|75%||
|B|70%|Chain Coins|
|B-|65%||
|C+|55%|Popular Tokens|
|C|50%|Popular Tokens|
|C-|45%||


### Adjustment due to Smart Contract
- deployment date, less than 2 years, -5%
- unlocked contract, -5%
### Adjustment due to Liquidation Risk
- TVL in ref.finance
    -  more than 10M, -0%
    -  [5M, 10M], -5%
    -  [1M, 5M], -10%
    -  less than 1M, -15%

| token | Level | basic CF | deployment | locking | LR | ADJ |
|---|---|---|---|---|---|---|
|usdc|A+|95%|-0%|-0%|10M+|-0%|
|usdt|A+|95%|-0%|-0%|10M+|-0%|
|dai|A+|95%|-0%|-0%|2.2M|-10%|
|frax|A|90%|-0%|-0%|4.6M|-10%|
|btc|B+|75%|-0%|-0%|0.8M|-15%|
|eth|B+|75%|-0%|-0%|1M|-10%|
|near|B|70%|-0%|-0%|10M+|-0%|
|woo|C+|55%|-0%|-0%|0.006M|-15%|
|aurora|C+|55%|-0%|-0%|0.6M|-15%|
|ref|C|50%|-0%|-0%|4.23M|-10%|

### Adjustment due to Market Risk
- Market Cap
    - 10000M <= MC, +5%
    - 1000M < MC < 10000M, +0%
    - MC <= 1000M, -5% 
- Average Volume
    - 50M <= AV, +5%
    - 5M < AV < 50M, +0%
    - AV <= 5M, -5%
- Normalized Volatility
    - NV < 0.025, +5%
    - 0.025 <= NV < 0.064, +0%
    - 0.064 <= NV, -5%

The volatility risk is based on the normalised fluctuations in the token price and is calculated as the standard deviation of the logarithmic returns:  

$$ \sigma[ln(\frac{close(t+1)}{close(t)})] $$  

​This metric is in line with industry standards used by Bitmex or Gauntlet.  
These values should be assessed at the following intervals: 1 week, 1 month, 3 months, 6 months, and 1 year.

| token | Market-Cap | ADJ | Day Volume | ADJ | NV | ADJ |
|---|---|---|---|---|---|---|
|usdc|32448M|+5%|4573M|+5%|0.000014|+5%|
|usdt|104578M|+5%|34589M|+5%|0.000055|+5%|
|dai|4917M|+0%|239M|+5%|0.000704|+5%|
|frax|647M|-5%|5.48M|+0%|0.001685|+5%|
|btc|1385231M|+5%|17295M|+5%|0.369959|-5%|
|eth|433812M|+5%|10778M|+5%|0.292461|-5%|
|near|7435M|+0%|264M|+5%|0.620237|-5%|
|woo|823M|-5%|16M|+0%|0.444674|-5%|
|aurora|168M|-5%|1M|-5%|0.727746|-5%|
|ref|15M|-5%|0.08M|-5%|0.708197|-5%|

### Actual Collateral Factor
scope: [30%, 95%]  
liquidity staking token:  
[-5%, -10%]  
Adjustment due to subject opinion of team:  
[-10%, +10%]

| token |basic CF | SC | LR | Market | Subject | ACF |
|------:|--------:|---:|---:|-------:|--------:|----:|
|usdc   |      95%| -0%| -0%|    +15%|       0%|  95%|
|usdt   |      95%| -0%| -0%|    +15%|       0%|  95%|
|dai    |      95%| -0%|-10%|    +10%|       0%|  95%|
|frax   |      90%| -0%|-10%|     +0%|       0%|  80%|
|btc    |      75%| -0%|-15%|     +5%|     +10%|  75%|
|eth    |      75%| -0%|-10%|     +5%|      +5%|  75%|
|near   |      70%| -0%| -0%|     -0%|       0%|  75%|
|woo    |      55%| -0%|-15%|    -10%|     +20%|  50%|
|aurora |      55%| -0%|-15%|    -15%|     +15%|  40%|
|ref    |      50%| -0%|-10%|    -15%|     +15%|  40%|