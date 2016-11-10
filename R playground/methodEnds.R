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

methodEnds2 = function (sampleSize){
    numTimesBigger = 0
    triangleSideSquared = 3
    alpha = runif(sampleSize,0,360)
    beta = runif(sampleSize,0,360)
    x1 = cos(alpha)
    x2 = sin(alpha)
    y1 = cos(beta)
    y2 = sin(beta)
    chrodSquared = (x1-y1)^2 + (x2-y2)^2
    numTimesBigger = chrodSquared - triangleSideSquared
    numTimesBigger = sign(numTimesBigger)
    numTimesBigger = numTimesBigger + 1
    numFinal = sum(numTimesBigger)/2
    return(numFinal/sampleSize)
}



methodEnds3 = function (sampleSize){
    numTimesBigger = 0
    triangleSideSquared = 3
    alpha = runif(sampleSize,0,360)
    beta = runif(sampleSize,0,360)
    numTimesBigger = sign((cos(alpha)-cos(beta))^2 + (sin(alpha)-sin(beta))^2 - triangleSideSquared)
    numFinal = sum(numTimesBigger[numTimesBigger>0])
    return(numFinal/sampleSize)
}


