class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        number_count = {}  #
        endpoints = {} # key start: end, and end: start

        for num in nums:
            if num not in number_count:
                plus = num + 1
                minus = num - 1
                if plus not in number_count and minus not in number_count:
                    number_count[num] = 1
                    # num IS THE NEW PLUS
                elif plus not in number_count:
                    number_count[num] = number_count[minus] + 1

                    # is greater than 1 connection
                    if minus in endpoints:
                        more_minus = endpoints[minus]

                        del endpoints[minus]
                        del endpoints[more_minus]

                        number_count[more_minus] = number_count[num]
                        
                        endpoints[more_minus] = num
                        endpoints[num] = more_minus
                    # connected to single value
                    else:
                        number_count[minus] = number_count[num]
                        endpoints[minus] = num
                        endpoints[num] = minus

                elif minus not in number_count:
                    number_count[num] = number_count[plus] + 1

                    # is greater than 1 connection
                    if plus in endpoints:
                        more_plus = endpoints[plus]

                        del endpoints[plus]
                        del endpoints[more_plus]

                        number_count[more_plus] = number_count[num]
                        
                        endpoints[more_plus] = num
                        endpoints[num] = more_plus
                    # connected to single value
                    else:
                        number_count[plus] = number_count[num]
                        endpoints[plus] = num
                        endpoints[num] = plus

                else:
                    number_count[num] = number_count[minus] + 1 + number_count[plus]
                    if plus in endpoints and minus in endpoints:
                        plus_plus = endpoints[plus]
                        minus_minus = endpoints[minus]

                        del endpoints[plus]
                        del endpoints[plus_plus]
                        del endpoints[minus]
                        del endpoints[minus_minus]

                        number_count[plus_plus] = number_count[num]
                        number_count[minus_minus] = number_count[num]

                        endpoints[plus_plus] = minus_minus
                        endpoints[minus_minus] = plus_plus

                    elif plus in endpoints:
                        plus_plus = endpoints[plus]

                        del endpoints[plus]
                        del endpoints[plus_plus]

                        number_count[plus_plus] = number_count[num]
                        number_count[minus] = number_count[num]

                        endpoints[minus] = plus_plus
                        endpoints[plus_plus] = minus

                    elif minus in endpoints:
                        minus_minus = endpoints[minus]

                        del endpoints[minus]
                        del endpoints[minus_minus]

                        number_count[minus_minus] = number_count[num]
                        number_count[plus] = number_count[num]

                        endpoints[plus] = minus_minus
                        endpoints[minus_minus] = plus
                    
                    else:
                        number_count[minus] = number_count[num]
                        number_count[plus] = number_count[num]

                        endpoints[minus] = plus
                        endpoints[plus] = minus

        return max(number_count.values())