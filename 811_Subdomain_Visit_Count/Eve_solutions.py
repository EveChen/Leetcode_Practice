
# https://leetcode.com/problems/subdomain-visit-count/

# Method 1: Use collections.Counter
# Time: O(N^2)?
# Space: O(N)
from collections import Counter
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        res = Counter()
        for domain in cpdomains:
            count, domain = domain.split()
            count = int(count)
            frags = domain.split(".")
            
            for i in range(len(frags)):
                res[".".join(frags[i:])] += count
        return ["{} {}".format(count, domain) for domain, count in res.items()]
    
    
    
# Method 2: Use hashmap
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        res = {}
        for domain in cpdomains:
            count, domain = domain.split()
            count, domain = int(count), domain.split(".")
            for i in range(len(domain)):
                _str = ".".join(domain[i:])
                if _str not in res:
                    res[_str] = 0
                res[_str] += count
                
        return [str(res[domain]) + ' ' + domain for domain in res]
        

