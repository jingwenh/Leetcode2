class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        counts = {}
        for s in cpdomains:
            tokens = s.split(" ")
            domain = tokens[1]
            count = int(tokens[0])
            domains = self.splitDomain(domain)
            for d in domains:
                if d in counts:
                    counts[d] = counts[d] + count
                else:
                    counts[d] = count
        
        res = []
        for k, v in counts.items():
            res.append(str(v) + " " + k)
        return res
            
    
    def splitDomain(self, d):
        tokens = d.split(".")
        count = []
        for i in range(len(tokens)):
            count.append(".".join(tokens[i:]))
        return count
