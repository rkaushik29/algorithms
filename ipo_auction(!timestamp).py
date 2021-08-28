# in this case, shares are divided s.t. each first gets one share and then they are removed from the list using some criteria

def getUnallottedUsers(bids, totalShares):
    sorted_bids = sorted(sorted(bids, key = lambda x:x[3], reverse = False), key = lambda x:x[2], reverse = True)
    shares_received = dict()
    for i in range(len(sorted_bids)):
        if totalShares > 0:
            if i == len(sorted_bids) - 1:
                return []
            elif sorted_bids[i][2] > sorted_bids[i+1][2]:
                if totalShares < sorted_bids[i][1]:
                    shares_received[sorted_bids[i][0]] = "1"
                    return sorted([x[0] for x in sorted_bids if x[0] not in list(shares_received.keys())])
                totalShares -= sorted_bids[i][1]
                shares_received[sorted_bids[i][0]] = "1"
                
            else:
                sum_req = sorted_bids[i][1]
                end = i
                for j in range(i, len(sorted_bids)-1):
                    end = j
                    if sorted_bids[j][2] == sorted_bids[j+1][2]:
                        sum_req += sorted_bids[j+1][1]
                        end = j+1
                        continue
                    else:
                        break
                
                if totalShares < (end-i+1):
                    for x in range(i, len(sorted_bids)):
                        if totalShares > 0:
                            shares_received[sorted_bids[x][0]] = "1"
                            totalShares -= 1
                        else:
                            return sorted([x[0] for x in sorted_bids if x[0] not in list(shares_received.keys())])
                        
                elif totalShares > sum_req:
                    for x in range(i, end+1):
                        shares_received[sorted_bids[x][0]] = "1"
                    totalShares -= sum_req
                    
                else:
                    for x in range(i, end+1):
                        shares_received[sorted_bids[x][0]] = "1"
                    return sorted([x[0] for x in sorted_bids if x[0] not in list(shares_received.keys())])
                
        else:
            return sorted([x[0] for x in sorted_bids if x[0] not in list(shares_received.keys())])
    
    return []