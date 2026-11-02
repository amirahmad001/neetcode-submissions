class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        st = []
        cars = sorted(zip(position, speed), reverse=True)
        for pos,speed in cars:
            #t = d/s
            time = (target-pos)/speed
            if st and time > st[-1]:
                st.append(time)
            elif not st:
                st.append(time)
            else:
                continue
                #st.append(time)
        return len(st)

        