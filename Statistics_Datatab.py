# Important Keyword on Basics of Statistics

"""
Population - parameter
Sample - statistic
Descriptive statistics - describes sample data
    Measure of central tendency
        Mean, median ( resistant to outliers ), Mode        
    measures of dispersion
        how spread out the values are
            Variance, Std Deviation, IQR, Range
            STD - avg deviation from mean  - use 1/n-1 if for sample
            Range = max - min
            IQR - Q3-Q1 - middle 50% of the data
    Tables
        Freq tables 
        contegency tables - between 2 category variables ( pivot )
    Charts

Inferential Statistics - draw conclusions based on sample data about the population ( educated guess )
    Six keys 
        1) Hypothesis  2) Population & Sample   3) Hypothesis Testing 4) p-Value  5) Significance  6) Error
        
        1) Hypothesis - testing a claim about a parameter in a population using data measured in a sample 
                Research / alternative hypothesis - trying to find an evidence for
                    e.g. the drug has an effect on BP
                    The alternative hypothesis typically assumes that there is an effect in the population, and that your observed data does not occur by chance
                Null Hypothesis 
                    e.g the drug has no effect
                    The null hypothesis typically assumes that there is no effect in the population, and that your observed data occurs by chance.
                
                we test the null hypothesis; and not alternate
                    e.g all swans are white. instead see if there an evidence to find atleast one black swan which proves alternate is incorrect
                                
        eg. Research Hyp - The drug has an effect on blood pressure
            Null - the no effect  assumption

            A random sample is drawn and say if the drug has large effect. 
            Then we ask how likely is draw an anoher sample the one which deviates even more than the results previously seen  - whats the probability?

            This probability is called the p-Value

            significance - usually 0.05 then it is statistically significance
            it means that the result is unlikely to have occured by chance alone and that we have enough evidence to reject the null hyp

            A small p value suggests that the observed data is inconsistant with null hyp. in favour of Alt Hyp
            a large p value suggests that it is consistant with null hyp; not reject

            Error
                a small p does not prove that the alt hyp is true; it is only saying that , it is unlikely  to get such a result or a more extreme
                a large p value does not prove that the null hyp is true; it is likely to get such a sample

                                            in reality, the null hyp is                            
            decision             accepted     correct         type II error
            about null hyp       Rejected     type 1 error    correct

            Type 1 error -  A true null Hyp is rejected
            Type II error - a false null hyp is not rejected. the drug does actually work but we accepted the null Hyp - the sample taken did not show that diff

            Hyp testing depends on levels of measurement

            4 Levels of measurement
                Normial - gender
                ordinal - ranked
                interval - age, body weight ( continuous )
                ratio - 4 hrs faster than lowest runner

            
            T Test
                Statistical Test procedure - analysis whether there is significance diff between the means of 2 groups
                Types of T test  -  
                    1 sample t-test   -  between mean of a sample & known reference, 
                    independent samples t-test  - between means of 2 groups, 
                    paired samples t-test - same people before & after ( diet results test )
                    1 sample t-test is approx to paired sample t-test
                Assumptions -  
                    metric ( mean ) must be normally distributed  - age, body weight & income                    
                    for independent t-test - variance must be like between 2 groups ( use levene test )
                    in general, the sample shd be a good representation of the population

                
                Null Hyp - 
                    the sample mean is equal to the reference value ( 1 sample )
                    the mean values between 2 groups are equal
                    the mean of the diff between the pairs are 0
                
                Why do we need a t-test
                    e.g. if there is diff between length of study between men and women in USA

                How do we calculate the t-test
                        t-test for 1 sample
                            t = Xbar - Mu / std D/sqrt(n) 
                                    Mu - known mean for 1 sample
                        t-test for independent
                            t =  X1 - X2 / sqrt(s1**2/n1 + s2**2/n2) 
                        t-test for paired sample
                            t = Xdiff - 0 / s/sqrt(n)
                        
                t value
                    directly proportional to diff in mean
                    t becomes smaller if we have larger dispersion.  so the more the data is disspersed the less meaningfull the given diff is
                
                How to use t value
                1) read critical t value
                2) calculate p value

                P value -  assume no diff; draw a sample. sample deviates from known mean by a certain amount. P values tells us how likly it is that a sample drawn has equal or more deviation
                           at significance 5%. there is only 5% chance that the drawn sample will have equal or more deviation. so we reject the null hypothesis

                critical t table
                    degree of freedom = 1sample / paired = n-1 , independent = n1+n2 -2                
                    so t > tcritical; we reject the null hyp
                
                Directed & undirected hypothesis
                    undirected = just assumes not equal to female != male
                    direted = if u are interested int he direction female > male / female < male

            ANOVA ( One WAY)
                Types 
                    Single factorial without measurement repetition - we will just talk about this one
                    Single factorial with measurement repetition
                    Two factorial without measurement repetition
                    TWO factorial with measurement repetition
                Why DO u need?
                    ANOVA tests whether there are statistically significant differences between three or more samples
                    is the extention of t test for independent samples to more than 2 groups
                Example
                    I might be interested to know if there is difference in age between people who use datatab, spss or R
                    Research question:
                        is there a difference in population between the diff groups of the independent variable w.r.t the dependent variable
                            Independent variable -  Datatab, spss, R ( one nomical variable )
                            Dependent variable - age ( Metric )
                            population - inferential statistics based on sample
                        Hypothesis
                            Null -  There are no differences between the means of individual groups
                            Alternate :  atleast 2 groups differ from each other in the population
            ANOVA ( TWO WAY )
                Statistical method used to test the effect of 2 categorical variables on a continuous variable
                e.g.  drug type - A , B  & Gender - Male & Female ( Factors - Nominal variable )
                      blood pressure - metric - continuous variable
                    
                What kind of statements can we make with a ANOVA?
                    Does factor 1 have an effect on the dependent variable
                    does factor 2 have an effect on the dependent variable
                    is there an interaction between factor 1 & factor 2
                
                Hypothesis?
                    H0:
                        there is no significant diff between groups of the first factor
                        there is no significant diff between groups of the second factor
                        one factor has no effect on the other factor
                    H1:
                        There is a significance diff between the groups of the first factor
                        There is a significance diff between the groups of the second factor
                        atleast one factor has an influence on the other factor
                    
                    Assumptions
                        Normally distributed - within the groups or alternatively the residuals shd be normal distributed - quantile-quantile plot
                        homogeneity of variances - levene's test
                        independence on mesurements - one group shd not be influenced by other group
                        metric scale level
                    
                    ANOVA - Analysis of variances?
                    in Two way
                    SStot = SSa + SSb + SSab + SSerr
                    total variance of the dependent variable
                    a - variance explained by factor a
                    b - variance explained by factor b
                    ab - variance explained by interaction of factors A & B
                    err = the error variance
                    SS = sum of squares

                    e.g sstot has some variance - if that variance is explaned then SSa,ssb, SSab will cover majority and very littlee on err 
                    F distribution & P value
                    degree of freedom - n - no of people , p,q - no of categories 

                    Fcal > Fcric then H0 is rejected 

                    e.g - https://datatab.net/statistics-calculator/hypothesis-test/two-way-anova-calculator?example=two_way_anova_medicine
            
            Repeated measures ANOVA
                something similar to paired samples. same group measured at different times 
                e.g investigate effectives of a training program at 1) before the training  2) immediatly after training completion 3) after 2 months
                The dependents samples, the same test units are measured several times under diff conditions

                What the hypothesis?
                    H0: there are no differences between the dependent groups - traning has no influence
                    H1 : there is a diff between the dependent groups - traning has influence
                
                What are the assumptions?
                    Normality  - not normal then non parametric 
                    Sphericity - the variances of the diff between all combinations of factor levels ( time points ) shd be the same  - Mauchly's test of sphericity
                       if P value > 0.05 then the variances are equal 
                            if violation then adjustments such as Greenhouse Geisser / Huynh Feldt test can be used - sphericity correction

                F distribution table and then P value 
                    Our goal  is to calculate the F value and then calculate P value
                
                if P < 0.05 then H1. do Bonferroni post-hoc tests to identify which group has that difference

            Mixed Model ANOVA - 2 two way ANOVA with repeated measues
                 A mixed model ANOVA is a statistical method used to analyze data that involve both between subject factors and within subject factors
                 e.g we want to test different diets ( A, B, C) has any effect in chlestrol levels
                 Between subjects factor ( groups with diets A, B & C)
                 Within subjects factors ( group with diest A measured at different intervals )
                 Mixed Model = One Way ANOVA + Repeated Mesures ANOVA

                 Factor 1 -  A, B & C
                 Factor 2 - measurement at diff time intervals

                 Answers to
                    Does the within subject factor have an effect? - diff time intervals
                    Does the between subject have an effect?  A, B & C
                    is there any interaction between 2 factors

                Hypothesis
                    H0: 
                        Within Subject:
                            the mean values of the different measurement time points do not differ
                        between subjects
                            The mean values of the different groups of between subject factor do not differ
                        interaction
                            one factor has no incluence on the other factor
                    
                Assumptions
                    Normally distributed
                            very strict in case of small sample size
                            ANOVA is somewhat robust to violations of normality in large sample size
                    Homogeneity of variances - levene test
                        Needs to be true for both between subjects and within subjects factors
                    Homogeneity of covariances ( Sphericity ) - mauchly's test - when violated ( Greenhouse-geisser or huynn feldt ) - within subject 
                        this applies to within subjects factor - the variances of the diff between all combinations of diff groups are equal
                            e.g. factor 2 - measurements at diff times
                                    grp1 - grp2 , grp1 - grp3, grp2 - grp3
                    No significant outliers
                        outliers can have a dispropotionate effect on ANOVA potentially leading to incorrect results
                    
                    e.g. - https://datatab.net/statistics-calculator/hypothesis-test/mixed-model-anova-calculator?example=two_factorial_anova_with_repeated_measures

                    Bonferroni Post-hoc-Tests can be done to understand the direction
                        Bonferroni Post-hoc-Tests factor 1
                        Bonferroni Post-hoc-Tests factor 2

            Parametric & Non parametric test - normality violations
                first check the assumptions 
                if the data is normally distributed then parametric tests
                    t-test, ANOVA or peasons corelation
                if the data is not normally distributed then Non parametric tests
                    Mann Whitney U test or spearmans's corelation
                what about other assumptions? fewer than parametrics.
                    if so then why parametrics test at all
                        parametrics test are more powerfull; if possible always use paramteric tests
                    
                    Parametric Test - Raw data
                    Non Parametrics test - Ranks of the data
                
                Goal                                      Parmetric test                        Non Parametric test
                One Sample                                Simple t-test                         Wilcoxon test for 1 sample
                Two dependent samples                     paired sample t-test                  Wilcoxon Test  
                Two independent samples                   independent T test                    Mann Whitney U test ( ranks )
                more than 2 independent samples           One factor ANOVA                      Kruskal Wallis Test
                more than 2 dependent samples             Repeated Measures ANOVA               Friedman Test
                corelation between 2 variables            Pearson corelation                    Spearmans rank corelation ( does not use raw data but ranks )

            Test For Normal Distribution
                Test ur data for normal distribution
                Has Bell Curve?

                2 Ways
                    1) Analytical
                            Kolmogorov Smirnov Test ( other than normal distribution can also be tested )
                            Shapiro Wilk Test
                            Anderson Darling Test ( other than normal distribution can also be tested )

                            for above H0: the data is normally distributed
                                P value < 0.05 then Normal distrbution is not assumed

                        Disadvantages of Analytical
                            P value depends on sample size
                            Distribution deviates very slightly from normal distribution - again on the sample size - we may reject the null Hyp

                            Graphical is always better

                    2) Graphical
                            Histogram - bell curve
                            Quantile-Quantile Plot

            Equality of Variance - Levene's Test
                Levene's test test the hypothesis that the variances are equal in different groups

                Hypothesis:
                    H0:  the variances of the group are equal ( P > 0.05 )
                    H1:  Atleast one of the group has a diff variance

                levene's test is used as a requirement for other hypothesis test's e.g T-test

                Steps
                1) Cal Mean of each group
                2) subtract the respective group mean from each person
                3) sum of those value from each group - the larger the sum the grater the variance
                4) calculate total mean again
                5) squared deviations of the group mean from the overall Mean and sum them up (1)
                6) squared deviation within the groups (2)

                L = ((num of cases - num of groups ) / ( num of group - 1) ) * ( SUM ( cases per grp * (1) ) / sum ( (2) ) )

                Test Statistic L is equal to the F statistic

                deg of freedom Numerator -  ( No of groups - 1 ) = K-1
                deg of freedom denemenator - ( no of cases - no of grps ) = N-k

            Mann Whitney U test ( ranks ) - Two independent samples - Non Parameteric 
                it is based on ranks on the data and not raw data
                e.g. gender & reaction time  - rank based on reaction time for the whole groups 

                H0: both ranks sums are equal
                H1 : both ranks sums are not equal

                Manual Calculation
                Step 1
                    T1 - female - sum of ranks
                    T2 - male - sum of ranks
                Step 2 - calculate U
                    U1 = n1.n2 + ((n1*(n2+1) / 2) - T1)                
                    U2 = n1.n2 + ((n1*(n2+1) / 2) - T2)   
                Step 3 - U value = min (U1,U2)
                Step 4 = expected value of U
                        Mu = n1*n2/2
                Step 5 = standard eror of U
                        Mu = sqrt(n1*n2*n1+n2+1/12)
                Step 6 - Z value = U - Mu / Sigma U
                Step 7 - calculate P value using Z value

                    For upto 25 cases exact values can be used
                    for larger samples, the normal distribution of the U value can be used as an approx.

            Wilcoxon Test - Two dependent samples - Non Parametric
                The rank is based on the diff in the mean between paired samples
                   i.e the smallest diff gets the highest rank

                Assumption and Hypothesis
                    only two dependent random samples with at least ordinally scaled charaterstics need to be available
                    the variables do not have to satisfy a distribution curve

                    Hyp:
                    H0: In the population, the mean of the two dependent samples are the same
                    H1 : In the population, the mean of the two dependent samples are not the same

                e.g. reaction time in morning & eve and are they diff?
                    
                Steps
                    e.g.  Case(7), morning , eve,  diff( eve - morning - usually normally distributed else WilTest), Rank , cal of Rank sum ( retain sign )
                    T+ = sum of ositive ranks
                    T- = suum of neg ranks

                    Test Statistic W = min ( T+,T-)
                    Exp value of W - Mw - 
                    Std error = Sigw

                    Z-value =  W - Mw / Sigw

                    if more than 25 cases , normal distribution is assumed
                    else the Critical T value is read from a table 

            Kruskal Wallis Test - Non Parametric ANOVA
                Non parametric counter part to one way ANOVA
                is there a diff in the rank totals ?

                How must the variables be scaled?
                    Independent Variable - nominal valiable with more than 2 possible values
                    Dependent variable - salary, weight etc - Ranked

                Assumptions
                    Only several independent random samples with at least ordinally scaled characterstics must be available
                    The variables do not have to satisfy a distribution curve - Since Rank & Ranksum is used 

                    Hypothesis
                        H0: The Independent samples all have the same central tendency and therefore come from the same pop
                        H1: Atleast one of the independent samples does not have the same central tendency as the other samples and therefore come from a diff population

                    E.g - reaction time of 3 diff groups - A,B & C

                    1) Rank all 3 groups
                    2) Ranksum & Mean Ranksum by groups  - Ra & RAb ( Mean )
                    3) Expected value of Rank sum - Er = n+1/2
                    4) Degree of freedom = Groups - 1 = 2
                    5) Rank variance = n**2 - 1 / 12 ( no of entries )
                    6) Test Statistic H - Chi Square value
                    7) Table of Chi-Squared Distribution

            FriedMan Test - Non Parametric ANOVA with repeated measures
                Tests whether there are statistically significant differences between 3 or more dependent samples
                Dependent sample - time dependent - measured at multiple time points
                is there a diff in the rank totals?

                H0:  No significant differences between the groups
                H1:  there is a significant diff between the dependent groups

                Calculation
                e.g - you might be interested to know if therapy after a slipped ddisc has any effect on pain percetion
                      measurement - before, middle & post therapy
                      7 entries

                1) Rank across ( per row ) - per sample ( largest value gets 1 )
                2) Rank sum by measurements
                3) Expected value - N(k+1)/2 
                4) Chi**2 calculation
                5) degree of freedom - k-1 
                6) Table of Chi Squared distribution
                7) if Chi**2 value is greater than Critical value then reject the null hypothesis

            Chi**2 Test 
                Test that is used when u want to determine if there is a relationship between two categorical variables

                e.g Gender, preferred Newspapaer, Education level - Categorical var
                is there a relationship between gender & preferred newspapaer - Chi**2 Test
                is there a relationship between gender & Education level - Chi**2 Test

                Note /Assumption:
                    Expected freq > 5
                    Chi**2 Test uses only the categories but not rankings.  
                    e.g Highest education level has inherient ranking. use spearman corelation if u want to account for rankings

                H0: There is no relationship
                H1: There is a relationship
                
                 
                Calculation
                    1) contingency table
                    2) contingency of the expected Freq ( values if the 2 variable are perfectly independent )
                    3) Chi**2 = sum ( (Ok - Ek)**2 / Ek  )
                    4) Degree of Freedom = (no of rows -1 ) (no of columns -1 )
                    5) if Chi**2 value is greater than Critical value then reject the null hypothesis











            


                










                







                    
                    







                
                














                














                    


                    







"""


