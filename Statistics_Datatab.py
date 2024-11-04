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
                                
        eg. Res Hyp - The drug has an effect on blood pressure
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
                    Single factorial without measurement repetition - we will jut talk about this one
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
                            Null -  There are no differences between the population between the means of individual groups
                            Alternate :  atleast 2 groups differ from each other in the population
            ANOVA ( TWo WAY )
                Statistical method used to test the effect of 2 categorical variables on a continuous variables
                e.g.  drug type - A , B  & Gender - male & Female ( Factors - Nominal variable )
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
                
                if P < 0.05 then H1. do Bonferroni post-hoc tests to identify which group has that difference

                F distribution table and then P value 

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
                    Homogeneity of covariances ( Sphericity ) - mauchly's test - when violated ( Greenhouse-geisser or huynn feldt )
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
                
                Goal                                        Parmetric test                        Non Parametric test
                One Sample                                  Simple t-test                       Wilcoxon test for 1 sample
                Two dependent samples                     paired sample t-test                  Wilcoxon Test  
                Two independent samples                   independent T test                    Mann Whitney U test
                more than 2 independent samples           One factor ANOVA                      Kruskal Wallis Test
                more than 2 dependent samples             Repeated Measures ANOVA               Friedman Test
                corelation between 2 variables            Pearson corelation                    Spearmans rak corelation

            Test For Normal Distribution
            






                    
                    







                
                














                














                    


                    







"""


