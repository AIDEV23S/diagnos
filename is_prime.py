def is_prime(x): #kollar om talet x är ett primtal
    # endast positva tal kan vara primtal och minsta primtal är 2 så vi börja kolla på 3
    if (x > 1):
        divisor = 2
    # eftersom inmatat tal alltid kan delas med sig självt kan vi använda rage 
    # funktionen för att ställa in rätt intervall
        for i in range(divisor,x):
            if (x % i) == 0: # jämnt delbart
                return False
    else:
        return False
    return True
