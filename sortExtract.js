const fs = require('fs');

try {
    const max = 'reducedBWImages110'
    const other = 'reducedBWImages90'

    const dataMax = fs.readFileSync(
        '/Users/ravill2/birdPhotos/CUB_200_2011/CUB_200_2011/model/' + max,'utf8')
    const dataOther = fs.readFileSync(
        '/Users/ravill2/birdPhotos/CUB_200_2011/CUB_200_2011/model/' + other,'utf8')

    const parsedJSONMax = JSON.parse(dataMax)
    const parsedJSONOther = JSON.parse(dataOther)
    
    // images in one but not the other
    const listOnesMax = Object.keys(parsedJSONMax)
                            .filter(q => parsedJSONMax[q] === 0)
                            .map(q => {return q.replace(max,other)})
                            .filter(q => parsedJSONOther[q] === 1)
    //console.log(listOnesMax)
    
    // sort by bird in max, get counts per bird type
    const listMax = Object.keys(parsedJSONMax)
                            .filter(q => parsedJSONMax[q] === 1)
                            .map(q=>{return q.split('/')[8]})
                            .sort()
                            .reduce((prev,next) => {
                                prev[next] = (prev[next] || 0) + 1
                                return prev;},{})
    console.log(listMax)

    //get list of birds that passed
    const listBirds = Object.keys(parsedJSONMax)
                            .filter(q => parsedJSONMax[q] === 1)
    //count number of matches
     const matches = Object.keys(parsedJSONMax)
                 .map(q => {return parsedJSONMax[q]})
                 .filter(q => q === 1)
                 .length

    //console.log(matches)
} catch(e) {
    console.log(e)
}

//10 1155
//20 2693
//30 3634
//40 4272
//50 4750
//60 5124
//70 5469
//80 5674
//90 5841
//100 5695
//110 5964
//120 5913
//130 5849
//140 5752
//150 5611


