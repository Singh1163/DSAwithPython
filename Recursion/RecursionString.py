class RecursionString:

    def palindrome_string(self, string: str) -> bool:
        if len(string) == 1:
            return True
        if len(string) == 2:
            return string[0] == string[len(string)-1]
        return string[0] == string[len(string)-1] and self.palindrome_string(string[1:len(string)-1])

    @staticmethod
    def is_palindrome(string: str) -> bool:
        i = 0
        j = len(string)-1
        while i <= j:
            if string[i] == string[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

    def count_occurrence_of_string(self, string: str, k: str) -> int:
        if len(k) > len(string):
            return 0
        count = self.count_occurrence_of_string(string[1:], k)
        if string.startswith(k):
            return count+1
        else:
            return count

    def print_all_subset_of_given_string(self, string: str, cur: str, i: int, res: set):
        if i == len(string):
            if cur != '':
                res.add(cur)
            return
        self.print_all_subset_of_given_string(string, cur + string[i], i+1, res)
        self.print_all_subset_of_given_string(string, cur, i+1, res)
        return res
