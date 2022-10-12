def find_average(nums): return sum(nums) / len(nums) if nums else 0

### Best Practices

def find_average(nums):
    return float(sum(nums)) / len(nums) if len(nums) !=0 else 0