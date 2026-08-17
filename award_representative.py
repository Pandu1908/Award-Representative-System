class Representative:

  def __init__(self, name, award):
    self.name = name
    self.award = award

  def __repr__(self):
    return f"Representative(name='{self.name}', award='{self.award}')"


# Usage
rep = Representative("Alice", "Best Speaker")
print(repr(rep))  # Output: Representative(name='Alice', award='Best Speaker')
```

### Program to Award a Grade/Prize
```python
def award_prize(score):
  if score >= 90:
    return "Gold Medal"
  elif score >= 75:
    return "Silver Medal"
  else:
    return "Certificate"


# Usage
score_input = 85
print(f"Award: {award_prize(score_input)}")  # Output: Award: Silver Medal
```

<FollowUp>
If you meant a different kind of **award representative** program or logic, please tell me:
* What the program **should input and output**
* Any specific **rules or data** you want to use

I can write the exact code for your project.
</FollowUp>
