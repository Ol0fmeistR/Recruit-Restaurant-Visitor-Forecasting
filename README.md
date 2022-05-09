## Visitor Forecasting (Recruit Holdings)
**Competition Description:** <br>
Running a thriving local restaurant isn't always as charming as first impressions appear. There are often all sorts of unexpected troubles popping up that could hurt business.

One common predicament is that restaurants need to know how many customers to expect each day to effectively purchase ingredients and schedule staff members. This forecast isn't easy to make because many unpredictable factors affect restaurant attendance, like weather and local competition. It's even harder for newer restaurants with little historical data.

Recruit Holdings has unique access to key datasets that could make automated future customer prediction possible. Specifically, Recruit Holdings owns Hot Pepper Gourmet (a restaurant review service), AirREGI (a restaurant point of sales service), and Restaurant Board (reservation log management software).

In this competition, you're challenged to use reservation and visitation data to predict the total number of visitors to a restaurant for future dates. This information will help restaurants be much more efficient and allow them to focus on creating an enjoyable dining experience for their customers.

For the hpg_reserve data, follow this <a href="https://www.kaggle.com/c/recruit-restaurant-visitor-forecasting/data">link</a> <br>

### Snapshot of the data: <br>

**Location of the restaurants featured in the competition:** <br>

<kbd><img src="https://www.kaggleusercontent.com/kf/2007818/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..SrSrC4NLlRi5dZPwkgq_gw.cUlvDwKUFOUsgs4AGs294M3vkmRfdVr-fVWWCsbG0hLwxGj7eyTW3eQFGQFM_jknzycNoyDH-OPLJHrSQiv5TQTJintTz5m6KMw30XJhuBIwQIGq5aXp_GjkrWTObVbm-KMht3UOAFce63hFP0AIaDn4x07OOQmPij2tg8f9Q8uAhVFWnz689PvzwmcaD8Y9toaW4eFNTaZe55QXZl7u_31VAwoHflj4UMoB86G85NC8g1c7epDqS5zYWGymQ5VmvejdgyEajvZGG9rSzsGmbM2-6bcZpoQP1LDcG0ESl0jhs-Sh8CwV5gdBtm8wJsQfK3CIUmfD-b1cSa0tbk2a3-TzUZ_dDwY61cK5lGwRPiOerSBmFLZuoMvRVYDSqyLLsjarRFZvchQGphz0WGShnoENNUtDsz2CASGtzPK8xu4SyrkXObclWU94Lt5_ugSKNsjS4_WXoLXhnXoQSIJnoCio4y0gMUQxeu_xm6as6F9DlcBhwQQ7xw_-Y2sYPoccq8imY5BkolVdxKDdLOMR5Yu6pYsklfgA-R2hTHQ5S0BaO-emPAJ5G78lqfkSfxaqrr4u66lClKNJg0ndlcb1lOUTIh9_uEvhMNCCFd9Q4vXuVb1wJxG9k8Vu-lHs4nWkMeOlBBRNLmBomVy1MCB44fH2x1eqTo6jyjw0Cs-FS6Q.80XOExifaiXG01W8HyC7aA/__results___files/__results___9_0.png"/></kbd> <br>


**Number of Visits vs Reservations:** <br>

*Few things to note:* <br>
1. The number of reservations only account for a fraction of the number of visits since most people would visit a restaurant without making
a reservation beforehand. <br>
2. Also, there a quite a few high frequency periods which probably arise due to day of the week since it seems logical for the common public to flock restaurant
chains during the weekend/friday instead of a weekday. <br>

