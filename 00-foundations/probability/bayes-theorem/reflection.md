## 1. What is a Prior?

A prior is your belief about something before seeing new evidence.

**Example:**  

You think there's a 30% chance it will rain today because it's monsoon season.

- Prior belief = 30% chance of rain

Think of a prior as your **starting assumption.**

## 2. What is Evidence?

Evidence is new information that helps you update your belief.

**Example:**

You look outside and see dark clouds.

Evidence = Dark clouds

Evidence provides additional information that may strengthen or weaken your prior belief.

## 3. What is a Posterior?

A **posterior** is your updated belief **after considering the evidence.**

Example:
- Prior: 30% chance of rain
- Evidence: Dark clouds
- Posterior: 80% chance of rain

So:

**Prior → Evidence → Posterior**

## 4. Why Can Intuition Fail in Probability?

Humans often focus on what seems obvious and ignore important background information (called the base rate).

**Example: Medical Test**

Suppose:

- Disease affects 1% of people
- Test is 95% accurate
- Your test result is positive

Many people intuitively think:

"I probably have the disease (95% chance)."

But after applying Bayes' Theorem, the actual probability may be much lower because the disease is rare.

Intuition often ignores:

- How common something is
- False positives
- Sample sizes

That's why probability can be surprising.

## 5. Why is Bayes' Theorem Useful?

Bayes' Theorem helps us:

1. Update beliefs when new evidence arrives.
2. Make better decisions under uncertainty.
3. Combine prior knowledge with new data.
4. Avoid common probability mistakes.
5. Power many AI and Machine Learning systems.
```
P(A∣B) = [P(B∣A)P(A)]/P(B)
```

```
Posterior = useful evidence / total evidence
```

In simple words:

Bayes answers:

"Given this new evidence, what should I believe now?"

## 6. Three Real-World Examples
### Example 1: Weather Forecast

**Prior:**
40% chance of rain.

**Evidence:**
Weather radar shows a storm approaching.

**Posterior:**
85% chance of rain.

### Example 2: Spam Email Detection

**Prior:**
Most emails are not spam.

**Evidence:**
Email contains words like "FREE MONEY" and many suspicious links.

**Posterior:**
High probability the email is spam.

This is how many email filters work.

### Example 3: Job Interview

**Prior:**
You think a candidate has a 50% chance of being a good hire.

**Evidence:**
Candidate performs exceptionally well in technical rounds and references are excellent.

**Posterior:**
You now believe there's an 85–90% chance they will succeed in the role.


### Memory Trick

**Prior → Evidence → Posterior**

**What did I believe? → What did I observe? → What do I believe now?**


## Most Important Insight

Bayes' Theorem is not really about probability.

It is about:
```
Learning from evidence.
```
That idea appears throughout:
- Data Science
- Machine Learning
- AI
- Decision Making