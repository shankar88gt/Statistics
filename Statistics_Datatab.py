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
                            Independent variable -  Datatab, spss, R
                            Dependent variable - age
                            population - inferential statistics based on sample
                        Hypothesis
                            Null -  There are no differences between the population between the means of individual groups
                            Alternate :  atleast 2 groups differ from each other in the population
                            










                    


                    







"""


