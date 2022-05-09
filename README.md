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

![](https://www.kaggleusercontent.com/kf/2007818/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..SrSrC4NLlRi5dZPwkgq_gw.cUlvDwKUFOUsgs4AGs294M3vkmRfdVr-fVWWCsbG0hLwxGj7eyTW3eQFGQFM_jknzycNoyDH-OPLJHrSQiv5TQTJintTz5m6KMw30XJhuBIwQIGq5aXp_GjkrWTObVbm-KMht3UOAFce63hFP0AIaDn4x07OOQmPij2tg8f9Q8uAhVFWnz689PvzwmcaD8Y9toaW4eFNTaZe55QXZl7u_31VAwoHflj4UMoB86G85NC8g1c7epDqS5zYWGymQ5VmvejdgyEajvZGG9rSzsGmbM2-6bcZpoQP1LDcG0ESl0jhs-Sh8CwV5gdBtm8wJsQfK3CIUmfD-b1cSa0tbk2a3-TzUZ_dDwY61cK5lGwRPiOerSBmFLZuoMvRVYDSqyLLsjarRFZvchQGphz0WGShnoENNUtDsz2CASGtzPK8xu4SyrkXObclWU94Lt5_ugSKNsjS4_WXoLXhnXoQSIJnoCio4y0gMUQxeu_xm6as6F9DlcBhwQQ7xw_-Y2sYPoccq8imY5BkolVdxKDdLOMR5Yu6pYsklfgA-R2hTHQ5S0BaO-emPAJ5G78lqfkSfxaqrr4u66lClKNJg0ndlcb1lOUTIh9_uEvhMNCCFd9Q4vXuVb1wJxG9k8Vu-lHs4nWkMeOlBBRNLmBomVy1MCB44fH2x1eqTo6jyjw0Cs-FS6Q.80XOExifaiXG01W8HyC7aA/__results___files/__results___19_0.png)


