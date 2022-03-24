# FRC Ranking with Monkeys

Ranking FRC teams is a difficult task because teams play in alliances that are three on three.
Who should get credit for the win? How much credit? Based on an idea that was used once for [football
teams](http://mathtourist.blogspot.com/2007/11/random-walks-to-football-rankings.html). The method used here
is to create a graph with nodes or each team and edges that represent that teams opponents.
We start by associating some large numbers of monkeys to the all the nodes randomly.
The monkeys monkeys are polled thousands of times, and some percentage of the time they chose to pick a new 
team (about 20%, right now). If the monkey changes from their chosen team, then it will move to own of their opponents
with the oppenents that have beaten our given team being about 5 times more likely to be chosen than an opponent that lost. 
Of the three opponents that we are choosing from we weight by their season point-differentials. Then we move the next monkey. 
We keep doing this thousands of times, in the hopes that it will become steady. 

Here are results from a recent run (```num_monkeys=4000, num_iterations=20000```):

| Rank | Team Number | Point Difference | Number of Monkeys |
| ---- | ----------- | ---------------- | ----------------- |
| 1    | 176         | 45.19            | 218               |
| 2    | 5813        | 37.24            | 145               |
| 3    | 7407        | 36.17            | 134               |
| 4    | 3467        | 15.75            | 119               |
| 5    | 177         | 30.14            | 103               |
| 6    | 125         | 34.20            | 102               |
| 7    | 6328        | 32.33            | 101               |
| 8    | 95          | 21.61            | 79                |
| 9    | 2262        | \-2.28           | 73                |
| 10   | 88          | 9.39             | 64                |
| 10   | 228         | 13.46            | 64                |
| 12   | 133         | 26.19            | 63                |
| 13   | 230         | 17.26            | 61                |
| 14   | 131         | 14.94            | 58                |
| 15   | 4909        | 8.03             | 57                |
| 16   | 6329        | 23.44            | 52                |
| 17   | 2168        | 23.94            | 50                |
| 18   | 3566        | \-8.77           | 49                |
| 19   | 7907        | \-4.53           | 45                |
| 19   | 467         | \-4.50           | 45                |
| 21   | 126         | 7.57             | 43                |
| 22   | 663         | 3.00             | 41                |
| 23   | 155         | 11.88            | 40                |
| 23   | 8085        | \-0.89           | 40                |
| 25   | 8889        | 17.17            | 39                |
| 26   | 8724        | 1.69             | 36                |
| 26   | 8013        | 2.93             | 36                |
| 28   | 1153        | 11.21            | 35                |
| 29   | 1991        | \-3.55           | 34                |
| 29   | 1768        | \-2.06           | 34                |
| 31   | 4564        | 14.89            | 33                |
| 32   | 1071        | \-7.89           | 32                |
| 32   | 3654        | \-3.50           | 32                |
| 32   | 151         | 1.89             | 32                |
| 35   | 1729        | \-5.25           | 31                |
| 35   | 1277        | \-1.00           | 31                |
| 37   | 4905        | 5.88             | 30                |
| 37   | 6620        | \-4.13           | 30                |
| 37   | 58          | 12.94            | 30                |
| 40   | 7153        | 4.00             | 29                |
| 41   | 5563        | 12.95            | 28                |
| 41   | 1474        | 5.00             | 28                |
| 41   | 195         | \-0.78           | 28                |
| 44   | 2877        | 11.94            | 27                |
| 44   | 6895        | \-3.75           | 27                |
| 46   | 238         | 11.69            | 25                |
| 46   | 1027        | 4.75             | 25                |
| 46   | 811         | \-8.75           | 25                |
| 49   | 178         | \-8.29           | 24                |
| 49   | 2370        | 11.29            | 24                |
| 49   | 5687        | \-1.56           | 24                |
| 49   | 4906        | \-2.14           | 24                |
| 53   | 7127        | 16.50            | 23                |
| 54   | 4546        | \-4.57           | 22                |
| 54   | 1073        | 14.14            | 22                |
| 54   | 3146        | \-11.25          | 22                |
| 54   | 1699        | \-11.71          | 22                |
| 54   | 236         | \-2.81           | 22                |
| 59   | 7869        | \-13.25          | 21                |
| 59   | 4041        | \-0.29           | 21                |
| 61   | 4761        | \-12.11          | 20                |
| 61   | 1740        | 2.53             | 20                |
| 61   | 8046        | \-3.64           | 20                |
| 61   | 6763        | \-2.79           | 20                |
| 61   | 558         | \-1.21           | 20                |
| 61   | 7694        | \-4.33           | 20                |
| 67   | 6690        | 1.31             | 19                |
| 67   | 5856        | 1.29             | 19                |
| 69   | 78          | 2.00             | 18                |
| 69   | 4572        | \-3.92           | 18                |
| 69   | 1350        | \-1.00           | 18                |
| 69   | 2648        | \-2.93           | 18                |
| 73   | 319         | \-7.00           | 17                |
| 73   | 237         | \-2.19           | 17                |
| 73   | 3461        | \-0.65           | 17                |
| 73   | 716         | \-2.07           | 17                |
| 73   | 3451        | \-6.86           | 17                |
| 78   | 246         | \-1.83           | 16                |
| 78   | 1922        | \-13.86          | 16                |
| 78   | 3719        | \-4.43           | 16                |
| 78   | 8167        | 0.58             | 16                |
| 78   | 4628        | \-4.17           | 16                |
| 78   | 157         | \-4.50           | 16                |
| 78   | 5494        | \-3.71           | 16                |
| 78   | 190         | \-9.14           | 16                |
| 86   | 3464        | \-17.21          | 15                |
| 86   | 6933        | \-3.92           | 15                |
| 86   | 2064        | \-3.29           | 15                |
| 86   | 6333        | \-9.92           | 15                |
| 86   | 1831        | \-11.79          | 15                |
| 91   | 5491        | \-6.92           | 14                |
| 91   | 501         | \-11.50          | 14                |
| 91   | 5902        | \-4.42           | 14                |
| 91   | 7913        | \-3.92           | 14                |
| 91   | 3182        | \-5.71           | 14                |
| 91   | 999         | \-10.14          | 14                |
| 91   | 166         | 1.29             | 14                |
| 98   | 2713        | \-5.50           | 13                |
| 98   | 6723        | \-6.86           | 13                |
| 98   | 97          | \-4.67           | 13                |
| 98   | 571         | \-8.38           | 13                |
| 98   | 1058        | \-8.43           | 13                |
| 98   | 2067        | \-0.29           | 13                |
| 104  | 8708        | \-3.00           | 12                |
| 104  | 173         | \-3.00           | 12                |
| 104  | 1124        | \-4.42           | 12                |
| 104  | 8023        | \-5.00           | 12                |
| 108  | 5735        | 2.21             | 11                |
| 108  | 5112        | \-1.50           | 11                |
| 108  | 1721        | \-8.33           | 11                |
| 108  | 1307        | \-14.17          | 11                |
| 108  | 172         | 4.57             | 11                |
| 113  | 2084        | \-17.75          | 10                |
| 113  | 2423        | \-13.58          | 10                |
| 113  | 3958        | \-5.79           | 10                |
| 113  | 5752        | \-13.67          | 10                |
| 113  | 1965        | \-2.50           | 10                |
| 113  | 8709        | \-8.25           | 10                |
| 113  | 4987        | \-8.00           | 10                |
| 113  | 1099        | \-8.29           | 10                |
| 113  | 4473        | \-30.36          | 10                |
| 122  | 5962        | \-18.83          | 9                 |
| 122  | 181         | \-9.58           | 9                 |
| 122  | 4097        | \-14.83          | 9                 |
| 122  | 2712        | \-17.79          | 9                 |
| 122  | 1247        | \-10.71          | 9                 |
| 122  | 2785        | \-7.42           | 9                 |
| 122  | 6153        | \-11.50          | 9                 |
| 129  | 5459        | \-11.43          | 8                 |
| 129  | 6529        | \-10.50          | 8                 |
| 129  | 7822        | \-5.92           | 8                 |
| 129  | 8604        | \-9.00           | 8                 |
| 129  | 3623        | \-14.50          | 8                 |
| 129  | 4925        | \-11.25          | 8                 |
| 129  | 1512        | \-8.42           | 8                 |
| 129  | 6346        | \-9.25           | 8                 |
| 129  | 6161        | \-17.57          | 8                 |
| 138  | 348         | \-9.29           | 7                 |
| 138  | 2342        | \-7.25           | 7                 |
| 138  | 5347        | \-8.25           | 7                 |
| 138  | 7462        | \-11.75          | 7                 |
| 138  | 5265        | \-23.00          | 7                 |
| 143  | 509         | \-4.57           | 6                 |
| 143  | 2876        | \-8.42           | 6                 |
| 143  | 5422        | \-22.07          | 6                 |
| 143  | 1761        | \-6.42           | 6                 |
| 143  | 4311        | \-7.08           | 6                 |
| 143  | 6324        | \-17.33          | 6                 |
| 143  | 4176        | \-23.67          | 6                 |
| 143  | 61          | \-14.33          | 6                 |
| 143  | 839         | \-9.67           | 6                 |
| 143  | 6762        | \-19.67          | 6                 |
| 153  | 175         | \-5.86           | 5                 |
| 153  | 2170        | \-17.50          | 5                 |
| 153  | 7314        | \-27.50          | 5                 |
| 156  | 6201        | \-10.00          | 4                 |
| 156  | 8567        | \-24.08          | 4                 |
| 158  | 4169        | \-15.00          | 3                 |
| 158  | 5142        | \-3.64           | 3                 |