![](https://www.kaggleusercontent.com/kf/2007818/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..SrSrC4NLlRi5dZPwkgq_gw.cUlvDwKUFOUsgs4AGs294M3vkmRfdVr-fVWWCsbG0hLwxGj7eyTW3eQFGQFM_jknzycNoyDH-OPLJHrSQiv5TQTJintTz5m6KMw30XJhuBIwQIGq5aXp_GjkrWTObVbm-KMht3UOAFce63hFP0AIaDn4x07OOQmPij2tg8f9Q8uAhVFWnz689PvzwmcaD8Y9toaW4eFNTaZe55QXZl7u_31VAwoHflj4UMoB86G85NC8g1c7epDqS5zYWGymQ5VmvejdgyEajvZGG9rSzsGmbM2-6bcZpoQP1LDcG0ESl0jhs-Sh8CwV5gdBtm8wJsQfK3CIUmfD-b1cSa0tbk2a3-TzUZ_dDwY61cK5lGwRPiOerSBmFLZuoMvRVYDSqyLLsjarRFZvchQGphz0WGShnoENNUtDsz2CASGtzPK8xu4SyrkXObclWU94Lt5_ugSKNsjS4_WXoLXhnXoQSIJnoCio4y0gMUQxeu_xm6as6F9DlcBhwQQ7xw_-Y2sYPoccq8imY5BkolVdxKDdLOMR5Yu6pYsklfgA-R2hTHQ5S0BaO-emPAJ5G78lqfkSfxaqrr4u66lClKNJg0ndlcb1lOUTIh9_uEvhMNCCFd9Q4vXuVb1wJxG9k8Vu-lHs4nWkMeOlBBRNLmBomVy1MCB44fH2x1eqTo6jyjw0Cs-FS6Q.80XOExifaiXG01W8HyC7aA/__results___files/__results___19_0.png) <br>


**Difference in days between Reservations and Visits:** <br>

Most of the time reservations are made a week (7 days) in advance. In only rare cases the reservations are made 15 or more days in advance. It will be interesting
to see if the customers who made those reservations end up visting or not. <br>

<kbd><img src="https://www.kaggleusercontent.com/kf/2258102/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..aEPwyIU14YwlhWj0T0qHBQ.W2vJ4Rk2FAN23ui1uOccOF_Ypl0Gl_g4aYc_7sH6TQGDwCQN_M1ZglT8WS1h9riqYrtw8tdUyfrG5dcE0zs16kB1OcqVX1t7f1844Te2XBigsO6vGQ2PhfDAtuXkArgv93jxDH2HTlOfDRKVhWWhUcqIfkq5cK7GqHDYC4KMQLIv1luR4DSj7Hhcez8pxDOB1xVH7cz6nJT9JE_H6lyIEOdi-uTOwxAAMzoIvS-AY2IwHWS4LMoqckj_LGHx1kCBwfKkYPy78FmCDkqEdwEejZmnWqRLvEAk2CI-tHjoTPQnLsnw1S64YFhr6objN11pvoLsyQ6xwHZ9f4MlKY_dMjMpU482Bpytw1bONt7h4FTQJuqp6cNI7SMoOEpt4UE0TjxC0-L1nebCCUnmB656fEAeEAucZWDRJ9_j68JyIYY6ykZM-yPBeo_W2iXJJeaG2ltJ8Pg3Dgw6G3WHT038LbNtgNqlJ0hVLGoFhvLc-_CRC8mV_yTZLUwEsQTbVk6Cvp-f20fry0T0OBGRvzSdOzNRYqt2RQEQHyvmS9M5s69LBU_fpoYAdUMAvT5l04phh2_Sz4vAhDuJ4zWHAb-ggwlYaMK-bSQT0Cmq1GbrSXTC7CA_FtL9l9doHQUSI0PuRiu1msdJAIDs0k9t1haspXMHF9uJSmysuzm1B4c92-g.dY4k1FYhbe6xirNN6eMl8g/__results___files/__results___31_0.png"/></kbd> <br>

Note: Open the images in a new tab if the axes are not visible in github's dark theme. <br>

### Takeaways: <br>
**Final Rank:** 207/2148 (top 10%) <br>
**Private Leaderboard RMSLE Score:** 0.51817 <br>
**Winning Solution Private Leaderboard RMSLE Score:** 0.50128 <br>
**Key Takeaway:** Keep time series cross validation in mind, regular k fold won't always cut it. Also, if the train and test data are from different distributions, then adversarial validation is your best bet.

