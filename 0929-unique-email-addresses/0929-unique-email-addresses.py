class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        address = 0
        domainSet = set()
        name = []
        names = set()
        res = 0
        
        def helper(email):
            nonlocal name
            l,d = email.split('@')
            for letter in l:
                if letter =="+":
                    break
                if letter ==".":
                    continue
                name.append(letter)
            names.add(''.join(name) +"@"+ d)
            name = []
       
        for email in emails:
            helper(email)

        
        return len(names)
    
    
    