methodEnds = function (sampleSize){
    numTimesIsBigger = 0
    triangleSideSquared = 3
    for(i in 1:sampleSize){
        alpha = runif(1,0,360)
        beta = runif(1,0,360)
        x1 = cos(alpha)
        x2 = sin(alpha)
        y1 = cos(beta)
        y2 = sin(beta)
        chrodSquared = (x1-y1)^2 + (x2-y2)^2
        if (chrodSquared > triangleSideSquared){
            numTimesIsBigger = numTimesIsBigger + 1
        }
    }
    return(numTimesIsBigger/sampleSize)
}