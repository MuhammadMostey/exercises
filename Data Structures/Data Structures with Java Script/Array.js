class myArray {

    constructor(){
        this.items = {};
        this.length = 0;
    }

    get(index){
        return this.items[index]
    }

}

// testing array
arrNew = new myArray();
console.log(arrNew);