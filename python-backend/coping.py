from sys import stdin

def allocate( max_pages ):
    pages = 0
    writers_used = 0
    i =  m - 1
    while i >= 0:
        if l[ i ] + pages > max_pages:
            writers_used += 1
            if writers_used == k:
                return False
            pages = l[ i ]
        else:
            pages += l[ i ]
        i -= 1
    return True

if __name__ == '__main__':
    n = int( stdin.readline().strip() )

    while n > 0:
        m, k = map( int, stdin.readline().strip().split() )
        l = list( map(int, stdin.readline().strip().split()) )

        lo, hi = max( l ), sum( l ) 
        while lo < hi:
            mid = lo + ( hi - lo ) // 2
            if allocate( mid ):
                hi = mid
            else:
                lo = mid + 1
        writers_assigned = [ False ] * m
        pages = 0
        writer_idx = k - 1
        i = m - 1
        while i >= 0:
            if pages + l[ i ] > lo or writer_idx == i + 1:
                writer_idx -= 1
                writers_assigned[ i ] = True
                pages = 0
            pages += l[ i ]
            i -= 1

        result = [ str(l[0]) ]
        if writers_assigned[ 0 ]:
            result.append( " /" )
        for i in range( 1, m ):
            result.append( " {}".format(l[i]) )
            if writers_assigned[i]:
                result.append( " /" )
        print( "".join(result) )

        n -= 1
