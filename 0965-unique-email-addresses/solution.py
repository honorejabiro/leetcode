class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # Create a function that checks the local name
        # Create a hashmap
        # Iterate over the list of strings
        # Change the domain name
        # Add the string to the. set
        # Return the number of the lenght of the set

        def local(local):
            res = []
            for i in local:
                if i == '+':
                    break
                if i == '.':
                    continue
                res.append(i)

            return ''.join(res)

        s = set()

        for email in emails:
            index = email.index('@')
            new = local(email[:index])
            forward = new + email[index:]
            s.add(forward)

        return len(s)
